"""Task 5c: services buildings to the regions. Design and decisions: audit/task5c.md.

All changes are Reg-mode only (single-region values unchanged); helpers from tools/task4_industry.py.
  * VT_FINTIMES_COM: the 163 services processes (fuel supply COM*, existing end-use techs C_ES-*, building
    stock NRbldg-*, electric services NRbldg_*) declared in all 19 regions, not on the hub; coefficients copied,
    STOCK and NCAP_PASTI x floor-area key (Reg_COM). COMAHT00/COMGHT00 (VT_FINTIMES_SUP) likewise.
  * New technologies (SUBRES_30 C_ES-*, NRbldg_N-*; SubRES_31 NRbldg_*; COMBATS*; COMGASH2C*): all regions.
  * Demand: ZUDemand NR rows and the NewHouses 'ServBldg Projection' split by key; the gas-grid stock of
    COMGAS00 split as AGRGAS00 (5a).
  * Copy tables with an FI column -> AllRegions (COM_FR, SubRES_30 shares/updates, SubRES_31 savings/costs);
    lookups on VEDA fill sheets read a region column (Reg mode) or the national sum of the region columns.
  * End-use share constraints RCUC-* national; their coefficients from the national stock.
  * Commodities declared in all regions, links hub <-> region, RS_PRD corrections (task 4 helpers).

    python tools/task5c.py            # dry run -> audit/task5c_dryrun.txt
    python tools/task5c.py --apply    # after approval
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import task4_industry as T4  # noqa: E402
from task4_industry import (  # noqa: E402
    ALL, BLUE, DEMAND_4B, DEMAND_5A, DEMAND_5B, ENV_LINKS, GASGRID, GREEN, ICM_SITE, KEYS, LINK_SHEET, LINKS, M,
    MOVE_4A, MOVE_4C, ORANGE, REG19, ROOT, SEL, SUB15_T, SUP, SYS, Book, Plan, apply_per_book, col_idx, col_let,
    dd_info, load_key, move_4b, move_5a, move_5b, newtech_4b, newtech_4c, newtech_5a, newtech_5b, plan_aggregates,
    plan_ava_rows, plan_book, plan_comms_links, plan_demand_4b, plan_env_decl, plan_generic, plan_generic_deps_pre,
    plan_prd_corrections, q, read_tables, regonly, regs_of, shares_of, sheet_ref, sw, write_dry)

MARK = "Task 5c (tools/task5c.py)"
COM_BOOK = M + "VT_FINTIMES_COM.xlsx"
SUB30_T = M + "SubRES_TMPL/SUBRES_30_TECHS_HeatingCooling_Trans.xlsx"
SUB31_T = M + "SubRES_TMPL/SubRES_31_TECHS_BUILDINGS_COM_Trans.xlsx"
SUB14_T = M + "SubRES_TMPL/SubRES_14_TECHS_STORAGE_Trans.xlsx"
RSDCOM = M + "SuppXLS/Scen_UC_RSD-COM.xlsx"
NEWH = M + "SuppXLS/Scen_NewHouses_and_retrofits.xlsx"
COMFR = [M + "SuppXLS/Scen_DEMAND_Com-FR_Sami.xlsm", M + "SuppXLS/Scen_DEMAND_Com-FR.xlsm"]

# building types: process code / demand name -> raku 15f7 class key (audit/task5c.md section 2)
BT = {"HO": "care", "HR": "commercial", "OF": "officeedu", "SL": "commercial", "SS": "commercial", "SR": "assembly"}
TYPE = {"Hosp": "care", "HoRest": "commercial", "Offic": "officeedu", "ShopL": "commercial", "ShopS": "commercial",
        "SpoRecr": "assembly"}
HEAT = {"ELC": "elc", "HET": "dh", "GAS": "oilgas", "OIL": "oilgas", "LPG": "oilgas", "BIO": "wood", "COA": "coal",
        "GEO": "ground", "SOL": "all"}
FUELP = {"BIO": "wood", "COA": "coal", "GAS": "oilgas", "OIL": "oilgas", "LPG": "oilgas", "GEO": "ground", "HTH": "dh",
         "SOL": "all", "ELC": "all", "COO": "all", "AHT": "all", "GHT": "ground"}
POP = "population_2010"
SERV_ALL = "bld_services_all_2010"
DEMAND_5C = {"NR_BuildLight": SERV_ALL, "NR_BuildTech": SERV_ALL, "NR_ICTM": SERV_ALL, "NR_Refrig": SERV_ALL,
             "NR_Vent": SERV_ALL, "NR_StLight": POP}
DEMAND_TYPES = {f"NR_{t}": f"bld_{c}_all_2010" for t, c in TYPE.items()}
SUP_5C = ("COMAHT00", "COMGHT00")
SVC_RX = re.compile(r"^(C_ES-|NRbldg|COM(BIO|COA|COO|ELC|GAS|GEO|HTH|LPG|OIL|SOL|AHT|GHT|BATS|GASH2C))")
LOOKUP_REG = 'IF(ISNUMBER(MATCH("FI1B1",COM_All!$1:$1,0)),"FI1B1","FI")'


def _key(cls, heat):
    k = f"bld_{cls}_{heat}_2010"
    return k if os.path.exists(os.path.join(KEYS, k + ".csv")) else f"bld_{cls}_all_2010"


def key_of_5c(p):
    m = re.match(r"^C_ES-(SH|WH|SC|CK|SP)-(HO|HR|OF|SL|SS|SR)_([A-Z]{3})", p)
    if m:
        return _key(BT[m.group(2)], HEAT.get(m.group(3), "all") if m.group(1) in ("SH", "WH") else "all")
    m = re.match(r"^NRbldg_(?:N-)?(BuildLight|BuildTech|ICTM|Refrig|Vent|StLight)", p)
    if m:
        return POP if m.group(1) == "StLight" else SERV_ALL
    m = re.match(r"^NRbldg[-_](HoRest|Hosp|Offic|ShopL|ShopS|SpoRecr)", p)
    if m:
        return _key(TYPE[m.group(1)], "all")
    m = re.match(r"^COM(BIO|COA|GAS|OIL|LPG|GEO|HTH|SOL|ELC|COO|AHT|GHT)\d", p)
    if m:
        return _key("services", FUELP[m.group(1)])
    if p.startswith(("COMBATS", "COMGASH2C")):
        return SERV_ALL
    return None


def move_5c():
    out = {}
    for t in read_tables(os.path.join(ROOT, COM_BOOK), tags=("~FI_PROCESS",)):
        for r in t["rows"]:
            p = r["cells"].get("TechName", (0, None))[1]
            if not isinstance(p, str) or p.startswith("*"):
                continue
            k = key_of_5c(p)
            if not k:
                sys.exit(f"{COM_BOOK}: no key for {p}")
            out[p] = k
    return out


def newtech_5c(top, exclude):
    out = {}
    for p in top:
        if p in exclude or not SVC_RX.match(p):
            continue
        k = key_of_5c(p)
        if not k:
            sys.exit(f"new services process without a key: {p}")
        out[p] = k
    return out


# ------------------------------------------------------------------------------------------- copy tables
def table_at(book, sheet, tag_cell, tags=("~",)):
    T = [t for t in read_tables(os.path.join(ROOT, book), sheets=[sheet], tags=tags) if t["tag_cell"] == tag_cell]
    if len(T) != 1:
        sys.exit(f"{book} {sheet}!{tag_cell}: table not found")
    return T[0]


LOOKUP_RX = re.compile(r"MATCH\((\$?[A-Z]{1,3}\$?\d+),COM_All!\$1:\$1,0\)")


def lookup_bodies(book, sheet):
    """{cell: (value, single body, Reg body)} of every formula of the sheet that looks a COM_All fill column
    up by a region header: in Reg mode the key is a region column of the fill (values are copies)."""
    b = Book(book)
    out = {}
    for (s, c), f in b.f.items():
        if s == sheet and f and "COM_All!$1:$1" in f:
            body = f[1:]
            reg = LOOKUP_RX.sub(f"MATCH({LOOKUP_REG},COM_All!$1:$1,0)", body)
            if reg == body:
                sys.exit(f"{book} {sheet}!{c}: COM_All formula without a header lookup: {f!r}")
            out[c] = (b.val(s, c), body, reg)
    return out


def plan_fi_to_all(plan, book, sheet, tag_cell, notes, reg_bodies=None):
    """Copy rule for a ~TFM table with an FI column: FI -> AllRegions in Reg mode. With an AllRegions column
    too, that column becomes a comment and its values reach the FI column where the FI cell is empty.
    reg_bodies: Reg-mode bodies of fill-lookup formulas of the sheet (lookup_bodies); used and removed here
    for the FI cells of this table."""
    b = Book(book)
    reg_bodies = {} if reg_bodies is None else reg_bodies
    t = table_at(book, sheet, tag_cell)
    hr = t["header_row"]
    if "FI" not in t["cols"]:
        sys.exit(f"{book} {sheet}!{tag_cell}: no FI column")
    fcol = col_let(t["cols"]["FI"])
    fic = f"{fcol}{hr}"
    ff = b.f.get((sheet, fic))
    if ff and SEL in ff:
        notes.append(f"{os.path.basename(book)} {sheet}!{fic}: already switched")
        return
    plan.edit(book, sheet, fic, "FI", sw(ff[1:] if ff else q("FI"), q("AllRegions")), BLUE,
              "copy rule: the FI values apply in every region (Reg mode)")
    arc = next((h for h in t["cols"] if h.lower() == "allregions"), None)
    n_ar = n_lk = 0
    if arc:
        ac = f"{col_let(t['cols'][arc])}{hr}"
        if b.f.get((sheet, ac)):
            sys.exit(f"{book} {sheet}!{ac}: AllRegions header is a formula")
        plan.edit(book, sheet, ac, arc, sw(q(arc), q("*" + arc)), BLUE,
                  "AllRegions column off in Reg mode (the FI column takes its place)")
    self_ref = re.compile(r"^=\$?%s\$?(\d+)$" % fcol)
    for r in t["rows"]:
        c = r["cells"]
        cell = f"{fcol}{r['row']}"
        f, v = b.f.get((sheet, cell)), b.val(sheet, cell)
        arref = None
        if arc and arc in c:
            af = c[arc][2] or ""
            m = self_ref.match(af)
            if not (m and int(m.group(1)) == r["row"]):        # AllRegions = the FI cell itself: nothing to add
                arref = c[arc][0]
        if f:
            body = f[1:]
            reg = reg_bodies.pop(cell, (v, body, body))[2]
            if arref:
                reg = f'IF(({reg})="",{arref},{reg})'
                n_ar += 1
            if reg != body:
                plan.edit(book, sheet, cell, v, sw(body, reg), BLUE,
                          "Reg mode: fill lookup in a region column" + (", AllRegions value where empty" if arref else ""))
                n_lk += reg != body and not arref
        elif v is None and arref:
            plan.edit(book, sheet, cell, None, regonly(arref), GREEN, "Reg mode: the AllRegions value")
            n_ar += 1
    notes.append(f"{os.path.basename(book)} {sheet}!{tag_cell}: FI -> AllRegions"
                 + (f", {n_ar} AllRegions values" if arc else "") + (f", {n_lk} lookups" if n_lk else ""))


def plan_copy_tables(plan, notes):
    for f in COMFR:
        plan_fi_to_all(plan, f, "N_VEDA_INPUT", "E2", notes)
    for tc in ("A7", "A15"):
        plan_fi_to_all(plan, SUB30_T, "RES_Share", tc, notes)
    for sh, tc in (("COM_Saving", "A3"), ("COM_Invcost", "A3")):
        plan_fi_to_all(plan, SUB31_T, sh, tc, notes)
    # SUBRES_30 updates of the new techs from the base-year techs (COM_All fill), per sheet
    by_sheet = {}
    for t in read_tables(os.path.join(ROOT, SUB30_T), tags=("~TFM_UPD", "~TFM_INS")):
        if t["sheet"].startswith("INS-UPD") and "FI" in t["cols"]:
            by_sheet.setdefault(t["sheet"], []).append(t["tag_cell"])
    n_rest = 0
    for sh, tcs in sorted(by_sheet.items()):
        bodies = lookup_bodies(SUB30_T, sh)
        for tc in tcs:
            plan_fi_to_all(plan, SUB30_T, sh, tc, notes, reg_bodies=bodies)
        for cell, (v, body, reg) in sorted(bodies.items()):        # helper cells outside the FI columns
            plan.edit(SUB30_T, sh, cell, v, sw(body, reg), BLUE, "Reg mode: fill lookup in a region column")
            n_rest += 1
    notes.append(f"SUBRES_30 INS-UPD: {sum(map(len, by_sheet.values()))} tables, {n_rest} helper lookups outside them")


# ------------------------------------------------------------------------------------------- constraints
def plan_rcuc(plan, notes):
    """Scen_UC_RSD-COM: RCUC-* national; coefficients (shares) from the national stock in Reg mode."""
    b = Book(RSDCOM)
    sh = "UC1"
    for cell in ("C1", "C11"):
        v = b.val(sh, cell)
        if b.f.get((sh, cell)) or (v or "").replace(" ", "").upper() != "~UC_SETS:R_E:ALLREGIONS":
            sys.exit(f"{RSDCOM} {sh}!{cell} = {v!r}")
        plan.edit(RSDCOM, sh, cell, v, sw(q(v), q("~UC_Sets: R_S: AllRegions")), BLUE,
                  "end-use shares national (sum over the regions): same meaning as the single-region model")
    nt = 0
    for t in read_tables(os.path.join(ROOT, RSDCOM), sheets=[sh], tags=("~UC_T",)):
        nt += 1
        for h, c in t["cols"].items():
            hc = f"{col_let(c)}{t['header_row']}"
            f = b.f.get((sh, hc))
            if h.startswith("UC_RHSR"):
                plan.edit(RSDCOM, sh, hc, h, sw(q(h), q(h.replace("UC_RHSR", "UC_RHS", 1))), BLUE,
                          "national constraint: RHS without region (rsum_rhs_scan)")
            elif h == "FI":
                plan.edit(RSDCOM, sh, hc, h, sw(f[1:] if f else q(h), q("AllRegions")), BLUE,
                          "share coefficients apply in every region of the sum")
            elif h.upper() == "ALLREGIONS":
                sys.exit(f"{RSDCOM} {sh}!{hc}: AllRegions column next to FI")
    sa = "Stock-AF"
    rx = re.compile(r"^=SUMIFS\(INDEX\(Stock!\$2:\$500,,MATCH\(L\$1,Stock!\$1:\$1,0\)\),Stock!\$C\$2:\$C\$500,'Stock-AF'!\$C(\d+)\)"
                    r"\*SUMIFS\(INDEX\(AF!\$2:\$500,,MATCH\(L\$1,AF!\$1:\$1,0\)\),AF!\$C\$2:\$C\$500,'Stock-AF'!\$C(\d+)\)$")
    hdr = "COUNTIF(Region_selection!$K$8:$AD$8,{s}!$L$1:$BZ$1)>0"
    n = 0
    for r in range(2, 600):
        f = b.f.get((sa, f"L{r}"))
        if not f:
            continue
        m = rx.match(f)
        if not m or int(m.group(1)) != r or int(m.group(2)) != r:
            sys.exit(f"{RSDCOM} {sa}!L{r}: unexpected formula {f!r}")
        stock = f"SUMPRODUCT(($C{r}=Stock!$C$2:$C$500)*({hdr.format(s='Stock')}),Stock!$L$2:$BZ$500)"
        afs = f"SUMPRODUCT(($C{r}=AF!$C$2:$C$500)*({hdr.format(s='AF')}),AF!$L$2:$BZ$500)"
        afn = f"SUMPRODUCT(($C{r}=AF!$C$2:$C$500)*({hdr.format(s='AF')})*ISNUMBER(AF!$L$2:$BZ$500))"
        plan.edit(RSDCOM, sa, f"L{r}", b.val(sa, f"L{r}"), sw(f[1:], f"{stock}*IF({afn}>0,{afs}/{afn},0)"), BLUE,
                  "national stock x AF: sum of the regional stock columns of the fill, AF (copy) averaged over them")
        n += 1
    notes.append(f"{os.path.basename(RSDCOM)}: RCUC national ({nt} tables); Stock-AF national formulas: {n}")


# ------------------------------------------------------------------------------------------- demand, stocks
def plan_servbldg(plan, notes):
    """NewHouses 'ServBldg Projection' (NR_<type> COM_PROJ 2010/2060 from the ServBldg fill of NRbldg-* PASTI):
    Reg mode - national 2010 = sum of the region columns of the fill, the table is off, Reg_ServBldg splits
    every row by its building-type key (FI 0)."""
    b = Book(NEWH)
    sh = "ServBldg Projection"
    t = table_at(NEWH, sh, "C4", tags=("~TFM_DINS",))
    if b.val(sh, "F5") != "FI" or b.f.get((sh, "F5")):
        sys.exit(f"{NEWH} {sh}!F5 is not the plain header FI")
    plan.edit(NEWH, sh, "C4", "~TFM_DINS", sw(q("~TFM_DINS"), q("*~TFM_DINS (Reg mode: Reg_ServBldg)")), BLUE,
              "table off in Reg mode: its rows are split by region on Reg_ServBldg")
    rows = []
    for r in t["rows"]:
        rr = r["row"]
        cn, yr = r["cells"]["CSET_CN"][1], r["cells"]["Year"][1]
        if cn not in DEMAND_TYPES:
            sys.exit(f"{NEWH} {sh} row {rr}: demand {cn!r} without a key")
        f = b.f.get((sh, f"F{rr}"))
        if f and f.startswith("=SUMIF(ServBldg!"):
            nat = (f"SUMPRODUCT((ServBldg!$C$2:$C$42=$A{rr})*(COUNTIF(Region_selection!$K$8:$AD$8,"
                   f"ServBldg!$L$1:$BZ$1)>0),ServBldg!$L$2:$BZ$42)")
            plan.edit(NEWH, sh, f"F{rr}", b.val(sh, f"F{rr}"), sw(f[1:], nat), BLUE,
                      "national 2010 floor area = sum of the region columns of the ServBldg fill (Reg mode)")
        rows.append((rr, cn, yr))
    cells = [("A1", f"{MARK}: COM_PROJ of the services building types (NR_*) from 'ServBldg Projection' split by "
                    "their floor-area keys (audit/task5c.md); FI 0. Read only in Reg mode.", None),
             ("A3", regonly(q("~TFM_DINS")), GREEN)]
    for i, h in enumerate(["Attribute", "Year", "CSET_CN", "FI"] + REG19):
        cells.append((f"{col_let(1 + i)}4", regonly(q(h)), GREEN))
    for k, (rr, cn, yr) in enumerate(rows):
        r = 5 + k
        key = load_key(DEMAND_TYPES[cn])
        ref = sheet_ref(sh, f"F{rr}")
        cells += [(f"A{r}", regonly(q("COM_PROJ")), GREEN), (f"B{r}", regonly(repr(int(yr))), GREEN),
                  (f"C{r}", regonly(q(cn)), GREEN), (f"D{r}", regonly("0"), ORANGE)]
        for j, reg in enumerate(REG19):
            if key.get(reg):
                cells.append((f"{col_let(5 + j)}{r}", regonly(f"{ref}*{key[reg]!r}"), ORANGE))
        cells.append((f"{col_let(6 + len(REG19))}{r}", f"source {ref} x {DEMAND_TYPES[cn]}", None))
    plan.sheets[NEWH]["Reg_ServBldg"] = cells
    notes.append(f"NewHouses: Reg_ServBldg {len(rows)} rows (NR_* building-type demands)")


def plan_gasgrid(plan, notes):
    """Scen_X-NATIONALGRIDS STOCK rows of moved gas fuel processes (FI column): commented in Reg mode and split
    on Reg_GasGrid (regenerated: AGRGAS00 of 5a and COMGAS00 of 5c)."""
    rows = {"AGRGAS00": DEMAND_5A["AGR_Agr_For_Fis"], "COMGAS00": key_of_5c("COMGAS00")}
    T = read_tables(os.path.join(ROOT, GASGRID), tags=("~TFM_INS",))
    gb = Book(GASGRID)
    cells = [("A1", f"{MARK}: existing gas-grid stock of the gas fuel processes moved to the regions (5a AGRGAS00, "
                    "5c COMGAS00) split by their keys. Read only in Reg mode.", None),
             ("A3", regonly(q("~TFM_INS")), GREEN)]
    for i, h in enumerate(["Attribute", "Pset_PN", "Year"] + REG19):
        cells.append((f"{col_let(1 + i)}4", regonly(q(h)), GREEN))
    for k, (p, keyname) in enumerate(rows.items()):
        hit = [(t, r) for t in T for r in t["rows"] if r["cells"].get("Pset_PN", (0, None))[1] == p
               and str(r["cells"].get("Attribute", (0, ""))[1]).upper() == "STOCK"]
        if len(hit) != 1 or "FI" not in hit[0][1]["cells"]:
            sys.exit(f"{GASGRID}: {p} STOCK row not found once")
        t, r = hit[0]
        first_c = min(t["cols"].values())
        fcell = f"{col_let(first_c)}{r['row']}"
        fv, ff = gb.val(t["sheet"], fcell), gb.f.get((t["sheet"], fcell))
        if p == "AGRGAS00":
            if not (ff and SEL in ff):
                sys.exit(f"{GASGRID} {t['sheet']}!{fcell}: AGRGAS00 row not commented by 5a")
        else:
            if ff or not isinstance(fv, str) or fv.startswith("*"):
                sys.exit(f"{GASGRID} {t['sheet']}!{fcell}: first column {fv!r} {ff!r}")
            plan.edit(GASGRID, t["sheet"], fcell, fv, sw(q(fv), q("*" + fv)), BLUE,
                      f"{p} stock row: comment in Reg mode (split to the regions on Reg_GasGrid)")
        key = load_key(keyname)
        ref = sheet_ref(t["sheet"], r["cells"]["FI"][0])
        rr = 5 + k
        cells += [(f"A{rr}", regonly(q("STOCK")), GREEN), (f"B{rr}", regonly(q(p)), GREEN),
                  (f"C{rr}", regonly(repr(int(r["cells"]["Year"][1]))), GREEN)]
        for j, reg in enumerate(REG19):
            if key.get(reg):
                cells.append((f"{col_let(4 + j)}{rr}", regonly(f"{ref}*{key[reg]!r}"), ORANGE))
    plan.sheets[GASGRID]["Reg_GasGrid"] = cells
    notes.append("Reg_GasGrid: AGRGAS00 (5a, unchanged) and COMGAS00 stock split")


def comms_cell(name):
    b = Book(SYS)
    hits = [c for (s, c), v in b.v.items() if s == "Comms" and v == name and c.startswith("D")]
    if len(hits) != 1:
        sys.exit(f"{SYS} Comms: {len(hits)} cells with {name} in column D")
    return "C" + hits[0][1:]


# ------------------------------------------------------------------------------------------- main
def run(a):
    T4.MARK = MARK
    plan, notes = Plan(), []
    move4b, m5 = move_4b(), move_5a()
    move5a = {p: k for p, (bk, k) in m5.items()}
    move5b = move_5b()
    move5c = move_5c()
    sup5c = {p: key_of_5c(p) for p in SUP_5C}
    move = dict(MOVE_4A)
    for d in (move4b, MOVE_4C, move5a, move5b, move5c, sup5c):
        move.update(d)
    shares = shares_of(move)
    top, ctype, decl, dd_links = dd_info(a.dd, a.run)
    nt5c = newtech_5c(top, set(move5c) | set(sup5c))
    chain = {p: sorted(shares[p]) for p in list(move4b) + list(MOVE_4C) + list(move5a) + list(move5b)}
    for nt in (newtech_4b(top), newtech_4c(top), newtech_5a(set(move5a)), newtech_5b(set(move5b))):
        chain.update({p: regs_of(k) for p, k in nt.items()})
    for p in list(move5c) + list(sup5c) + list(nt5c):
        chain[p] = sorted(REG19)            # declared / available in all regions (stock by key)
    # 1. base-year processes
    mode = plan_book(plan, COM_BOOK, move5c, shares_of(move5c), notes, decl_all=True,
                     split_tags=("STOCK", "NCAP_PASTI", "PASTI"))
    mode.update(plan_book(plan, SUP, sup5c, shares_of(sup5c), notes, decl_all=True))
    if "Reg_SUP" in plan.sheets.get(SUP, {}):
        sys.exit("COMAHT00/COMGHT00 would regenerate Reg_SUP (4a): not expected")
    copied = [p for p in move5c if mode.get(p) == "copy"]
    plan_generic(plan, notes, extra=copied, books=(COM_BOOK,))
    plan_generic_deps_pre(plan, notes, COM_BOOK)
    # 2. demand and stocks outside the BY workbook
    plan_demand_4b(plan, notes, {**DEMAND_4B, **DEMAND_5A, **DEMAND_5B, **DEMAND_5C})
    plan_servbldg(plan, notes)
    plan_gasgrid(plan, notes)
    # 3. new technologies
    plan_ava_rows(plan, SUB30_T, [{"PSET_PN": "C_ES-*,NRbldg_N-*", "AllRegions": 1, "FI": 0}],
                  "new services end-use technologies in all regions, not on the hub (Reg mode)", notes)
    plan_ava_rows(plan, SUB31_T, [{"PSET_PN": "*", "AllRegions": 1, "FI": 0}],
                  "new services buildings and retrofits in all regions, not on the hub (Reg mode)", notes)
    plan_ava_rows(plan, SUB14_T, [{"PSET_PN": "COMBATS*", "AllRegions": 1, "FI": 0}],
                  "services batteries in all regions, not on the hub (Reg mode)", notes)
    plan_ava_rows(plan, SUB15_T, [{"PSet_PN": "COMGASH2C*", "AllRegions": 1, "FI": 0}],
                  "hydrogen blending into services gas in all regions, not on the hub (Reg mode)", notes)
    # 4. copy tables and constraints
    plan_copy_tables(plan, notes)
    plan_rcuc(plan, notes)
    # 5. commodities and links
    plan_aggregates(plan, notes, {"COMFINOIL": comms_cell("COMFINOIL")})
    env = sorted({c for p in list(move5c) + list(sup5c) + list(nt5c) for c, io in top.get(p, ())
                  if ctype.get(c) == "ENV" and decl.get(c, set()) == {"FI"}})
    if env:
        plan_env_decl(plan, env, notes)
    link_shares = dict(shares)
    for p in list(move5c) + list(sup5c):
        link_shares[p] = {r: 1.0 for r in REG19}
    old_links = {v for (s_, c_), v in Book(LINKS).v.items() if s_ == LINK_SHEET and isinstance(v, str) and v.startswith("TB_")}
    plan_comms_links(plan, move, link_shares, mode, a.dd, a.run, notes, chain=chain)
    cells = plan.sheets[LINKS][LINK_SHEET]
    have = {v for (_, v, _) in cells if isinstance(v, str) and v.startswith("TB_")}
    r = max(int(re.sub(r"^[A-Z]+", "", c)) for (c, _, _) in cells) + 1
    for c in ENV_LINKS:
        for reg in sorted(set(ICM_SITE.values())):
            name = f"TB_{c}_FI_{reg}"
            if name in have or (name in dd_links and name not in old_links):
                continue
            for j, v in enumerate(["FI", reg, c, c, c, name, "B"]):
                cells.append((f"{col_let(3 + j)}{r}", v, GREEN))
            r += 1
    new_links = {v for (_, v, _) in cells if isinstance(v, str) and v.startswith("TB_")}
    lost = sorted(old_links - new_links)
    if lost:
        sys.exit(f"links of 4a-5b would be lost: {lost[:10]} ({len(lost)})")
    notes.append(f"link sheet: {len(old_links)} links before, {len(new_links)} after; new commodities: "
                 f"{sorted({x.split('_FI_')[0][3:] for x in new_links - old_links})}")
    plan_prd_corrections(plan, a.dd, a.run, new_links, notes)
    head = [f"5c processes (VT_FINTIMES_COM): {len(move5c)}; SUP: {sorted(sup5c)}; new technologies: {len(nt5c)}",
            "keys: " + ", ".join(f"{p}={k}" for p, k in sorted({**move5c, **sup5c}.items())), "",
            "new technologies: " + ", ".join(f"{p}->{k}" for p, k in sorted(nt5c.items())), ""]
    write_dry(plan, notes, os.path.join(ROOT, "audit", "task5c_dryrun.txt"), head)
    if a.apply:
        apply_per_book(plan)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dd", default=os.path.join(ROOT, "GAMS_WrkTIMES"))
    ap.add_argument("--run", default="5bfix7.run")
    run(ap.parse_args())


if __name__ == "__main__":
    main()
