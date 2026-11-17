"""Task 4a (industry, single sites): rest of steel, refinery and coke oven, HVO, copper, glass and
refinery-gas autoproducers to their regions. Design: audit/task4_industry.md.

Mechanisms (all Reg mode only; single-region values unchanged):
  * switch  - a data table whose moved processes all go to ONE site and that holds no other process:
              its `FI` header becomes the site (as in the steel pilot); the process is declared only there.
  * copy    - otherwise: the process is declared only in its regions (not on the hub: a hub copy
              without stock or capacity cost has no capacity variable in TIMES and runs for free);
              a Reg-only sheet `Reg_<book>` carries one row per calibrated `FI` cell with one column
              per region: formulas on the original cell (coefficients copied, STOCK x regional share).
              The FI STOCK row is commented out in Reg mode.
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
            # existing (*00) plants are declared only at their sites in both modes: a hub copy without
            # stock and capacity costs gets no capacity variable (TIMES REDUCE) -> free, unlimited activity
            new = ",".join(regs)
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
    top_reg = collections.defaultdict(set)      # processes already moved (no hub topology any more)
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
            if h == "TOP" and len(t) >= 3:
                if t[0] == "FI":
                    top[t[1]].add((t[2], l.strip().split(".")[-1]))
                else:
                    top_reg[t[1]].add((t[2], l.strip().split(".")[-1]))
            elif h == "COM_TMAP" and len(t) >= 3:
                ctype[t[2]] = t[1]
                decl[t[2]].add(t[0])
            elif h == "TOP_IRE":
                links |= {x for x in t if x.startswith("TB_")}
    for p, cs in top_reg.items():
        if p not in top:
            top[p] = cs
    return top, ctype, decl, links


def existing_links():
    """TB_* link names already defined in ScenTrade__Trade_Links (other sheets) - not defined twice."""
    out = set()
    b = Book(LINKS)
    for (s, cell), v in b.v.items():
        if s != LINK_SHEET and isinstance(v, str) and v.startswith("TB_"):
            out.add(v)
    return out


def plan_comms_links(plan, move, shares, mode_all, dd_dir, run, notes, chain=None):
    """chain: {process: regions} of whole sector chains (4b). Their commodities are declared in those
    regions; only commodities that also have processes outside the chains get a link."""
    top, ctype, decl, dd_links = dd_info(dd_dir, run)
    # links defined on this tool's own sheet are regenerated with it (not 'already defined')
    own = {v for (s_, c_), v in Book(LINKS).v.items() if s_ == LINK_SHEET and isinstance(v, str) and v.startswith("TB_")}
    have = (dd_links - own) | existing_links()
    use = collections.defaultdict(set)        # region -> commodities to link
    dec = collections.defaultdict(set)        # region -> commodities to declare
    chain = chain or {}
    intra = intra_commodities(top, set(chain)) if chain else set()
    if chain:
        notes.append(f"commodities inside the moved chains (declared, not linked): {sorted(intra)}")
    for p, sh in list(shares.items()) + [(p, {r: 1 for r in regs}) for p, regs in chain.items() if p not in shares]:
        if p == "BRF1_HVO":
            continue
        if p not in top:
            notes.append(f"{p}: no topology on FI in the DD files ({dd_dir}/{run})")
        for c, io in top.get(p, ()):
            if ctype.get(c) == "ENV":
                if p in chain and not decl.get(c, set()) >= set(REG19):
                    notes.append(f"ENV commodity {c} of {p} not declared in all regions (check)")
                continue
            for reg in sh:
                dec[reg].add(c)
                if not (p in chain and c in intra):
                    use[reg].add(c)
    for reg in HVO:
        for c, io in top.get("BRF1_HVO", ()):
            if ctype.get(c) != "ENV":
                use[reg].add(c)
                dec[reg].add(c)
    comms = sorted(set().union(*use.values()))
    dcomms = sorted(set().union(*dec.values()))
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
    for c in dcomms:
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
    last = max(r for r in range(8, 400) if b.val(sh, f"B{r}") not in (None, "") or b.f.get((sh, f"B{r}")))
    ire_col = hdr.get("UC_IRE-I") or col_let(max(col_idx(c) for c in hdr.values()) + 1)
    # correction rows already written (Reg-only formulas: their single-mode values are empty)
    have = set()
    for row in range(8, last + 1):
        fu, fp = b.f.get((sh, f"{hdr['UC_N']}{row}"), ""), b.f.get((sh, f"{hdr['Pset_PN']}{row}"), "")
        mu, mp = re.search(r'"(RS_PRD_[^"]+)"\)$', fu), re.search(r'"TB_(.+)_\*"\)$', fp)
        if mu and mp:
            have.add((mu.group(1), mp.group(1)))
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
            if (uc, x) in have:
                continue
            for col, v in (("UC_N", q(uc)), ("Pset_PN", q(f"TB_{x}_*")), ("Cset_CN", q(x)), ("Year", repr(y))):
                plan.edit(CALIB, sh, f"{hdr[col]}{r}", None, regonly(v), GREEN,
                          f"{uc}: subtract internal imports of {x} (FX component of {c}, COM_AGG {a:g})")
            plan.edit(CALIB, sh, f"{ire_col}{r}", None, regonly(repr(-float(k) * a)), GREEN,
                      f"{uc}: UC_IRE-I = -UC_COMPRD x COM_AGG on TB_{x}_* (an internal import is not production)")
            r += 1
            n += 1
    notes.append(f"RS_PRD corrections: {n} rows on {CALIB} {sh} rows {last + 1}-{r - 1}")


# ------------------------------------------------------------------- fix after the first 4a run
# (audit/task4_industry.md section 9): hub copies of moved plants; FI-only stock fills of the
# route-share constraints; internal imports counted as production in those constraints.
UCIND = M + "SuppXLS/Scen_UC-IND.xlsx"
REGCOLS = [col_let(c) for c in range(col_idx("G"), col_idx("Z") + 1)]      # 20 region columns
SELCOLS = [col_let(c) for c in range(col_idx("K"), col_idx("AD") + 1)]     # Region_selection!K8:AD8
FILLS = {  # sheet: (header row, data rows, {total row: data rows}, {share cell: total row})
    "FILL-IIS": (12, [13, 14, 15, 16, 17, 18], {19: [13, 14, 15, 16, 17, 18]},
                 {f"G{r}": 19 for r in range(33, 39)}),
    "FILL-IALICU": (4, [5, 6, 7, 9, 10], {8: [5, 6, 7], 11: [9, 10]},
                    {"G19": 8, "G20": 8, "G21": 8, "G23": 11, "G24": 11}),
}
UCIIS_INSERT = 24          # first empty row below the LO table of UC-IIS (rows 8-23)


def ucis_lo_rows(b):
    """Rows of the UC-IIS LO table whose coefficient is a formula (constants are literal zeros)."""
    out, uc = [], None
    for r in range(8, 24):
        uc = b.val("UC-IIS", f"A{r}") or uc
        if (b.f.get(("UC-IIS", f"G{r}")) or "").startswith("="):
            out.append((r, uc))
    return out


def plan_hub_decl(plan, notes):
    """Copy-mode processes: Reg-mode Region list without the hub."""
    pat = re.compile(r'^=IF\(' + re.escape(SEL) + r',"FI","FI,([A-Z0-9,]+)"\)$')
    for book in (IND, SUP):
        b = Book(book)
        for t in read_tables(os.path.join(ROOT, book), tags=("~FI_PROCESS",)):
            rc = t["cols"].get("Region")
            for r in t["rows"]:
                p = r["cells"].get("TechName", (0, None))[1]
                cell = f"{col_let(rc)}{r['row']}"
                m = pat.match(b.f.get((t["sheet"], cell)) or "")
                if p in MOVE_4A and m:
                    plan.edit(book, t["sheet"], cell, "FI", sw(q("FI"), q(m.group(1))), BLUE,
                              f"{p}: declared only in {m.group(1)} in Reg mode (no free hub copy)")
    n = sum(len(v) for v in plan.edits.values())
    notes.append(f"hub declarations removed: {n} Region cells")


def plan_generic(plan, notes, extra=()):
    """Copied rows: VEDA lets the original table's generic (year/no-region) value beat the Reg_IND
    regional copy of the calibrated FI value (first 4a run: AOD, EAF, FeCr at their sites got the
    generic coefficients). In Reg mode the generic cell of every copied row with an FI value is blanked;
    Reg_IND gives every site region the FI value, and the hub no longer holds these processes."""
    n = 0
    for book in (IND, SUP):
        b = Book(book)
        regsheet = "Reg_" + ("IND" if book == IND else "SUP")
        copied = set()
        for (sh, cell), f in b.f.items():
            if sh == regsheet and cell.startswith("B"):
                m = re.search(r'"",\"([A-Za-z0-9_]+)\"\)$', f or "")
                if m:
                    copied.add(m.group(1))
        copied |= set(extra)
        if not copied:
            continue
        regions = set(REG19) | {"FI"}
        for t in read_tables(os.path.join(ROOT, book), tags=("~FI_T",)):
            if t["sheet"].startswith("Reg_") or "FI" not in t["cols"]:
                continue
            for p, rows in tech_rows(t).items():
                if p not in copied:
                    continue
                for r in rows:
                    c = r["cells"]
                    if "FI" not in c:
                        continue
                    for h, (cell, val, f) in c.items():
                        if h in DESCR or h in regions or h.upper() in ("TECHNAME", "TECHDESC"):
                            continue
                        expr = f[1:] if f else (q(val) if isinstance(val, str) else repr(val))
                        plan.edit(book, t["sheet"], cell, val, sw(expr, '""'), BLUE,
                                  f"{p}: generic {h} value blank in Reg mode (sites get the calibrated FI value "
                                  f"{c['FI'][0]} via {regsheet})")
                        n += 1
    notes.append(f"generic values of copied rows blanked in Reg mode: {n} cells")


AGGREGATES = {"INDFINSOLID": "C73", "INDFINGAS": "C75"}   # SysSettings Comms


def plan_aggregates(plan, notes):
    """Aggregates of the national production sums RS_PRD_INDFIN* (task 0) in every region: the COM_AGG
    rows (SubRES_21, region-independent) and the UC_COMPRD term (RegSum, R_S AllRegions) only reach a
    region where the aggregate is declared. Hub-only, the sum ignored fuel produced and used in a region
    while the UC_IRE-I corrections still subtracted regional imports (coke to Raahe penalised by the
    LO dual, first 4a run)."""
    b = Book(SYS)
    for c, cell in AGGREGATES.items():
        if b.val("Comms", f"D{cell[1:]}") != c or b.val("Comms", cell) != "FI" or b.f.get(("Comms", cell)):
            sys.exit(f"{SYS} Comms!{cell}: expected plain 'FI' for {c}")
        plan.edit(SYS, "Comms", cell, "FI", sw('"FI"', ALL), BLUE,
                  f"{c}: aggregate of the national RS_PRD sum declared in every region (COM_AGG + UC term there)")
    notes.append("aggregates INDFINSOLID, INDFINGAS declared in all regions")


def plan_misc(plan, notes):
    """Data lost in the first 4a run (single vs regional parameter comparison of every moved process):
    * refinery lower output shares: header 'FI~LO' of the Flexible Refinery table stayed on the hub;
    * NETSCO2 (non-ETS CO2, ESR target) not declared in the regions -> copper's emissions dropped.
      Reg-only declaration row copying the hub row (as ELCCO2N/ETSCO2/GreenCert in task 3)."""
    b = Book(SUP)
    sh, cell = "Flexible Refinery", "L25"
    if b.f.get((sh, cell)) != '=AS4&"~LO"' or b.val(sh, "AS4") != "FI":
        sys.exit(f"{SUP} {sh}!{cell}: expected =AS4&\"~LO\" with AS4 = FI")
    plan.edit(SUP, sh, cell, "FI~LO", sw('AS4&"~LO"', q("FI1B1~LO")), BLUE,
              "SSCDRFLX00 lower output shares at Porvoo (the FI header of this table is already FI1B1 in Reg mode)")
    s = Book(SYS)
    if s.val("Comms", "X25") != "NETSCO2" or any(s.val("Comms", f"{c}80") is not None for c in "VWXYZ"):
        sys.exit(f"{SYS} Comms: expected NETSCO2 in row 25 and a free row 80")
    for c in "VXYZ":
        plan.edit(SYS, "Comms", f"{c}80", None, regonly(f"{c}25"), GREEN,
                  "NETSCO2 declared in the 19 regions (copy of the hub row 25)")
    plan.edit(SYS, "Comms", "W80", None, regonly('_xlfn.TEXTJOIN(",",TRUE,Region_selection!$L$8:$AD$8)'), GREEN,
              "NETSCO2: the 19 regions")
    notes.append("refinery FI~LO header -> FI1B1~LO; NETSCO2 declared in the regions")


def plan_fills(plan, notes):
    """~TFM_FILL stock tables of the route shares read every region and sum them (as the pilot's MISRIR table)."""
    b = Book(UCIND)
    for sh, (hr, rows, totals, shares) in FILLS.items():
        if b.val(sh, f"G{hr}") != "FI" or b.f.get((sh, f"G{hr}")):
            sys.exit(f"{UCIND} {sh}!G{hr}: expected the plain header 'FI'")
        for c, s in zip(REGCOLS, SELCOLS):
            plan.edit(UCIND, sh, f"{c}{hr}", "FI" if c == "G" else None, f"=Region_selection!{s}8", BLUE,
                      "fill header: one column per modelled region (Region_selection), like the MISRIR table")
        for r in rows:
            plan.edit(UCIND, sh, f"AA{r}", None, regonly(f"SUM(G{r}:Z{r})"), GREEN,
                      "national stock = sum of the regional fills (Reg mode)")
        for tr, rr in totals.items():
            plan.edit(UCIND, sh, f"AA{tr}", None, regonly(f"SUM(AA{rr[0]}:AA{rr[-1]})"), GREEN, "national total")
        refs = set(rows) | set(totals)
        for cell, tr in shares.items():
            f = b.f.get((sh, cell))
            if not f or SEL in f:
                sys.exit(f"{UCIND} {sh}!{cell}: expected an unswitched share formula, found {f!r}")
            reg = re.sub(r"\bG(\$?)(\d+)\b", lambda m: f"AA{m.group(1)}{m.group(2)}" if int(m.group(2)) in refs
                         else m.group(0), f[1:])
            plan.edit(UCIND, sh, cell, b.val(sh, cell), sw(f[1:], reg), BLUE,
                      f"share from the national (summed) stock in Reg mode: {reg}")
    notes.append("fills: FILL-IIS crude steel and FILL-IALICU aluminium/copper read all regions")


def plan_uc_shares(plan, notes, inserted):
    """Route-share UCs: national copper constraint; UC_IRE-I corrections on the internal links
    (an internal import is counted as production by UC_COMPRD)."""
    b = Book(UCIND)
    # UC-IALICU (aluminium + copper): one national constraint each in Reg mode
    sh = "UC-IALICU"
    for cell, single, reg in (("B2", "~UC_Sets: R_E: AllRegions", "~UC_Sets: R_S: AllRegions"),
                              ("G5", "FI", "AllRegions"), ("H5", "UC_RHSRTS~LO", "UC_RHSTS~LO"),
                              ("I5", "UC_RHSRTS~LO~0", "UC_RHSTS~LO~0"),
                              ("G19", "FI", "AllRegions"), ("H19", "UC_RHSRTS~LO", "UC_RHSTS~LO"),
                              ("I19", "UC_RHSRTS~LO~0", "UC_RHSTS~LO~0")):
        if b.val(sh, cell) != single or b.f.get((sh, cell)):
            sys.exit(f"{UCIND} {sh}!{cell}: expected {single!r}")
        plan.edit(UCIND, sh, cell, single, sw(q(single), q(reg)), BLUE, "national constraint in Reg mode (UC_R_SUM)")
    plan.edit(UCIND, sh, "J19", None, regonly(q("Pset: PN")), GREEN, "process filter of the correction rows")
    plan.edit(UCIND, sh, "K19", None, regonly(q("UC_IRE-I")), GREEN, "internal imports are not production")
    out, uc = 26, None
    for r in range(20, 26):
        uc = b.val(sh, f"A{r}") or uc
        for col, v in (("A", q(uc)), ("D", q("MCUSCU")), ("E", f"E{r}"), ("J", q("TB_MCUSCU_*")), ("K", f"-G{r}")):
            plan.edit(UCIND, sh, f"{col}{out}", None, regonly(v), GREEN,
                      f"{uc}: UC_IRE-I = -UC_COMPRD of row {r} on TB_MCUSCU_*")
        out += 1
    # UC-IIS crude-steel shares (already national since 4a): correction rows
    sh = "UC-IIS"
    lo = ucis_lo_rows(b)
    n = len(lo)
    if not inserted:
        notes.append(f"UC-IIS: {n} rows must first be inserted at row {UCIIS_INSERT} (--step insert)")
        return
    if b.val(sh, f"E{27 + n}") is None or "~UC_T" not in str(b.val(sh, f"E{27 + n}")):
        sys.exit(f"{UCIND} UC-IIS: UP table tag not found at E{27 + n} - rows not inserted?")
    plan.edit(UCIND, sh, "J7", None, regonly(q("UC_IRE-I")), GREEN, "internal imports are not production")
    for k, (r, uc) in enumerate(lo):
        o = UCIIS_INSERT + k
        for col, v in (("A", q(uc)), ("C", q("TB_MISCST_*")), ("D", q("MISCST")), ("E", f"E{r}"), ("J", f"-G{r}")):
            plan.edit(UCIND, sh, f"{col}{o}", None, regonly(v), GREEN, f"{uc}: UC_IRE-I = -UC_COMPRD of row {r}")
    hdr = 28 + n
    plan.edit(UCIND, sh, f"J{hdr}", None, regonly(q("UC_IRE-I")), GREEN, "internal imports are not production")
    o, uc = hdr + 5, None
    for r in range(hdr + 1, hdr + 5):
        uc = b.val(sh, f"A{r}") or uc
        if b.val(sh, f"E{r}") is None:
            sys.exit(f"{UCIND} UC-IIS: no UP row at {r}")
        for col, v in (("A", q(uc)), ("C", q("TB_MISCST_*")), ("D", q("MISCST")), ("E", f"E{r}"), ("J", f"-G{r}")):
            plan.edit(UCIND, sh, f"{col}{o}", None, regonly(v), GREEN, f"{uc}: UC_IRE-I = -UC_COMPRD of row {r}")
        o += 1
    notes.append(f"UC-IIS: {n} LO and 4 UP correction rows; UC-IALICU: 6 copper correction rows")


def insert_ucis_rows(apply_it):
    """Make room for the correction rows inside the UC-IIS LO table (Excel row insert, xlwings)."""
    b = Book(UCIND)
    n = len(ucis_lo_rows(b))
    tag = str(b.val("UC-IIS", "E27") or "")
    if "~UC_T" not in tag:
        print(f"UC-IIS: E27 holds {tag!r}; rows already inserted? nothing to do")
        return True
    empty = all(b.val("UC-IIS", f"{c}{r}") is None for r in (24, 25) for c in "ABCDEFGHIJ")
    if not empty:
        sys.exit("UC-IIS rows 24-25 are not empty")
    print(f"UC-IIS: insert {n} empty rows at row {UCIIS_INSERT} (UP table moves from rows 27-32 to {27 + n}-{32 + n})")
    if not apply_it:
        return False
    import xlwings as xw
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    try:
        wb = app.books.open(os.path.join(ROOT, UCIND), update_links=False)
        try:
            if wb.sheets["Region_selection"].range("B8").value != "FINTIMES":
                raise RuntimeError("Region_selection!B8 is not FINTIMES")
            ws = wb.sheets["UC-IIS"]
            before = {c: ws.range(c).value for c in ("G29", "G30", "G31", "G32")}
            ws.api.Rows(f"{UCIIS_INSERT}:{UCIIS_INSERT + n - 1}").Insert()
            app.calculate()
            after = {c: ws.range(f"{c[0]}{int(c[1:]) + n}").value for c in before}
            if list(before.values()) != list(after.values()) or "~UC_T" not in str(ws.range(f"E{27 + n}").value):
                raise RuntimeError(f"insert check failed: {before} vs {after}")
            wb.save()
            print("  inserted and saved")
        finally:
            wb.close()
    finally:
        app.quit()
    return True


# =========================================================================== 4b (audit/task4b.md)
IPP_KEY, ICH_KEY, ILM_KEY, IAM_KEY = "ind_ipp_2013-2020", "ind_ich_2013-2020", "ind_ilm_2013-2020", "ind_iam_2013-2020"
SECTOR_RX = [(re.compile(r"^(IPP|INDIPPHTH00$)"), IPP_KEY), (re.compile(r"^ICH"), ICH_KEY),
             (re.compile(r"^ILM"), ILM_KEY), (re.compile(r"^IAM"), IAM_KEY)]
BLQ_CHP = {"CHPAUTOGENBLQ00": "power_CHPAUTOGENBLQ00"}       # black-liquor CHP: plant register (step 3)
DEMAND_4B = {"IPL": IPP_KEY, "IPH": IPP_KEY, "ICH": ICH_KEY, "ILM": ILM_KEY, "IAM": IAM_KEY}
NEWTECH_RX = [(re.compile(r"^(IPP|BBLQ)"), IPP_KEY), (re.compile(r"^ICH"), ICH_KEY),
              (re.compile(r"^ILM"), ILM_KEY), (re.compile(r"^IAM"), IAM_KEY)]
DEMAND_BOOK = M + "SuppXLS/Scen_ZUDemand_REF2016.xlsx"
SUB10_T = M + "SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND_Trans.xlsx"
GROWTH = M + "SuppXLS/Scen_ZUGROWTH_Yearly.xlsx"
COAL = M + "SuppXLS/Scen_UC_LimitCOAL.xlsx"
UC_4B = [  # (book, sheet, UC_Sets cell): zero-RHS share constraints made national (R_S AllRegions)
    (UCIND, "FI", "B3"), (UCIND, "UC-PUP", "B2"), (UCIND, "INDPRC", "C29"),
    (COAL, "UC_IPPCOA", "C4"), (GROWTH, "GROWTH ACT", "B3"),
]


def move_4b():
    """Existing 4b processes (declared in VT_FINTIMES_IND) -> key."""
    move = {}
    for t in read_tables(os.path.join(ROOT, IND), tags=("~FI_PROCESS",)):
        for r in t["rows"]:
            p = r["cells"].get("TechName", (0, None))[1]
            if not isinstance(p, str):
                continue
            for rx, key in SECTOR_RX:
                if rx.match(p):
                    move[p] = key
    move.update(BLQ_CHP)
    return move


def newtech_4b(top):
    """New technologies of the 4b sectors (SubRES_10, FI only today) -> key."""
    out = {}
    for f in ("10_techs_chp_sup_ind.dd",):
        for l in open(os.path.join(ROOT, "GAMS_WrkTIMES", f), encoding="latin-1"):
            m = re.match(r"^'FI'\.'([A-Za-z0-9_\-]+)'\.'[A-Za-z0-9_\-]+'\.(IN|OUT)$", l.strip())
            if m:
                for rx, key in NEWTECH_RX:
                    if rx.match(m.group(1)) and not m.group(1).endswith("00"):
                        out[m.group(1)] = key
    return out


def plan_ucs_general(plan, items, notes):
    """UC_Sets R_E (FI or AllRegions with an FI coefficient column) -> R_S AllRegions in Reg mode."""
    for book, sheet, cell in items:
        b = Book(book)
        v, f = b.val(sheet, cell), b.f.get((sheet, cell), "")
        if f and SEL in f:
            continue
        vv = (v or "").replace(" ", "").upper()
        if vv not in ("~UC_SETS:R_E:FI", "~UC_SETS:R_E:ALLREGIONS"):
            sys.exit(f"{book} {sheet}!{cell} = {v!r}")
        plan.edit(book, sheet, cell, v, sw(q(v), q("~UC_Sets: R_S: AllRegions")), BLUE,
                  "national constraint (sum over FI and the regions): same meaning as the single-region model")
        for t in read_tables(os.path.join(ROOT, book), sheets=[sheet], tags=("~UC_T",)):
            for h, c in t["cols"].items():
                hc = f"{col_let(c)}{t['header_row']}"
                if b.f.get((sheet, hc), "").startswith("=IF("):
                    continue
                if h.startswith("UC_RHSR"):
                    plan.edit(book, sheet, hc, h, sw(q(h), q(h.replace("UC_RHSR", "UC_RHS", 1))), BLUE,
                              "national constraint: RHS without region")
                elif h == "FI":
                    plan.edit(book, sheet, hc, h, sw(q(h), q("AllRegions")), BLUE,
                              "coefficients written for FI apply in every region of the sum")
    notes.append(f"constraints made national: {', '.join(f'{os.path.basename(b)}:{s}' for b, s, _ in items)}")


def plan_fill(plan, book, sh, col0, hr, rows, totals, shares, notes):
    """A ~TFM_FILL stock table reads every region (20 columns from col0), Reg-only sum column after them,
    shares from the sum in Reg mode (4a lesson: FI-only fills give zero shares once stocks move)."""
    b = Book(book)
    c0 = col_idx(col0)
    regcols = [col_let(c0 + i) for i in range(20)]
    sumc = col_let(c0 + 20)
    if b.val(sh, f"{col0}{hr}") != "FI" or b.f.get((sh, f"{col0}{hr}")):
        sys.exit(f"{book} {sh}!{col0}{hr}: expected the plain header 'FI'")
    for c, s in zip(regcols, SELCOLS):
        plan.edit(book, sh, f"{c}{hr}", "FI" if c == col0 else None, f"=Region_selection!{s}8", BLUE,
                  "fill header: one column per modelled region")
    for r in rows:
        plan.edit(book, sh, f"{sumc}{r}", None, regonly(f"SUM({regcols[0]}{r}:{regcols[-1]}{r})"), GREEN,
                  "national stock = sum of the regional fills (Reg mode)")
    for tr, rr in totals.items():
        plan.edit(book, sh, f"{sumc}{tr}", None, regonly(f"SUM({sumc}{rr[0]}:{sumc}{rr[-1]})"), GREEN, "national total")
    refs = set(rows) | set(totals)
    rx = re.compile(r"\b" + col0 + r"(\$?)(\d+)\b")
    for cell in shares:
        f = b.f.get((sh, cell))
        if not f or SEL in f:
            sys.exit(f"{book} {sh}!{cell}: expected an unswitched share formula, found {f!r}")
        reg = rx.sub(lambda m: f"{sumc}{m.group(1)}{m.group(2)}" if int(m.group(2)) in refs else m.group(0), f[1:])
        plan.edit(book, sh, cell, b.val(sh, cell), sw(f[1:], reg), BLUE, f"share from the national stock: {reg}")
    notes.append(f"fill {os.path.basename(book)}:{sh} reads all regions ({len(rows)} rows, {len(shares)} shares)")


def plan_ire_rows(plan, book, sh, hdr_row, pn_col, ire_col, rows, notes):
    """Reg-only UC_IRE-I correction rows: an internal import of a linked commodity is not production.
    rows: [(row, {col: expr})]; the header gets 'Pset_PN' and 'UC_IRE-I' columns (Reg-only)."""
    b = Book(book)
    for c, h in ((pn_col, "Pset_PN"), (ire_col, "UC_IRE-I")):
        if b.val(sh, f"{c}{hdr_row}") is not None:
            sys.exit(f"{book} {sh}!{c}{hdr_row} is not empty")
        plan.edit(book, sh, f"{c}{hdr_row}", None, regonly(q(h)), GREEN, "correction columns (Reg mode)")
    for r, cells in rows:
        for c, expr in cells.items():
            if b.val(sh, f"{c}{r}") is not None:
                sys.exit(f"{book} {sh}!{c}{r} is not empty")
            plan.edit(book, sh, f"{c}{r}", None, regonly(expr), GREEN, "UC_IRE-I correction on internal links")
    notes.append(f"{os.path.basename(book)}:{sh}: {len(rows)} UC_IRE-I correction rows")


def plan_minshare_elc(plan, notes):
    """TUC_MinShareofCenELCinINDELC (CHPShares rows 16-18, R_S in Reg mode): 1.02 x grid INDELC00 output
    - 0.75 x COMPRD(INDELC) >= 0. An internal INDELC import counts as production in the importing region,
    so every PJ sent over TB_INDELC_* was counted twice (second 4b run: pulp mill electricity made the
    constraint bind on its dummy, barrier diverged). Reg-only row 19: UC_IRE-I = -UC_COMPRD on TB_INDELC_*."""
    sh = "CHPShares"
    b = Book(UCIND)
    if b.val(sh, "A18") != "TUC_MinShareofCenELCinINDELC" or b.val(sh, "B17") != "Pset_PN":
        sys.exit(f"{UCIND} {sh}: TUC_MinShareofCenELCinINDELC table not where expected (A18, header row 17)")
    for c in ("H17", "H18", "I17", "I18") + tuple(f"{x}19" for x in "ABCDEFGHI"):
        if b.val(sh, c) is not None or b.f.get((sh, c)):
            sys.exit(f"{UCIND} {sh}!{c} is not empty")
    plan.edit(UCIND, sh, "H17", None, regonly(q("UC_IRE-I")), GREEN, "correction column (Reg mode)")
    plan.edit(UCIND, sh, "I17", None, regonly(q("Year")), GREEN, "explicit year of the correction row (tag year 2015)")
    for cell, expr in (("A19", "A18"), ("B19", q("TB_INDELC_*")), ("C19", q("INDELC")), ("H19", "-E18"),
                       ("I19", "2015")):
        plan.edit(UCIND, sh, cell, None, regonly(expr), GREEN,
                  "TUC_MinShareofCenELCinINDELC: UC_IRE-I = -UC_COMPRD on TB_INDELC_* (an internal import is not production)")
    notes.append(f"{os.path.basename(UCIND)}:{sh}: UC_IRE-I correction row 19 for TUC_MinShareofCenELCinINDELC")


def plan_demand_4b(plan, notes):
    """COM_PROJ of the 4b products split by the sector key (Split rule): FI rows commented out in Reg mode
    ('*' in the first column), a Reg-only table gives FI 0 and each region FI x share."""
    T = read_tables(os.path.join(ROOT, DEMAND_BOOK), tags=("~TFM_DINS",))
    keys = {k: load_key(k) for k in set(DEMAND_4B.values())}
    b = Book(DEMAND_BOOK)
    out, years = [], collections.defaultdict(set)
    for t in T:
        first = min(t["cols"].items(), key=lambda kv: kv[1])
        for r in t["rows"]:
            c = r["cells"]
            cn = c.get("Cset_CN", (0, None))[1]
            if cn not in DEMAND_4B or str(c.get("Attribute", (0, ""))[1]).upper() != "COM_PROJ" or "FI" not in c:
                continue
            fcell = f"{col_let(first[1])}{r['row']}"
            done = b.f.get((t["sheet"], fcell), "") == regonly(q(f"*{cn} COM_PROJ split: Reg_Demand"))
            if not done and (b.val(t["sheet"], fcell) not in (None, "") or b.f.get((t["sheet"], fcell))):
                sys.exit(f"{DEMAND_BOOK} {t['sheet']}!{fcell}: first column not empty")
            plan.edit(DEMAND_BOOK, t["sheet"], fcell, None, regonly(q(f"*{cn} COM_PROJ split: Reg_Demand")), BLUE,
                      f"{cn}: FI row commented out in Reg mode (split by {DEMAND_4B[cn]})")
            y = c["Year"][1]
            years[cn].add(y)
            out.append((cn, y, sheet_ref(t["sheet"], c["FI"][0])))
    for cn in DEMAND_4B:
        if 2010 not in years[cn]:
            sys.exit(f"{cn}: no 2010 projection row (the hub's base-year value would not be overridden)")
    cells = [("A1", f"{MARK}: COM_PROJ of pulp/paper, chemicals, lime and fertiliser split by the sector key "
                    "(data/keys/ind_*.csv); FI 0. Read only in Reg mode.", None),
             ("A3", regonly(q("~TFM_DINS")), GREEN)]
    hdr = ["Attribute", "Year", "Cset_CN", "FI"] + REG19
    for i, h in enumerate(hdr):
        cells.append((f"{col_let(1 + i)}4", regonly(q(h)), GREEN))
    for k, (cn, y, ref) in enumerate(out):
        r = 5 + k
        cells += [(f"A{r}", regonly(q("COM_PROJ")), GREEN), (f"B{r}", regonly(repr(int(y))), GREEN),
                  (f"C{r}", regonly(q(cn)), GREEN), (f"D{r}", regonly("0"), ORANGE)]
        for j, reg in enumerate(REG19):
            s = keys[DEMAND_4B[cn]].get(reg)
            if s:
                cells.append((f"{col_let(5 + j)}{r}", regonly(f"{ref}*{s!r}"), ORANGE))
        cells.append((f"{col_let(6 + len(REG19))}{r}", f"source {ref}", None))
    plan.sheets[DEMAND_BOOK]["Reg_Demand"] = cells
    notes.append(f"demand split: {len(out)} rows ({', '.join(f'{c} {len(years[c])} years' for c in DEMAND_4B)})")


def plan_ava_4b(plan, newtech, notes):
    """New technologies of the 4b sectors available in their key regions, not on the hub (Reg mode):
    rows appended to the SubRES_10 ~TFM_AVA table (later rows win, as the pilot's MISRIR row)."""
    b = Book(SUB10_T)
    sh = "TechSelection AVA"
    if b.f.get((sh, "G7")) != "=Region_selection!Z8" or b.val(sh, "F7") != "FI":
        sys.exit(f"{SUB10_T} {sh}: unexpected header")
    others = [r for r in REG19 if r != "FI1D9"]          # G7 is FI1D9 in Reg mode
    cols = {r: col_let(col_idx("H") + i) for i, r in enumerate(others)}
    cols["FI1D9"] = "G"
    for r, c in cols.items():
        if r == "FI1D9":
            continue
        cur = b.val(sh, f"{c}7")
        if cur is not None:
            sys.exit(f"{SUB10_T} {sh}!{c}7 not empty")
        plan.edit(SUB10_T, sh, f"{c}7", None, regonly(q(r)), GREEN, "region column (Reg mode)")
    # a note in I17 would fall under a region column in Reg mode: kept as text in single mode only
    note = b.val(sh, "I17")
    if note:
        plan.edit(SUB10_T, sh, "I17", note, sw(q(note), '""'), BLUE, "note hidden in Reg mode (cell is a region column there)")
    last = max(r for r in range(8, 400) if any(b.val(sh, f"{c}{r}") is not None for c in "BCDEFG"))
    keys = {k: load_key(k) for k in set(newtech.values())}
    r = last + 1
    for p in sorted(newtech):
        plan.edit(SUB10_T, sh, f"C{r}", None, regonly(q(p)), GREEN, f"{p}: available in its sector's regions")
        plan.edit(SUB10_T, sh, f"F{r}", None, regonly("0"), GREEN, f"{p}: not on the hub (sector moved)")
        for reg in keys[newtech[p]]:
            plan.edit(SUB10_T, sh, f"{cols[reg]}{r}", None, regonly("1"), GREEN, f"{p}: {reg}")
        r += 1
    notes.append(f"new technologies available in their regions: {len(newtech)} (rows {last + 1}-{r - 1})")


REF_RX = re.compile(r"(?<![A-Za-z0-9_.$'\"])(?:('[^']+'|[A-Za-z0-9_]+)!)?(\$?)([A-Z]{1,3})(\$?)(\d+)(?![\d(A-Za-z_])")


def blanked_generic(book):
    """Generic cells blanked in Reg mode by plan_generic (4a fix and 4b dry runs)."""
    out = set()
    for f in ("task4a_fix_dryrun.txt", "task4b_dryrun.txt"):
        p = os.path.join(ROOT, "audit", f)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        sec = txt.split(f"--- {book}")
        for part in sec[1:]:
            part = part.split("\n--- ")[0]
            for m in re.finditer(r"~ '([^']+)'!([A-Z]+\d+) \[[^\]]*\]: [^\n]*\n      -> [^\n]*\n      \([^\n]*generic", part):
                out.add((m.group(1), m.group(2)))
    return out


def plan_generic_deps(plan, notes):
    """Formulas that read a generic cell blanked in Reg mode (e.g. the IPP calibration column H and the
    stock formulas built on it) get the original value from a Reg-only helper cell: the reference X becomes
    IF(single, X, helper). Without this, pulp's stocks and coefficients were errors in Reg mode (4b run 1)."""
    b = Book(IND)
    blank = blanked_generic(IND)
    sheets = {s for s, _ in blank}
    maxcol = collections.defaultdict(int)
    for (s, c) in list(b.v) + list(b.f):
        if s in sheets:
            maxcol[s] = max(maxcol[s], col_idx(re.match(r"[A-Z]+", c).group(0)))
    helper = {}
    for s, c in sorted(blank):
        hc = col_let(maxcol[s] + 3)
        helper[(s, c)] = f"{hc}{re.search(r'\d+', c).group(0)}"
    def orig(s, c):
        f = b.f.get((s, c), "")
        m = re.match(r"^=IF\(" + re.escape(SEL) + r",(.*),\"\"\)$", f)
        if not m:
            sys.exit(f"{IND} {s}!{c}: not a blanked generic cell ({f!r})")
        return m.group(1)
    def rewrite(sheet, expr):
        def rep(m):
            qs, d1, col, d2, row = m.groups()
            s = qs.strip("'") if qs else sheet
            key = (s, f"{col}{row}")
            if key not in helper:
                return m.group(0)
            href = helper[key] if s == sheet else f"{sheet_ref(s, helper[key])}"
            return f"IF({SEL},{m.group(0)},{href})"
        return REF_RX.sub(rep, expr)
    n_dep = 0
    for (s, c), f in sorted(b.f.items()):
        if (s, c) in blank or not f.startswith("=") or SEL in f and f.startswith("=IF(" + SEL + ",\"\""):
            continue
        new = "=" + rewrite(s, f[1:])
        if new != f:
            plan.edit(IND, s, c, b.val(s, c), new, BLUE,
                      "reads a generic cell that is blank in Reg mode: original value from its helper cell")
            n_dep += 1
    for (s, c), hc in sorted(helper.items()):
        if b.val(s, hc) is not None or b.f.get((s, hc)):
            sys.exit(f"{IND} {s}!{hc}: helper cell not free")
        plan.edit(IND, s, hc, None, regonly(rewrite(s, orig(s, c))), BLUE,
                  f"helper: original value of the generic cell {c} (blank in Reg mode) for the formulas that use it")
    notes.append(f"generic cells blanked in Reg mode: {len(blank)}; dependent formulas rerouted: {n_dep}; helper cells: {len(helper)}")


def intra_commodities(top, chain):
    """Commodities touched only by processes of the moved chains (sector heat made in the sector, pulp,
    process heat, demand products): stay inside a region, no link."""
    touch = collections.defaultdict(set)
    for p, cs in top.items():
        for c, io in cs:
            touch[c].add(p)
    return {c for c, ps in touch.items() if ps and ps <= chain}


def run_4b(a):
    """Task 4b (audit/task4b.md): pulp and paper, lime, chemicals, fertiliser with their whole chains."""
    plan, notes = Plan(), []
    move4b = move_4b()
    move = dict(MOVE_4A)
    move.update(move4b)
    shares = shares_of(move)
    top, ctype, decl, dd_links = dd_info(a.dd, a.run)
    newtech = newtech_4b(top)
    keyshare = {k: load_key(k) for k in set(newtech.values())}
    chain = {p: sorted(shares[p]) for p in move4b}
    chain.update({p: sorted(keyshare[k]) for p, k in newtech.items()})
    mode = {}
    mode.update(plan_book(plan, IND, move, shares, notes))
    mode.update(plan_book(plan, SUP, move, shares, notes))
    plan_generic(plan, notes, extra=[p for p in move4b if mode.get(p) == "copy"])
    plan_demand_4b(plan, notes)
    plan_ava_4b(plan, newtech, notes)
    plan_ucs_general(plan, UC_4B, notes)
    plan_fill(plan, UCIND, "FILL-PUP", "G", 4, [5, 6, 7], {8: [5, 6, 7]}, ["G16", "G17", "G18"], notes)
    plan_fill(plan, UCIND, "INDPRC", "K", 5, list(range(6, 26)), {},
              [f"K{r}" for r in (33, 34, 35, 38, 39, 40, 43, 44, 45, 48, 49, 50)], notes)
    # corrections: linked sector heat counted as production in national sums (an import is not production)
    plan_ire_rows(plan, UCIND, "INDPRC", 32, "N", "O", [
        (53, {"B": "2011", "C": "C38", "H": q("ICHHTH"), "N": q("TB_ICHHTH_*"), "O": 'IFERROR(-K38,"")'}),
        (54, {"B": "2011", "C": "C48", "H": q("IPPHTH"), "N": q("TB_IPPHTH_*"), "O": 'IFERROR(-K48,"")'})], notes)
    plan_ire_rows(plan, UCIND, "CHPShares", 4, "K", "L", [
        (13, {"A": "A12", "D": q("IPPHTH"), "E": "E12", "K": q("TB_IPPHTH_*"), "L": "-G12"}),
        (14, {"A": "A6", "D": q("ICHHTH"), "E": "E6", "K": q("TB_ICHHTH_*"), "L": "-G6"})], notes)
    plan_ire_rows(plan, COAL, "UC_IPPCOA", 7, "N", "O", [
        (9, {"B": "2010", "C": q("TUC_UP_IPP_COA"), "H": q("IPPHTH"), "N": q("TB_IPPHTH_*"), "O": "-K8"})], notes)
    plan_comms_links(plan, move, shares, mode, a.dd, a.run, notes, chain=chain)
    new_links = {v for (cell, v, colour) in plan.sheets[LINKS][LINK_SHEET] if isinstance(v, str) and v.startswith("TB_")}
    plan_prd_corrections(plan, a.dd, a.run, new_links, notes)
    out = os.path.join(ROOT, "audit", "task4b_dryrun.txt")
    L = ["modes (4b): " + ", ".join(f"{p}={mode.get(p)}" for p in sorted(move4b)), "",
         "new technologies: " + ", ".join(f"{p}->{k}" for p, k in sorted(newtech.items())), ""]
    L += ["NOTE " + n for n in notes] + [""]
    for book in plan.books():
        L.append(f"--- {book}")
        for sheet, cell, old, new, colour, why in plan.edits.get(book, []):
            L.append(f"  ~ '{sheet}'!{cell} [{colour}]: {old!r}" + chr(10) + f"      -> {new}" + chr(10) + f"      ({why})")
        for sname, cells in plan.sheets.get(book, {}).items():
            L.append(f"  + sheet '{sname}' ({len(cells)} cells)")
            for cell, v, colour in cells:
                L.append(f"      {cell} [{colour}] {v}")
    open(out, "w", encoding="utf-8").write(chr(10).join(L) + chr(10))
    n_e = sum(len(v) for v in plan.edits.values())
    n_s = sum(len(c) for d in plan.sheets.values() for c in d.values())
    print(f"dry run 4b: {n_e} cell edits in {len(plan.edits)} workbooks, {n_s} cells on regenerated/new sheets -> {out}")
    for n in notes:
        print("NOTE", n[:400])
    if a.apply:
        import task3_power
        task3_power.MARK = MARK      # sheets made by this tool (4a) may be regenerated
        res = apply(plan)
        print(res)
        sys.exit(0 if all(v == "ok" for v in res.values()) else 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dd", default=os.path.join(ROOT, "GAMS_WrkTIMES"))
    ap.add_argument("--run", default="baseline-sami.run")
    ap.add_argument("--out", default=os.path.join(ROOT, "audit", "task4a_dryrun.txt"))
    ap.add_argument("--step", choices=["all", "prd", "insert", "fix", "4b", "4bfix", "4bfix2"], default="all",
                    help="prd: only the RS_PRD import corrections (after the rest is applied); "
                         "insert, then fix: corrections after the first 4a run (audit section 9)")
    a = ap.parse_args()
    if a.step == "insert":
        insert_ucis_rows(a.apply)
        return
    if a.step == "4b":
        run_4b(a)
        return
    if a.step in ("4bfix", "4bfix2"):
        plan, notes = Plan(), []
        if a.step == "4bfix":
            plan_generic_deps(plan, notes)
            out = os.path.join(ROOT, "audit", "task4b_fix_dryrun.txt")
        else:
            plan_minshare_elc(plan, notes)
            out = os.path.join(ROOT, "audit", "task4b_fix2_dryrun.txt")
        L = ["NOTE " + n for n in notes] + [""]
        for book in plan.books():
            L.append(f"--- {book}")
            for sheet, cell, old, new, colour, why in plan.edits.get(book, []):
                L.append(f"  ~ '{sheet}'!{cell} [{colour}]: {old!r}" + chr(10) + f"      -> {new}" + chr(10) + f"      ({why})")
        open(out, "w", encoding="utf-8").write(chr(10).join(L) + chr(10))
        print(f"dry run: {sum(len(v) for v in plan.edits.values())} cell edits -> {out}")
        print(chr(10).join(notes))
        if a.apply:
            res = apply(plan)
            print(res)
            sys.exit(0 if all(v == "ok" for v in res.values()) else 1)
        return
    if a.step == "fix":
        plan, notes = Plan(), []
        plan_hub_decl(plan, notes)
        plan_generic(plan, notes)
        plan_aggregates(plan, notes)
        plan_misc(plan, notes)
        plan_fills(plan, notes)
        b = Book(UCIND)
        plan_uc_shares(plan, notes, inserted="~UC_T" not in str(b.val("UC-IIS", "E27") or ""))
        out = os.path.join(ROOT, "audit", "task4a_fix_dryrun.txt")
        L = ["NOTE " + n for n in notes] + [""]
        for book in plan.books():
            L.append(f"--- {book}")
            for sheet, cell, old, new, colour, why in plan.edits.get(book, []):
                L.append(f"  ~ '{sheet}'!{cell} [{colour}]: {old!r}\n      -> {new}\n      ({why})")
        open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
        print(f"dry run: {sum(len(v) for v in plan.edits.values())} cell edits -> {out}")
        print(chr(10).join(notes))
        if a.apply:
            res = apply(plan)
            print(res)
            sys.exit(0 if all(v == "ok" for v in res.values()) else 1)
        return
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
