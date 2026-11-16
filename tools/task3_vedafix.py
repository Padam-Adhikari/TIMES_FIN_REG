"""Task 3 fix after the first server run (Baseline-Reg, 2026-11-16, infeasible).

Found by solving the server's DD files locally (CPLEX conflict refiner) and comparing them with the
validated prototype (tools/dd_regionalise.py --step3), see audit/task3_power.md section 6:

1. The power commodities were declared only in FI (SysSettings 'Comms', Region = 'FI'). VEDA drops
   every topology entry, activity unit, FLO_EMIS and trade link that names a commodity the region
   does not have: the moved plants had no inputs/outputs in their regions (OL3 could not be
   built -> RS_NCAP_ENFI_OLKILUOTO-3_FX infeasible) and 186 of the 220 new links were missing.
   Fix: the Region cell lists every region in Reg mode (same TEXTJOIN formula the model already
   uses for ELCCO2N, ETSCO2, INDCOA, ...). Single mode still gives 'FI'.
2. Emission/certificate commodities (ENV: ELCCO2N, ETSCO2, GreenCert-ELC) have no balance in the
   regions (LimType N), so a region could keep its CO2 or certificates instead of sending them to the
   hub, where the national caps, taxes and certificate rules sit. In Reg mode the hub row keeps 'FI'
   (unchanged balance) and a Reg-only row declares them in the 19 regions with LimType FX:
   everything a region emits goes to the hub over its TB_* link (as in the prototype).
3. The 2030 coal phase-out (Scen_KILL_CoalPhaseOut2030, CAP_BND UP 0) is written in the FI column,
   so the moved coal and peat plants escaped it. Zero bound = Copy rule: AllRegions in Reg mode.

Usage:  python tools/task3_vedafix.py [--apply]     (dry run by default)
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from task3_power import (BLUE, GREEN, M, SEL, Book, Plan, apply, col_idx, col_let, regonly, sw)  # noqa: E402

SYS = M + "SysSettings.xlsx"
COAL = M + "SuppXLS/Scen_KILL_CoalPhaseOut2030.xlsx"
ALL = '_xlfn.TEXTJOIN(",",TRUE,Region_selection!$K$8:$AD$8)'      # FI + 19 regions (Reg mode)
REGS = '_xlfn.TEXTJOIN(",",TRUE,Region_selection!$L$8:$AD$8)'     # the 19 regions only
# commodities the moved plants use in their regions (TOP, FLO_EMIS) -> declared in every region
DECLARE = ["ELCCOH", "ELCCOL", "ELCDST", "ELCGAS", "ELCHFO", "ELCHIG", "ELCHYD", "ELCNUC", "ELCSOL",
           "ELCWIN", "ELCWOO", "HETHTH"]
ENV_FX = ["ELCCO2N", "ETSCO2", "GreenCert-ELC"]
# ~FI_Comm tables on 'Comms': (Region column, CommName column)
TABLES = [("C", "D"), ("W", "X"), ("M", "N"), ("AG", "AH"), ("AQ", "AR"), ("BA", "BB"), ("BL", "BM")]
NEW_ROWS = [75, 76, 77]                     # below table V3 (last row 74), columns V..AD


def find_rows(b, sheet):
    out = {}
    for rc, nc in TABLES:
        for (s, cell), v in b.v.items():
            if s == sheet and cell.startswith(nc) and cell[len(nc):].isdigit() and isinstance(v, str):
                out.setdefault(v, []).append((rc, int(cell[len(nc):])))
    return out


def plan_comms(plan):
    b = Book(SYS)
    sh = "Comms"
    rows = find_rows(b, sh)
    for c in DECLARE + ENV_FX:
        if len(rows.get(c, [])) != 1:
            sys.exit(f"{SYS} {sh}: {c} found {rows.get(c)} (expected exactly one declaration)")
    for c in DECLARE:
        rc, r = rows[c][0]
        cell = f"{rc}{r}"
        if b.val(sh, cell) != "FI" or (sh, cell) in b.f:
            sys.exit(f"{sh}!{cell} ({c}): expected the constant 'FI', found {b.f.get((sh, cell), b.val(sh, cell))!r}")
        plan.edit(SYS, sh, cell, "FI", sw('"FI"', ALL), BLUE,
                  f"{c}: declared in every region in Reg mode (moved plants use it there)")
    # ENV: hub row keeps FI; Reg-only rows in the 19 regions with LimType FX
    for c in ENV_FX:
        rc, r = rows[c][0]
        cell = f"{rc}{r}"
        f = b.f.get((sh, cell))
        if f and SEL in f:
            continue
        if f is not None and f.replace(" ", "") != "=" + ALL.replace(" ", ""):
            sys.exit(f"{sh}!{cell} ({c}): unexpected formula {f!r}")
        if f is None and b.val(sh, cell) != "FI":
            sys.exit(f"{sh}!{cell} ({c}): unexpected value {b.val(sh, cell)!r}")
        if f is not None:
            plan.edit(SYS, sh, cell, "FI", sw(ALL, '"FI"'), BLUE,
                      f"{c}: hub row only on FI in Reg mode (the regions get their own FX row)")
    busy = b.empty(sh, [f"{col}{r}" for r in NEW_ROWS + [NEW_ROWS[-1] + 1]
                        for col in ("V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD")])
    if busy:
        sys.exit(f"{sh}: rows {NEW_ROWS} (+1) not free: {busy[:5]}")
    if b.val(sh, "X74") is None or b.val(sh, "W4") != "Region":
        sys.exit(f"{sh}: table V3 not as expected (X74 {b.val(sh, 'X74')!r}, W4 {b.val(sh, 'W4')!r})")
    for c, r in zip(ENV_FX, NEW_ROWS):
        src = rows[c][0][1]
        scol = {"C": "B", "W": "V"}[rows[c][0][0]]
        cols = [col_let(col_idx(scol) + i) for i in range(9)]                    # B..J or V..AD
        tgt = ["V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD"]
        for i, (sc, tc) in enumerate(zip(cols, tgt)):
            if i == 1:
                expr = REGS
            elif i == 5:
                expr = '"FX"'
            else:
                if b.val(sh, f"{sc}{src}") is None:
                    continue
                expr = f"{sc}{src}"
            plan.edit(SYS, sh, f"{tc}{r}", None, regonly(expr), GREEN,
                      f"{c} in the 19 regions, LimType FX: all regional emissions/certificates go to the hub")
    print(f"{SYS}: {len(DECLARE)} declarations, ENV rows {NEW_ROWS}")


def plan_coal(plan):
    b = Book(COAL)
    sh = "INS"
    if b.val(sh, "B2") != "~TFM_INS" or b.val(sh, "O3") != "AllRegions" or b.val(sh, "P3") != "FI":
        sys.exit(f"{COAL}: table not as expected")
    for r in range(4, 12):
        v = b.val(sh, f"P{r}")
        if v is None:
            continue
        if b.val(sh, f"O{r}") is not None and not b.f.get((sh, f"O{r}"), "").startswith(f'=IF({SEL},"",'):
            sys.exit(f"{COAL} O{r} not empty")
        plan.edit(COAL, sh, f"O{r}", None, regonly(f"P{r}"), BLUE,
                  "coal phase-out is a zero bound (Copy rule): every region in Reg mode")
    print(f"{COAL}: FI values copied to AllRegions in Reg mode")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    plan = Plan()
    plan_comms(plan)
    plan_coal(plan)
    for book in plan.books():
        print(f"--- {book}")
        for sheet, cell, old, new, colour, why in plan.edits.get(book, []):
            print(f"  ~ '{sheet}'!{cell} [{colour}]: {old!r}\n      -> {new}\n      ({why})")
    if a.apply:
        res = apply(plan)
        print(res)
        if any(v != "ok" for v in res.values()):
            sys.exit(1)


if __name__ == "__main__":
    main()
