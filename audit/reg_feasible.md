# Making the regional case solve (Baseline-Reg, FI + FI1B1 + FI1D9)

The regional run of 11 Nov 2026 (`baseline-reg_new`) was infeasible. Its DD files
(`GAMS_WrkTIMES/`) were solved locally with TIMES v4.8.3 and CPLEX, using the conflict refiner
(`iis 1`, `names yes`) and the shadow prices of the solved model. Each fix was tested in the DD
files before it was written into the workbooks (`tools/task0.py`, `tools/reg_feasible.py`).

| # | Finding (evidence) | Cause | Fix (Reg mode only) | Owner |
|---|---|---|---|---|
| 1 | Conflict: `EQG_COMBAL(FI,2010,OILDST)` - diesel exports LO 101.9 PJ, imports UP 78.3 PJ, refinery absent | `VT_FINTIMES_SUP` *Flexible Refinery* rows 42-46 hold `ACT_BND FX` twice: column `FX` = 0 and column `FI` = real value. Task 0 blanked only `FI`, so `ACT_BND FX 0` remained and stopped the Porvoo refinery | Whole rows switched off (`Attribute` -> `\I:`); value kept in `RS_ACT_SSCDRFLX00_*`. Extractor now reads limit-type headers (`FX`/`UP`/`LO`, `FI~LO`) as value columns | task 0 tool |
| 2 | Conflict: `EQE_UCRTS(FI1D9,2015,UC_VARI_ELE_Cons_Cap)` = 0 with FI1D9 steel needing electricity | Variable-RES module (`Scen_SepDb-ZIET_VAR`, `_Stor`) declared `R_E: AllRegions`; its identities only make sense where `ELE_CONS_CAP` exists (FI). In FI1D9 the copy reads "0 = FI1D9 electricity use" | 9 `~UC_Sets` lines -> `R_E: FI`. Exact in the hub design: FI consumption includes the exports to the regions | `reg_feasible.py` |
| 3 | Optimal but +33 % objective; shadow price of `TUC_Istruc_RIR-BLA` 2.0e6 (single run: 0) | `R_S` share UC with `UC_COMPRD(MISRIR)`; TIMES counts imports as production (`eqcombal.mod`: `cal_ire IMP OUT`), so pig iron sent FI1D9 -> FI is counted twice | Correction rows in `Scen_UC-IND` / `UC_MISRIR` (rows 15-23, column K `UC_IRE-I`): `-k` on internal links `TB_MISRIR_*` for each production coefficient `k` | `reg_feasible.py` |

Result with the fixes (local solve of the server DD files): **Optimal, objective 1,527,754 M EUR
vs 1,529,920 M EUR single-region (-0.14 %)**, no dummy imports, COM_PROJ and NCAP_PASTI conserved
exactly. The remaining gap comes from the first task-0 version still in those DD files (CO2-sink
potentials 40,330 instead of 14.4, fixed since) and is expected to shrink after the next sync.

Single-region mode: rescan of all 21 touched workbooks - every table reads exactly as before
(ACTCOST differs only in a table that is off in single-region mode); no new table is active.

## Second round (server run with Baseline-Sami, 13 Nov 16:35: optimal, -0.096 %)

| # | Finding (evidence) | Fix (Reg mode only) |
|---|---|---|
| 4 | Parameter comparison single-FI vs regional-FI1D9 for the steel processes: 270 `FLO_BND UP 0` (industrial coal phase-out from 2030) missing in FI1D9 - `Scen_UC_LimitCOAL` / `INDCOA` writes them in a column headed `FI` | header `FI` -> `AllRegions` (zero bound = Copy rule). Not binding today (COREX unused) |
| 5 | Net `INDSCO2N` (captured CO2) 1,703 kt/yr in FI1D9 from 2028, 0 in the single run; CO2 transport/storage costs lower | links FI<->FI1D9 for `INDSCO2N`, `GASBFT`, `GreenCert-FIN` (`ScenTrade__Trade_Links`, rows 19-21). Gap -0.096 % -> -0.025 % |

Remaining -0.025 % and the FI-only emission aggregates (`INDCO2`, `CO2WOT`; reporting only) go to
task 1. Also: the case Baseline-Reg must use the scenario group of its single-region reference
(a run with group Baseline gave +1.1 % only because of a different demand file).

## Rules learned (now in CLAUDE.md)

1. **Internal links and production/consumption sums.** `UC_COMPRD` / `UC_COMCON` / COM_BNDPRD
   summed over regions count internal imports/exports twice. Every national (`R_S`) term on a
   linked commodity needs a `UC_IRE-I` (production) or `UC_IRE-E` (consumption) correction on
   the `TB_*` links with the opposite coefficient. `UC_COMNET` needs none.
2. **Single-region modules declared `AllRegions`** (variable-RES, utilisation, storage
   competition) must be restricted to the hub or rebuilt per region when their processes move.

## Not done here

- The variable-RES module must be regionalised with the grid (tasks 2-3).
