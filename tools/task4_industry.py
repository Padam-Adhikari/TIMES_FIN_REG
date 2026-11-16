"""Task 4a (industry, single sites): rest of steel, refinery and coke oven, HVO, copper, glass and
refinery-gas autoproducers to their regions. Design: audit/task4_industry.md.

Mechanisms (all Reg mode only; single-region values unchanged):
  * switch  - a data table whose moved processes all go to ONE site and that holds no other process:
              its `FI` header becomes the site (as in the steel pilot); the process is declared only there.
  * copy    - otherwise: the process is declared on FI and in its regions; FI keeps its calibrated
              coefficients with stock 0; a Reg-only sheet `Reg_<book>` carries one row per calibrated
              `FI` cell with one column per region: formulas on the original cell (coefficients
              copied, STOCK x regional share). The FI STOCK cell gets 0 in Reg mode.
  * SubRES  - HVO: availability and existing capacity (by vintage) in its two sites (Trans file).
  * UCs     - FI-only constraints over moved processes become national (R_S AllRegions, RHS without
              region, FI coefficient column -> AllRegions).
  * Commodities used by moved processes are declared in every region (SysSettings 'Comms');
    links hub <-> region for every non-ENV commodity they use (new sheet in ScenTrade__Trade_Links).

    python tools/task4_industry.py                 # dry run -> audit/task4a_dryrun.txt
    python tools/task4_industry.py --apply
"""
import argparse
import collections
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from task0 import ROOT, SEL  # noqa: E402
from task3_power import (BLUE, GREEN, ORANGE, YELLOW, REG19, Book, Plan, apply, col_idx, col_let, q,  # noqa: E402
                         regonly, sw)
from veda_tables import read_tables, tech_rows  # noqa: E402

M = "Reg-FINTIMES/"
IND = M + "VT_FINTIMES_IND.xlsx"
SUP = M + "VT_FINTIMES_SUP.xlsx"
SYS = M + "SysSettings.xlsx"
LINKS = M + "SuppXLS/Trades/ScenTrade__Trade_Links.xlsx"
LINK_SHEET = "FI internal trades industry"
BRF_T = M + "SubRES_TMPL/SubRES_22_TECHS_BIOREFINERIES_Trans.xlsx"
KEYS = os.path.join(ROOT, "data", "keys")
MARK = "Task 4a (tools/task4_industry.py)"
ALL = '_xlfn.TEXTJOIN(",",TRUE,Region_selection!$K$8:$AD$8)'

# process -> site region or key file (data/keys/<key>.csv)
MOVE_4A = {
    # SSAB Raahe integrated works (with the pilot blast-furnace route in FI1D9)
    "IISBOXFUR00": "FI1D9", "IISBOXSCR00": "FI1D9", "IISSINTER00": "FI1D9", "IISPELLET00": "FI1D9",
    "IISDRIEAF00": "FI1D9", "IISDRISPN00": "FI1D9", "IISCUPOLA00": "FI1D9",
    # Outokumpu Tornio: ferrochrome and stainless (AOD)
    "IISFECRFR00": "FI1D7", "IISAODFUR00": "FI1D7",
    # electric-arc furnaces Tornio / Ovako Imatra; finishing and steel heat by site allocation
    "IISELAFUR00": "ind_iis_eaf_2013-2020", "IISFINPRO00": "ind_iis_2013-2020", "INDIISHTH00": "ind_iis_2013-2020",
    # Boliden Harjavalta (and Pori)
    "ICUFINPRO00": "FI196", "ICUOREPRD00": "FI196", "ICURECPRD00": "FI196",
    # Karhula packaging glass
    "IGHHOLLOW00": "FI1C7", "IGHRECYCL00": "FI1C7", "IGFFLATGL00": "FI1C7",
    # Neste Porvoo refinery and its refinery-gas autoproducers; SSAB Raahe coke oven
    "SSCDRFLX00": "FI1B1", "SUPREFHTH00": "FI1B1", "CHPAUTOGENRFG00": "FI1B1",
    "SSCDCOKE00": "FI1D9",
}
# HVO: vintages of BRF1_HVO (SubRES_22 'SUP_Gen1': PASTI~2007 200, ~2009 200, ~2015 120 kt) =
# Neste Porvoo NEXBTL 1 (2007) and 2 (2009), UPM Lappeenranta BioVerno (2015, 120 kt)
HVO = {"FI1B1": {2007: 200, 2009: 200}, "FI1C5": {2015: 120}}
UC_NATIONAL = [  # (book, sheet, UC_Sets cell)
    (M + "SuppXLS/Scen_UC-IND.xlsx", "UC-IIS", "B2"),          # steel route shares TUC_Istruc_CST-*
    (M + "SuppXLS/Scen_UC-IND.xlsx", "CHPShares", "B1"),       # UCI_UP_CHPShare-* (refinery-gas CHP)
    (M + "SuppXLS/Scen_REFINERIES_Lim.xlsx", "UCT4", "B2"),    # UC_Refineries_Lim
]
DESCR = {"TechName", "Attribute", "LimType", "Year", "TimeSlice", "CommName", "Comm-IN", "Comm-IN-A",
         "Comm-OUT", "Comm-Out", "Comm-OUT-A", "CommGrp", "Other_Indexes", "Curr", "Cset_CN"}


def load_key(name):
    s = {r["region"]: float(r["share"]) for r in csv.DictReader(open(os.path.join(KEYS, name + ".csv"), encoding="utf-8"))
         if r["region"] in REG19}
    assert abs(sum(s.values()) - 1) < 1e-9, name
    return {k: v for k, v in s.items() if v > 0}


def shares_of(move):
    out = {}
    for p, tgt in move.items():
        out[p] = {tgt: 1.0} if tgt in REG19 else load_key(tgt)
    return out


def sheet_ref(sheet, cell):
    return f"'{sheet}'!{cell}" if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", sheet) else f"{sheet}!{cell}"


def inner(b, sheet, cell):
    """Expression of a cell usable inside IF(): its formula (without '=', refs qualified) or its constant."""
    f = b.f.get((sheet, cell))
    if f:
        expr = f[1:]
        # qualify bare cell references with the sheet (the expression may be used on another sheet)
        return re.sub(r"(?<![!A-Za-z_$'])(\$?[A-Z]{1,3}\$?\d+)(?![\d(])", lambda m: sheet_ref(sheet, m.group(1)), expr)
    v = b.val(sheet, cell)
    return q(v) if isinstance(v, str) else repr(float(v))


# ------------------------------------------------------------------------------- workbook data
def plan_book(plan, book, move, shares, notes):
    """Declarations + data of moved processes in one VEDA BY workbook."""
    b = Book(book)
    T = read_tables(os.path.join(ROOT, book))
    data = [t for t in T if t["tag"].upper().startswith("~FI_T")]
    procs = [t for t in T if t["tag"].upper().startswith("~FI_PROCESS")]
    # mode per process: switch if all its FI-data tables are single-destination tables of moved processes
    tables_of = collections.defaultdict(list)
    for t in data:
        for p in tech_rows(t):
            if p in move:
                tables_of[p].append(t)
    def single_dest(t):
        tr = tech_rows(t)
        tg = {move.get(p) for p in tr}
        return all(p in move for p in tr) and len(tg) == 1 and next(iter(tg)) in REG19
    mode = {}
    for p in move:
        if p not in tables_of and not any(r for t in procs for r in t["rows"]
                                          if r["cells"].get("TechName", (0, None))[1] == p):
            continue
        mode[p] = "switch" if tables_of[p] and all(single_dest(t) for t in tables_of[p]) else "copy"
    # 1. declarations
    for t in procs:
        rc = t["cols"].get("Region")
        for r in t["rows"]:
            p = r["cells"].get("TechName", (0, None))[1]
            if p not in mode:
                continue
            cell = f"{col_let(rc)}{r['row']}"
            f = b.f.get((t["sheet"], cell))
            if f and SEL in f:
                notes.append(f"{p}: Region cell {t['sheet']}!{cell} already switched (pilot) - kept")
                continue
            if b.val(t["sheet"], cell) != "FI":
                sys.exit(f"{book} {t['sheet']}!{cell}: Region of {p} is {b.val(t['sheet'], cell)!r}")
            regs = sorted(shares[p])
            new = ",".join(regs) if mode[p] == "switch" else ",".join(["FI"] + regs)
            plan.edit(book, t["sheet"], cell, "FI", sw('"FI"', q(new)), BLUE,
                      f"{p} ({mode[p]}): declared in {new} in Reg mode")
    # 2. switch tables: FI header -> site
    for t in data:
        tr = tech_rows(t)
        if not any(p in mode for p in tr):
            continue
        if single_dest(t) and all(mode.get(p) == "switch" for p in tr if p in move):
            site = move[next(iter(tr))]
            if "FI" not in t["cols"]:
                if t["tag"].upper().replace(" ", "").endswith(":FI"):
                    plan.edit(book, t["sheet"], t["tag_cell"], t["tag"], sw(q(t["tag"]), q(t["tag"][:-2] + site)), BLUE,
                              f"table of {sorted(tr)} for {site} only")
                continue
            cell = f"{col_let(t['cols']['FI'])}{t['header_row']}"
            f = b.f.get((t["sheet"], cell))
            if f and SEL in f:
                continue
            old = f[1:] if f else q("FI")
            plan.edit(book, t["sheet"], cell, "FI", sw(old, q(site)), BLUE,
                      f"FI data of {sorted(tr)} -> {site} (single site)")
    # 3. copy tables: Reg sheet rows + FI STOCK -> 0
    rows_out = collections.defaultdict(list)      # (tag, descriptor header tuple) -> rows
    for t in data:
        tr = tech_rows(t)
        cp = [p for p in tr if mode.get(p) == "copy"]
        if not cp:
            continue
        if "FI" not in t["cols"]:
            notes.append(f"{book} {t['sheet']} {t['tag_cell']} {t['tag']}: no FI column for {cp} - nothing to copy")
            continue
        desc = [h for h in t["cols"] if h in DESCR]
        att_col = "Attribute" in t["cols"]
        for p in cp:
            for r in tr[p]:
                c = r["cells"]
                if "FI" not in c:
                    continue
                fic = c["FI"][0]
                att = str(c.get("Attribute", ("", ""))[1] or "").upper()
                is_stock = att == "STOCK" or (not att_col and "STOCK" in t["tag"].upper())
                vals = {}
                for reg, s in shares[p].items():
                    ref = sheet_ref(t["sheet"], fic)
                    if is_stock:
                        vals[reg] = (f"={ref}*{s!r}", ORANGE)
                    else:
                        vals[reg] = (f"={ref}", GREEN)
                d = {h: (p if h == "TechName" else c.get(h, (None, None))[1]) for h in desc}
                if "TechName" not in d:
                    d["TechName"] = p
                rows_out[(t["tag"], tuple(sorted(d)))].append((d, vals, f"{t['sheet']}!{fic}"))
                if is_stock:
                    # the stock cell itself stays untouched (other stock cells refer to it); in Reg mode
                    # the row becomes a VEDA comment ('*' in TechName), so FI's copy has no stock
                    tnc = f"{col_let(t['cols']['TechName'])}{r['row']}"
                    tv = b.val(t["sheet"], tnc)
                    if tnc in [e[1] for e in plan.edits.get(book, []) if e[0] == t["sheet"]]:
                        pass
                    elif tv == p:
                        plan.edit(book, t["sheet"], tnc, p, sw(q(p), q(f"*{p} stock: Reg sheet")), BLUE,
                                  f"{p}: FI copy keeps coefficients, no stock (stock in {sorted(shares[p])})")
                    elif tv is None:
                        plan.edit(book, t["sheet"], tnc, None, regonly(q(f"*{p} stock: Reg sheet")), BLUE,
                                  f"{p}: FI copy keeps coefficients, no stock (stock in {sorted(shares[p])})")
                    else:
                        sys.exit(f"{book} {t['sheet']}!{tnc}: unexpected TechName {tv!r} on the stock row of {p}")
                    # keep the block context for the rows after the comment
                    nxt = [x for x in tr[p] if x["row"] == r["row"] + 1]
                    if nxt and "TechName" not in nxt[0]["cells"]:
                        nc = f"{col_let(t['cols']['TechName'])}{r['row'] + 1}"
                        plan.edit(book, t["sheet"], nc, None, regonly(q(p)), BLUE,
                                  f"{p}: process name repeated after the commented stock row")
    if rows_out:
        sheet = "Reg_" + os.path.basename(book).split("_")[-1].split(".")[0]
        cells = [("A1", f"{MARK}: data of processes in several regions (one column per region; formulas on the "
                        f"original FI cells; STOCK x regional share). Green = copied, orange = split.", None)]
        r0 = 3
        for (tag, keys), rows in rows_out.items():
            desc = [h for h in ("TechName", "Attribute", "LimType", "Year", "TimeSlice", "CommName", "Comm-IN",
                                "Comm-IN-A", "Comm-OUT", "Comm-Out", "CommGrp", "Other_Indexes", "Curr") if h in keys]
            cells.append((f"B{r0}", f'=IF({SEL},"{tag[1:]}","{tag}")', GREEN))
            for i, h in enumerate(desc + REG19):
                cells.append((f"{col_let(2 + i)}{r0 + 1}", regonly(q(h)), GREEN))
            rr = r0 + 2
            for d, vals, src in rows:
                for i, h in enumerate(desc):
                    v = d.get(h)
                    if v is not None:
                        cells.append((f"{col_let(2 + i)}{rr}", regonly(q(v) if isinstance(v, str) else repr(v)), GREEN))
                for j, reg in enumerate(REG19):
                    if reg in vals:
                        f, colr = vals[reg]
                        cells.append((f"{col_let(2 + len(desc) + j)}{rr}", regonly(f[1:]), colr))
                cells.append((f"{col_let(2 + len(desc) + len(REG19) + 1)}{rr}", f"source {src}", None))
                rr += 1
            r0 = rr + 2
        plan.sheets[book][sheet] = cells
    return mode


# ------------------------------------------------------------------------------- HVO (SubRES)
def plan_hvo(plan, notes):
    b = Book(BRF_T)
    T = read_tables(os.path.join(ROOT, BRF_T), tags=("~TFM_AVA", "~TFM_INS"))
    ava = [t for t in T if t["tag"].upper().startswith("~TFM_AVA")]
    if not ava or list(ava[0]["cols"])[:3] != ["PSET_PN", "AllRegions", "FI"]:
        sys.exit(f"{BRF_T}: AVA table not as expected")
    sheet = "Reg_HVO"
    cells = [("A1", f"{MARK}: HVO (BRF1_HVO) at its sites - Neste Porvoo NEXBTL 1 and 2 (vintages 2007, 2009, "
                    "200 kt each) and UPM Lappeenranta (2015, 120 kt); vintages and capacities of SubRES_22 "
                    "'SUP_Gen1' (PASTI~2007/2009/2015).", None),
             ("B3", f'=IF({SEL},"TFM_AVA","~TFM_AVA")', GREEN),
             ("B4", regonly(q("PSET_PN")), GREEN), ("C4", regonly(q("FI")), GREEN),
             ("D4", regonly(q("FI1B1")), GREEN), ("E4", regonly(q("FI1C5")), GREEN),
             ("B5", regonly(q("BRF1_HVO")), GREEN), ("C5", regonly("0"), GREEN),
             ("D5", regonly("1"), GREEN), ("E5", regonly("1"), GREEN),
             ("B8", f'=IF({SEL},"TFM_INS","~TFM_INS")', GREEN)]
    hdr = ["Attribute", "Year", "Pset_PN", "FI1B1", "FI1C5"]
    for i, h in enumerate(hdr):
        cells.append((f"{col_let(2 + i)}9", regonly(q(h)), GREEN))
    r = 10
    for y in (2007, 2009, 2015):
        cells += [(f"B{r}", regonly(q("NCAP_PASTI")), GREEN), (f"C{r}", regonly(str(y)), GREEN),
                  (f"D{r}", regonly(q("BRF1_HVO")), GREEN),
                  (f"E{r}", regonly(str(HVO["FI1B1"].get(y, 0))), ORANGE),
                  (f"F{r}", regonly(str(HVO["FI1C5"].get(y, 0))), ORANGE)]
        r += 1
    plan.sheets[BRF_T][sheet] = cells
    notes.append("HVO: SubRES PASTI applies to every region where BRF1_HVO is available; the Reg-only AVA "
                 "removes it from FI and the TFM_INS gives each site its own vintages (others 0).")


# ------------------------------------------------------------------------------- UCs
def plan_ucs(plan, notes):
    for book, sheet, cell in UC_NATIONAL:
        b = Book(book)
        v = b.val(sheet, cell)
        if not (isinstance(v, str) and v.replace(" ", "").upper().startswith("~UC_SETS:R_E:FI")):
            f = b.f.get((sheet, cell), "")
            if SEL in f:
                continue
            sys.exit(f"{book} {sheet}!{cell} = {v!r}")
        plan.edit(book, sheet, cell, v, sw(q(v), q("~UC_Sets: R_S: AllRegions")), BLUE,
                  "national constraint: terms in the regions where the processes now are")
        T = read_tables(os.path.join(ROOT, book), sheets=[sheet], tags=("~UC_T",))
        for t in T:
            for h, c in t["cols"].items():
                hc = f"{col_let(c)}{t['header_row']}"
                if h.startswith("UC_RHSR"):
                    plan.edit(book, sheet, hc, h, sw(q(h), q(h.replace("UC_RHSR", "UC_RHS", 1))), BLUE,
                              "national constraint: RHS without region")
                elif h == "FI":
                    plan.edit(book, sheet, hc, h, sw(q(h), q("AllRegions")), BLUE,
                              "coefficients written for FI apply in every region (Copy rule)")


# ------------------------------------------------------------------------------- DD helpers
TOK = re.compile(r"'([^']*)'")


def dd_info(dd_dir, run):
    files = re.findall(r"BATINCLUDE\s+(\S+\.dd)", open(os.path.join(dd_dir, run), encoding="latin-1").read())
    top = collections.defaultdict(set)
    ctype, decl = {}, collections.defaultdict(set)
    links = set()
    for f in files:
        h = None
        for l in open(os.path.join(dd_dir, f), encoding="latin-1"):
            m = re.match(r"^SET\s+(\S+)", l) or re.match(r"^([A-Za-z_0-9]+) ' '/", l)
            if m:
                h = m.group(1)
                continue
            t = TOK.findall(l)
            if h == "TOP" and len(t) >= 3 and t[0] == "FI":
                top[t[1]].add((t[2], l.strip().split(".")[-1]))
            elif h == "COM_TMAP" and len(t) >= 3:
                ctype[t[2]] = t[1]
                decl[t[2]].add(t[0])
            elif h == "TOP_IRE":
                links |= {x for x in t if x.startswith("TB_")}
    return top, ctype, decl, links


def existing_links():
    """TB_* link names already defined in ScenTrade__Trade_Links (other sheets) - not defined twice."""
    out = set()
    b = Book(LINKS)
    for (s, cell), v in b.v.items():
        if s != LINK_SHEET and isinstance(v, str) and v.startswith("TB_"):
            out.add(v)
    return out


def plan_comms_links(plan, move, shares, mode_all, dd_dir, run, notes):
    top, ctype, decl, dd_links = dd_info(dd_dir, run)
    have = dd_links | existing_links()
    use = collections.defaultdict(set)        # region -> commodities
    for p, sh in shares.items():
        if p == "BRF1_HVO":
            continue
        if p not in top:
            notes.append(f"{p}: no topology on FI in the DD files ({dd_dir}/{run})")
        for c, io in top.get(p, ()):
            if ctype.get(c) == "ENV":
                continue
            for reg in sh:
                use[reg].add(c)
    for reg in HVO:
        for c, io in top.get("BRF1_HVO", ()):
            if ctype.get(c) != "ENV":
                use[reg].add(c)
    comms = sorted(set().union(*use.values()))
    # declarations in SysSettings
    b = Book(SYS)
    sh = "Comms"
    T = read_tables(os.path.join(ROOT, SYS), sheets=[sh], tags=("~FI_COMM",))
    found = {}
    for t in T:
        for r in t["rows"]:
            n = r["cells"].get("CommName", (0, None))[1]
            if isinstance(n, str):
                found.setdefault(n, []).append((t, r))
    regs_needed = set(REG19)
    for c in comms:
        if decl.get(c, set()) >= (regs_needed - {"FI200"}) and len(decl.get(c, ())) >= 19:
            continue
        hits = found.get(c, [])
        if len(hits) != 1:
            notes.append(f"commodity {c}: {len(hits)} declarations in {SYS} Comms - not changed (check)")
            continue
        t, r = hits[0]
        cell = f"{col_let(t['cols']['Region'])}{r['row']}"
        f = b.f.get((sh, cell), "")
        if f:
            if SEL not in f and "TEXTJOIN" not in f:
                notes.append(f"commodity {c}: Region {cell} formula {f!r} - not changed")
            continue
        if b.val(sh, cell) != "FI":
            notes.append(f"commodity {c}: Region {cell} = {b.val(sh, cell)!r} - not changed")
            continue
        plan.edit(SYS, sh, cell, "FI", sw('"FI"', ALL), BLUE, f"{c}: used by moved industry processes in the regions")
    # links
    rows = [(reg, c) for reg in REG19 if reg in use for c in sorted(use[reg]) if f"TB_{c}_FI_{reg}" not in have]
    notes.append(f"links already defined (pilot, power): {sum(1 for reg in use for c in use[reg] if f'TB_{c}_FI_{reg}' in have)}")
    cells = [("A1", f"{MARK}: internal links FI hub <-> region for every commodity the moved industry processes "
                    "use there (fuels, materials, products, heat); read from the DD files.", None),
             ("C2", f'=IF(Region_selection!$B$8=Region_selection!$D$9,"~TradeLinks_DINS","TradeLinks_DINS")', GREEN)]
    for i, h in enumerate(["Reg1", "Reg2", "Comm", "Comm1", "Comm2", "Tech", "TradeLink"]):
        cells.append((f"{col_let(3 + i)}3", h, GREEN))
    for i, (reg, c) in enumerate(rows):
        r = 4 + i
        for j, v in enumerate(["FI", reg, c, c, c, f"TB_{c}_FI_{reg}", "B"]):
            cells.append((f"{col_let(3 + j)}{r}", v, GREEN))
    plan.sheets[LINKS][LINK_SHEET] = cells
    notes.append(f"links: {len(rows)} ({len(comms)} commodities): " + ", ".join(
        f"{c} {sum(1 for _, x in rows if x == c)}" for c in comms))
    return use


CALIB = M + "SuppXLS/Scen_ZATEMP_Calibration.xlsx"


def plan_prd_corrections(plan, dd_dir, run, new_links, notes):
    """National production sums (RS_PRD_*, task 0) on aggregates whose components have an FX balance:
    TIMES aggregates the gross production (VAR_COMPRD) of FX components, and an internal import counts
    as production, so commodities sent over TB_* links are counted twice (hub and region). Correction:
    UC_IRE-I = -(UC_COMPRD coefficient x COM_AGG) on the internal links of every linked FX component."""
    files = re.findall(r"BATINCLUDE\s+(\S+\.dd)", open(os.path.join(dd_dir, run), encoding="latin-1").read())
    agg, lim, links = collections.defaultdict(dict), {}, set(new_links)
    for f in files:
        h = None
        for l in open(os.path.join(dd_dir, f), encoding="latin-1"):
            m = re.match(r"^SET\s+(\S+)", l) or re.match(r"^([A-Za-z_0-9]+) ' '/", l)
            if m:
                h = m.group(1)
                continue
            t = TOK.findall(l)
            if h == "COM_AGG" and len(t) >= 3 and t[0] == "FI":
                agg[t[2]][t[1]] = float(l.split()[-1])
            elif h == "COM_LIM" and len(t) >= 2 and t[0] == "FI":
                lim[t[1]] = l.strip().split(".")[-1]
            elif h == "TOP_IRE":
                links |= {x for x in t if x.startswith("TB_")}
    linked = {re.match(r"^TB_(.+)_FI_FI\w+$", x).group(1) for x in links if re.match(r"^TB_(.+)_FI_FI\w+$", x)}
    b = Book(CALIB)
    sh = "RegSum"
    hdr = {b.val(sh, f"{col_let(c)}7"): col_let(c) for c in range(2, 30) if b.val(sh, f"{col_let(c)}7")}
    for need in ("UC_N", "Pset_PN", "Cset_CN", "Year", "UC_COMPRD"):
        if need not in hdr:
            sys.exit(f"{CALIB} {sh}: header {need} missing ({hdr})")
    last = max(r for r in range(8, 400) if b.val(sh, f"B{r}") is not None)
    ire_col = hdr.get("UC_IRE-I") or col_let(max(col_idx(c) for c in hdr.values()) + 1)
    if "UC_IRE-I" not in hdr:
        plan.edit(CALIB, sh, f"{ire_col}7", None, regonly(q("UC_IRE-I")), GREEN,
                  "new column: internal imports subtracted from national production (table read in Reg mode only)")
    r = last + 1
    n = 0
    for row in range(8, last + 1):
        uc, c, y, k = (b.val(sh, f"{hdr[x]}{row}") for x in ("UC_N", "Cset_CN", "Year", "UC_COMPRD"))
        if not (isinstance(uc, str) and uc.startswith("RS_PRD_") and k):
            continue
        comps = [(x, a) for x, a in agg.get(c, {}).items() if lim.get(x) == "FX" and x in linked]
        if c in linked:
            comps.append((c, 1.0))
        for x, a in sorted(comps):
            for col, v in (("UC_N", q(uc)), ("Pset_PN", q(f"TB_{x}_*")), ("Cset_CN", q(x)), ("Year", repr(y))):
                plan.edit(CALIB, sh, f"{hdr[col]}{r}", None, regonly(v), GREEN,
                          f"{uc}: subtract internal imports of {x} (FX component of {c}, COM_AGG {a:g})")
            plan.edit(CALIB, sh, f"{ire_col}{r}", None, regonly(repr(-float(k) * a)), GREEN,
                      f"{uc}: UC_IRE-I = -UC_COMPRD x COM_AGG on TB_{x}_* (an internal import is not production)")
            r += 1
            n += 1
    notes.append(f"RS_PRD corrections: {n} rows on {CALIB} {sh} rows {last + 1}-{r - 1}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dd", default=os.path.join(ROOT, "GAMS_WrkTIMES"))
    ap.add_argument("--run", default="baseline-sami.run")
    ap.add_argument("--out", default=os.path.join(ROOT, "audit", "task4a_dryrun.txt"))
    ap.add_argument("--step", choices=["all", "prd"], default="all",
                    help="prd: only the RS_PRD import corrections (after the rest is applied)")
    a = ap.parse_args()
    if a.step == "prd":
        plan, notes = Plan(), []
        new_links = {v for (s_, c_), v in Book(LINKS).v.items() if s_ == LINK_SHEET and isinstance(v, str) and v.startswith("TB_")}
        plan_prd_corrections(plan, a.dd, a.run, new_links, notes)
        for sheet, cell, old, new, colour, why in plan.edits.get(CALIB, []):
            print(f"  ~ '{sheet}'!{cell}: {old!r} -> {new}")
        print(chr(10).join(notes))
        if a.apply:
            res = apply(plan)
            print(res)
            sys.exit(0 if all(v == "ok" for v in res.values()) else 1)
        return
    shares = shares_of(MOVE_4A)
    shares["BRF1_HVO"] = {"FI1B1": 1.0, "FI1C5": 1.0}
    plan, notes = Plan(), []
    mode = {}
    mode.update(plan_book(plan, IND, MOVE_4A, shares, notes))
    mode.update(plan_book(plan, SUP, MOVE_4A, shares, notes))
    plan_hvo(plan, notes)
    plan_ucs(plan, notes)
    use = plan_comms_links(plan, MOVE_4A, shares, mode, a.dd, a.run, notes)
    new_links = {v for (cell, v, colour) in plan.sheets[LINKS][LINK_SHEET] if isinstance(v, str) and v.startswith("TB_")}
    plan_prd_corrections(plan, a.dd, a.run, new_links, notes)
    L = ["modes: " + ", ".join(f"{p}={m}" for p, m in sorted(mode.items())), ""] + ["NOTE " + n for n in notes] + [""]
    for book in plan.books():
        L.append(f"--- {book}")
        for sheet, cell, old, new, colour, why in plan.edits.get(book, []):
            L.append(f"  ~ '{sheet}'!{cell} [{colour}]: {old!r}\n      -> {new}\n      ({why})")
        for sname, cells in plan.sheets.get(book, {}).items():
            L.append(f"  + new sheet '{sname}' ({len(cells)} cells)")
            for cell, v, colour in cells:
                L.append(f"      {cell} [{colour}] {v}")
    open(a.out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    n_e = sum(len(v) for v in plan.edits.values())
    n_s = sum(len(c) for d in plan.sheets.values() for c in d.values())
    print(f"dry run: {n_e} cell edits in {len(plan.edits)} workbooks, {n_s} cells on new sheets -> {a.out}")
    for n in notes:
        print("NOTE", n)
    if a.apply:
        res = apply(plan)
        print(res)
        if any(v != "ok" for v in res.values()):
            sys.exit(1)


if __name__ == "__main__":
    main()
