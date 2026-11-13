"""Task 3 (power): existing power and CHP plants, hydro, wind, PV and nuclear units to their regions.

Design (tested first on the server's DD files with tools/dd_regionalise.py --step3; solved with
TIMES 4.8.3 + CPLEX: objective 1,529,544.94 vs 1,529,541.78 M EUR for the skeleton with empty
regions (+0.0002 %), no dummy imports, every NCAP_PASTI / PRC_RESID total conserved):

1. Existing classes (VT_FINTIMES_ELC 'ELC_ExistingStock'): the ~FI_Process Region cell lists the
   regions with a non-zero key share (Reg mode). The ~FI_T data (no region column) follow.
2. Existing capacity (Scen_Power_from_JRC-IDEES-2015 CHP_VEDA / ELE_VEDA, NCAP_PASTI): the original
   ~TFM_DINS-TS tables are switched off in Reg mode; a Reg-only copy on sheet Reg_PASTI gives
   every region its share (value x key, Split rule; year-0 interpolation codes are not scaled).
   Hydro dams (BY_Trans HYDRO_CAP_ACTBND, STOCK): region columns added to the table.
3. Data written only in the FI column for these processes (AFA, EFF, CHPR, AF profiles, CEFF of
   the LowAF twins): copied to AllRegions in Reg mode (Copy rule). AF profiles of wind, PV and
   hydro are national profiles for now (yellow: regional profiles from reV/ENSPRESO in step 7).
4. Nuclear units (SubRES 00_Nuc-EU): available only at their site (Loviisa FI1B1, Olkiluoto FI196,
   Pyhajoki FI1D9) through ~TFM_AVA; the OL3 firm-commitment bound follows to FI196.
5. LowAF twins (SubRES 12, utilisation module) follow their plants; their pseudo commodities
   LowAF_* close inside each region (dummy suppliers LowAF_DumBase/DumPeak available there too)
   and are never traded.
6. User constraints:
   * per-plant identities UC_VARU_* ('Utilisation (2)'): R_E AllRegions (each region);
   * national electricity-system balances (VAR module, storage competition, non-decreasing RES
     capacity, coal share): R_S AllRegions (one constraint summed over the regions), RHS
     UC_RHSRT(S) -> UC_RHST(S), coefficients written in the FI column copied to AllRegions;
   * the coal share uses UC_COMPRD on ELCHIG: TIMES counts an internal import as production, so
     UC_IRE-I terms with the opposite coefficient are added on the internal links TB_ELCHIG_*;
   * variable electricity import (UC_VAR4_IMP, IRE set) excludes the internal links TB_*.
7. Internal links FI <-> region (new table on 'FI internal trades power') for every commodity the
   moved processes use in a region (fuels, power, heat, emissions, certificates), read from the
   server DD files; LowAF_* pseudo commodities are not linked.

Every written cell is coloured (CLAUDE.md): blue = switch, orange = key split, green = Reg-only
table, yellow = needs better data. Single-region mode is unchanged (checked after writing).

Usage:
    python tools/task3_power.py                 # dry run (prints every cell it would write)
    python tools/task3_power.py --apply         # write with xlwings
"""
import argparse
import collections
import csv
import glob
import os
import re
import shutil
import sys
import tempfile
import warnings

import openpyxl

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from task0 import ROOT, SEL, TRADE_PARAMS  # noqa: E402

M = "Reg-FINTIMES/"
REG19 = ["FI196", "FI198", "FI199", "FI19A", "FI19B", "FI1B1", "FI1C1", "FI1C2", "FI1C5", "FI1C6",
         "FI1C7", "FI1D5", "FI1D7", "FI1D8", "FI1D9", "FI1DA", "FI1DB", "FI1DC", "FI200"]
KEYS = os.path.join(ROOT, "data", "keys")
BLUE, ORANGE, GREEN, YELLOW = "#DDEBF7", "#FCE4D6", "#E2EFDA", "#FFF2CC"
SINGLE = "FINTIMES"
MARK = "Task 3 (tools/task3_power.py)"

# existing public power classes -> key (data/keys/power_<key>.csv, Energy Authority register)
CLASS_KEY = {
    "EUHYDDAM00": "EUHYDDAM00", "EEPP_windON": "EEPP_windON", "EEPP_windOFF": "EEPP_windOFF",
    "EEPP_PV": "EEPP_PV", "ECHP_coal_thermal": "ECHP_coal_thermal",
    "ECHP_lignite_thermal": "ECHP_lignite_thermal", "ECHP_biomass_thermal": "ECHP_biomass_thermal",
    "ECHP_naturalgas_CCGT": "ECHP_naturalgas", "ECHP_naturalgas_OCGT": "ECHP_naturalgas",
    "ECHP_naturalgas_thermal": "ECHP_naturalgas", "ECHP_HFO_thermal": "ECHP_HFO_thermal",
    "ECHP_LFO_thermal": "ECHP_LFO_thermal", "EEPP_coal_thermal": "EEPP_coal_thermal",
    "EEPP_lignite_thermal": "EEPP_lignite_thermal", "EEPP_naturalgas_CCGT": "EEPP_all",
    "EEPP_naturalgas_OCGT": "EEPP_all", "EEPP_naturalgas_thermal": "EEPP_all",
    "EEPP_HFO_thermal": "EEPP_HFO_thermal", "EEPP_LFO_thermal": "EEPP_LFO_thermal",
    "EEPP_biomass_thermal": "EEPP_biomass_thermal",
}
# nuclear units -> site region (STUK / Energy Authority register)
NUCLEAR = {"ENFI_LOVIISA-1_00": "FI1B1", "ENFI_LOVIISA-2_00": "FI1B1", "ENFI_OLKILUOTO-1_00": "FI196",
           "ENFI_OLKILUOTO-2_00": "FI196", "ENFI_OLKILUOTO-3": "FI196", "ENFI_OLKILUOTO-4": "FI196",
           "ENFI_PYHA-YOKI": "FI1D9"}
NUC_AVA = [("ENFI_LOVIISA*", "FI1B1"), ("ENFI_OLKILUOTO*", "FI196"), ("ENFI_PYHA*", "FI1D9")]
# plant -> LowAF twin: UC_VARU_CAP_* rows of Scen_SepDb-ZIET_VAR 'Utilisation (2)' (plant +1, twin -1)
TWINS = {"EEPP_HFO_thermal": "LowAF_EEPP_HFO_th", "EEPP_coal_thermal": "LowAF_EEPP_coal_th",
         "EEPP_lignite_thermal": "LowAF_EEPP_lignite_th", "EEPP_naturalgas_CCGT": "LowAF_EEPP_natgas_CCGT",
         "EEPP_naturalgas_OCGT": "LowAF_EEPP_natgas_OCGT", "EEPP_naturalgas_thermal": "LowAF_EEPP_naturalgas_th"}
LOWAF_DUMMIES = ["LowAF_DumBase", "LowAF_DumPeak"]

ELC = M + "VT_FINTIMES_ELC.xlsx"
JRC = M + "SuppXLS/Scen_Power_from_JRC-IDEES-2015.xlsx"
BYT = M + "BY_Trans.xlsx"
NUC = M + "SubRES_TMPL/SubRes_00_Nuc-EU_Trans.xlsx"
LOWAF = M + "SubRES_TMPL/SubRes_12_TECHS_PowerLowAF_Trans.xlsx"
VAR = M + "SuppXLS/Scen_SepDb-ZIET_VAR.xlsx"
STOR = M + "SuppXLS/Scen_SepDb-ZIET_VAR_Stor.xlsx"
UCELC = M + "SuppXLS/Scen_UC-ELC.xlsx"
LINKS = M + "SuppXLS/Trades/ScenTrade__Trade_Links.xlsx"
LINK_SHEET = "FI internal trades power"


def sw(single, reg):
    """Region switch formula (both arguments are Excel expressions)."""
    return f"=IF({SEL},{single},{reg})"


def regonly(expr):
    return f'=IF({SEL},"",{expr})'


def q(s):
    return '"' + str(s).replace('"', '""') + '"'


def col_idx(col):
    n = 0
    for ch in col:
        n = n * 26 + ord(ch) - 64
    return n


def col_let(n):
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def split(cell):
    m = re.match(r"([A-Z]+)(\d+)$", cell)
    return m.group(1), int(m.group(2))


class Book:
    """Cached values and formulas of one workbook (openpyxl, read only)."""

    def __init__(self, rel):
        self.rel = rel
        path = os.path.join(ROOT, rel)
        wv = openpyxl.load_workbook(path, read_only=True, data_only=True)
        wf = openpyxl.load_workbook(path, read_only=True, data_only=False)
        self.v, self.f = {}, {}
        for ws in wv.worksheets:
            try:
                for row in ws.iter_rows():
                    for c in row:
                        if getattr(c, "value", None) is not None:
                            self.v[(ws.title, c.coordinate)] = c.value
            except Exception:
                pass
        for ws in wf.worksheets:
            try:
                for row in ws.iter_rows():
                    for c in row:
                        x = getattr(c, "value", None)
                        if x is not None and not isinstance(x, (int, float, str)):
                            x = getattr(x, "text", str(x))         # array formulas
                        if isinstance(x, str) and x.startswith("="):
                            self.f[(ws.title, c.coordinate)] = x
            except Exception:
                pass
        self.sheets = wv.sheetnames
        wv.close()
        wf.close()

    def val(self, sheet, cell):
        v = self.v.get((sheet, cell))
        return None if v == "" else v

    def empty(self, sheet, cells):
        """Cells that are not free (a Reg-only formula written by this tool counts as free)."""
        own = f'=IF({SEL},"",'
        return [c for c in cells if (self.val(sheet, c) is not None or (sheet, c) in self.f)
                and not self.f.get((sheet, c), "").startswith(own)]


class Plan:
    def __init__(self):
        self.edits = collections.defaultdict(list)    # book -> [(sheet, cell, old, new, colour, why)]
        self.sheets = collections.defaultdict(dict)   # book -> {sheet: [(cell, value, colour)]}
        self.notes = []

    def edit(self, book, sheet, cell, old, new, colour, why):
        self.edits[book].append((sheet, cell, old, new, colour, why))

    def books(self):
        return sorted(set(self.edits) | set(self.sheets))


# ----------------------------------------------------------------------------------------- keys

def load_key(name):
    path = os.path.join(KEYS, f"power_{name}.csv")
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    s = {r["region"]: float(r["share"]) for r in rows if r["region"] in REG19}
    tot = sum(s.values())
    if abs(tot - 1.0) > 1e-9:
        sys.exit(f"{path}: shares sum to {tot!r}, not 1")
    return s


def keys_sheet(keys, title):
    """Reg_Keys sheet: one row per key, one column per region (orange), sum check (must be 1)."""
    cells = [("A1", f"{MARK}: regional shares (Split rule). Source: data/keys/power_<key>.csv "
                    "(tools/power_register.py, tools/power_keys.py; audit/power_keys.md).", None),
             ("A2", title, None), ("A4", "Key", GREEN), ("B4", "Source", GREEN)]
    pos = {}
    for j, r in enumerate(REG19):
        cells.append((f"{col_let(3 + j)}4", r, GREEN))
    sumcol = col_let(3 + len(REG19))
    cells.append((f"{sumcol}4", "Sum (=1)", GREEN))
    for i, name in enumerate(sorted(keys)):
        row = 5 + i
        cells += [(f"A{row}", name, GREEN), (f"B{row}", f"data/keys/power_{name}.csv", GREEN)]
        for j, r in enumerate(REG19):
            cells.append((f"{col_let(3 + j)}{row}", round(keys[name].get(r, 0.0), 15), ORANGE))
            pos[(name, r)] = f"Reg_Keys!${col_let(3 + j)}${row}"
        cells.append((f"{sumcol}{row}", f"=SUM(C{row}:{col_let(2 + len(REG19))}{row})", GREEN))
    return cells, pos


# ---------------------------------------------------------------------------------- plan parts

def plan_elc(plan, shares):
    b = Book(ELC)
    sh = "ELC_ExistingStock"
    assert b.val(sh, "O1") == "~FI_Process" and b.val(sh, "P2") == "Region" and b.val(sh, "Q2") == "TechName"
    done = set()
    for r in range(3, 60):
        p = b.val(sh, f"Q{r}")
        if p in CLASS_KEY:
            regs = [x for x in REG19 if shares[p].get(x, 0) > 0]
            old = b.val(sh, f"P{r}")
            if old != "FI":
                sys.exit(f"{ELC} {sh}!P{r}: region {old!r}, expected FI")
            plan.edit(ELC, sh, f"P{r}", "FI", sw('"FI"', q(",".join(regs))), BLUE,
                      f"{p}: declared in its {len(regs)} regions (key power_{CLASS_KEY[p]})")
            done.add(p)
    miss = set(CLASS_KEY) - done
    if miss:
        sys.exit(f"{ELC}: classes not found: {sorted(miss)}")
    print(f"{ELC}: {len(done)} existing classes declared in their regions")


def plan_pasti(plan, shares, keys):
    b = Book(JRC)
    cells, pos = keys_sheet({k: keys[k] for k in sorted({CLASS_KEY[p] for p in CLASS_KEY})},
                            "Existing power/CHP capacity by NUTS-3 region (Energy Authority power plant register).")
    plan.sheets[JRC]["Reg_Keys"] = cells
    out = [("A1", f"{MARK}: existing capacity (NCAP_PASTI) of the power and CHP classes by region = "
                  "national value (sheets CHP_VEDA / ELE_VEDA) x regional share (sheet Reg_Keys). "
                  "Read by VEDA only in Reg-FINTIMES mode; the original tables are then switched off.", None)]
    row = 3
    n_rows = 0
    for src, last_col in (("CHP_VEDA", "M"), ("ELE_VEDA", "T")):
        tag = b.val(src, "B1")
        if tag != "~TFM_DINS-TS":
            sys.exit(f"{JRC} {src}!B1 = {tag!r}")
        plan.edit(JRC, src, "B1", tag, sw('"~TFM_DINS-TS"', '"TFM_DINS-TS (Reg-FINTIMES: see sheet Reg_PASTI)"'),
                  BLUE, "national PASTI table off in Reg mode (replaced by regional rows on Reg_PASTI)")
        cols = [col_let(i) for i in range(2, col_idx(last_col) + 1)]
        hdr = {c: b.val(src, f"{c}2") for c in cols}
        assert hdr["B"] == "Region" and hdr["C"] == "Attribute" and hdr["D"] == "PSET_PN" and hdr["E"] == 0, hdr
        ycols = [c for c in cols if c not in ("B", "C", "D")]
        out.append((f"B{row}", regonly('"~TFM_DINS-TS"'), GREEN))
        for c in cols:
            out.append((f"{c}{row + 1}", f"={src}!{c}2", GREEN))
        row += 2
        r = 3
        while b.val(src, f"D{r}") is not None:
            p = b.val(src, f"D{r}")
            vals = {c: b.val(src, f"{c}{r}") for c in ycols}
            has = any(isinstance(vals[c], (int, float)) and c != "E" for c in ycols)
            if p not in CLASS_KEY:
                if has:
                    sys.exit(f"{JRC} {src} row {r}: {p} has capacity but is not a moved class")
                r += 1
                continue
            if not has:
                r += 1
                continue
            k = CLASS_KEY[p]
            for reg in REG19:
                if shares[p].get(reg, 0) <= 0:
                    continue
                out += [(f"B{row}", reg, GREEN), (f"C{row}", f"={src}!C{r}", GREEN),
                        (f"D{row}", f"={src}!D{r}", GREEN)]
                for c in ycols:
                    if c == "E":       # year 0 = interpolation option code: copied, never scaled
                        out.append((f"{c}{row}", f'=IF(ISNUMBER({src}!{c}{r}),{src}!{c}{r},"")', GREEN))
                    else:
                        out.append((f"{c}{row}", f'=IF(ISNUMBER({src}!{c}{r}),{src}!{c}{r}*{pos[(k, reg)]},"")',
                                    ORANGE))
                row += 1
                n_rows += 1
            r += 1
        row += 2
    plan.sheets[JRC]["Reg_PASTI"] = out
    print(f"{JRC}: Reg_PASTI with {n_rows} region x class rows; Reg_Keys with {len(pos) // len(REG19)} keys")
    # FI-only data of these processes -> AllRegions (Copy rule)
    sh = "Other charact"
    n = 0
    for tag_row, allc, fic in ((2, "G", "H"), (40, "G", "H"), (56, "G", "H"), (33, "H", "I")):
        hr = tag_row + 1
        assert b.val(sh, f"{allc}{hr}") == "AllRegions" and b.val(sh, f"{fic}{hr}") == "FI", (sh, hr)
        r = hr + 1
        while b.val(sh, f"B{r}") is not None:
            if b.val(sh, f"{allc}{r}") is None and b.val(sh, f"{fic}{r}") is not None:
                plan.edit(JRC, sh, f"{allc}{r}", None, regonly(f"{fic}{r}"), BLUE,
                          f"{b.val(sh, f'B{r}')} {b.val(sh, f'D{r}')}: FI value copied to AllRegions (Copy rule)")
                n += 1
            r += 1
    print(f"{JRC} {sh}: {n} FI values copied to AllRegions")


def plan_by_trans(plan, shares, keys):
    b = Book(BYT)
    sh = "SolWin-AF"
    for cell, p in (("E4", "EEPP_WindON"), ("E34", "EEPP_PV")):
        assert b.val(sh, cell) == "FI", (sh, cell)
        plan.edit(BYT, sh, cell, "FI", sw('"FI"', '"AllRegions"'), YELLOW,
                  f"AF profile of {p}: national profile in every region (regional reV/ENSPRESO profiles: step 7)")
    sh = "HYDRO_CAP_ACTBND"
    assert b.val(sh, "H31") == "FI" and b.val(sh, "F31") == "Attribute"
    plan.edit(BYT, sh, "H31", "FI", sw('"FI"', '"AllRegions"'), YELLOW,
              "AF profile of EUHYDDAM00: national profile in every region (regional inflow data: step 7)")
    assert [b.val(sh, c) for c in ("D4", "F4", "G4", "H4")] == ["STOCK", "Pset_PN", "AllRegions", "FI"] or \
        [b.val(sh, c) for c in ("D4", "F4", "G4", "H4")] == ["Attribute", "Pset_PN", "AllRegions", "FI"], \
        [b.val(sh, c) for c in ("D4", "F4", "G4", "H4")]
    regs = [r for r in REG19 if shares["EUHYDDAM00"].get(r, 0) > 0]
    cols = [col_let(9 + j) for j in range(len(regs))]       # I, J, ...
    busy = b.empty(sh, [f"{c}{r}" for c in cols for r in range(3, 26)])
    if busy:
        sys.exit(f"{BYT} {sh}: cells for the regional columns are not empty: {busy[:5]}")
    cells, pos = keys_sheet({"EUHYDDAM00": keys["EUHYDDAM00"]}, "Existing hydro (dams/reservoirs) by NUTS-3 region.")
    plan.sheets[BYT]["Reg_Keys"] = cells
    for c, reg in zip(cols, regs):
        plan.edit(BYT, sh, f"{c}4", None, regonly(q(reg)), GREEN, f"region column {reg} (Reg mode only)")
        for r in range(5, 25):
            if b.val(sh, f"F{r}") == "EUHYDDAM00" and b.val(sh, f"D{r}") == "STOCK":
                plan.edit(BYT, sh, f"{c}{r}", None, regonly(f"$H{r}*{pos[('EUHYDDAM00', reg)]}"), ORANGE,
                          f"EUHYDDAM00 STOCK {b.val(sh, f'E{r}')} x share {reg}")
    print(f"{BYT}: hydro STOCK split over {len(regs)} regions; 3 AF profiles to AllRegions (yellow)")


def plan_nuclear(plan):
    b = Book(NUC)
    sh = "NUC"
    assert [b.val(sh, c) for c in ("B3", "C3", "D3", "B4", "C4", "B5", "D5")] == \
        ["PSET_PN", "AllRegions", "FI", "*", 0, "ENFI*", 1]
    busy = b.empty(sh, [f"{c}{r}" for c in "BCDEFG" for r in range(6, 10)] + ["E3", "F3", "G3"])
    if busy:
        sys.exit(f"{NUC} {sh}: target cells not empty: {busy}")
    plan.edit(NUC, sh, "D5", 1, sw("1", "0"), BLUE, "ENFI* not on the FI hub in Reg mode (each unit at its site)")
    for i, (pat, reg) in enumerate(NUC_AVA):
        c = col_let(5 + i)
        plan.edit(NUC, sh, f"{c}3", None, regonly(q(reg)), GREEN, f"region column {reg}")
        plan.edit(NUC, sh, f"B{6 + i}", None, regonly(q(pat)), GREEN, f"{pat} available in {reg}")
        plan.edit(NUC, sh, f"{c}{6 + i}", None, regonly("1"), GREEN, f"{pat} available in {reg}")
    sh = "Updates"
    assert b.val(sh, "A23") == "~TFM_DINS-AT" and b.val(sh, "B24") == "Region" and b.val(sh, "D25") == "ENFI_OLKILUOTO-3"
    plan.edit(NUC, sh, "B25", "FI", sw('"FI"', '"FI196"'), BLUE, "OL3 firm commitment (NCAP_BND N) at its site FI196")
    print(f"{NUC}: nuclear units at Loviisa (FI1B1), Olkiluoto (FI196), Pyhajoki (FI1D9)")


def plan_lowaf(plan, shares):
    b = Book(LOWAF)
    sh = "AVA"
    assert [b.val(sh, c) for c in ("B2", "B3", "C3", "D3", "E3", "C4", "D4", "E4")] == \
        ["~TFM_AVA", "PSET_SET", "PSET_PN", "AllRegions", "FI", "*", 0, 1]
    last = 4
    while b.val(sh, f"C{last + 1}") is not None:          # last row of the ~TFM_AVA table
        last += 1
    regs_by_twin = {t: [r for r in REG19 if shares[p].get(r, 0) > 0] for p, t in TWINS.items()}
    union = [r for r in REG19 if any(r in v for v in regs_by_twin.values())]
    cols = {r: col_let(6 + j) for j, r in enumerate(union)}      # F, G, ...
    first = last + 1
    rows = list(TWINS.values()) + LOWAF_DUMMIES
    busy = b.empty(sh, [f"{c}{r}" for c in ["C", "E"] + list(cols.values()) for r in range(first, first + len(rows))]
                   + [f"{c}3" for c in cols.values()] + [f"{c}{r}" for c in cols.values() for r in range(4, first)])
    if busy:
        sys.exit(f"{LOWAF} {sh}: target cells not empty: {busy[:5]}")
    for r, c in cols.items():
        plan.edit(LOWAF, sh, f"{c}3", None, regonly(q(r)), GREEN, f"region column {r}")
    for i, name in enumerate(rows):
        row = first + i
        plan.edit(LOWAF, sh, f"C{row}", None, regonly(q(name)), GREEN,
                  "twin follows its plant" if name in regs_by_twin else "free dummy supplier of the LowAF pseudo inputs")
        if name in regs_by_twin:
            plan.edit(LOWAF, sh, f"E{row}", None, regonly("0"), GREEN, f"{name} not on the FI hub (plant moved)")
            here = regs_by_twin[name]
        else:
            here = union
        for r in here:
            plan.edit(LOWAF, sh, f"{cols[r]}{row}", None, regonly("1"), GREEN, f"{name} available in {r}")
    print(f"{LOWAF}: {len(TWINS)} twins follow their plants; LowAF dummies in {len(union)} regions")
    return union


def uc_sets_switch(plan, book, b, sheet, cell, reg_text, why, colour=BLUE):
    v = b.val(sheet, cell)
    if not (isinstance(v, str) and v.startswith("~UC_Sets")):
        sys.exit(f"{book} {sheet}!{cell} = {v!r}")
    plan.edit(book, sheet, cell, v, sw(q(v), q(reg_text)), colour, why)


def rhs_headers(plan, book, b, sheet, rows):
    n = 0
    for (s, cell), v in sorted(b.v.items()):
        if s != sheet or split(cell)[1] not in rows or not isinstance(v, str) or not v.startswith("UC_RHSRT"):
            continue
        plan.edit(book, sheet, cell, v, sw(q(v), q(v.replace("UC_RHSRT", "UC_RHST", 1))), BLUE,
                  "national constraint: RHS without region (R_S)")
        n += 1
    return n


def copy_fi_to_all(plan, book, b, sheet, hdr_row, allc, fic, first, last):
    assert str(b.val(sheet, f"{allc}{hdr_row}")).lower() == "allregions" and b.val(sheet, f"{fic}{hdr_row}") == "FI"
    n = 0
    for r in range(first, last + 1):
        if b.val(sheet, f"{allc}{r}") is None and b.val(sheet, f"{fic}{r}") is not None:
            plan.edit(book, sheet, f"{allc}{r}", None, regonly(f"{fic}{r}"), BLUE,
                      "coefficient written for FI only: every region (Copy rule)")
            n += 1
    return n


def plan_ucs(plan):
    nat = "~UC_Sets: R_S: AllRegions"
    why = "national electricity-system constraint: one constraint summed over FI and the regions"
    # --- VAR module
    b = Book(VAR)
    uc_sets_switch(plan, VAR, b, "Variables", "B17", nat, why)
    n = rhs_headers(plan, VAR, b, "Variables", range(18, 60))
    assert b.val("Variables", "B43") == "UC_VAR4_IMP" and b.val("Variables", "D43") == "-EXPCO2*"
    plan.edit(VAR, "Variables", "D43", "-EXPCO2*", sw('"-EXPCO2*"', '"-EXPCO2*,-TB_*"'), BLUE,
              "variable import = imports from abroad only (internal links TB_* excluded)")
    for c, rows in (("C13", range(15, 25)), ("C26", range(28, 37))):
        uc_sets_switch(plan, VAR, b, "CapIntermitt", c, nat, why)
        n += rhs_headers(plan, VAR, b, "CapIntermitt", rows)
    v = b.val("Utilisation (2)", "B2")
    assert v == "~UC_Sets: R_E: AllRegions", v
    plan.edit(VAR, "Utilisation (2)", "B2", v, sw(q(v), q(v)), BLUE,
              "per-plant utilisation identities (UC_VARU_*): in every region where the plant and its twin are")
    print(f"{VAR}: Variables + CapIntermitt (SystemAdequacy, MINDISP) national, {n} RHS headers; "
          "UC_VARU_* per region; UC_VAR4_IMP without TB_*")
    # --- storage / excess module
    b = Book(STOR)
    sh = "UC_VAR2_EXC"
    uc_sets_switch(plan, STOR, b, sh, "B7", nat, why)
    n = rhs_headers(plan, STOR, b, sh, range(8, 121))
    m = 0
    for hdr in (12, 24, 33, 42, 82):
        m += copy_fi_to_all(plan, STOR, b, sh, hdr, "O", "P", hdr + 1, hdr + 7)
    uc_sets_switch(plan, STOR, b, sh, "D122", nat, why)
    n += rhs_headers(plan, STOR, b, sh, range(124, 135))
    assert b.val(sh, "J103") == "~TFM_INS" and b.val(sh, "P104") == "FI" and b.val(sh, "J105") == "CEFF"
    plan.edit(STOR, sh, "P104", "FI", sw('"FI"', '"AllRegions"'), BLUE, "CEFF of the LowAF twins in every region (Copy rule)")
    sh = "UC_StorageCompetition"
    uc_sets_switch(plan, STOR, b, sh, "C32", nat, why)
    n += rhs_headers(plan, STOR, b, sh, range(34, 45))
    print(f"{STOR}: VAR2/VAR3, utilisation and storage competition national, {n} RHS headers, "
          f"{m} FI coefficients copied to AllRegions")
    # --- UC-ELC
    b = Book(UCELC)
    uc_sets_switch(plan, UCELC, b, "DESERTEC", "B3", nat, "non-decreasing national RES capacity (summed over regions)")
    n = rhs_headers(plan, UCELC, b, "DESERTEC", range(5, 15))
    sh = "Coal ELC Share"
    uc_sets_switch(plan, UCELC, b, sh, "A2", nat, "national coal share of power production")
    n += rhs_headers(plan, UCELC, b, sh, range(3, 6))
    assert b.val(sh, "F3") == "~UC_T: UC_COMPRD~UP" and b.val(sh, "H4") == "FI" and b.val(sh, "E5") == "ELCHIG"
    plan.edit(UCELC, sh, "H4", "FI", sw('"FI"', '"AllRegions"'), BLUE,
              "ELCHIG production of every region in the national share (Copy rule)")
    busy = b.empty(sh, [f"{c}{r}" for c in "ABCDEFGHIJ" for r in range(23, 28)])
    if busy:
        sys.exit(f"{UCELC} {sh}: rows 23-27 not empty: {busy}")
    plan.edit(UCELC, sh, "A24", None, regonly('"~UC_T"'), GREEN, "internal-link correction (Reg mode only)")
    for c, h in zip("ABCDE", ("UC_N", "Pset_PN", "Cset_CN", "Year", "UC_IRE-I")):
        plan.edit(UCELC, sh, f"{c}25", None, regonly(q(h)), GREEN, "internal-link correction header")
    for c, e in zip("ABCDE", ("A5", '"TB_ELCHIG_*"', '"ELCHIG"', "F5", "-H5")):
        plan.edit(UCELC, sh, f"{c}26", None, regonly(e), GREEN,
                  "TIMES counts an internal ELCHIG import as production: subtract it (coefficient = -UC_COMPRD)")
    print(f"{UCELC}: NonDecr RES capacity and coal share national ({n} RHS headers), TB_ELCHIG_* correction")


def dd_commodities(dd_dir, run, moved):
    """Commodities each moved process uses in the server's DD files (TOP, FLO_EMIS, ...)
    plus the emissions of those commodities (VDA_EMCB)."""
    tok = re.compile(r"'([^']*)'")
    files = re.findall(r"BATINCLUDE\s+(\S+\.dd)", open(os.path.join(dd_dir, run), encoding="latin-1").read())
    declared, emcb, used = set(), collections.defaultdict(set), collections.defaultdict(set)
    lines = []
    for f in files:
        blk = None
        for l in open(os.path.join(dd_dir, f), encoding="latin-1"):
            m = re.match(r"^([A-Z_][A-Z0-9_]*) ' '/", l) or re.match(r"^SET ([A-Z_][A-Z0-9_]*)", l)
            if m:
                blk = m.group(1)
                continue
            t = tok.findall(l)
            if len(t) < 2 or t[0] != "FI":
                continue
            if blk == "COM_UNIT":
                declared.add(t[1])
            elif blk == "VDA_EMCB" and len(t) >= 3:
                emcb[t[1]].add(t[2])
            lines.append(t)
    for t in lines:
        for p in t[1:3]:
            if p in moved:
                used[p] |= {x for x in t[2:] if x in declared}
    for p in used:
        used[p] |= {e for c in list(used[p]) for e in emcb.get(c, ())}
    return used


def plan_links(plan, shares, dd_dir, run):
    moved = dict(shares)
    for p, t in TWINS.items():
        moved[t] = shares[p]
    for p, r in NUCLEAR.items():
        moved[p] = {r: 1.0}
    used = dd_commodities(dd_dir, run, moved)
    miss = [p for p in moved if p not in used]
    if miss:
        sys.exit(f"no DD lines for {miss} in {dd_dir}/{run}")
    pairs = collections.defaultdict(set)
    for p, sh in moved.items():
        for r, s in sh.items():
            if s > 0:
                pairs[r] |= {c for c in used[p] if not c.startswith("LowAF_")}
    b = Book(LINKS)
    pilot = {(str(b.val("FI internal trades", f"D{r}")), str(b.val("FI internal trades", f"E{r}")))
             for r in range(4, 40) if b.val("FI internal trades", f"E{r}")}
    rows = sorted((r, c) for r in pairs for c in pairs[r] if (r, c) not in pilot)
    sel_reg = "Region_selection!$B$8=Region_selection!$D$9"
    cells = [("A1", f"{MARK}: internal links FI hub <-> region for every commodity the moved power plants "
                    "use there (fuels, power, heat, emissions, certificates; read from the server DD files). "
                    "LowAF_* pseudo commodities close inside each region and are not linked.", None),
             ("C2", f'=IF({sel_reg},"~TradeLinks_DINS","TradeLinks_DINS")', GREEN)]
    for c, h in zip("CDEFGHI", ("Reg1", "Reg2", "Comm", "Comm1", "Comm2", "Tech", "TradeLink")):
        cells.append((f"{c}3", h, GREEN))
    for i, (r, c) in enumerate(rows):
        row = 4 + i
        for col, v in zip("CDEFGHI", ("FI", r, c, c, c, f"TB_{c}_FI_{r}", "B")):
            cells.append((f"{col}{row}", v, GREEN))
    plan.sheets[LINKS][LINK_SHEET] = cells
    per_c = collections.Counter(c for _, c in rows)
    print(f"{LINKS}: {len(rows)} new links on '{LINK_SHEET}' ({len(pairs)} regions): "
          + ", ".join(f"{c} {n}" for c, n in sorted(per_c.items())))
    return rows


# ------------------------------------------------------------------------------------- apply

def apply(plan, log=print):
    import xlwings as xw
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    res = {}
    tmp = tempfile.mkdtemp(prefix="task3_")
    tpl_path = os.path.join(tmp, "region_selection_template.xlsx")
    shutil.copyfile(os.path.join(ROOT, TRADE_PARAMS), tpl_path)
    try:
        tpl = app.books.open(tpl_path, update_links=False, read_only=True)
        for book in plan.books():
            path = os.path.join(ROOT, book)
            wb = app.books.open(path, update_links=False)
            try:
                names = [s.name for s in wb.sheets]
                if "Region_selection" in names:
                    if wb.sheets["Region_selection"].range("B8").value != SINGLE:
                        raise RuntimeError("Region_selection!B8 is not FINTIMES")
                else:
                    tpl.sheets["Region_selection"].copy(after=wb.sheets[-1])
                    ws = wb.sheets[-1]
                    ws.name = "Region_selection"
                    ws.range("B30:C40").clear()
                    log(f"  {book}: Region_selection sheet added")
                for sname, cells in plan.sheets.get(book, {}).items():
                    if sname in [s.name for s in wb.sheets]:
                        ws = wb.sheets[sname]
                        if not str(ws.range("A1").value or "").startswith(MARK):
                            raise RuntimeError(f"sheet {sname} exists and was not made by this tool")
                        ws.delete()
                    ws = wb.sheets.add(sname, after=wb.sheets[-1])
                    for cell, v, colour in cells:
                        ws.range(cell).formula = v if isinstance(v, str) else v
                        if colour:
                            ws.range(cell).color = colour
                    log(f"  {book}: sheet {sname} ({len(cells)} cells)")
                todo = []
                for sheet, cell, old, new, colour, why in plan.edits.get(book, []):
                    rng = wb.sheets[sheet].range(cell)
                    if isinstance(new, str) and new.startswith("="):
                        done = (rng.formula or "").replace("_xlfn.", "") == new.replace("_xlfn.", "")
                    else:
                        done = rng.value == new
                    if done:
                        continue
                    cur = rng.value
                    same = (cur in (None, "") and old is None) or cur == old or \
                        (isinstance(cur, float) and isinstance(old, (int, float)) and abs(cur - old) < 1e-12)
                    if not same:
                        raise RuntimeError(f"{sheet}!{cell} holds {cur!r}, dry run expected {old!r}")
                    todo.append((sheet, cell, new))
                for sheet, cell, new in todo:
                    wb.sheets[sheet].range(cell).formula = new if isinstance(new, str) else new
                for sheet, cell, old, new, colour, why in plan.edits.get(book, []):
                    wb.sheets[sheet].range(cell).color = colour
                log(f"  {book}: {len(todo)} cell(s) written, {len(plan.edits.get(book, [])) - len(todo)} already in place")
                # a reference to a sheet written before the sheet existed becomes an external link
                # named like the sheet: remove only those (other external links belong to the model)
                ours = set(plan.sheets.get(book, {}))
                for link in (wb.api.LinkSources(1) or []):
                    if os.path.basename(str(link)) in ours or "region_selection_template" in str(link):
                        wb.api.BreakLink(link, 1)
                        log(f"  {book}: stray external link removed: {link}")
                write_legend(wb)
                app.calculate()
                for sheet, cell, old, new, colour, why in plan.edits.get(book, []):
                    cur = wb.sheets[sheet].range(cell).value
                    ok = (cur in (None, "") and old is None) or cur == old or \
                        (isinstance(cur, float) and isinstance(old, (int, float)) and abs(cur - old) < 1e-12)
                    if not ok:
                        raise RuntimeError(f"single-region value of {sheet}!{cell} is {cur!r}, expected {old!r}")
                wb.save()
                res[book] = "ok"
                log(f"  saved {book}")
            except Exception as ex:
                res[book] = f"FAILED: {ex}"
                log(f"  FAILED {book}: {ex} (not saved)")
            finally:
                wb.close()
        tpl.close()
    finally:
        app.quit()
        shutil.rmtree(tmp, ignore_errors=True)
    return res


def write_legend(wb):
    from task0_apply import write_legend as wl
    wl(wb, log=lambda *a: None)


# --------------------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dd", default=os.path.join(ROOT, "GAMS_WrkTIMES"), help="server DD folder")
    ap.add_argument("--run", default="baseline-reg_new.run", help="run file listing the DD files")
    ap.add_argument("--out", default=os.path.join(ROOT, "audit", "task3_power_dryrun.txt"))
    a = ap.parse_args()
    keys = {k: load_key(k) for k in sorted(set(CLASS_KEY.values()))}
    shares = {p: keys[k] for p, k in CLASS_KEY.items()}
    plan = Plan()
    plan_elc(plan, shares)
    plan_pasti(plan, shares, keys)
    plan_by_trans(plan, shares, keys)
    plan_nuclear(plan)
    plan_lowaf(plan, shares)
    plan_ucs(plan)
    plan_links(plan, shares, a.dd, a.run)
    lines = []
    for book in plan.books():
        lines.append(f"--- {book}")
        for sheet, cell, old, new, colour, why in plan.edits.get(book, []):
            lines.append(f"  ~ '{sheet}'!{cell} [{colour}]: {old!r}\n      -> {new}\n      ({why})")
        for sname, cells in plan.sheets.get(book, {}).items():
            lines.append(f"  + new sheet '{sname}' ({len(cells)} cells)")
            for cell, v, colour in cells:
                lines.append(f"      {cell} [{colour}] {v}")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    n_e = sum(len(v) for v in plan.edits.values())
    n_s = sum(len(c) for d in plan.sheets.values() for c in d.values())
    print(f"dry run: {n_e} cell edits in {len(plan.edits)} workbooks, {n_s} cells on new sheets -> {a.out}")
    if a.apply:
        res = apply(plan)
        if any(v != "ok" for v in res.values()):
            sys.exit(1)


if __name__ == "__main__":
    main()
