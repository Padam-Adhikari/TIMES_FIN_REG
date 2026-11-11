"""Read-only scanner for VEDA tables in the Reg-FINTIMES workbooks.

Never writes anything. Opens workbooks with openpyxl read_only=True twice: once with
cached values (what VEDA sees in the mode the file was last saved in) and once with
formulas (to detect tags/cells that depend on the Region_selection switch).

Usage:
    python tools/veda_scan.py [--case Baseline-Sami] [--json out.json]
"""
import argparse
import json
import os
import re
import sys
import warnings

import openpyxl

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
MODEL = os.path.normpath(os.path.join(ROOT, "Reg-FINTIMES"))

# A tag cell: "~NAME" optionally followed by ":" parameters. Disabled tags (no "~",
# e.g. produced by the Region_selection IF) are recognised by name.
TAG_RE = re.compile(r"^\s*~?\s*([A-Za-z_][A-Za-z0-9_\-]*)\s*(?::\s*(.*))?$")
KNOWN_TAGS = {
    "FI_T", "FI_PROCESS", "FI_COMM", "TFM_INS", "TFM_DINS", "TFM_UPD", "TFM_MIG",
    "TFM_INS-TS", "TFM_INS-AT", "TFM_DINS-TS", "TFM_DINS-AT", "TFM_TOPINS", "TFM_UPD-N",
    "TFM_FILL", "TFM_FILL-R", "TFM_COMGRP", "TFM_PSETS", "TFM_CSETS", "UC_T", "UC_SETS",
    "TRADELINKS", "TRADELINKS_DINS", "COMEMI", "PRCCOMEMI", "COMAGG", "COMAGG_R1C2",
    "BOOKREGIONS_MAP", "STARTYEAR", "ACTIVEPDEF", "TIMEPERIODS", "TIMESLICES",
    "CURRENCIES", "DEFUNITS", "DEFAULTYEAR", "MILESTONEYEARS", "TFM_AVA", "TFM_AVA-C",
}


def scenario_files(case):
    """Map a VEDA case (via AppData/Cases.json + Groups.json) to workbook paths."""
    with open(os.path.join(MODEL, "AppData", "Cases.json"), encoding="utf-8-sig") as f:
        cases = {c["Name"]: c for c in json.load(f)}
    with open(os.path.join(MODEL, "AppData", "Groups.json"), encoding="utf-8-sig") as f:
        groups = {g["GroupName"]: g for g in json.load(f)}
    grp = groups[cases[case]["ScenarioGroup"]]
    files = []

    def add(path, scen):
        if os.path.exists(path):
            files.append((scen, path))
        else:
            files.append((scen, None))

    for s in json.loads(grp["Settings"]):
        if not s["Checked"]:
            continue
        name, kind = s["Name"], s["ShortName"]
        if kind == "B":
            for fn in sorted(os.listdir(MODEL)):
                if fn.startswith("VT_") and fn.endswith(".xlsx"):
                    add(os.path.join(MODEL, fn), "BASE")
            add(os.path.join(MODEL, "BY_Trans.xlsx"), "BASE")
        elif kind == "SR":
            d = os.path.join(MODEL, "SubRES_TMPL")
            for fn in sorted(os.listdir(d)):
                stem = fn.rsplit(".", 1)[0]
                if fn.startswith("~$"):
                    continue
                if stem.lower() in (f"subres_{name}".lower(), f"subres_{name}_trans".lower()):
                    add(os.path.join(d, fn), name)
        elif kind == "SS":
            add(os.path.join(MODEL, "SysSettings.xlsx"), name)
        elif kind == "TS":
            add(os.path.join(MODEL, "SuppXLS", "Trades", f"ScenTrade_{name}.xlsx"), name)
        else:
            d = os.path.join(MODEL, "SuppXLS")
            hit = [fn for fn in os.listdir(d)
                   if fn.rsplit(".", 1)[0].lower() == f"scen_{name}".lower()]
            add(os.path.join(d, hit[0]) if hit else os.path.join(d, f"Scen_{name}.xlsx"), name)
    # Trade links are always read by VEDA (not a scenario).
    add(os.path.join(MODEL, "SuppXLS", "Trades", "ScenTrade__Trade_Links.xlsx"), "TradeLinks")
    return files


def _grid(ws):
    """Return dict {(row, col): value} of non-empty cells (1-based)."""
    g = {}
    for row in ws.iter_rows():
        for c in row:
            v = getattr(c, "value", None)
            if v is not None and not (isinstance(v, str) and v.strip() == ""):
                g[(c.row, c.column)] = v
    return g


def col_letter(c):
    return openpyxl.utils.get_column_letter(c)


def parse_tag(v):
    if not isinstance(v, str):
        return None
    m = TAG_RE.match(v)
    if not m:
        return None
    name = m.group(1).upper()
    active = v.strip().startswith("~")
    if not active and name not in KNOWN_TAGS:
        return None
    return name, (m.group(2) or "").strip(), active


def scan_workbook(path):
    """Yield table dicts for every VEDA tag found in the workbook."""
    wbv = openpyxl.load_workbook(path, read_only=True, data_only=True)
    wbf = openpyxl.load_workbook(path, read_only=True, data_only=False)
    tables = []
    mode = None
    if "Region_selection" in wbv.sheetnames:
        mode = wbv["Region_selection"]["B8"].value
    for ws in wbv.worksheets:
        try:
            gv = _grid(ws)
        except Exception:  # chartsheets etc.
            continue
        gf = _grid(wbf[ws.title])
        if ws.title == "Region_selection":
            continue
        tagcells = []
        for (r, c), v in gv.items():
            t = parse_tag(v)
            if t:
                tagcells.append((r, c, t))
        tagcells.sort()
        tagpos = {(r, c) for r, c, _ in tagcells}
        for r, c, (name, params, active) in tagcells:
            f = gf.get((r, c))
            tag_formula = f if isinstance(f, str) and f.startswith("=") else None
            if name in ("UC_SETS",):
                tables.append(dict(sheet=ws.title, cell=f"{col_letter(c)}{r}", tag=name,
                                   params=params, active=active, tag_formula=tag_formula,
                                   tag_value=gv.get((r, c)), header=[], header_formulas=[],
                                   rows=[], row0=r, col0=c, ncols=0))
                continue
            # header row = r+1: the contiguous non-blank run through the tag column
            # (VEDA extends the header to the left of the tag cell as well).
            hr = r + 1
            tc = c
            while c > 1 and (hr, c - 1) in gv and (hr, c - 1) not in tagpos:
                c -= 1
            header, cc = [], c
            while (hr, cc) in gv and (hr, cc) not in tagpos:
                header.append(str(gv[(hr, cc)]).strip())
                cc += 1
            rows = []
            rr = hr + 1
            while True:
                vals = [gv.get((rr, c + k)) for k in range(len(header))]
                if not header or all(v is None for v in vals):
                    break
                if any((rr, c + k) in tagpos for k in range(len(header))):
                    break
                frm, fcells = {}, []
                for k in range(len(header)):
                    fv = gf.get((rr, c + k))
                    fv = fv if isinstance(fv, str) and fv.startswith("=") else None
                    fcells.append(fv)
                    if fv:
                        frm[header[k]] = fv
                # values/formulas: dict by header (convenient); cells/fcells: aligned
                # with header positions (exact, survives duplicate headers).
                rows.append(dict(row=rr, values=dict(zip(header, vals)), formulas=frm,
                                 cells=vals, fcells=fcells))
                rr += 1
            hdr_f = []
            for k in range(len(header)):
                fv = gf.get((hr, c + k))
                hdr_f.append(fv if isinstance(fv, str) and fv.startswith("=") else None)
            tables.append(dict(sheet=ws.title, cell=f"{col_letter(tc)}{r}", tag=name,
                               params=params, active=active, tag_formula=tag_formula,
                               tag_value=gv.get((r, tc)), header=header,
                               header_formulas=hdr_f, rows=rows, row0=r, col0=c,
                               ncols=len(header)))
    wbv.close()
    wbf.close()
    return mode, tables


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", default="Baseline-Sami")
    ap.add_argument("--json", help="write full table dump here")
    a = ap.parse_args()
    out = []
    for scen, path in scenario_files(a.case):
        if path is None:
            print(f"MISSING file for scenario {scen}", file=sys.stderr)
            continue
        mode, tables = scan_workbook(path)
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        out.append(dict(scenario=scen, file=rel, mode=mode, tables=tables))
        print(f"{rel}: mode={mode} tables={len(tables)}", file=sys.stderr)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(out, f, default=str, indent=0)
    print(f"{len(out)} workbooks, {sum(len(w['tables']) for w in out)} tables", file=sys.stderr)


if __name__ == "__main__":
    main()
