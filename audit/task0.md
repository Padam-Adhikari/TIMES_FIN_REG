# Task 0 audit: internal link cost, national bounds, non-zero-RHS user constraints

Case: **Baseline-Sami** | generated 2026-11-11 by `tools/task0.py --write-audit` (read-only) |
100 workbooks, 1010 tagged tables (incl. `~UC_Sets` lines and disabled tags).

Method: every workbook of the case (from `AppData/Cases.json` + `Groups.json`: BASE `VT_*`,
`BY_Trans`, the SubRES pairs, SysSettings, TradeParameters, the 55 checked SuppXLS scenarios and
the trade links) was read with openpyxl `read_only=True` - cached values and formulas. Values are
the ones VEDA sees with the switch at **FINTIMES** (all files are saved in single-region mode).
VEDA aliases were resolved (`BNDACT`/`ACTBND` = ACT_BND, `CUM` = ACT_CUM, ...), `\I:` rows and
columns, `*` comment columns and year-`0` interpolation cells were skipped, and the FI_T
`TechName` / UC_T `UC_N` carry-forward was applied. Cross-check: every non-zero FI bound in
`AppData/GAMSSAVE/baseline.gdx` maps to one of the tables below, except items that no longer
exist in the files (that GDX is older than the current workbooks).

## 1. Internal link cost

| File | Sheet | Table | Value now | Proposed |
|---|---|---|---|---|
| SuppXLS/Trades/ScenTrade_TradeParameters.xlsx | FI internal trades | C2 `~TFM_INS` (AllRegions, `Pset_PN = TB_*`) | ACTCOST **10** | **0.0001** |

- Units are M EUR / PJ, so 10 = 10 EUR/GJ = 36 EUR/MWh on every PJ that crosses a link
  (`TB_INDELC_FI_FI1D9` etc.), both directions. That is a real cost, not an anti-stalling tie
  breaker; it penalises the regional run against the single-region run.
- The tag cell is `=IF(Region_selection!$B$8=Region_selection!$D$9,"~TFM_INS","TFM_INS")`, so
  the table is only read in Reg-FINTIMES mode: single-region runs are not affected by the change.
- **Choice: 0.0001 M EUR/PJ** (= 0.36 EUR/GWh). On the hub links the cost has only one job: break
  ties between equivalent routes so the LP does not circulate flows FI -> region -> FI. In the hub
  design these links are a copper plate; real transport costs and losses belong on the physical
  region-region grid links of task 3 (adding them here would double count the grid cost already in
  the national data). The value satisfies both bounds:
  - *seen by the solver*: CPLEX runs barrier + crossover, so the simplex optimality tolerance
    (default 1e-6) decides. With G_DRATE 3.5 % from 2015 a 2070 flow is weighted by
    1.035^-55 = 0.15, i.e. 1.5e-5 per PJ: 15x the tolerance, so ties are still broken in the last
    period (1e-5 would sink to the tolerance late in the horizon).
  - *not visible in results*: even fully regionalised (every PJ of primary energy, ~2600 PJ/yr,
    crossing a hub link and paying at both link ends) the discounted total over 2015-2070 is
    1e-4 x 2600 x 2 x 25.3 = 13 M EUR = 8.6e-7 of the objective (1.53e7 M EUR in
    `baseline.gdx`), below the 1e-6 relative tolerance of `check_run.py`. 0.001 would already give
    5.7e-6, and the old 10 gives 0.06 (6 % of the objective), a real distortion.
- So the link cost changes the regional objective by < 1e-6 relative and needs no separate
  explanation in the run check.

## 2. Non-zero national bounds

Counts of non-zero bound values: KEEP 4, LINK 236, NONBIND 2, POT 92, SKIP 1, SUM 124.

One line per table x attribute x limit x item. `Region` is the column the value sits in (`-` = no region column: SubRES/VT rows apply to every region where the process exists; today that is FI only, because every SubRES `~TFM_AVA` sets `AllRegions 0, FI 1`).


### 2.1 **Sum** -> `RS_*` UC_R_SUM (Reg mode)

| File | Sheet | Table | Attribute | Lim | Item(s) | Region | Values (year: value) | Cells |
|---|---|---|---|---|---|---|---|---|
| VT_FINTIMES_ELC.xlsx | Dist Heat | G19 `~FI_T` | ACT_BND | LO | EEHP_DistHeating | FI | 2010: 61.19, 2011: 52.88, 2012: 63.22, 2013: 55.95, 2014: 59.75 | J22, J23, J24, J25, J26 |
| VT_FINTIMES_SUP.xlsx | VEDA Tables | G38 `~FI_T` | ACT_BND | FX | SSCDCOKE00 | FI | 2010: 30.7897, 2011: 32.745, 2012: 33.6326, 2013: 33.6744, 2014: 34.6039, 2015: 34.6039 | I49, I50, I51, I52, I53, I54 |
| VT_FINTIMES_SUP.xlsx | VEDA Tables | G38 `~FI_T` | ACT_BND | LO | SSCDCOKE00 | FI | 2016: 17.302, 2025: 8.65098 | I55, I57 |
| VT_FINTIMES_SUP.xlsx | VEDA Tables | G38 `~FI_T` | ACT_BND | UP | SSCDCOKE00 | FI | 2016: 34.6039, 2025: 25, 2030: 17 | I56, I58, I59 |
| VT_FINTIMES_SUP.xlsx | Flexible Refinery | G24 `~FI_T` | ACT_BND | FX | SSCDRFLX00 | FI | 2010: 438.924, 2011: 470.542, 2012: 456.607, 2013: 483.616, 2014: 475.18 | K42, K43, K44, K45, K46 |
| VT_FINTIMES_SUP.xlsx | Flexible Refinery | G24 `~FI_T` | ACT_BND | UP | SSCDRFLX00 | FI | 2015: 483.616 | K47 |
| VT_FINTIMES_SUP.xlsx | Flexible Refinery | G24 `~FI_T` | ACT_BND | LO | SSCDRFLX00 | FI | 2020: 338.531 | K48 |
| SubRES_TMPL/SubRES_00_Nuc-EU.xlsx | ELC_FI | E4 `~FI_T` | CAP_BND | UP | ENFI_LOVIISA-1_00 comm-in=ELCNUC comm-out=ELCHIG | - | 1977: 0.496 | L7 |
| SubRES_TMPL/SubRES_00_Nuc-EU.xlsx | ELC_FI | E4 `~FI_T` | CAP_BND | UP | ENFI_LOVIISA-2_00 comm-in=ELCNUC comm-out=ELCHIG | - | 1980: 0.496 | L8 |
| SubRES_TMPL/SubRES_00_Nuc-EU.xlsx | ELC_FI | E4 `~FI_T` | CAP_BND | UP | ENFI_OLKILUOTO-1_00 comm-in=ELCNUC comm-out=ELCHIG | - | 1978: 0.88 | L9 |
| SubRES_TMPL/SubRES_00_Nuc-EU.xlsx | ELC_FI | E4 `~FI_T` | CAP_BND | UP | ENFI_OLKILUOTO-2_00 comm-in=ELCNUC comm-out=ELCHIG | - | 1980: 0.88 | L10 |
| SubRES_TMPL/SubRES_00_Nuc-EU.xlsx | ELC_FI | E4 `~FI_T` | NCAP_BND | FX | ENFI_OLKILUOTO-3 comm-in=ELCNUC comm-out=ELCHIG | - | 2023: 1.6 | M11 |
| SubRES_TMPL/SubRES_00_Nuc-EU.xlsx | ELC_FI | E4 `~FI_T` | CAP_BND | UP | ENFI_OLKILUOTO-4 comm-in=ELCNUC comm-out=ELCHIG | - | 2200: 1.5 | L12 |
| SubRES_TMPL/SubRES_00_Nuc-EU.xlsx | ELC_FI | E4 `~FI_T` | CAP_BND | UP | ENFI_PYHA-YOKI comm-in=ELCNUC comm-out=ELCHIG | - | 2200: 1.5 | L13 |
| SubRES_TMPL/SubRES_22_TECHS_BIOREFINERIES.xlsx | SUP_Blending | G14 `~FI_T` | ACT_BND | LO | BLDGSLE85 comm-out=TRAGSLE85 | - | -: 0.12 | U50 |
| SubRES_TMPL/SubRes_40_TRADE-EXTRAEU_Trans.xlsx | SUP | C16 `~TFM_INS` | CAP_BND | UP | LNGREGAS_New | ALLREGIONS | 2030: 1500 | G20 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_DETPre45* (7 processes) | FI | 2060: 111.65 | H60 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_DETPre69* (7 processes) | FI | 2060: 204.21 | H61 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_DETPre79* (7 processes) | FI | 2060: 162.213 | H62 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_DETPre89* (7 processes) | FI | 2060: 128.532 | H63 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_DETPre99* (7 processes) | FI | 2060: 93.8487 | H64 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_FLTPre45* (7 processes) | FI | 2060: 156.198 | H65 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_FLTPre69* (7 processes) | FI | 2060: 285.689 | H66 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_FLTPre79* (7 processes) | FI | 2060: 226.935 | H67 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_FLTPre89* (7 processes) | FI | 2060: 179.816 | H68 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_FLTPre99* (7 processes) | FI | 2060: 131.294 | H69 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_SDEPre45* (7 processes) | FI | 2060: 84.3882 | H70 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_SDEPre69* (7 processes) | FI | 2060: 154.347 | H71 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_SDEPre79* (7 processes) | FI | 2060: 122.605 | H72 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_SDEPre89* (7 processes) | FI | 2060: 97.1482 | H73 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_SDEPre99* (7 processes) | FI | 2060: 70.9333 | H74 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_DETPre09* (7 processes) | FI | 2060: 91.6667 | H75 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_FLTPre09* (7 processes) | FI | 2060: 128.241 | H76 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Retrofit control | B40 `~TFM_INS` | CAP_BND | UP | pset_ci=Bldg_SDEPre09* (7 processes) | FI | 2060: 69.2841 | H77 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Gas Calibration | B3 `~TFM_INS-TS` | COM_BNDPRD | UP | cset_cn=RSDGAS | FI | 2010: 2.10642, 2011: 1.35975, 2012: 1.46475, 2013: 1.29465, 2014: 1.26 | F7, G7, H7, I7, J7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Gas Calibration | B3 `~TFM_INS-TS` | COM_BNDPRD | UP | cset_cn=COMGAS | FI | 2010: 1.6296, 2011: 1.6296, 2012: 1.4742, 2013: 1.52775, 2014: 1.28625 | F8, G8, H8, I8, J8 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Gas Calibration | B3 `~TFM_INS-TS` | COM_BNDPRD | UP | cset_cn=TRAGAS | FI | 2010: 0.6426, 2011: 0.4914, 2012: 0.52185, 2013: 0.40845, 2014: 0.4242 | F9, G9, H9, I9, J9 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Heat Calibration | B4 `~TFM_INS-TS` | FLO_BND | UP | IND* pset_pd=Fuel Tech* cset_cn=HETHTH (28 processes) | FI | 2010: 70.0497, 2011: 65.0234, 2012: 64.4112, 2013: 61.2014, 2014: 54.831 | I7, J7, K7, L7, M7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Heat Calibration | B4 `~TFM_INS-TS` | FLO_BND | UP | RSD* pset_pd=Fuel Tech* cset_cn=HETHTH (23 processes) | FI | 2010: 76.5261, 2011: 66.3726, 2012: 72.9992, 2013: 70.2629, 2014: 68.7582 | I8, J8, K8, L8, M8 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Heat Calibration | B4 `~TFM_INS-TS` | FLO_BND | UP | COM* pset_pd=Fuel Tech* cset_cn=HETHTH (20 processes) | FI | 2010: 49.3668, 2011: 43.3524, 2012: 46.6651, 2013: 44.4612, 2014: 44.3877 | I9, J9, K9, L9, M9 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | B3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=INDFINSOLID | FI | 2015: 21.2058, 2030: 11.781 | G5, H5 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | L3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=INDFINSOLID | FI | 2015: 24.7401, 2030: 35.343 | Q5, R5 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | W3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=TRAFINOIL | FI | 2015: 159.274, 2030: 106.183 | AB6, AC6 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | W3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=RSDFINOIL | FI | 2015: 14.4, 2030: 9.6 | AB7, AC7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | W3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=COMFINOIL | FI | 2015: 10.08, 2030: 6.72 | AB8, AC8 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | AG3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=TRAFINOIL | FI | 2015: 194.668, 2030: 265.457 | AL6, AM6 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | AG3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=RSDFINOIL | FI | 2015: 17.6, 2030: 24 | AL7, AM7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | AG3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=COMFINOIL | FI | 2015: 12.32, 2030: 16.8 | AL8, AM8 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | AR3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=INDFINGAS | FI | 2015: 31.0574, 2030: 16.346 | AW5, AX5 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | AR3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=RSDGAS | FI | 2015: 1.04595, 2030: 0.5505 | AW7, AX7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | AR3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=COMGAS | FI | 2015: 1.11055, 2030: 0.5845 | AW8, AX8 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | BB3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=INDFINGAS | FI | 2015: 34.3266, 2030: 65.384 | BG5, BH5 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | BB3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=RSDGAS | FI | 2015: 1.15605, 2030: 2.202 | BG7, BH7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | BB3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=COMGAS | FI | 2015: 1.22745, 2030: 2.338 | BG8, BH8 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | BM3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=RSDHET | FI | 2015: 63.45, 2030: 35.25 | BR7, BS7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | BM3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=COMHET | FI | 2015: 40.77, 2030: 22.65 | BR8, BS8 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | BW3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=RSDHET | FI | 2015: 77.55, 2030: 105.75 | CB7, CC7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | BW3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=COMHET | FI | 2015: 49.83, 2030: 67.95 | CB8, CC8 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | CG3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=RSDBIO | FI | 2015: 45.0333, 2030: 47.5351 | CL7, CM7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | CG3 `~TFM_DINS-TS` | COM_BNDPRD | LO | cset_cn=COMBIO | FI | 2015: 2.934, 2030: 3.097 | CL8, CM8 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | CQ3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=RSDBIO | FI | 2015: 52.5389, 2030: 75.0555 | CV7, CW7 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | Calibration 2015-2050 | CQ3 `~TFM_DINS-TS` | COM_BNDPRD | UP | cset_cn=COMBIO | FI | 2015: 3.423, 2030: 4.89 | CV8, CW8 |

### 2.2 **Sum** (resource potential) -> `RS_*` UC_R_SUM; Split rule replaces it when regional resource data exist

| File | Sheet | Table | Attribute | Lim | Item(s) | Region | Values (year: value) | Cells |
|---|---|---|---|---|---|---|---|---|
| VT_FINTIMES_SUP.xlsx | Reserves | G2 `~FI_T` | ACT_BND | UP | MINCOLRSV1 | FI | 2015: 89.137, 2050: 89.137 | H4, H5 |
| VT_FINTIMES_SUP.xlsx | Reserves | G2 `~FI_T` | ACT_BND | UP | MINCOLRSV2 | FI | 2015: 25, 2050: 25 | H10, H9 |
| VT_FINTIMES_SUP.xlsx | Reserves | G2 `~FI_T` | ACT_BND | UP | MINCOLRSV3 | FI | 2015: 25, 2050: 25 | H14, H15 |
| VT_FINTIMES_SUP.xlsx | Reserves | G2 `~FI_T` | ACT_BND | UP | MINMPPWOO1 | FI | 2005: 60.2, 2010: 60.2, 2020: 67, 2030: 73.8, 2040: 73.2, 2050: 73.2 | H49, H50, H51, H52, H53, H54 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND.xlsx | SUP | E108 `~FI_T` | ACT_BND | UP | MINSNKAFF1 comm-out=SNKAFF | - | 2010: 40330, 2020: 51330, 2030: 18330, 2040: 18330, 2050: 91670 | O122, P122, Q122, R122, S122 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND.xlsx | SUP | E108 `~FI_T` | ACT_BND | UP | MINSNKAFF2 comm-out=SNKAFF | - | 2010: 95330, 2030: 73330, 2040: 73330, 2050: 73330 | O123, Q123, R123, S123 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND.xlsx | SUP | E108 `~FI_T` | ACT_BND | UP | MINSNKAFF3 comm-out=SNKAFF | - | 2010: 25670, 2020: 157670, 2030: 62330 | O124, P124, Q124 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND.xlsx | SUP | E108 `~FI_T` | ACT_BND | UP | MINSNKAFF4 comm-out=SNKAFF | - | 2040: 179670, 2050: 143000 | R125, S125 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND_Trans.xlsx | CO2_Storage_Potential | A1 `~TFM_INS` | ACT_BND | UP | MINSNKAFF1 | FI | 2010: 14.3935, 2020: 18.3193, 2030: 6.54185, 2040: 6.54185, 2050: 32.7164 | G32, G33, G34, G35, G36 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND_Trans.xlsx | CO2_Storage_Potential | A1 `~TFM_INS` | ACT_BND | UP | MINSNKAFF2 | FI | 2010: 34.0226, 2030: 26.171, 2040: 26.171, 2050: 26.171 | G38, G40, G41, G42 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND_Trans.xlsx | CO2_Storage_Potential | A1 `~TFM_INS` | ACT_BND | UP | MINSNKAFF3 | FI | 2010: 9.16144, 2020: 56.2713, 2030: 22.2451 | G44, G45, G46 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND_Trans.xlsx | CO2_Storage_Potential | A1 `~TFM_INS` | ACT_BND | UP | MINSNKAFF4 | FI | 2040: 64.1229, 2050: 51.0357 | G53, G54 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BIO | E4 `~TFM_INS` | ACT_BND | UP | MINBIOCRP41 | FI | 2020: 3.5, 2030: 4.2, 2040: 6, 2050: 7.4 | L59, L60, L61, L62 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BIO | E4 `~TFM_INS` | ACT_BND | UP | MINBIOGAS1 | FI | 2005: 0.9, 2010: 0.9, 2020: 0.9, 2030: 2.1, 2040: 5.4, 2050: 6.5 | L81, L82, L83, L84, L85, L86 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BIO | E4 `~TFM_INS` | ACT_BND | UP | MINBIOAGRW1 | FI | 2005: 14.5, 2010: 14.5, 2020: 17, 2030: 17.9, 2040: 17.9, 2050: 17.9 | L94, L95, L96, L97, L98, L99 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BIO | E4 `~TFM_INS` | ACT_BND | UP | MINBIOWOO | FI | 2005: 56, 2010: 55.7, 2020: 74.2, 2030: 82.8, 2040: 82.1, 2050: 80.6 | L107, L108, L109, L110, L111, L112 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BIO | E4 `~TFM_INS` | ACT_BND | UP | MINBIOFRSR1 | FI | 2005: 19, 2010: 18.7, 2020: 18.7, 2030: 40.3, 2040: 42.5, 2050: 43.9 | L133, L134, L135, L136, L137, L138 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BIO | E4 `~TFM_INS` | ACT_BND | UP | MINBIOWOOW1a | FI | 2005: 55, 2010: 55.1, 2020: 63, 2030: 84.3, 2040: 84.3, 2050: 84.3 | L159, L160, L161, L162, L163, L164 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BIO | E4 `~TFM_INS` | ACT_BND | UP | MINBIOMUN1 | FI | 2005: 8, 2010: 8.1, 2020: 9.4, 2030: 11.8, 2040: 14.5, 2050: 17 | L185, L186, L187, L188, L189, L190 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BIO | E4 `~TFM_INS` | ACT_BND | UP | MINBIOSLU1 | FI | 2005: 2, 2010: 2.2, 2020: 2.5, 2030: 3, 2040: 3.6, 2050: 4.1 | L198, L199, L200, L201, L202, L203 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BIO | E4 `~TFM_INS` | ACT_BND | UP | MINMPPWOO1 | FI | 2005: 60.2, 2010: 60.2, 2020: 67, 2030: 73.8, 2040: 73.2, 2050: 73.2 | L210, L211, L212, L213, L214, L215 |

### 2.3 Link: external trade, stays on FI hub - no change

| File | Sheet | Table | Attribute | Lim | Item(s) | Region | Values (year: value) | Cells |
|---|---|---|---|---|---|---|---|---|
| SubRES_TMPL/SubRes_41_TRADE-ELC-EXTRAEU_Trans.xlsx | IMP-EXP_ELC_ExtraEU | B2 `~TFM_DINS` | ACT_BND | FX | IMPELC-RU | FI | 2005: 11.4025, 2010: 11.4025, 2015: 12.5798, 2020: 9.6768 | G4, G5, G6, G7 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B10 `~TFM_INS` | ACT_BND | UP | IMPBIOWOO | FI | 2010: 10.5938, 2012: 6.8413, 2016: 2.5784, 2018: 11.4686, 2020: 22.3377, 2023: 12.4201 | H12, H13, H14, H15, H16, H17 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B10 `~TFM_INS` | ACT_BND | LO | IMPBIOWOO | FI | 2010: 8.66765, 2012: 5.59743, 2016: 2.1096, 2018: 9.3834, 2020: 18.2763, 2023: 10.1619 | H19, H20, H21, H22, H23, H24 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B27 `~TFM_INS` | ACT_BND | UP | IMPBIOETH | FI | 2010: 133.719, 2012: 149.359, 2016: 123.406, 2018: 153.484, 2020: 170.156, 2023: 170.156 | H29, H30, H31, H32, H33, H34 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B27 `~TFM_INS` | ACT_BND | LO | IMPBIOETH | FI | 2010: 109.406, 2012: 122.203, 2016: 100.969, 2018: 125.578, 2020: 139.219, 2023: 139.219 | H36, H37, H38, H39, H40, H41 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B45 `~TFM_INS` | ACT_BND | UP | IMPBIOEMHV | FI | 2010: 68.541, 2012: 68.541, 2014: 222.643, 2016: 595.981 | H47, H48, H49, H50 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B54 `~TFM_INS` | ACT_BND | UP | IMPBIOOIL | FI | 2010: 360.703, 2015: 522.574, 2020: 605.421, 2025: 675.522 | H56, H57, H58, H59 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | K59 `~TFM_INS` | ACT_BND | UP | IMPOILHFO | FI | 2010: 29.5965, 2012: 33.1762, 2014: 50.6728, 2016: 49.3289, 2018: 18.1414, 2020: 18.4638, 2023: 22.5438 | Q61, Q62, Q63, Q64, Q65, Q66, Q67 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | K59 `~TFM_INS` | ACT_BND | LO | IMPOILHFO | FI | 2010: 24.2153, 2012: 27.1442, 2014: 41.4596, 2016: 40.36, 2018: 14.843, 2020: 15.1067, 2023: 18.4449 | Q69, Q70, Q71, Q72, Q73, Q74, Q75 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | V59 `~TFM_INS` | ACT_BND | UP | IMPOILNAP | FI | 2010: 19.4016, 2012: 6.51047, 2014: 7.79582, 2016: 16.6132, 2018: 19.8915, 2020: 16.3453, 2023: 15.5916 | AB61, AB62, AB63, AB64, AB65, AB66, AB67 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | V59 `~TFM_INS` | ACT_BND | LO | IMPOILNAP | FI | 2010: 15.8741, 2012: 5.32675, 2014: 6.3784, 2016: 13.5926, 2018: 16.2749, 2020: 13.3734, 2023: 12.7568 | AB69, AB70, AB71, AB72, AB73, AB74, AB75 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B62 `~TFM_INS` | ACT_BND | UP | IMPOILGSL | FI | 2010: 1.23887, 2014: 23.8241, 2016: 28.6461, 2018: 27.7849, 2020: 29.5488, 2023: 29.4567 | H66, H67, H68, H69, H70, H71 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B62 `~TFM_INS` | ACT_BND | LO | IMPOILGSL | FI | 2010: 1.01362, 2014: 19.4925, 2016: 23.4377, 2018: 22.7331, 2020: 24.1763, 2023: 24.1009 | H73, H74, H75, H76, H77, H78 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | K81 `~TFM_INS` | ACT_BND | UP | IMPOILLPG | FI | 2010: 11.8277, 2012: 13.3978, 2014: 36.1614, 2016: 34.1685, 2018: 36.3456, 2020: 38.7991, 2023: 49.7266 | Q83, Q84, Q85, Q86, Q87, Q88, Q89 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | K81 `~TFM_INS` | ACT_BND | LO | IMPOILLPG | FI | 2010: 9.67722, 2012: 10.9618, 2014: 29.5866, 2016: 27.956, 2018: 29.7373, 2020: 31.7447, 2023: 40.6854 | Q91, Q92, Q93, Q94, Q95, Q96, Q97 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | V81 `~TFM_INS` | ACT_BND | UP | IMPOILDST | FI | 2010: 78.2555, 2012: 100.96, 2014: 93.2693, 2016: 82.8903, 2018: 66.8548, 2020: 82.526, 2023: 79.7083 | AB83, AB84, AB85, AB86, AB87, AB88, AB89 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | V81 `~TFM_INS` | ACT_BND | LO | IMPOILDST | FI | 2010: 64.0272, 2012: 82.604, 2014: 76.3113, 2016: 67.8193, 2018: 54.6994, 2020: 67.5213, 2023: 65.2159 | AB91, AB92, AB93, AB94, AB95, AB96, AB97 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B82 `~TFM_INS` | ACT_BND | UP | IMPOILKER | FI | 2010: 30.0545, 2014: 19.0931, 2016: 25.3519, 2018: 21.1015, 2020: 31.0795, 2023: 21.4821 | H84, H85, H86, H87, H88, H89 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B82 `~TFM_INS` | ACT_BND | LO | IMPOILKER | FI | 2010: 24.5901, 2014: 15.6216, 2016: 20.7425, 2018: 17.2648, 2020: 25.4286, 2023: 17.5762 | H91, H92, H93, H94, H95, H96 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B100 `~TFM_INS` | ACT_BND | UP | IMPOILOTH | FI | 2010: 15.1185, 2012: 17.0947, 2014: 3.21965, 2016: 1.85057, 2018: 2.78004, 2020: 1.5533, 2020: 5.43865, 2023: 1.66635 | H102, H103, H104, H105, H106, H107, H108, H109 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | B100 `~TFM_INS` | ACT_BND | LO | IMPOILOTH | FI | 2010: 12.3697, 2012: 13.9866, 2014: 2.63426, 2016: 1.5141, 2018: 2.27457, 2020: 1.27088, 2020: 4.44981, 2023: 1.36337 | H111, H112, H113, H114, H115, H116, H117, H118 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Imports (bio & fossil) | K101 `~TFM_INS` | ACT_BND | UP | IMPISOBUT | FI | 2010: 26.93 | Q103 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | B17 `~TFM_INS` | ACT_BND | UP | EXPOILGSL | FI | 2010: 100.232, 2012: 107.115, 2014: 135.539, 2016: 129.808, 2018: 130.419, 2020: 130.243, 2023: 126.944 | H21, H22, H23, H24, H25, H26, H27 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | B17 `~TFM_INS` | ACT_BND | LO | EXPOILGSL | FI | 2010: 82.008, 2012: 87.6396, 2014: 110.896, 2016: 106.206, 2018: 106.706, 2020: 106.562, 2023: 103.863 | H29, H30, H31, H32, H33, H34, H35 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | K17 `~TFM_INS` | ACT_BND | UP | EXPOILHFO | FI | 2010: 28.8177, 2012: 44.983, 2014: 34.0764, 2016: 53.4864, 2018: 47.068, 2020: 47.7128, 2023: 53.8129 | Q19, Q20, Q21, Q22, Q23, Q24, Q25 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | K17 `~TFM_INS` | ACT_BND | LO | EXPOILHFO | FI | 2010: 23.5782, 2012: 36.8043, 2014: 27.8807, 2016: 43.7616, 2018: 38.5102, 2020: 39.0377, 2023: 44.0288 | Q27, Q28, Q29, Q30, Q31, Q32, Q33 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | V17 `~TFM_INS` | ACT_BND | UP | EXPOILLPG | FI | 2010: 0.230274, 2012: 0.276329, 2014: 0.695009, 2016: 0.464735, 2018: 0.230274, 2020: 0.464735, 2023: 0.184219 | AB19, AB20, AB21, AB22, AB23, AB24, AB25 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | V17 `~TFM_INS` | ACT_BND | LO | EXPOILLPG | FI | 2010: 0.188406, 2012: 0.226087, 2014: 0.568644, 2016: 0.380238, 2018: 0.188406, 2020: 0.380238, 2023: 0.150725 | AB27, AB28, AB29, AB30, AB31, AB32, AB33 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | B38 `~TFM_INS` | ACT_BND | UP | EXPOILKER | FI | 2010: 3.66345, 2012: 6.86635, 2014: 3.92303, 2016: 3.40387, 2018: 2.32786, 2020: 4.48406, 2023: 4.82738 | H40, H41, H42, H43, H44, H45, H46 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | B38 `~TFM_INS` | ACT_BND | LO | EXPOILKER | FI | 2010: 2.99737, 2012: 5.61792, 2014: 3.20975, 2016: 2.78498, 2018: 1.90461, 2020: 3.66878, 2023: 3.94967 | H48, H49, H50, H51, H52, H53, H54 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | K38 `~TFM_INS` | ACT_BND | UP | EXPOILNAP | FI | 2012: 0.133978, 2014: 2.43672, 2016: 6.07086, 2018: 3.50016, 2020: 5.49308, 2023: 3.06653 | Q41, Q42, Q43, Q44, Q45, Q46 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | K38 `~TFM_INS` | ACT_BND | LO | EXPOILNAP | FI | 2012: 0.109618, 2014: 1.99368, 2016: 4.96707, 2018: 2.86377, 2020: 4.49434, 2023: 2.50898 | Q49, Q50, Q51, Q52, Q53, Q54 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | V38 `~TFM_INS` | ACT_BND | UP | EXPOILDST | FI | 2010: 124.591, 2012: 133.601, 2014: 157.16, 2016: 164.357, 2018: 154.116, 2020: 145.366, 2023: 120.262 | AB40, AB41, AB42, AB43, AB44, AB45, AB46 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BAU Exports fossil | V38 `~TFM_INS` | ACT_BND | LO | EXPOILDST | FI | 2010: 101.938, 2012: 109.31, 2014: 128.585, 2016: 134.474, 2018: 126.095, 2020: 118.936, 2023: 98.3959 | AB48, AB49, AB50, AB51, AB52, AB53, AB54 |
| SuppXLS/Scen_Trades_FIN.xlsx | UPD | B2 `~TFM_INS` | CAP_BND | FX | IMPELC-EetoFI | FI | 2010: 0.35, 2015: 1, 2020: 1 | G4, G5, G6 |
| SuppXLS/Scen_Trades_FIN.xlsx | UPD | B2 `~TFM_INS` | CAP_BND | UP | IMPELC-EetoFI | FI | 2025: 1, 2030: 1.5, 2040: 2, 2050: 3 | G10, G7, G8, G9 |
| SuppXLS/Scen_Trades_FIN.xlsx | UPD | B2 `~TFM_INS` | CAP_BND | FX | IMPELC-NOtoFI | FI | 2010: 0.1, 2015: 0.1, 2020: 0.1 | G11, G12, G13 |
| SuppXLS/Scen_Trades_FIN.xlsx | UPD | B2 `~TFM_INS` | CAP_BND | UP | IMPELC-NOtoFI | FI | 2025: 0.1, 2030: 0.3, 2040: 0.5, 2050: 1 | G14, G15, G16, G17 |
| SuppXLS/Scen_Trades_FIN.xlsx | UPD | B2 `~TFM_INS` | CAP_BND | FX | IMPELC-SEtoFI | FI | 2010: 2.05, 2015: 2.55, 2020: 2.7 | G18, G19, G20 |
| SuppXLS/Scen_Trades_FIN.xlsx | UPD | B2 `~TFM_INS` | CAP_BND | UP | IMPELC-SEtoFI | FI | 2025: 3.1, 2030: 4.5, 2040: 6, 2050: 8 | G21, G22, G23, G24 |

### 2.4 No change: cumulative UP bound on an FI-hub process

| File | Sheet | Table | Attribute | Lim | Item(s) | Region | Values (year: value) | Cells |
|---|---|---|---|---|---|---|---|---|
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND_Trans.xlsx | CO2_Storage_Potential | A1 `~TFM_INS` | ACT_CUM | UP | MINSNKAFF1 | FI | -: 785.164 | G27 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND_Trans.xlsx | CO2_Storage_Potential | A1 `~TFM_INS` | ACT_CUM | UP | MINSNKAFF2 | FI | -: 1126 | G28 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND_Trans.xlsx | CO2_Storage_Potential | A1 `~TFM_INS` | ACT_CUM | UP | MINSNKAFF3 | FI | -: 877.956 | G29 |
| SubRES_TMPL/SUBRES_10_TECHS_CHP_SUP_IND_Trans.xlsx | CO2_Storage_Potential | A1 `~TFM_INS` | ACT_CUM | UP | MINSNKAFF4 | FI | -: 1152.76 | G30 |

### 2.5 No change: sentinel, not a limit

| File | Sheet | Table | Attribute | Lim | Item(s) | Region | Values (year: value) | Cells |
|---|---|---|---|---|---|---|---|---|
| SuppXLS/Scen_HydrogenUStore.xlsx | USTORE-H2 | B4 `~TFM_INS` | ACT_BND | UP | STH2SUG | FI | 2010: 999999 | F6 |
| SuppXLS/Scen_ZUEmisCO2.xlsx | Negative Emissions | D5 `~TFM_INS` | COM_BNDNET | LO | cset_cn=ELCCO2N,ETSCO2,SUPCO2N,INDCO2*,TOTCO2 | ALLREGIONS | -: -1e+07 | H8 |

### 2.6 No change: not a quantity

| File | Sheet | Table | Attribute | Lim | Item(s) | Region | Values (year: value) | Cells |
|---|---|---|---|---|---|---|---|---|
| SubRES_TMPL/SubRes_00_Nuc-EU_Trans.xlsx | Updates | A23 `~TFM_DINS-AT` | NCAP_BND | N | ENFI_OLKILUOTO-3 | FI | 2013: 2012 | F25 |

## 3. User constraints with a non-zero RHS

| File | Sheet | Table | UC_N | Region set now | RHS attribute | Lim | Values (year: value) |
|---|---|---|---|---|---|---|---|
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BioImport | H10 | AU_EU-IMP_ETH | R_S: AL,BE,BG,CY,DE,DK,EE,ES,FI,FR,EL,HR,IE,IS,IT,LT,LV,ME,MT,NL,NO,PL,PT,RO,SE,SI,UK | UC_RHST | UP | 2005: 6573.71, 2020: 6573.71, 2030: 22788.8, 2040: 22788.8, 2050: 22788.8 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BioImport | H10 | AU_EU-IMP_EMHV | R_S: AL,BE,BG,CY,DE,DK,EE,ES,FI,FR,EL,HR,IE,IS,IT,LT,LV,ME,MT,NL,NO,PL,PT,RO,SE,SI,UK | UC_RHST | UP | 2005: 7012.99, 2020: 7012.99, 2030: 12181.8, 2040: 12181.8, 2050: 12181.8 |
| SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx | BioImport | H10 | AU_EU-IMP_WOO | R_S: AL,BE,BG,CY,DE,DK,EE,ES,FI,FR,EL,HR,IE,IS,IT,LT,LV,ME,MT,NL,NO,PL,PT,RO,SE,SI,UK | UC_RHST | UP | 2005: 283, 2020: 283, 2030: 517, 2040: 517, 2050: 517 |
| SuppXLS/Scen_CO2target_NONETS_2030.xlsx | ESRnonETS | L4 | CO2TargetESR2030 | R_E: AllRegions | UC_RHSRT | UP | 2010: 33364.8, 2020: 21554.7, 2030: 11264.2 |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Stock | D14 | UCR_OldStock-DetH | R_E: AllRegions | UC_RHSRT | FX | 2012: 313.968, 2014: 312.087, 2016: 310.217, 2018: 308.359, 2020: 306.512, 2022: 304.675, 2024: 302.85, 2026: 301.036, 2028: 299.232, 2030: 297.439, 2032: 295.657, 2034: 293.886, 2036: 292.125, 2038: 290.375, 2040: 288.636, 2042: 286.906, 2044: 285.1 ... (28 values) |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Stock | D45 | UCR_OldStock-DetH-70 | R_E: AllRegions | UC_RHSRT | FX | 2012: 475.309, 2014: 474.359, 2016: 473.411, 2018: 472.464, 2020: 471.52, 2022: 470.577, 2024: 469.636, 2026: 468.698, 2028: 467.761, 2030: 466.826, 2032: 465.893, 2034: 464.961, 2036: 464.032, 2038: 463.104, 2040: 462.178, 2042: 461.255, 2044: 460.3 ... (28 values) |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Stock | D76 | UCR_OldStock-Flat | R_E: AllRegions | UC_RHSRT | FX | 2012: 1103.74, 2014: 1099.33, 2016: 1094.94, 2018: 1090.57, 2020: 1086.21, 2022: 1081.87, 2024: 1077.54, 2026: 1073.24, 2028: 1068.95, 2030: 1064.68, 2032: 1060.42, 2034: 1056.19, 2036: 1051.97, 2038: 1047.76, 2040: 1043.57, 2042: 1039.4, 2044: 1035. ... (28 values) |
| SuppXLS/Scen_NewHouses_and_retrofits.xlsx | Stock | D107 | UCR_OldStock-SDetH | R_E: AllRegions | UC_RHSRT | FX | 2012: 596.314, 2014: 593.931, 2016: 591.558, 2018: 589.194, 2020: 586.839, 2022: 584.494, 2024: 582.159, 2026: 579.832, 2028: 577.515, 2030: 575.208, 2032: 572.909, 2034: 570.62, 2036: 568.339, 2038: 566.068, 2040: 563.806, 2042: 561.553, 2044: 559.3 ... (28 values) |
| SuppXLS/Scen_Diversified_Cement.xlsx | ICMFICO2 | D4 | cementCO2 | R_E: FI | UC_RHSRTS | LO | 2010: 900, 2014: 900, 2019: 847, 2020: 847, 2021: 847 |
| SuppXLS/Scen_EmisUC_V1Point.xlsx | INS | C8 | CO2TargetAllSectors2030FI | R_S: AllRegions | UC_RHSTS | UP | 2010: 64081, 2012: 54240, 2016: 46229, 2020: 40967, 2023: 31846.5, 2025: 27627, 2029: 27627, 2030: 22765.7, 2039: 22765.7, 2040: 11382.9, 2049: 11382.9, 2050: 5691.43, 2060: 5691.43 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Solar | D16 | AU_ELC_SOLPV-CAP-Resid | R_E: AllRegions | UC_RHSRT | UP | 2006: 12.7181, 2050: 12.7181 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Solar | D25 | AU_ELC_SOLPV-CAP-Comm | R_E: AllRegions | UC_RHSRT | UP | 2006: 11.4298, 2050: 11.4298 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Solar | D34 | AU_ELC_SOLPV-CAP-Ground | R_E: AllRegions | UC_RHSRT | UP | 2006: 103.725, 2050: 103.725 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Hydro | D7 | AU_ELC_HYLCAP_LC | R_E: AllRegions | UC_RHSRT | UP | 2006: 3.08, 2010: 3.27, 2040: 3.555 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Hydro | D27 | AU_ELC_HYRCAP | R_E: AllRegions | UC_RHSRT | UP | 2006: 0.01, 2010: 2.17, 2015: 3.26, 2020: 0.288, 2030: 0.288 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Hydro | D52 | AU_ELC_HYD | R_E: AllRegions | UC_RHSRT | UP | 2020: 55, 2050: 64 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Geoth | D16 | AU_ELC_GEOORCACT | R_E: AllRegions | UC_RHSRTS | UP | 2050: 0.047304 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Geoth | D26 | AU_ELC_GEOEGSACT | R_E: AllRegions | UC_RHSRTS | UP | 2050: 9.4135 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Geoth | D33 | AU_ELC_GEOMIN | R_E: AllRegions | UC_RHSRTS | UP | 2006: 1, 2020: 1, 2050: 79.4458 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Ocean | D6 | AU_ELC_NWAVEACT | R_E: AllRegions | UC_RHSRTS | UP | 2050: 1.1088 |
| SuppXLS/Scen_UC_ElcPot.xlsx | Ocean | D14 | AU_ELC_OffWAVEACT | R_E: AllRegions | UC_RHSRTS | UP | 2050: 4.4352 |
| SuppXLS/Scen_UC_HeatPumps_MaxCAP.xlsx | VDA_table | E3 | UC_RSD_HPCAP-DH_Max | R_E: AllRegions | UC_RHSRTS | UP | 2010: 652.585, 2050: 652.585, 2060: 652.585 |
| SuppXLS/Scen_UC_HeatPumps_MaxCAP.xlsx | VDA_table | E3 | UC_RSD_HPCAP-FL_Max | R_E: AllRegions | UC_RHSRTS | UP | 2010: 652.585, 2050: 621.639, 2060: 621.639 |
| SuppXLS/Scen_UC_HeatPumps_MaxCAP.xlsx | VDA_table | E3 | UC_RSD_HPCAP-SD_Max | R_E: AllRegions | UC_RHSRTS | UP | 2010: 652.585, 2050: 652.585, 2060: 652.585 |
| SuppXLS/Scen_UC_HeatPumps_MaxCAP.xlsx | VDA_table | E3 | UC_RSD_GHPCAP-DH_Max | R_E: AllRegions | UC_RHSRTS | UP | 2010: 396.061, 2050: 444.347, 2060: 444.347 |
| SuppXLS/Scen_UC_HeatPumps_MaxCAP.xlsx | VDA_table | E3 | UC_RSD_GHPCAP-FL_Max | R_E: AllRegions | UC_RHSRTS | UP | 2010: 221.634, 2050: 248.655, 2060: 248.655 |
| SuppXLS/Scen_UC_HeatPumps_MaxCAP.xlsx | VDA_table | E3 | UC_RSD_GHPCAP-SD_Max | R_E: AllRegions | UC_RHSRTS | UP | 2010: 93.8234, 2050: 93.8234, 2060: 93.8234 |
| SuppXLS/Scen_UC_HeatPumps_MinCAP_Lo.xlsx | VDA_table | E3 | UC_RSD_MinCAP-AHP_High | R_E: AllRegions | UC_RHSRTS | LO | 2014: 507.965, 2020: 507.965, 2030: 507.965, 2050: 507.965 |
| SuppXLS/Scen_UC_HeatPumps_MinCAP_Lo.xlsx | VDA_table | E3 | UC_RSD_MinCAP-GHP_High | R_E: AllRegions | UC_RHSRTS | LO | 2014: 85.294, 2020: 85.294, 2030: 85.294, 2050: 85.294 |
| SuppXLS/Scen_UC_REFScen16_data.xlsx | Sheet1 | G6 | UC_AUCoalWithoutCCS | R_E: FI | UC_RHSRTS | UP | 2015: 4.33988, 2020: 3.30271, 2025: 2.30772 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | ELC Trade calib | H6 | UCE_Base-Exp-Calib-Min | R_E: AllRegions | UC_RHSRT | LO | 2010: 17.8456, 2011: 13.0097, 2012: 5.6259, 2013: 6.41592, 2014: 12.5001, 2016: 10.8038, 2020: 22.8114, 2021: 22.9961 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | ELC Trade calib | H6 | UCE_Base-Imp-Calib-Min | R_E: AllRegions | UC_RHSRT | LO | 2010: 53.759, 2011: 60.3835, 2012: 65.2844, 2013: 60.1612, 2014: 73.9472, 2016: 75.6162, 2020: 74.4671, 2021: 83.7626 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | ELC Trade calib | H30 | UCE_Base-Exp-Calib-Max | R_E: AllRegions | UC_RHSRT | UP | 2010: 18.7378, 2011: 13.6602, 2012: 5.9072, 2013: 6.73672, 2014: 13.1251, 2016: 11.344, 2020: 23.952, 2021: 24.1459 |
| SuppXLS/Scen_ZATEMP_Calibration.xlsx | ELC Trade calib | H30 | UCE_Base-Imp-Calib-Max | R_E: AllRegions | UC_RHSRT | UP | 2010: 56.4469, 2011: 63.4027, 2012: 68.5486, 2013: 63.1693, 2014: 77.6446, 2016: 79.397, 2020: 78.1904, 2021: 87.9508 |
| SuppXLS/Scen_ZIETASSUMPTIONS.xlsx | INS | J23 | AU_NUC_CAPLifeExt | R_E: FI | UC_RHSRT | UP | 2019: 2.902, 2022: 2.902, 2023: 3.022, 2050: 3.022, 2060: 3.022 |
| SuppXLS/Scen_UC_CO2Storage_300.xlsx | UCStorage | D20 | CO2_Max_Stor_MS | R_E: FI | UC_RHSRTS | UP | 2040: 15000, 2045: 20000, 2050: 40000, 2060: 40000, 2075: 40000, 2100: 40000 |
| SuppXLS/Scen_ZUGROWTH_Yearly.xlsx | GROWTHs 3y bio vs fossil | I7 | UC_Growth_solar | R_E: FI | UC_RHSRT | LO | -: -1 |
| SuppXLS/Scen_ZUGROWTH_Yearly.xlsx | GROWTHs 3y bio vs fossil | I7 | UC_Growth_wind_ON | R_E: FI | UC_RHSRT | LO | -: -1.5 |
| SuppXLS/Scen_ZUGROWTH_Yearly.xlsx | GROWTHs 3y bio vs fossil | I7 | UC_Growth_wind_OFF | R_E: FI | UC_RHSRT | LO | -: -0.75 |
| SuppXLS/Scen_ZUGROWTH_Yearly.xlsx | GROWTHs 3y bio vs fossil | I7 | UC_Growth_STOR | R_E: FI | UC_RHSRT | LO | -: -800 |
| SuppXLS/Scen_ZUGROWTH_Yearly.xlsx | GROWTHs 3y bio vs fossil | I7 | UC_Growth_CCS | R_E: FI | UC_RHSRT | LO | -: -800 |

Zero-RHS UC tables that share a `~UC_Sets` line with a table above and therefore switch with it:

- SuppXLS/Scen_UC_ElcPot.xlsx / Geoth / D7 AU_ELC_GEOFLASHACT: safe (UP, coefficients >= 0, so R_S <= 0 is the same as R_E <= 0)
- SuppXLS/Scen_UC_ElcPot.xlsx / Hydro / D16 AU_ELC_HYLCAP_SC: safe (UP, coefficients >= 0, so R_S <= 0 is the same as R_E <= 0)
- SuppXLS/Scen_UC_ElcPot.xlsx / Hydro / D41 AU_ELC_HYPCAP: safe (UP, coefficients >= 0, so R_S <= 0 is the same as R_E <= 0)
- SuppXLS/Scen_UC_ElcPot.xlsx / Ocean / D33 AU_ELC_TIDACT: safe (UP, coefficients >= 0, so R_S <= 0 is the same as R_E <= 0)
- SuppXLS/Scen_UC_ElcPot.xlsx / Solar / D7 AU_ELC_SOLTHE: safe (UP, coefficients >= 0, so R_S <= 0 is the same as R_E <= 0)

## 4. Disabled tables (tag without `~` in the current mode) holding bounds/RHS

- SubRES_TMPL/SubRes_40_TRADE-EXTRAEU.xlsx / SUP_LNG / D2 `FI_T: NCAP_BND~FX`
- SubRES_TMPL/SubRes_40_TRADE-EXTRAEU.xlsx / SUP_LNG / D19 `FI_T: `
- SuppXLS/Scen_Power_from_JRC-IDEES-2015.xlsx / Other charact / F69 `UC_T: UC_COMPRD~LO`
- SuppXLS/Scen_UC_ElcPot.xlsx / Wind / C13 `UC_T: UC_RHSRTS~UP`
- SuppXLS/Scen_UC_ElcPot.xlsx / Wind / C21 `UC_T: UC_RHSRTS~UP`
- SuppXLS/Scen_UC_ElcPot.xlsx / Wind / C31 `UC_T: UC_RHSRTS~UP`
- SuppXLS/Scen_UC_ElcPot.xlsx / Wind / C44 `UC_T: UC_RHSRTS~UP`
- SuppXLS/Scen_UC_ElcPot.xlsx / Wind / C56 `UC_T: UC_RHSRTS~UP`
- SuppXLS/Scen_UC_LimitCOAL.xlsx / UC_AUTOGEN / I34 `UC_T: UC_COMPRD~2006`
- SuppXLS/Scen_UC-ELC.xlsx / Non increasing IMP / H41 `UC_T: `
- SuppXLS/Scen_ZUGROWTH_Yearly.xlsx / Diffusion rate (GROWTH) biANN / I7 `UC_T: `

## 5. Proposal: how each item becomes a UC_R_SUM constraint that still works in single-region mode

### 5.1 Principle

Every change is a switch on `Region_selection!B8` (the pattern already used in
`ScenTrade_TradeParameters` and `VT_FINTIMES_IND`):

```
=IF(Region_selection!$B$8=Region_selection!$D$8, <today's value>, <Reg-FINTIMES value>)
```

In single-region mode every switched cell evaluates to exactly today's text/number, and every
new table has a tag without `~`, so VEDA reads the same data as now: the single-region run must
reproduce the previous objective to solver precision (regression check). Workbooks without a
`Region_selection` sheet get one copied from `ScenTrade_TradeParameters.xlsx`;
`select_model.xlsm` flips every workbook that has that sheet (it walks the model folder,
`SubRES_TMPL`, `SuppXLS`, `SuppXLS/Trades`), so no macro change is needed.

### 5.2 User constraints with a non-zero RHS (section 3)

Changed in place, in the same table, so scenario membership and UC names stay the same:

1. The governing `~UC_Sets: R_E: FI` / `R_E: AllRegions` cell -> `~UC_Sets: R_S: AllRegions`
   in Reg mode. TIMES then builds one constraint summed over FI + all regions (`UC_R_SUM`).
2. The RHS attribute loses its region index in Reg mode: `UC_RHSRT` -> `UC_RHST`,
   `UC_RHSRTS` -> `UC_RHSTS` (tag parameter, header cells, `~0` interpolation columns, and
   `Attribute` cells). Values, years, LimType and interpolation codes are untouched.
3. LHS columns are region-less in all target tables, so the coefficients apply in every region;
   any LHS column headed by a single region would be switched to `AllRegions` (none found).
4. `ELC Trade calib` (`UCE_Base-*-Calib-*`) sums `UC_IRE` over `TB*,GI*,EXPELC-*`; `TB*` also
   matches the internal links `TB_<C>_FI_FI1D9`. In Reg mode the selector gets
   `,-TB_*_FI*_FI*` so internal flows never count as national imports/exports.
5. `BioImport` (`AU_EU-IMP_*`) is already R_S, but over a fixed list of EU countries that does
   not contain FI1xx: in Reg mode the list becomes `AllRegions`.
6. Already national and unchanged: `CO2TargetAllSectors2030FI` (Scen_EmisUC_V1Point) and the
   cumulative CO2 caps in Scen_ZZ_CumulativeCO2 (both `R_S: AllRegions`).

A `~UC_Sets` line governs every `~UC_T` below it on the sheet, so zero-RHS tables under the same
line switch too. Each such table was checked: all are `UP` with coefficients >= 0 and RHS 0,
for which "sum <= 0" and "each region <= 0" are the same constraint.

### 5.3 National bounds (section 2.1, Sum rule)

Each bound item becomes its own constraint in a new Reg-only `~UC_T` table:

```
~UC_Sets: R_S: AllRegions        (tag text without ~ in single-region mode)
~UC_Sets: T_E:
~UC_T
UC_N                     Pset_PN       Cset_CN  Year  LimType  UC_ACT  UC_RHST  UC_RHST~0
RS_ACT_SSCDCOKE00_FX     SSCDCOKE00                            1
                         SSCDCOKE00             2010  FX               30.79
                         ...                                                     <IE code>
```

- Coefficient 1 on the same variable: ACT_BND -> UC_ACT, CAP_BND -> UC_CAP,
  NCAP_BND -> UC_NCAP, FLO_BND(p,c) -> UC_FLO, COM_BNDPRD -> UC_COMPRD, COM_BNDNET -> UC_COMNET.
  All bounds found are ANNUAL, so the UC is annual (UC_RHST, no timeslice set).
- RHS = the national value VEDA ends up with: every value of the same attribute, limit, item and
  year is replayed in scenario order (zeros and later overrides included, blank year = start year
  2010), the last one wins; a LO whose final values are all 0 is dropped. Same years, same LimType.
- Interpolation: the bound's explicit option is copied to `UC_RHST~0`: the table's own year-0
  value if there is one, else the SysSettings `~TFM_MIG` default (ACT_BND: 1, ACT_BND UP: 15,
  CAP_BND UP/LO: 5, NCAP_BND: 1, ...). Where neither exists the TIMES default applies, and it is
  the same for both: in the TIMES source (`preppm.mod`, block "NON-REGULAR NON-COST PARAMETERS: NOT
  interpolated by default") CAP_BND, NCAP_BND, ACT_BND, FLO_BND, COM_BNDPRD and UC_RHST(S) are all
  prepared with the same default option.
- One UC per item: a wildcard row (`PSET_PN=IND*`, `PSET_CI=Bldg_DETPre45*`, a CSET list)
  bounds **each** matched process/commodity in VEDA, so it becomes one UC per match, never one
  summed UC (that would be tighter than today). Matches are expanded from the topology GDX.
- UP bounds stay where they are: under the sum they can never bind tighter than the UC. LO and
  FX bounds are switched off at source in Reg mode (row: `Attribute` cell -> `\I:`; column: header
  -> `\I:<header>`; otherwise the value cell -> blank), because an FI-only LO/FX would pin moved
  activity to FI.
- Where the Reg-only tables live: bounds from a `SuppXLS/Scen_*` file -> new sheet `RegSum` in
  the same workbook (same scenario, so other cases are unaffected). Bounds from BASE (`VT_*`) and
  SubRES files -> one new workbook `SuppXLS/Scen_RegSum_Base.xlsx` (no BASE/SubRES file holds a
  `~UC_T` today). **In VEDA: add scenario `RegSum_Base` to the Reg cases right after
  SysSettings**, before the other scenarios, so that later scenarios still override the base values
  as now. (In single-region cases it is harmless: all its tags are off.)

### 5.4 Decisions taken (scientific basis)

1. **ACTCOST = 1e-4 M EUR/PJ** (section 1): the smallest value the solver still sees in 2070,
   and below the regression tolerance even with full regionalisation.
2. **Resource potentials (`MIN*`: biomass, coal reserves, CO2 sink rates) are summed now**
   (section 2.2). The national potential is what the data say today; splitting it needs regional
   resource data (e.g. Luke regional forest statistics for biomass), and invented shares would be
   less correct than the national total. When supply processes appear in regions the UC keeps the
   national total; the Split rule replaces it once regional data are in.
3. **Physically regional limits are summed for now** (hydro, solar, geothermal and wave potentials
   in `Scen_UC_ElcPot`, nuclear per-plant `CAP_BND`, `CO2_Max_Stor_MS`): a sum is exact at national
   level and never infeasible. They are split in tasks 2-3 with the plant register, reV and
   ENSPRESO data, which is where that information enters the model.
4. **External trade bounds stay on the FI hub** (section 2.3, Link rule): in the hub design FI is
   the national border node, so these bounds stay correct while the links stay there.
5. **UP bounds stay at source**: under a national sum an FI-only UP bound can never bind tighter
   than the UC. LO and FX bounds are switched off in Reg mode.
6. **Cumulative `ACT_CUM` sink limits stay** (section 2.4): UP bounds on processes that exist only
   on the FI hub; a cumulative UC (`UC_CUMACT`) is needed only if sinks are regionalised.
7. Sentinels (`STH2SUG` ACT_BND UP 999999, `COM_BNDNET LO -9999999`) and the `NCAP_BND N` flag are
   not quantities. Zero bounds and zero-RHS UCs follow the Copy rule.

### 5.5 Test on a copy of the model (before touching the repository)

`tools/task0.py --apply` was run on a copy of `Reg-FINTIMES`, then:
- single-region mode: every existing table of the 17 edited workbooks reads exactly as before
  (rescan + table-by-table comparison). The only difference is ACTCOST, in a table that is off in
  single-region mode. All new tables are inactive;
- `--verify`: all 104 switched cells give the intended text in Reg-FINTIMES mode and the old value
  in FINTIMES mode;
- Reg-FINTIMES rescan: all converted UC_Sets read `R_S: AllRegions`, RHS attributes are
  region-less (UC_RHST/UC_RHSTS only), all `RS_*` constraints are active, and the only LO/FX
  bounds still read from FI are the 101 external-trade bounds (Link rule).

### 5.6 What the change does

- Cell edits: 104 in 17 workbooks (all `=IF(Region_selection...)` switches; single-region values unchanged).
- New `RS_*` constraints (Reg mode only): 184.
- Workbooks that need a `Region_selection` sheet first (17): SubRES_TMPL/SubRES_00_Nuc-EU.xlsx, SubRES_TMPL/SubRES_22_TECHS_BIOREFINERIES.xlsx, SuppXLS/Scen_BIOPOT_BIOM16_ForestBAU.xlsx, SuppXLS/Scen_CO2target_NONETS_2030.xlsx, SuppXLS/Scen_Diversified_Cement.xlsx, SuppXLS/Scen_NewHouses_and_retrofits.xlsx, SuppXLS/Scen_RegSum_Base.xlsx, SuppXLS/Scen_UC_CO2Storage_300.xlsx, SuppXLS/Scen_UC_ElcPot.xlsx, SuppXLS/Scen_UC_HeatPumps_MaxCAP.xlsx, SuppXLS/Scen_UC_HeatPumps_MinCAP_Lo.xlsx, SuppXLS/Scen_UC_REFScen16_data.xlsx, SuppXLS/Scen_ZATEMP_Calibration.xlsx, SuppXLS/Scen_ZIETASSUMPTIONS.xlsx, SuppXLS/Scen_ZUGROWTH_Yearly.xlsx, VT_FINTIMES_ELC.xlsx, VT_FINTIMES_SUP.xlsx.

## 6. Related traps found during the audit (not task 0, recorded for the next tasks)

- Many zero-RHS share/coupling UCs are `R_E: FI` with coefficients in a column headed `FI`
  (e.g. `Scen_UC-IND` `TUC_Istruc_*` steel route shares, `Scen_UC_RSD-COM` `RCUC-*`,
  `Scen_TRA_CO2_target` `UC_CO2_Cars` with 555 rows, `Scen_UC_LimitCOAL`). When a sector moves,
  those constraints no longer see the moved processes. Task 1 (steel) must check `UC-IIS`.
- `ELC Trade calib` and other `UC_IRE` sums use `TB*`, which also catches internal links.
- `SubRES_10_TECHS_CHP_SUP_IND_Trans` `~TFM_AVA` makes `MISRIR` producers unavailable in FI in
  Reg mode (steel pilot); the same switch pattern will be needed for every moved sector.
- `ACT_CUM` CO2 storage potentials (`CO2_Storage_Potential`) are cumulative: if they are ever
  summed they need `UC_CUMACT`, not `UC_ACT`.
- `tools/check_run.py` is referenced in CLAUDE.md, but the file is at the repo root
  (`check_run.py`).
