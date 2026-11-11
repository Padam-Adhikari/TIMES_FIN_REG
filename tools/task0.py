"""Task 0: internal link cost + national bounds / non-zero-RHS UCs -> UC_R_SUM.

READ-ONLY in this version. Default mode is the dry run: it scans the Baseline-Sami
workbooks, classifies every non-zero bound and every user constraint with a non-zero
RHS, and prints exactly which cells / sheets / tables it would write. Nothing is
written to the model. `--apply` is deliberately not implemented until Jack has
approved the dry-run output (CLAUDE.md, "Excel safety").

Usage:
    python tools/task0.py                       # dry run (scans workbooks, ~4 min)
    python tools/task0.py --scan-json scan.json # dry run reusing a veda_scan dump
    python tools/task0.py --write-audit         # also (re)write audit/task0.md
    python tools/task0.py --actcost 0.001       # proposed ACTCOST for TB_* links

Design (see audit/task0.md for the full rationale):
  * Everything is gated by the Region_selection switch, so single-region mode
    (B8 = FINTIMES) reads exactly the same values as today:
        =IF(Region_selection!$B$8=Region_selection!$D$8, <FI value>, <regional value>)
  * Existing UC tables (R_E, non-zero RHS)  -> same table, in place: UC_Sets R_E -> R_S,
    UC_RHSRT(S) -> UC_RHST(S) in Reg mode only.
  * National bounds (Sum rule)             -> new Reg-only ~UC_T table, one UC per
    bound item, R_S: AllRegions, coefficient 1, RHS = national value, same LimType,
    same interpolation option. LO/FX bounds are switched off at source in Reg mode
    (an FI-only LO/FX would pin moved activity to FI); UP bounds stay (redundant
    under the sum, never binding tighter than it).
  * External-trade bounds (Link rule), resource potentials (Split rule, Jack's
    shares), sentinel values (|v| >= 999999) and zero bounds (Copy rule) are listed
    but not changed.
"""
import argparse
import collections
import csv
import fnmatch
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
MODEL = os.path.join(ROOT, "Reg-FINTIMES")
sys.path.insert(0, HERE)
import veda_scan  # noqa: E402

SEL = "Region_selection!$B$8=Region_selection!$D$8"
CASE = "Baseline-Sami"
TRADE_PARAMS = "Reg-FINTIMES/SuppXLS/Trades/ScenTrade_TradeParameters.xlsx"
NEW_BASE_BOOK = "Reg-FINTIMES/SuppXLS/Scen_RegSum_Base.xlsx"
NEW_SHEET = "RegSum"
REGIONS = {"FI", "FI196", "FI198", "FI199", "FI19A", "FI19B", "FI1B1", "FI1C1", "FI1C2",
           "FI1C5", "FI1C6", "FI1C7", "FI1D5", "FI1D7", "FI1D8", "FI1D9", "FI1DA", "FI1DB",
           "FI1DC", "FI200"}
ALLREG = "ALLREGIONS"
# VEDA aliases (from VEDA/xl2times attribute definitions) for the attributes we touch.
ALIAS = {"ACTBND": "ACT_BND", "BNDACT": "ACT_BND", "BNDCAP": "CAP_BND", "BNDINV": "NCAP_BND",
         "IBOND": "NCAP_BND", "CBNDNET": "COM_BNDNET", "ENVBND": "COM_BNDNET",
         "CBNDPRD": "COM_BNDPRD", "CUM": "ACT_CUM", "ENVCUM": "COM_CUMNET",
         "ENV_CUMMAX": "COM_CUMNET", "IRE_XXBND": "IRE_XBND", "S_INBND": "STGIN_BND",
         "S_OUTBND": "STGOUT_BND", "SHARE": "FLO_SHAR", "SHARE-I": "FLO_SHAR",
         "SHARE-O": "FLO_SHAR", "FLOSHAR": "FLO_SHAR", "STOCK": "PRC_RESID",
         "RESID": "PRC_RESID", "PASTI": "NCAP_PASTI", "DEMAND": "COM_PROJ"}
BOUNDS = {"ACT_BND", "CAP_BND", "NCAP_BND", "FLO_BND", "COM_BNDPRD", "COM_BNDNET", "FLO_CUM",
          "ACT_CUM", "RCAP_BND", "COM_CUMPRD", "COM_CUMNET", "IRE_BND", "IRE_XBND",
          "STGIN_BND", "STGOUT_BND"}
UC_OF = {"ACT_BND": "UC_ACT", "CAP_BND": "UC_CAP", "NCAP_BND": "UC_NCAP", "FLO_BND": "UC_FLO",
         "COM_BNDPRD": "UC_COMPRD", "COM_BNDNET": "UC_COMNET"}
SHORT = {"ACT_BND": "ACT", "CAP_BND": "CAP", "NCAP_BND": "NCAP", "FLO_BND": "FLO",
         "COM_BNDPRD": "PRD", "COM_BNDNET": "NET"}
RHS_R2S = {"UC_RHSRT": "UC_RHST", "UC_RHSRTS": "UC_RHSTS", "UC_RHSR": "UC_RHS",
           "UC_RHSRS": "UC_RHSS"}
LIMS = {"UP", "LO", "FX", "N"}
DATA_TAGS = {"FI_T", "TFM_INS", "TFM_DINS", "TFM_INS-TS", "TFM_DINS-TS", "TFM_INS-AT",
             "TFM_DINS-AT", "TFM_UPD", "UC_T"}
# Non-data columns of VEDA tables (lower case).
ID_COLS = {"techname", "techdesc", "commname", "commdesc", "comm-in", "comm-out", "comm-in-a",
           "comm-out-a", "commgrp", "attribute", "attrib", "limtype", "year", "year2",
           "timeslice", "region", "curr", "currency", "other_indexes", "side", "sow", "stage",
           "uc_n", "uc_desc", "uc_attr", "attrib_cond", "top_check", "pset_pn", "pset_pd",
           "pset_ci", "pset_co", "pset_set", "cset_cn", "cset_cd", "cset_set", "pset: pn",
           "pset: co", "pset: ci", "pset:pn", "cset: cn", "cset:cn", "cset:set", "unit",
           "sourcescen", "ts_filter", "value"}
SENTINEL = 999999.0
START_YEAR = "2010"   # SysSettings ~StartYear: VEDA puts a blank year here


# --------------------------------------------------------------------------- helpers
def norm_hdr(h):
    return re.sub(r"\s+", "", str(h)).lower()


def canon(a):
    a = str(a).strip().upper()
    return ALIAS.get(a, a)


def split_hdr(h):
    """'ACT_BND~2010~UP' -> (attr, lim, year, region, other)."""
    parts = [p.strip() for p in str(h).split("~")]
    attr = canon(parts[0])
    lim = year = reg = other = None
    for p in parts[1:]:
        P = p.upper()
        if P in LIMS:
            lim = P
        elif re.fullmatch(r"\d{4}|0", P):
            year = P
        elif P in REGIONS or P == ALLREG:
            reg = P
        elif P:
            other = P
    return attr, lim, year, reg, other


def num(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return None


def col_letter(c):
    s = ""
    while c:
        c, r = divmod(c - 1, 26)
        s = chr(65 + r) + s
    return s


def xl_literal(v):
    if v is None:
        return '""'
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return repr(v)
    return '"' + str(v).replace('"', '""') + '"'


def gated(orig_value, orig_formula, reg_expr):
    """=IF(single, <original>, <regional>) keeping the original formula if any."""
    fi = orig_formula[1:] if orig_formula else xl_literal(orig_value)
    return f"=IF({SEL},{fi},{reg_expr})"


def is_ignored(v):
    """VEDA ignore marker for a row / identifier cell (a leading * is a wildcard here)."""
    return isinstance(v, str) and v.strip().upper().startswith("\\I:")


def is_ignored_col(h):
    """Ignored column: header starts with \\I: or * (comment column)."""
    return isinstance(h, str) and h.strip().upper().startswith(("\\I:", "*"))


def vmatch(name, pattern_list):
    """VEDA list match: comma list, '-' = exclude, * and ? wildcards, case-insensitive."""
    if pattern_list is None or str(pattern_list).strip() == "":
        return True
    inc, exc = [], []
    for p in str(pattern_list).split(","):
        p = p.strip().upper()
        if not p:
            continue
        (exc if p.startswith("-") else inc).append(p.lstrip("-"))
    n = name.upper()
    ok = any(fnmatch.fnmatchcase(n, p) for p in inc) if inc else True
    return ok and not any(fnmatch.fnmatchcase(n, p) for p in exc)


def has_wild(s):
    return s is not None and any(ch in str(s) for ch in "*?,-")


# --------------------------------------------------------------------------- topology
class Topology:
    """Process/commodity sets of region FI from a solved GDX (for wildcard expansion)."""

    def __init__(self, gdx):
        self.gdx = gdx
        self.ok = False
        self.prc, self.desc, self.com = set(), {}, set()
        self.top_in, self.top_out = collections.defaultdict(set), collections.defaultdict(set)
        self.sets = collections.defaultdict(set)
        exe = shutil.which("gdxdump") or next(
            (p for p in (r"C:\GAMS\54\gdxdump.exe",) if os.path.exists(p)), None)
        if not exe or not os.path.exists(gdx):
            return
        self.exe = exe
        for row in self._sym("PRC_DESC", settext=True):
            if row[0] == "FI":
                self.prc.add(row[1])
                self.desc[row[1]] = row[2] if len(row) > 2 else ""
        for row in self._sym("TOP"):
            if row[0] == "FI":
                (self.top_in if row[3].upper() == "IN" else self.top_out)[row[1]].add(row[2])
        for row in self._sym("PRC_MAP"):
            if row[0] == "FI":
                self.sets[row[2]].add(row[1].upper())
        for row in self._sym("COM_GMAP"):
            if row[0] == "FI":
                self.com.add(row[2])
        for row in self._sym("COM"):
            self.com.add(row[0])
        self.ok = bool(self.prc)

    def _sym(self, name, settext=False):
        args = [self.exe, self.gdx, f"symb={name}", "format=csv"]
        if settext:
            args.append("CSVSetText")
        res = subprocess.run(args, capture_output=True, text=True)
        rows = list(csv.reader(io.StringIO(res.stdout)))
        return rows[1:] if rows else []

    def processes(self, f):
        """f: dict of Pset_* filters -> sorted list of matching FI processes."""
        out = []
        for p in self.prc:
            if not vmatch(p, f.get("PN")):
                continue
            if f.get("PD") and not vmatch(self.desc.get(p, ""), f["PD"]):
                continue
            if f.get("CI") and not any(vmatch(c, f["CI"]) for c in self.top_in[p]):
                continue
            if f.get("CO") and not any(vmatch(c, f["CO"]) for c in self.top_out[p]):
                continue
            if f.get("SET") and not any(vmatch(s, f["SET"]) for s in self.sets[p]):
                continue
            out.append(p)
        return sorted(out)

    def commodities(self, pattern):
        return sorted(c for c in self.com if vmatch(c, pattern))


# --------------------------------------------------------------------------- extraction
class Entry:
    """One numeric value cell of a VEDA table that sets a bound / UC RHS."""
    __slots__ = ("book", "scen", "sheet", "tagcell", "tag", "row", "col", "header",
                 "attr", "lim", "year", "region", "ts", "value", "formula", "ident", "src",
                 "unit", "cls", "note", "items", "table")

    def coord(self):
        return f"{col_letter(self.col)}{self.row}"


def ident_of(t, cells, carry):
    """Identifier columns of a row (with FI_T TechName / UC_T UC_N carry-forward)."""
    d = {}
    for k, h in enumerate(t["header"]):
        n = norm_hdr(h)
        if n in ID_COLS and cells[k] is not None:
            d[n] = cells[k]
    for key in ("techname", "uc_n"):
        if key in d:
            carry[key] = d[key]
        elif key in carry:
            d[key] = carry[key]
    return d


def filters_of(ident):
    f = {}
    for k, v in ident.items():
        k2 = k.replace(" ", "").replace(":", "_")
        m = re.fullmatch(r"pset_(pn|pd|ci|co|set)", k2)
        if m:
            f[m.group(1).upper()] = str(v)
    if "techname" in ident:
        f["PN"] = str(ident["techname"])
    return f


def cset_of(ident):
    for k in ("cset_cn", "cset:cn", "cset: cn", "commname"):
        if k in ident:
            return str(ident[k])
    return None


def extract(scan):
    """Return (entries, ie_rows, uc_tables, disabled_tables)."""
    entries, ie, inactive = [], [], []
    for wb in scan:
        for t in wb["tables"]:
            if t["tag"] not in DATA_TAGS:
                continue
            if not t["active"]:
                inactive.append((wb, t))
                continue
            hdr = t["header"]
            tp = split_hdr(t["params"]) if t["params"] else None
            tag_attr = tp[0] if tp and (tp[0] in BOUNDS or tp[0].startswith("UC_")) else None
            tag_lim = tp[1] if tp else None
            if tp and not tag_attr and tp[0] in LIMS:   # e.g. "~UC_T: LO"
                tag_lim = tp[0]
            cols = {norm_hdr(h): k for k, h in enumerate(hdr)}
            carry = {}
            for r in t["rows"]:
                cells, fcells = r["cells"], r["fcells"]
                if cells and is_ignored(cells[0]):
                    continue
                ident = ident_of(t, cells, carry)
                if any(is_ignored(v) for k, v in ident.items() if k not in ("uc_desc", "techdesc")):
                    continue
                row_attr = ident.get("attribute") or ident.get("attrib")
                row_attr = canon(row_attr) if row_attr else None
                row_lim = str(ident["limtype"]).upper() if "limtype" in ident else None
                row_year = ident.get("year")
                row_reg = str(ident["region"]).upper() if "region" in ident else None
                row_ts = ident.get("timeslice")
                for k, h in enumerate(hdr):
                    if is_ignored_col(h) or norm_hdr(h) in ID_COLS:
                        continue
                    v = cells[k]
                    if v is None or num(v) is None:
                        continue
                    a, lim, year, reg, other = split_hdr(h)
                    hu = str(h).strip().upper()
                    if hu in REGIONS or hu == ALLREG or re.fullmatch(r"\d{4}|0", hu):
                        # value column: attribute from the row or the tag
                        a = row_attr or tag_attr
                        src = "row" if row_attr else "tag"
                        reg = hu if (hu in REGIONS or hu == ALLREG) else row_reg
                        year = hu if re.fullmatch(r"\d{4}|0", hu) else row_year
                        lim = row_lim or tag_lim
                    else:
                        src = "col"
                        lim = lim or row_lim or tag_lim
                        year = year if year is not None else row_year
                        reg = reg or row_reg
                    if a is None:
                        continue
                    year = None if year is None else str(year).strip()
                    is_rhs = a.startswith("UC_RHS")
                    if a not in BOUNDS and not is_rhs:
                        continue
                    if a in ("ACT_BND", "COM_BNDPRD", "FLO_BND") and not lim:
                        lim = "UP"
                    e = Entry()
                    e.book, e.scen, e.sheet, e.tagcell, e.tag = wb["file"], wb["scenario"], t["sheet"], t["cell"], t["tag"]
                    e.row, e.col, e.header = r["row"], t["col0"] + k, h
                    e.attr, e.lim, e.year, e.region = a, (lim or "UP"), year, reg
                    e.ts = str(row_ts).upper() if row_ts else None
                    e.value, e.formula, e.ident, e.src = num(v), fcells[k], ident, src
                    e.table, e.items, e.unit, e.cls, e.note = t, None, None, None, ""
                    if year == "0":
                        ie.append(e)
                    else:
                        entries.append(e)
    return entries, ie, inactive


# --------------------------------------------------------------------------- IE options
def sys_ie_rules(scan):
    """Interpolation defaults from SysSettings ~TFM_MIG rows with Year2 = 0."""
    rules = []
    for wb in scan:
        if not wb["file"].endswith("SysSettings.xlsx"):
            continue
        for t in wb["tables"]:
            if t["tag"] != "TFM_MIG" or not t["active"]:
                continue
            for r in t["rows"]:
                v = {norm_hdr(h): r["cells"][k] for k, h in enumerate(t["header"])}
                if str(v.get("year2")) != "0" or v.get("attribute") is None:
                    continue
                code = num(v.get("allregions"))
                if code is None:
                    continue
                lims = [x.strip().upper() for x in str(v.get("limtype") or "").split(",") if x.strip()]
                rules.append(dict(attr=canon(v["attribute"]), lims=lims, pn=v.get("pset_pn"),
                                  code=int(code), cell=f"{t['sheet']}!row{r['row']}"))
    return rules


def ie_code(attr, lim, proc, rules, local):
    """Explicit IE option: row/table-level (year 0) first, then SysSettings defaults."""
    if local is not None:
        return local, "table"
    code = None
    for ru in rules:                       # last matching rule wins
        if ru["attr"] != attr:
            continue
        if ru["lims"] and lim not in ru["lims"]:
            continue
        if ru["pn"] and proc and not vmatch(proc, ru["pn"]):
            continue
        if ru["pn"] and not proc:
            continue
        code = (ru["code"], f"SysSettings {ru['cell']}")
    return code if code else (None, "TIMES default")


# --------------------------------------------------------------------------- classify
def classify(entries, topo):
    for e in entries:
        if e.attr.startswith("UC_RHS"):
            e.cls = "UC"
            continue
        f = filters_of(e.ident)
        procs = None
        if e.attr not in ("COM_BNDPRD", "COM_BNDNET", "COM_CUMPRD", "COM_CUMNET"):
            if "PN" in f and not any(k in f for k in ("PD", "CI", "CO", "SET")) and not has_wild(f["PN"]):
                procs = [f["PN"]]
            elif topo.ok and f:
                procs = topo.processes(f)
            elif f:
                procs = None
        e.items = procs
        names = procs or ([f["PN"]] if "PN" in f else [])
        if e.value == 0:
            e.cls, e.note = "COPY", "zero bound: same value in every region (Copy rule)"
        elif e.lim == "N":
            e.cls, e.note = "SKIP", "LimType N is a flag, not a quantity"
        elif abs(e.value) >= SENTINEL:
            e.cls, e.note = "NONBIND", "sentinel value, not a real limit"
        elif e.attr in ("IRE_BND", "IRE_XBND") or (names and all(
                re.match(r"(IMP|EXP)", n, re.I) for n in names)):
            e.cls, e.note = "LINK", "external trade: stays on the FI hub (Link rule)"
        elif e.attr == "ACT_CUM" and e.lim == "UP":
            # cumulative UP bound: can never be tighter than a national sum, and the
            # MINSNK* sink processes exist only on the FI hub -> valid as it is
            e.cls, e.note = "KEEP", "cumulative UP bound on an FI-hub process, kept at source"
        else:
            # resource potentials (MIN*) are summed too: the national potential is what is
            # known today; the Split rule replaces the UC once regional resource data exist
            e.cls = "POT" if names and all(n.upper().startswith("MIN") for n in names) else "SUM"
            if e.attr not in UC_OF:
                e.note = f"{e.attr}: no automatic conversion (cumulative/storage) - manual"
            if e.ts and e.ts != "ANNUAL":
                e.note = f"timeslice {e.ts}: needs a TS-level UC - manual"


# --------------------------------------------------------------------------- planning
class Plan:
    def __init__(self):
        self.edits = collections.defaultdict(list)    # book -> [(sheet, cell, old, new, why)]
        self.new_tables = collections.defaultdict(list)  # book -> [table dict]
        self.need_rs = set()
        self.blocked = []
        self.notes = []
        self.copies = collections.defaultdict(list)  # book -> Reg-only TFM_INS rows

    def edit(self, book, sheet, cell, old, new, why):
        self.edits[book].append((sheet, cell, old, new, why))
        self.need_rs.add(book)


def plan_link_cost(scan, plan, actcost):
    for wb in scan:
        if wb["file"] != TRADE_PARAMS:
            continue
        for t in wb["tables"]:
            for r in t["rows"]:
                for k, h in enumerate(t["header"]):
                    if str(h).upper() == ALLREG and str(r["values"].get("Attribute", "")).upper() == "ACTCOST":
                        cell = f"{col_letter(t['col0'] + k)}{r['row']}"
                        plan.edit(wb["file"], t["sheet"], cell, r["cells"][k], actcost,
                                  f"ACTCOST on {r['values'].get('Pset_PN')} {r['cells'][k]} -> {actcost} "
                                  "(M EUR/PJ; 10 = 10 EUR/GJ = 36 EUR/MWh). Table is Reg-mode only "
                                  f"(tag {t['tag_formula']}).")
    return plan


def uc_scope(wb, sheet):
    """Ordered (UC_SETS|UC_T) tables of a sheet."""
    return [t for t in wb["tables"] if t["sheet"] == sheet and t["tag"] in ("UC_SETS", "UC_T")]


def plan_uc_tables(scan, entries, plan):
    """R_E -> R_S in place (Reg mode only) for UC tables with a non-zero RHS."""
    hit = collections.defaultdict(set)
    for e in entries:
        if e.cls == "UC" and e.value != 0:
            hit[(e.book, e.sheet)].add(e.tagcell)
    report = []
    for wb in scan:
        sheets = sorted({s for (b, s) in hit if b == wb["file"]})
        for sh in sheets:
            seq = uc_scope(wb, sh)
            # which region UC_Sets lines govern at least one non-zero-RHS table
            live, cur = set(), None
            for t in seq:
                if t["tag"] == "UC_SETS":
                    if re.match(r"\s*R_[ES]\s*:", t["params"], re.I) and t["active"]:
                        cur = t["cell"]
                elif t["active"] and t["cell"] in hit[(wb["file"], sh)] and cur:
                    live.add(cur)
            cur_r = None
            for t in seq:
                if t["tag"] == "UC_SETS":
                    if re.match(r"\s*R_[ES]\s*:", t["params"], re.I) and t["active"]:
                        cur_r = t
                    continue
                if not t["active"]:
                    continue
                nz = t["cell"] in hit[(wb["file"], sh)]
                rs = cur_r["params"] if cur_r else "(none: VEDA default R_E all regions)"
                rec = dict(book=wb["file"], sheet=sh, table=t["cell"], nonzero=nz, rset=rs,
                           ucs=sorted({str(r["values"].get(next((h for h in t["header"] if norm_hdr(h) == "uc_n"), ""), "") or "")
                                       for r in t["rows"]} - {""}))
                report.append(rec)
                if not cur_r or cur_r["cell"] not in live:
                    continue
                kind, _, regs = cur_r["params"].partition(":")
                kind, regs = kind.strip().upper(), regs.strip()
                if kind == "R_S":
                    if regs.upper() != "ALLREGIONS" and nz:
                        new = f'"~UC_Sets: R_S: AllRegions"'
                        plan.edit(wb["file"], sh, cur_r["cell"], cur_r["tag_value"],
                                  gated(cur_r["tag_value"], cur_r["tag_formula"], new),
                                  "R_S over a fixed country list excludes FI1xx regions; Reg mode -> AllRegions")
                    continue
                # R_E -> R_S (whole UC_Sets scope; zero-RHS co-tables checked below)
                key = (wb["file"], sh, cur_r["cell"])
                if key not in getattr(plan, "_done_sets", set()):
                    plan.__dict__.setdefault("_done_sets", set()).add(key)
                    plan.edit(wb["file"], sh, cur_r["cell"], cur_r["tag_value"],
                              gated(cur_r["tag_value"], cur_r["tag_formula"], '"~UC_Sets: R_S: AllRegions"'),
                              f"UC_Sets {cur_r['params']} -> R_S: AllRegions in Reg mode")
                if not nz:
                    safe = uc_zero_rhs_safe(t)
                    rec["co_table"] = safe
                    if safe != "safe":
                        plan.blocked.append(f"{wb['file']} {sh}!{t['cell']}: zero-RHS table shares the "
                                            f"UC_Sets line but {safe}; split the UC_Sets before converting")
                # tag parameter
                if "UC_RHSR" in (t["params"] or "").upper():
                    newp = re.sub(r"UC_RHSR(TS|T|S)?", lambda m: RHS_R2S["UC_RHSR" + (m.group(1) or "")],
                                  t["tag_value"], flags=re.I)
                    plan.edit(wb["file"], sh, t["cell"], t["tag_value"],
                              gated(t["tag_value"], t["tag_formula"], xl_literal(newp)),
                              "RHS attribute in tag -> region-less in Reg mode")
                # header cells
                for k, h in enumerate(t["header"]):
                    if re.match(r"UC_RHSR", str(h), re.I):
                        newh = re.sub(r"^UC_RHSR(TS|T|S)?", lambda m: RHS_R2S["UC_RHSR" + (m.group(1) or "")],
                                      str(h), flags=re.I)
                        cell = f"{col_letter(t['col0'] + k)}{t['row0'] + 1}"
                        plan.edit(wb["file"], sh, cell, h, gated(h, t["header_formulas"][k], xl_literal(newh)),
                                  "RHS column -> region-less in Reg mode")
                # Attribute-column cells naming an RHS attribute
                for r in t["rows"]:
                    for k, h in enumerate(t["header"]):
                        if norm_hdr(h) in ("attribute", "attrib") and re.match(r"UC_RHSR", str(r["cells"][k] or ""), re.I):
                            newv = re.sub(r"^UC_RHSR(TS|T|S)?", lambda m: RHS_R2S["UC_RHSR" + (m.group(1) or "")],
                                          str(r["cells"][k]), flags=re.I)
                            cell = f"{col_letter(t['col0'] + k)}{r['row']}"
                            plan.edit(wb["file"], sh, cell, r["cells"][k],
                                      gated(r["cells"][k], r["fcells"][k], xl_literal(newv)), "RHS attribute -> region-less")
                # LHS coefficients in a column headed by a single region would only
                # count that region's terms under R_S.
                rhs_tag = "UC_RHS" in (t["params"] or "").upper()
                for k, h in enumerate(t["header"]):
                    hu = str(h).strip().upper()
                    if hu in REGIONS and not rhs_tag:
                        lhs = [r for r in t["rows"] if r["cells"][k] not in (None, "") and
                               not str((r["values"].get("Attribute") or "")).upper().startswith("UC_RHS")]
                        if lhs:
                            cell = f"{col_letter(t['col0'] + k)}{t['row0'] + 1}"
                            plan.edit(wb["file"], sh, cell, h, gated(h, t["header_formulas"][k], '"AllRegions"'),
                                      f"LHS coefficients headed '{h}' -> AllRegions so every region's terms are summed")
                # internal trade links must not count as national exports/imports
                for r in t["rows"]:
                    for k, h in enumerate(t["header"]):
                        if norm_hdr(h) in ("pset_pn",) and isinstance(r["cells"][k], str) \
                                and re.search(r"(^|,)\s*TB\*", r["cells"][k], re.I):
                            cell = f"{col_letter(t['col0'] + k)}{r['row']}"
                            newv = r["cells"][k] + ",-TB_*_FI*_FI*"
                            plan.edit(wb["file"], sh, cell, r["cells"][k],
                                      gated(r["cells"][k], r["fcells"][k], xl_literal(newv)),
                                      "exclude internal links TB_<C>_FI*_FI* from national trade sums")
    return report


def uc_zero_rhs_safe(t):
    """A zero-RHS UC stays equivalent under R_S if it is UP with only non-negative
    coefficients (sum <= 0 of non-negative terms == each <= 0)."""
    lims = {str(r["values"].get("LimType") or "").upper() for r in t["rows"]} - {""}
    tl = split_hdr(t["params"])[1] if t["params"] else None
    lims |= {tl} if tl else set()
    if lims - {"UP"}:
        return f"LimType {sorted(lims)}"
    for r in t["rows"]:
        for k, h in enumerate(t["header"]):
            a = split_hdr(h)[0]
            v = num(r["cells"][k])
            if v is not None and a.startswith("UC_") and not a.startswith("UC_RHS") and v < 0:
                return f"negative coefficient in {h}"
            if v is not None and str(h).upper() in REGIONS | {ALLREG} and v < 0 and "RHS" not in (t["params"] or "").upper():
                return f"negative coefficient in {h}"
    return "safe"


def plan_bounds(scan, entries, ie_entries, plan, rules, topo):
    """Sum-rule bounds -> Reg-only UC tables; LO/FX sources switched off in Reg mode."""
    # local IE options (year 0) per (book, table, attr, lim, item)
    local_ie = {}
    for e in ie_entries:
        if e.attr in BOUNDS:
            f = filters_of(e.ident)
            key = (e.book, e.tagcell, e.attr, e.lim, f.get("PN"), cset_of(e.ident))
            local_ie[key] = int(e.value)
    ucs = collections.OrderedDict()   # uc name -> dict
    disable_units = collections.OrderedDict()
    for e in entries:
        if e.cls not in ("SUM", "POT") or e.note:
            if e.cls in ("SUM", "POT") and e.note:
                plan.blocked.append(f"{e.book} {e.sheet}!{e.coord()} {e.attr} {e.lim} {e.value}: {e.note}")
            continue
        f = filters_of(e.ident)
        comm = cset_of(e.ident)
        items = []
        if e.attr in ("COM_BNDPRD", "COM_BNDNET"):
            cs = topo.commodities(comm) if (topo.ok and has_wild(comm)) else [c.strip() for c in str(comm).split(",")]
            items = [(None, c) for c in cs]
        elif e.attr == "FLO_BND":
            cdef = e.ident.get("comm-out") or e.ident.get("comm-in") or comm
            procs = e.items or []
            for p in procs:
                for c in (topo.top_in[p] | topo.top_out[p]) if topo.ok else {cdef}:
                    if vmatch(c, cdef):
                        items.append((p, c))
        else:
            items = [(p, None) for p in (e.items or [])]
        if not items:
            plan.blocked.append(f"{e.book} {e.sheet}!{e.coord()} {e.attr} {e.lim}={e.value}: selector "
                                f"{f or comm} matched nothing in the topology GDX - check after sync")
            continue
        if len(items) > 1:
            e.note = f"selector matches {len(items)} items -> one UC each (VEDA applies the bound per item)"
        lim = "FX" if e.lim == "FX" else e.lim
        for p, c in items:
            name = "RS_" + SHORT[e.attr] + "_" + "_".join(x for x in (p, c) if x) + "_" + lim
            if len(name) > 60:
                name = name[:52] + "_" + hashlib.md5(name.encode()).hexdigest()[:6]
            key = (e.book, e.tagcell, e.attr, e.lim, f.get("PN"), comm)
            code, src = ie_code(e.attr, e.lim, p, rules, local_ie.get(key))
            uc = ucs.setdefault(name, dict(name=name, attr=e.attr, coef=UC_OF[e.attr], p=p, c=c,
                                           lim=lim, rhs={}, ie=code, ie_src=src, srcs=set(),
                                           home=home_book(e.book)))
            if code is not None and uc["ie"] != code:
                if uc["ie"] is not None and uc["ie_src"] == "table" and src == "table":
                    plan.notes.append(f"{name}: interpolation option {uc['ie']} and {code} in different "
                                      f"tables; using {code} (later source)")
                if uc["ie"] is None or src == "table":
                    uc["ie"], uc["ie_src"] = code, src
            uc["srcs"].add(f"{os.path.basename(e.book)} {e.sheet}!{e.coord()}")
        # LO / FX must not stay on FI alone in Reg mode
        if e.lim in ("LO", "FX"):
            unit = source_unit(e)
            disable_units.setdefault(unit[:3], (unit, []))[1].append(e)
    # RHS = the value VEDA ends up with: replay EVERY value of the same attribute / limit /
    # item / year in scenario order (zeros and other classes included); last one wins.
    # A blank year is VEDA's start year.
    bykey = {(u["attr"], u["lim"], u["p"], u["c"]): u for u in ucs.values()}
    for e in entries:
        if e.attr not in UC_OF or e.lim == "N":
            continue
        y = e.year or START_YEAR
        if e.attr in ("COM_BNDPRD", "COM_BNDNET"):
            comm = cset_of(e.ident)
            keys = [(e.attr, e.lim, None, c.strip()) for c in str(comm or "").split(",")]
        elif e.attr == "FLO_BND":
            cdef = e.ident.get("comm-out") or e.ident.get("comm-in") or cset_of(e.ident)
            keys = [k for k in bykey if k[0] == "FLO_BND" and k[1] == e.lim and k[2] in (e.items or [])
                    and vmatch(k[3], cdef)]
        else:
            keys = [(e.attr, e.lim, p, None) for p in (e.items or [])]
        for k in keys:
            u = bykey.get(k)
            if u is None:
                continue
            if y in u["rhs"] and u["rhs"][y] != e.value:
                plan.notes.append(f"{u['name']} {y}: {u['rhs'][y]:g} -> {e.value:g} "
                                  f"({os.path.basename(e.book)} {e.sheet}!{e.coord()}, later value wins)")
            u["rhs"][y] = e.value
    for name in list(ucs):
        u = ucs[name]
        if u["lim"] == "LO" and all(v == 0 for v in u["rhs"].values()):
            plan.notes.append(f"{name}: dropped - every LO value is overridden to 0, so the bound "
                              "does not exist in the single-region model either")
            del ucs[name]
    # source switches
    for (book, sheet, cell), (unit, es) in disable_units.items():
        kind, old, oldf, reg = unit[3], unit[4], unit[5], unit[6]
        if kind == "cell":
            deps = dependents(book, sheet, cell)
            if deps:
                plan.blocked.append(f"{book} {sheet}!{cell} {es[0].attr} {es[0].lim}={old}: cannot blank "
                                    f"the value cell, formulas depend on it ({', '.join(deps[:4])})")
                continue
        plan.edit(book, sheet, cell, old, gated(old, oldf, reg),
                  f"switch off {kind} in Reg mode ({len(es)} LO/FX value(s) now in RS_* UCs)")
    for uc in ucs.values():
        plan.new_tables[uc["home"]].append(uc)
        plan.need_rs.add(uc["home"])
    # every value in a switched-off unit must be re-created
    for (book, sheet, cell), (unit, es) in disable_units.items():
        if unit[3] == "cell":
            continue
        tagcell = es[0].tagcell
        for e in entries:
            if e.book != book or e.sheet != sheet or e.tagcell != tagcell or not in_unit(e, unit):
                continue
            if e.cls in ("SUM", "POT") and e.value != 0 and e.attr in UC_OF and not (e.ts and e.ts != "ANNUAL"):
                continue          # has its own RS_* UC
            # a zero next to a non-zero value for the same key in the same row is a
            # duplicate VEDA overrides (e.g. VT_SUP 'ACT_BND' helper column): never copy it
            if e.value == 0 and any(x.row == e.row and x.attr == e.attr and x.lim == e.lim
                                    and x.year == e.year and x.value != 0 for x in es):
                plan.notes.append(f"{os.path.basename(book)} {sheet}!{e.coord()}: zero {e.attr} {e.lim} "
                                  f"{e.year} duplicates a non-zero value in the same row; not copied")
                continue
            # zero (Copy rule) -> every region; anything else keeps its original region
            reg = ALLREG if e.value == 0 else (e.region or "FI")
            plan.copies[home_book(book)].append(dict(
                attr=e.attr, lim=e.lim, year=e.year, ts=e.ts, region=reg, value=e.value,
                sel=filters_of(e.ident),
                cset=cset_of(e.ident) or e.ident.get("comm-out") or e.ident.get("comm-in"),
                src=f"{os.path.basename(book)} {sheet}!{e.coord()}", cls=e.cls))
            plan.need_rs.add(home_book(book))
    return ucs


def home_book(book):
    """Where the Reg-only UC table goes: same workbook for Scen_ files (keeps scenario
    membership); one new early scenario file for BASE / SubRES sources."""
    return book if "/SuppXLS/Scen_" in book else NEW_BASE_BOOK


def source_unit(e):
    """(book, sheet, cell, kind, old, old_formula, reg_expr) that switches the value off."""
    t = e.table
    hdr = t["header"]
    if e.src == "col":
        k = e.col - t["col0"]
        return (e.book, e.sheet, f"{col_letter(e.col)}{t['row0'] + 1}", "column", hdr[k],
                t["header_formulas"][k], xl_literal("\\I:" + str(hdr[k])))
    if e.src == "row":
        k = next(i for i, h in enumerate(hdr) if norm_hdr(h) in ("attribute", "attrib"))
        r = next(r for r in t["rows"] if r["row"] == e.row)
        other = [h for i, h in enumerate(hdr) if i != k and r["cells"][i] is not None
                 and split_hdr(h)[0] not in BOUNDS and norm_hdr(h) not in ID_COLS
                 and str(h).upper() not in REGIONS | {ALLREG} and not re.fullmatch(r"\d{4}|0", str(h))]
        # a row that carries a TechName for the rows below must stay readable
        ti = next((i for i, h in enumerate(hdr) if norm_hdr(h) == "techname"), None)
        nxt = next((x for x in t["rows"] if x["row"] > e.row), None)
        carries = (ti is not None and r["cells"][ti] not in (None, "") and nxt is not None
                   and nxt["cells"][ti] in (None, ""))
        if not other and not carries:
            return (e.book, e.sheet, f"{col_letter(t['col0'] + k)}{e.row}", "row", r["cells"][k],
                    r["fcells"][k], '"\\I:"')
    return (e.book, e.sheet, e.coord(), "cell", e.value, e.formula, '""')


_FORMULAS = {}
_REF = re.compile(r"(?:(?:'([^']+)'|([A-Za-z0-9_\.]+))!)?\$?([A-Z]{1,3})\$?(\d+)(?::\$?([A-Z]{1,3})\$?(\d+))?")


def _col_num(s):
    n = 0
    for ch in s:
        n = n * 26 + ord(ch) - 64
    return n


def dependents(book, sheet, cell):
    """Cells whose formula references book!sheet!cell (read-only scan, cached per book)."""
    import openpyxl
    if book not in _FORMULAS:
        wb = openpyxl.load_workbook(os.path.join(ROOT, book), read_only=True, data_only=False)
        lst = []
        for ws in wb.worksheets:
            try:
                for row in ws.iter_rows():
                    for c in row:
                        v = getattr(c, "value", None)
                        if isinstance(v, str) and v.startswith("="):
                            lst.append((ws.title, c.coordinate, v))
            except Exception:
                continue
        wb.close()
        _FORMULAS[book] = lst
    tc = _col_num(re.match(r"[A-Z]+", cell).group(0))
    tr = int(re.search(r"\d+", cell).group(0))
    hits = []
    for sh, coord, f in _FORMULAS[book]:
        for m in _REF.finditer(f.replace('"', ' " ')):
            ref_sheet = m.group(1) or m.group(2) or sh
            if ref_sheet != sheet:
                continue
            c1, r1 = _col_num(m.group(3)), int(m.group(4))
            c2, r2 = (_col_num(m.group(5)), int(m.group(6))) if m.group(5) else (c1, r1)
            if c1 <= tc <= c2 and r1 <= tr <= r2 and not (sh == sheet and coord == cell):
                hits.append(f"{sh}!{coord}")
                break
    return hits


def in_unit(e, unit):
    kind = unit[3]
    col = re.match(r"[A-Z]+", unit[2]).group(0)
    row = int(re.search(r"\d+", unit[2]).group(0))
    if kind == "column":
        return col_letter(e.col) == col and e.row > row
    if kind == "row":
        return e.row == row
    return False


# --------------------------------------------------------------------------- output
def fmt_uc_table(ucs):
    lines = ["    UC_N | coef | Pset_PN | Cset_CN | LimType | RHS by year (UC_RHST) | UC_RHST~0 (IE) | from"]
    for u in ucs:
        rhs = ", ".join(f"{y}:{v:g}" for y, v in sorted(u["rhs"].items()))
        lines.append(f"    {u['name']} | {u['coef']}=1 | {u['p'] or ''} | {u['c'] or ''} | {u['lim']} | "
                     f"{rhs} | {u['ie'] if u['ie'] is not None else '-'} ({u['ie_src']}) | "
                     f"{'; '.join(sorted(u['srcs']))}")
    return "\n".join(lines)


def print_plan(plan, scan, entries, inactive, uc_report, ucs, actcost, out):
    w = out.write
    have_rs = {wb["file"] for wb in scan if wb["mode"]}
    w("=" * 100 + "\nTASK 0 DRY RUN - nothing has been written.\n" + "=" * 100 + "\n")
    w(f"Case scanned: {CASE} ({len(scan)} workbooks).  Formula used for every switch:\n"
      f"  =IF({SEL}, <single-region value>, <Reg-FINTIMES value>)\n\n")
    books = sorted(set(plan.edits) | set(plan.new_tables) | set(plan.copies))
    for b in books:
        w(f"--- {b}\n")
        if b in plan.need_rs and b not in have_rs:
            w(f"  + add sheet Region_selection (copy of {TRADE_PARAMS} Region_selection, B8 = FINTIMES)\n")
        if b == NEW_BASE_BOOK:
            w("  + NEW workbook (scenario 'RegSum_Base'): add it to every case right after SysSettings,\n"
              "    before the first SuppXLS scenario, so later scenarios still override it.\n")
        for sheet, cell, old, new, why in plan.edits.get(b, []):
            w(f"  ~ '{sheet}'!{cell}: {old!r}\n      -> {new}\n      ({why})\n")
        if plan.new_tables.get(b):
            u = plan.new_tables[b]
            w(f"  + sheet '{NEW_SHEET}': gated tags (Reg mode only)\n"
              f"      B2 =IF({SEL},\"UC_Sets: R_S: AllRegions\",\"~UC_Sets: R_S: AllRegions\")\n"
              f"      B3 =IF({SEL},\"UC_Sets: T_E:\",\"~UC_Sets: T_E:\")\n"
              f"      B5 =IF({SEL},\"UC_T\",\"~UC_T\")   {len(u)} constraints:\n")
            w(fmt_uc_table(u) + "\n")
        if plan.copies.get(b):
            cp = plan.copies[b]
            w(f"  + sheet '{NEW_SHEET}': Reg-only copy of values whose source row/column is switched off\n"
              f"      tag =IF({SEL},\"TFM_INS\",\"~TFM_INS\")   {len(cp)} rows:\n"
              "    Attribute | LimType | Year | Pset filters | Cset | Region | Value | class | from\n")
            for c in cp:
                sel = " ".join(f"Pset_{k}={v}" for k, v in c["sel"].items())
                w(f"    {c['attr']} | {c['lim']} | {c['year'] or ''} | {sel} | {c['cset'] or ''} | "
                  f"{c['region']} | {c['value']:g} | {c['cls']} | {c['src']}\n")
        w("\n")
    if plan.blocked:
        w("NOT HANDLED AUTOMATICALLY (need a decision or manual table):\n")
        for x in plan.blocked:
            w(f"  ! {x}\n")
        w("\n")
    if plan.notes:
        w("NOTES:\n" + "".join(f"  - {x}\n" for x in plan.notes) + "\n")
    c = collections.Counter(e.cls for e in entries if e.value != 0 and not e.attr.startswith("UC_RHS"))
    w(f"Non-zero bound values by class: {dict(c)}\n")
    w(f"Edits: {sum(len(v) for v in plan.edits.values())} cells in {len(plan.edits)} workbooks; "
      f"new RS_* constraints: {len(ucs)}; workbooks needing a Region_selection sheet: "
      f"{len([b for b in plan.need_rs if b not in have_rs])}\n")


# --------------------------------------------------------------------------- audit
def write_audit(path, scan, entries, inactive, uc_report, ucs, plan, actcost, topo):
    from task0_audit import render
    with open(path, "w", encoding="utf-8") as f:
        f.write(render(scan=scan, entries=entries, inactive=inactive, uc_report=uc_report,
                       ucs=ucs, plan=plan, actcost=actcost, topo=topo, CASE=CASE))


# --------------------------------------------------------------------------- verify
_REG_ARG = re.compile(r',("(?:[^"]|"")*")\)$')


def verify_copy(plan):
    """Run on a COPY after --apply (the plan is recomputed from the pre-apply scan)."""
    from task0_apply import flip_and_read, _same
    if os.path.exists(os.path.join(ROOT, ".git")):
        return "--verify flips workbooks: run it only on a copy of the model, not in the repository"
    books = sorted(set(plan.edits) | set(plan.new_tables) | set(plan.copies))
    cells = [(b, sh, c) for b in plan.edits for (sh, c, *_ ) in plan.edits[b]]
    expect_reg, expect_single = {}, {}
    for b in plan.edits:
        for sh, c, old, new, why in plan.edits[b]:
            expect_single[(b, sh, c)] = old
            if isinstance(new, str) and new.startswith("=IF("):
                m = _REG_ARG.search(new)
                expect_reg[(b, sh, c)] = m.group(1)[1:-1].replace('""', '"') if m else None
            else:
                expect_reg[(b, sh, c)] = new
    reg = flip_and_read(ROOT, books, cells, "Reg-FINTIMES")
    bad = [f"REG  {k}: {reg.get(k)!r} != {v!r}" for k, v in expect_reg.items()
           if not _same(reg.get(k) if reg.get(k) != "" else None, v if v != "" else None)]
    single = flip_and_read(ROOT, books, cells, "FINTIMES")
    for k, v in expect_single.items():
        exp = expect_reg[k] if not str(plan_new(plan, k)).startswith("=") else v
        if not _same(single.get(k), exp):
            bad.append(f"SINGLE {k}: {single.get(k)!r} != {exp!r}")
    for x in bad:
        print("  !", x)
    print(f"verify: {len(cells)} switched cells checked in both modes, {len(bad)} problems")
    return 1 if bad else 0


def plan_new(plan, key):
    b, sh, c = key
    return next(new for (s2, c2, old, new, why) in plan.edits[b] if s2 == sh and c2 == c)


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scan-json", help="reuse a dump from tools/veda_scan.py --json (else scan now)")
    ap.add_argument("--topology-gdx", default=os.path.join(MODEL, "AppData", "GAMSSAVE", "baseline.gdx"),
                    help="solved GDX used to expand wildcard selectors (FI processes/topology)")
    ap.add_argument("--actcost", type=float, default=1e-4, help="new ACTCOST for TB_* links (M EUR/PJ)")
    ap.add_argument("--write-audit", action="store_true", help="(re)write audit/task0.md")
    ap.add_argument("--apply", action="store_true",
                    help="write the plan with xlwings (only after the dry run is approved)")
    ap.add_argument("--verify", action="store_true",
                    help="ON A COPY OF THE MODEL ONLY: flip the edited workbooks to Reg-FINTIMES, check "
                         "every switched cell, flip back and check single-region values are unchanged")
    a = ap.parse_args()
    if a.scan_json:
        with open(a.scan_json, encoding="utf-8") as f:
            scan = json.load(f)
    else:
        scan = []
        for scen, path in veda_scan.scenario_files(CASE):
            if path:
                mode, tables = veda_scan.scan_workbook(path)
                scan.append(dict(scenario=scen, file=os.path.relpath(path, ROOT).replace("\\", "/"),
                                 mode=mode, tables=tables))
    topo = Topology(a.topology_gdx)
    entries, ie_entries, inactive = extract(scan)
    classify(entries, topo)
    rules = sys_ie_rules(scan)
    plan = Plan()
    plan_link_cost(scan, plan, a.actcost)
    uc_report = plan_uc_tables(scan, entries, plan)
    ucs = plan_bounds(scan, entries, ie_entries, plan, rules, topo)
    if not topo.ok:
        plan.notes.append(f"topology GDX not readable ({a.topology_gdx}); wildcard selectors not expanded")
    else:
        plan.notes.append(f"wildcards expanded with {os.path.relpath(a.topology_gdx, ROOT)} "
                          f"({len(topo.prc)} FI processes) - this GDX is older than the current files; "
                          "re-check the expansions when a fresh Baseline-Sami GDX is pushed")
    if a.verify:
        sys.exit(verify_copy(plan))
    print_plan(plan, scan, entries, inactive, uc_report, ucs, a.actcost, sys.stdout)
    if a.apply:
        if plan.blocked:
            sys.exit("refusing --apply: items in 'NOT HANDLED AUTOMATICALLY' need a decision first")
        from task0_apply import apply_plan
        print("\nAPPLYING (xlwings) ...")
        res = apply_plan(plan, ROOT, TRADE_PARAMS, SEL, NEW_SHEET)
        bad = {b: r for b, r in res.items() if r != "ok"}
        print(f"applied: {len(res) - len(bad)} workbooks ok, {len(bad)} failed")
        if bad:
            sys.exit(1)
    if a.write_audit:
        p = os.path.join(ROOT, "audit", "task0.md")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        write_audit(p, scan, entries, inactive, uc_report, ucs, plan, a.actcost, topo)
        print(f"\nwrote {os.path.relpath(p, ROOT)}")


if __name__ == "__main__":
    main()
