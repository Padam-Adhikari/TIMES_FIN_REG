"""Make the regional case solve: fixes found by solving the Reg-FINTIMES DD files locally.

Found with the CPLEX conflict refiner and shadow prices on the server's own DD files
(GAMS_WrkTIMES, run baseline-reg_new), see audit/reg_feasible.md:

1. Variable-RES module (Scen_SepDb-ZIET_VAR, _Stor): its UCs are national electricity-balance
   identities written for one region. As `R_E: AllRegions` every region gets a copy; in FI1D9
   UC_VARI_ELE_Cons_Cap reads "0 = FI1D9 electricity use" (ELE_CONS_CAP exists only in FI)
   and the model is infeasible. In the hub design all electricity passes the FI node and
   FI's consumption includes its exports to the regions, so the FI copy is the national
   identity: Reg mode -> `R_E: FI`. Revisit in task 2/3 when plants and grid leave FI.
2. Pig-iron route shares (Scen_UC-IND, UC_MISRIR): `R_S: AllRegions` UCs with UC_COMPRD on
   MISRIR. TIMES counts imports as production (eqcombal.mod: cal_ire IMP OUT), so the
   pig iron sent FI1D9 -> FI is counted twice (shadow price 2e6). Correction: for each
   UC_COMPRD coefficient k add UC_IRE-I = -k on the internal links TB_MISRIR_* (national
   production = sum of regional production - internal imports), Reg mode only.

The refinery fix (VT_FINTIMES_SUP 'Flexible Refinery') is part of tools/task0.py.

Usage: python tools/reg_feasible.py [--apply]   (dry run by default)
"""
import argparse
import os
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from task0 import Plan, ROOT, SEL, TRADE_PARAMS, NEW_SHEET, gated, xl_literal  # noqa: E402

VAR_BOOKS = ["Reg-FINTIMES/SuppXLS/Scen_SepDb-ZIET_VAR.xlsx",
             "Reg-FINTIMES/SuppXLS/Scen_SepDb-ZIET_VAR_Stor.xlsx"]
UCIND = "Reg-FINTIMES/SuppXLS/Scen_UC-IND.xlsx"


def read_cells(book):
    wbv = openpyxl.load_workbook(os.path.join(ROOT, book), read_only=True, data_only=True)
    wbf = openpyxl.load_workbook(os.path.join(ROOT, book), read_only=True, data_only=False)
    vals, forms = {}, {}
    for ws in wbv.worksheets:
        try:
            for row in ws.iter_rows():
                for c in row:
                    if getattr(c, "value", None) is not None:
                        vals[(ws.title, c.coordinate)] = c.value
        except Exception:
            continue
    for ws in wbf.worksheets:
        try:
            for row in ws.iter_rows():
                for c in row:
                    v = getattr(c, "value", None)
                    if isinstance(v, str) and v.startswith("="):
                        forms[(ws.title, c.coordinate)] = v
        except Exception:
            continue
    return vals, forms


def plan_var_module(plan):
    for book in VAR_BOOKS:
        vals, forms = read_cells(book)
        n = 0
        for (sheet, cell), v in sorted(vals.items()):
            if isinstance(v, str) and v.strip().upper().replace(" ", "") == "~UC_SETS:R_E:ALLREGIONS":
                plan.edit(book, sheet, cell, v, gated(v, forms.get((sheet, cell)), '"~UC_Sets: R_E: FI"'),
                          "variable-RES module is a national identity: in Reg mode only the FI hub copy")
                n += 1
        print(f"{book}: {n} UC_Sets lines -> R_E: FI in Reg mode")


def plan_misrir(plan):
    vals, forms = read_cells(UCIND)
    sh = "UC_MISRIR"
    hdr = {vals.get((sh, f"{c}5")): c for c in "BCDEFGHIJK"}
    assert hdr.get("UC_N") == "B" and hdr.get("UC_COMPRD") == "H" and hdr.get("Year") == "F", hdr
    used = [k for k in vals if k[0] == sh and k[1][0] in "BCDEFGHIJK" and 15 <= int(k[1][1:]) <= 23]
    if used or (sh, "K5") in vals:
        sys.exit(f"{UCIND} {sh}: target cells K5 or rows 15-23 are not empty: {sorted(used)[:5]}")
    plan.edit(UCIND, sh, "K5", None, f'=IF({SEL},"","UC_IRE-I")',
              "new column: internal-import term (UC_IRE with IMP)")
    r = 15
    for first, uc in ((6, "TUC_Istruc_RIR-BLA"), (9, "TUC_Istruc_RIR-COR"), (12, "TUC_Istruc_RIR-CYC")):
        assert vals.get((sh, f"B{first}")) == uc, (first, uc, vals.get((sh, f"B{first}")))
        for src in (first, first + 1, first + 2):
            for col, expr in (("B", f'"{uc}"'), ("D", '"TB_MISRIR_*"'), ("E", '"MISRIR"'),
                              ("F", f"F{src}"), ("K", f"-H{src}")):
                plan.edit(UCIND, sh, f"{col}{r}", None, f'=IF({SEL},"",{expr})',
                          f"{uc}: subtract internal MISRIR imports (coefficient = -UC_COMPRD of row {src})")
            r += 1
    print(f"{UCIND} {sh}: 9 correction rows (15-23) + header K5")


LIMITCOAL = "Reg-FINTIMES/SuppXLS/Scen_UC_LimitCOAL.xlsx"


def plan_coal_phaseout(plan):
    """Industrial coal phase-out (FLO_BND UP 0 from 2030 on INDCO* inputs of PRE/ELE/HPL
    processes) is written in a column headed 'FI', so the COREX plant moved to FI1D9
    escaped it (regional run 0.1 % cheaper). Zero bound = Copy rule: every region."""
    vals, forms = read_cells(LIMITCOAL)
    sh = "INDCOA"
    tag = [k for k, v in vals.items() if k[0] == sh and isinstance(v, str) and v.strip().upper() == "~TFM_INS"]
    assert len(tag) == 1, tag
    import re as _re
    col = _re.match(r"[A-Z]+", tag[0][1]).group(0)
    hr = int(tag[0][1][len(col):]) + 1
    hdr = {v: c[1] for c, v in vals.items() if c[0] == sh and c[1].endswith(str(hr))
           and _re.fullmatch(r"[A-Z]+" + str(hr), c[1])}
    assert "FLO_BND" in {vals.get((sh, f"{_re.match(r'[A-Z]+', hdr['Attribute']).group(0)}{hr + 1}"))}, hdr
    cell = hdr["FI"]
    plan.edit(LIMITCOAL, sh, cell, "FI", gated("FI", forms.get((sh, cell)), '"AllRegions"'),
              "coal phase-out is a zero bound (Copy rule): every region, incl. moved plants")
    print(f"{LIMITCOAL} {sh}!{cell}: 'FI' -> 'AllRegions' in Reg mode")


LINKS = "Reg-FINTIMES/SuppXLS/Trades/ScenTrade__Trade_Links.xlsx"
NEW_LINKS = ["INDSCO2N", "GASBFT", "GreenCert-FIN"]


def plan_links(plan):
    """Steel pilot gaps: commodities produced in FI1D9 whose consumers are only on the FI hub.
    INDSCO2N (captured CO2) vanished for free instead of entering CO2 transport/storage
    (regional run 0.1 % cheaper); GASBFT (top gas) and GreenCert-FIN (certificates) unused.
    The TradeLinks_DINS table builds region x commodity rows from the lists in L and M."""
    vals, forms = read_cells(LINKS)
    sh = "FI internal trades"
    last = max(r for r in range(4, 40) if vals.get((sh, f"M{r}")) is not None)
    free = all(vals.get((sh, f"{c}{r}")) is None for c in "ACDEFGHIM" for r in (19, 20, 21))
    if last != 18 or not free:
        sys.exit(f"{LINKS}: trade-link table not as expected (last commodity row {last}, rows 19-21 free {free})")
    plan.colours = getattr(plan, "colours", {})
    for i, com in enumerate(NEW_LINKS):
        r = 19 + i
        cells = [("M", com), ("A", f"=A{r-1}+1"), ("C", "FI"),
                 ("D", f"{{=INDEX($L$4:$L$1048576,1+MOD(A{r}-1,COUNTA($L$4:$L$1048576)),0)}}"),
                 ("E", f"{{=INDEX($M$4:$M$1048576,1+QUOTIENT(A{r}-1,COUNTA($L$4:$L$22)),0)}}"),
                 ("F", f"=E{r}"), ("G", f"=F{r}"),
                 ("H", f'=_xlfn.TEXTJOIN("_",TRUE,"TB",E{r},C{r},D{r})'), ("I", "B")]
        for col, v in cells:
            plan.edit(LINKS, sh, f"{col}{r}", None, v, f"new internal link TB_{com}_FI_FI1D9 (steel pilot gap)")
            plan.colours[(LINKS, sh, f"{col}{r}")] = "#E2EFDA"
    print(f"{LINKS}: links for {NEW_LINKS} (rows 19-21)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    plan = Plan()
    plan_var_module(plan)
    plan_misrir(plan)
    plan_coal_phaseout(plan)
    plan_links(plan)
    for b, eds in plan.edits.items():
        print(f"--- {b}")
        for sheet, cell, old, new, why in eds:
            print(f"  ~ '{sheet}'!{cell}: {old!r}\n      -> {new}\n      ({why})")
    if a.apply:
        from task0_apply import apply_plan
        res = apply_plan(plan, ROOT, TRADE_PARAMS, SEL, NEW_SHEET)
        if any(v != "ok" for v in res.values()):
            sys.exit(1)


if __name__ == "__main__":
    main()
