# Task 5c: services buildings to the regions — audit and design

Status: applied 2026-11-20 (sections 8-9); server run 1 not solved (section 10, too slow); rerun pending. Audit on the DD files of the passing 5b run (case `5bfix7`,
`GAMS_WrkTIMES/5bfix7.run`). Nothing in the model changed yet; two composite floor-area keys added
(`tools/regional_keys.py`, section 2). Part of step 5 (`audit/task5.md`).

## 1. What is on the hub

509 services processes, all declared in FI only (DD scan of `5bfix7.run`):

| Part | Processes | Source | Existing stock (FI, 2010) |
|---|---|---|---|
| Fuel supply to services `COM<fuel>00/01` (BIO, COA, GAS, GEO, HTH = district heat, LPG, OIL, SOL), `COMELC00`, `COMCOO100/200` (cooling), `COMAHT00`, `COMGHT00` | 21 | `VT_FINTIMES_COM` `COM_Fuel`, `TechComm` | `Stock`: COMOIL00 13.29, COMBIO00 3.67, COMGAS00 1.26, COMCOA00 0.14, COMHTH00 4.39 |
| Existing end-use techs `C_ES-<use>-<bldg>_<fuel>`: space heat SH, water heat WH, cooling SC, cooking CK x 6 building types x fuel | 144 | `VT_FINTIMES_COM` `TechHeat/WaterHeat/Cool/Cook-COM` | `~FI_T: Stock` tables: SH 15.16, WH 1.51, SC 0.69, CK 107.12 |
| Building stock `NRbldg-<type>` (6 types) and electric services `NRbldg_<service>` (BuildLight, BuildTech, ICTM, Refrig, StLight, Vent) | 12 | `VT_FINTIMES_COM` `Building stock`, `TechELC-COM` | `NCAP_PASTI` 107.12 (6 types); `Stock` of the 6 electric services = their 2010 demand (1,919 PJ-units) |
| New end-use techs `C_ES-*` (heat pumps, condensing boilers, fuel cells `C_ES-SP-*`, ...) | ~298 | `SUBRES_30_TECHS_HeatingCooling` (+ `_Trans`) | - |
| New buildings and retrofits `NRbldg_<type>-MG1..` | 42 | `SubRES_31_TECHS_BUILDINGS_COM` (+ `_Trans`) | - |
| Services batteries `COMBATS01-03` | 3 | `SubRES_14_TECHS_STORAGE` | - |
| Hydrogen blending into services gas `COMGASH2C01` | 1 | `SubRES_15_TECHS_HYDROGEN` | - |

Building types (code in the process names): `HO` hospitals (`NR_Hosp`), `HR` hotels and restaurants
(`NR_HoRest`), `OF` offices (`NR_Offic`), `SL` large shops (`NR_ShopL`), `SS` small shops (`NR_ShopS`),
`SR` sport and recreation (`NR_SpoRecr`).

Chain: hub fuel (ELCLOW, GASNAT, HETHTH, BIOWOO, OIL*, COA*, REN*, ...) -> `COM*00` -> `COMELC/COMGAS/COMHET/...`
-> `C_ES-*` -> `NR_ES-<bldg>-<use>` -> `NRbldg*` -> demand `NR_*`. Retrofit commodities `Bldg_<type>-Cei/Wal/Win`
stay inside the chain.

Demand (`COM_PROJ`), three sources, all FI:

| Demand | Source | Values |
|---|---|---|
| `NR_BuildLight`, `NR_BuildTech`, `NR_ICTM`, `NR_Refrig`, `NR_StLight`, `NR_Vent` | `VT_FINTIMES_COM` `TechELC-COM`!E103 (2010) and `Scen_ZUDemand_REF2016` (2010-2070, wins) | 2010: 108.7, 35.2, 771.0, 217.5, 724.7, 62.0 |
| `NR_HoRest`, `NR_Hosp`, `NR_Offic`, `NR_ShopL`, `NR_ShopS`, `NR_SpoRecr` (floor area served) | `Scen_NewHouses_and_retrofits` `ServBldg Projection` (`~TFM_DINS`, 2010 and 2060; the 2010 value is read from the `ServBldg` fill of `NRbldg-*` PASTI through the `FI` header) | 2010: 6.0, 8.4, 28.1, 19.2, 16.2, 29.1 |

## 2. Keys (Split rule; Statistics Finland raku 15f7, floor area 2010)

| Model item | Key | Basis |
|---|---|---|
| `HO` hospitals | `bld_care_<heat>` (class 06) | health and social care buildings |
| `HR` hotels/restaurants, `SL`, `SS` shops | `bld_commercial_<heat>` (class 03) | class 03 = retail, wholesale, hotels, restaurants |
| `OF` offices | `bld_officeedu_<heat>` (classes 04 + 08) | **decision (yellow)**: the model has no education type; schools have the daytime use profile of offices. Offices alone: `bld_office_*` |
| `SR` sport and recreation | `bld_assembly_<heat>` (class 07) | assembly = sports halls, culture, religious |
| electric services `NRbldg_BuildLight/BuildTech/ICTM/Refrig/Vent` and their demands | `bld_services_all` (classes 03+04+06+07+08) | in-building electricity scales with services floor area |
| street lighting `NRbldg_StLight`, `NR_StLight` | `population_2010` | |
| `COM<fuel>00` fuel supply (stock = capacity) | `bld_services_<heat>` of the fuel | |

Heat source of a `C_ES-SH/WH` existing tech (stock split): ELC -> `elc`, HET -> `dh`, GAS/OIL/LPG -> `oilgas`,
BIO -> `wood`, COA -> `coal`, GEO -> `ground`, SOL -> `all`. Cooling (SC), cooking (CK), fuel cells (SP) and
building stock: `<class>_all`. If a class has no floor area for that heat source nationally, `<class>_all`.
New keys `bld_services_<heat>` and `bld_officeedu_<heat>` (16 files) are sums of the native classes
fetched in the same query; every one passes the exact share-sum and national-total checks (`audit/keys.md`).

New technologies (SubRES_30/31, COMBATS, COMGASH2C01) are available in all 19 regions and not on the hub.

## 3. Workbooks and treatment

| Workbook / table | Now | Treatment (rule) |
|---|---|---|
| `VT_FINTIMES_COM` `~FI_Process` (163) | `Region` FI | Reg mode: the 19 regions of the process key (copy mode: no hub copy) |
| `VT_FINTIMES_COM` `~FI_T: Stock` tables, `COM_Fuel` stocks | `FI` column | Reg sheet: STOCK x key (orange); FI stock row commented in Reg mode (4b mechanism) |
| `VT_FINTIMES_COM` `Building stock` `~FI_T: NCAP_PASTI` | `FI` column | **split** (x type key). `plan_book` treats only `STOCK` as split: extend to `NCAP_PASTI` (task 4 tool change) |
| `VT_FINTIMES_COM` `~FI_T: EFF/PRC_CAPACT/NCAP_AFA/LIFE/INPUT/Share/...` | `FI` column | copy to the regions (Reg sheet) |
| `VT_FINTIMES_COM` `TechELC-COM` `~FI_T: DEMAND` (2010) | `FI` | overridden by `Reg_Demand` 2010 (FI 0, regions x key) |
| `Scen_ZUDemand_REF2016` NR rows | `FI` | `Reg_Demand` split (4b mechanism) |
| `Scen_NewHouses_and_retrofits` `ServBldg Projection` | `FI`, value via fill lookup | Reg mode: table off, the 12 rows go to `Reg_Demand` (2010 = 6 `NRbldg-*` PASTI as in single mode, x type key) |
| `SUBRES_30_..._Trans` `AVA` | FI | Reg-only rows: `C_ES-*` all regions, not FI (`R_ES-*` stay on FI until 5d) |
| `SUBRES_30_..._Trans` `INS-UPD Heat/WaterHeat/SpCool/Others` (`~TFM_UPD`/`INS`, `FI` + `AllRegions` columns) | FI values from the `COM_All` fill (`MATCH(<FI header>)`) | copy: `FI` header -> `AllRegions`, old `AllRegions` -> comment, lookups read a region column that has services (as `5bfix4`); rows with only an `AllRegions` value keep it in the Reg formula |
| `SubRES_31_..._Trans` `AVA`, `COM_Saving`, `COM_Invcost` (`FI`) | FI | AVA all regions not FI; `FI` -> `AllRegions` (copy) |
| `SubRES_14` / `SubRES_15` Trans `AVA` | FI | `COMBATS*`, `COMGASH2C01` all regions |
| `Scen_DEMAND_Com-FR_Sami` `N_VEDA_INPUT` `~TFM_INS` (`COM_FR` of R_* and NR_* demands) | `FI` column (J3) | copy: `FI` -> `AllRegions` in Reg mode (without it the regional demands get the default flat profile) |
| `Scen_UC_RSD-COM` `COP_HP` `~TFM_UPD` (heat-pump ACT_EFF) | `FI` | copy: `FI` -> `AllRegions` |
| `Scen_UC_STORAGE` `Sheet1` (`FI` + `AllRegions`), `WinterPeakLimit` | zero `STGOUT_BND` of COMBATS at the winter peak | copy (check the dry run: FI column values must reach the regions) |
| `SysSettings` `Comms` | `COM*`, `NR_*`, `Bldg_*`, `COMFINOIL` declared FI | all regions (`COMFINOIL` = aggregate of `RS_PRD_COMFINOIL_*`: 4a lesson) |
| `ScenTrade__Trade_Links` | | links region <-> hub for every hub fuel the moved chain uses (computed from the DD topology by the tool); `HETHTH` gets the regions without a CHP link (copper plate until 5e) |

Every other scenario file that sets services parameters (`BAU-General` green certificates,
`FuelPrices-DELIV`, `SysSettings` FLO_SHAR/FLO_DELIV, `ZATEMP` NCAP_AFA/FLO_DELIV, `ZIETAssumptions_DRATE`,
`ZUILED`, `ZZZCostUpdate`, `Kill_Zebras`, `X-NationalGrids`) is written for every region where the processes
exist (they already write the 5b vehicles' regional rows): no change; checked after the run by comparing all
parameters of the moved processes (single FI vs regions).

## 4. Constraints

| Family | Source | Now | Treatment |
|---|---|---|---|
| End-use shares `RCUC-Lo/Up_C_ES-*` (min. electricity, cooking; max. district heat), 2015/2020/2050 | `Scen_UC_RSD-COM` `UC1` | `R_E: AllRegions`, coefficients in the `FI` column (header `=Shares!C$1`), `UC_RHSRT` 0 | national (`R_S`, `UC_RHST`), coefficients `AllRegions` (`plan_ucs_general`). Residential rows of the same tables become national too (residential is on the hub only: no change) |
| Their coefficients | `Stock-AF`!L (stock x AF per process, `MATCH("FI", fill header)`) -> `Shares` -> `UC1` | the `Stock`/`AF` fills (`~TFM_Fill-R`) get one column per region in Reg mode: **the FI lookup fails, every share is an error** | Reg-mode formula in `Stock-AF`!L: AF x sum of the regional stocks (`SUMPRODUCT` over the `Region_selection` columns). AF is a copy attribute (one row per process, checked), so the national share equals the single-mode share exactly |
| Unit/SPL boilers `UC_R_UnitBoiler_*`, `UC_R_SPLBoiler_*` | `Scen_UC_RSD-COM` `UC unit boilers` | residential only | 5d |
| Heat-pump caps `UC_RSD_*HPCAP*` | `Scen_UC_HeatPumps_*` | residential only | 5d |
| Battery discharge limits `UC_COMBatt1-3_DischLimit` | `Scen_UC_STORAGE` `UCStorage` | `R_E: AllRegions`, per battery | unchanged (per region: each region's batteries) |
| Calibration `COM_BNDPRD` UP (COMBIO, COMGAS, COMHET, COMFINOIL), `FLO_BND COMHTH00.HETHTH` UP | `Scen_ZATEMP_Calibration` | FI bounds + national twins `RS_PRD_COM*_LO/UP`, `RS_FLO_COMHTH00_HETHTH_UP` (task 0, all years) | unchanged: the FI upper bounds go slack (no services on the hub), the national twins carry the limits; no link corrections needed (COMBIO/COMGAS/COMHET are made and used inside each region) |
| Variable-RES adequacy `UC_VARI_ELE_Cons_Cap` (COMCON `COMELC`), `UC_VAR5_DSM`, `UC_VAR_MinStor5h` | `Scen_SepDb-ZIET_VAR*` | national since 5bfix6/7 | unchanged: regional COMELC is counted; it does not cross a link |

## 5. Size and risk

Services have 1,275 topology entries on the hub; in 19 regions ~24,000 (the whole 5b model has 30,485). The LP
(3.7 M rows in 5b, 41 min barrier) may grow by roughly half. Mitigation if needed: the new end-use techs
could be limited to the regions with that heat source (key > 0), which the key data already allow.

## 6. Checks after the run

As 5b: no dummy imports; COM_PROJ, NCAP_PASTI, PRC_RESID conserved (now incl. services); `rsum_rhs_scan`
0; `uc_ire_scan` clean; RCUC shares national and equal to single (DD coefficients); `COM_FR` of NR demands
present in every region; parameters of the moved processes single-FI vs regions (`parcmp`); objective
change explained (expected small: services are a copper plate on the hub's fuels).

## 7. Decisions (yellow)

1. Offices key incl. education buildings (`bld_officeedu_*`) - alternative `bld_office_*`.
2. New end-use technologies in all 19 regions (vs only where the heat source exists).

## 8. Dry run (2026-11-20, `python tools/task5c.py` -> `audit/task5c_dryrun.txt`)

Decisions confirmed: offices with education (`bld_officeedu_*`); new end-use technologies in all 19 regions.
Fuel supply (`COM*`, `COMAHT00`, `COMGHT00`) and the existing end-use techs are declared in all 19 regions
too (stock only where the key is positive), so a new heat pump or boiler can run in any region.

976 cell edits in 13 workbooks, every one a `Region_selection` switch (single mode unchanged), plus
regenerated/new sheets:

| Workbook | Edits | Sheets |
|---|---|---|
| `VT_FINTIMES_COM` | 163 declarations (19 regions, not FI); 13 stock tables off in Reg mode (their TechName cells feed the tables below, 5bfix3) | `Reg_COM`: 152 stock/past-investment rows x key (each sums to 1), 689 copied coefficient rows in all 19 regions |
| `VT_FINTIMES_SUP` | `COMAHT00`, `COMGHT00` declared in the regions (generic table: no copy needed; `Reg_SUP` untouched) | |
| `Scen_ZUDemand_REF2016` | NR rows commented in Reg mode | `Reg_Demand` regenerated: 4b-5b rows + 6 services demands x 13 years |
| `Scen_NewHouses_and_retrofits` | `ServBldg Projection` off; 2010 national = sum of the fill's region columns | `Reg_ServBldg` 12 rows x building-type key |
| `Scen_X-NATIONALGRIDS` | `COMGAS00` stock row commented | `Reg_GasGrid`: AGRGAS00 (5a) + COMGAS00 |
| `SUBRES_30` Trans | AVA `C_ES-*,NRbldg_N-*` regions; 15 INS/UPD tables FI -> AllRegions; 64 `COM_All` lookups read a region column (FI1B1, else FI) | |
| `SubRES_31` / `_14` / `_15` Trans | AVA rows; `COM_Saving`, `COM_Invcost` FI -> AllRegions | |
| `Scen_DEMAND_Com-FR(_Sami)` | `COM_FR` FI -> AllRegions | |
| `Scen_UC_RSD-COM` | `UC1` R_S, RHS `UC_RHST`, coefficients AllRegions; 214 `Stock-AF` formulas = national stock x AF | |
| `SysSettings` | services commodities and `COMFINOIL` in all regions | |
| `ScenTrade__Trade_Links` | | 1,083 -> 1,423 links: new hub fuels for services (BIOGAS, BIOMUN, BIOSLU, COA*, OIL*, RENAHT, RENGHT, COOFRE, GASGWG, battery AUX) and `HETHTH` for the 2 regions without a CHP link |

Tool changes (`tools/task4_industry.py`, defaults unchanged for earlier steps): `plan_book` options
`decl_all` and `split_tags` (NCAP_PASTI split; stock tables of moved processes off as a whole);
`plan_generic(books=...)`; `plan_ava_rows` finds the end of an AVA table past Reg-only rows.

Formula tests in Excel (scratch copies): in single mode the new `Stock-AF` (214 rows) and ServBldg (6 rows)
formulas equal the original values exactly; with a simulated regional fill (stock split over two region
columns, AF in each, a text column between) the national values are reproduced exactly, while the original
`FI` lookup returns nothing.

After apply: `regmode_check`, `reg_header_scan`; after the server sync: `rsum_rhs_scan`, `uc_ire_scan`.

## 9. Applied (2026-11-20)

`python tools/task5c.py --apply`: all 15 workbooks ok (first attempt stopped before saving `Scen_X-NATIONALGRIDS`:
the 5c sheet note did not start with the tool-family mark, so the ownership check refused to rewrite
`Reg_GasGrid`; workbooks restored from git, mark fixed, applied again from scratch).

`regmode_check` then found lookups keyed on an `FI` header that is `AllRegions` in Reg mode; fixed by
`python tools/task5c.py --fix --apply` (`audit/task5c_fix_dryrun.txt`, 357 cells):
- `Scen_DEMAND_Com-FR(_Sami)` `N_VEDA_INPUT`: rows 112+ read the profile sheet named by the header
  (`INDIRECT(ADDRESS(..,J$3))`): the sheet stays `"FI"` in Reg mode (188 + 132 cells).
- `SUBRES_30` `INS-UPD *`: 37 lookups in the residential fills (`RES_*`) keep the `FI` column (residential
  is on the hub until 5d; 5d switches them to a region column like the `COM_All` lookups).

Checks: `regmode_check` 0 new Reg-mode errors in all 15 workbooks; `reg_header_scan` 0 duplicate headers;
single-mode values of every original sheet identical to the committed workbooks (cell by cell, 15 books).
Next: server run, case named after the step (e.g. `5c`); then `rsum_rhs_scan`, `uc_ire_scan`, `check_run`,
`audit_run`, parameter comparison of the moved processes, and the `COM_FR` of the NR demands in every region.

## 10. Server run 1 (case `5c`): not solved, barrier too slow

Run commit `67a6d93` (rebuilt from the local commit `28d0327`, kept as `backup/pre-5crun-split`; left out: `5bfix7.gdx`
157 MB and a stale regional `baseline-sami.gdx` 226 MB = the unsolved run 6, objective 1.24e10). The log is a snapshot
taken at 21:16 while CPLEX was still in barrier (the commit message says "stopped by hand"; whether the run was stopped
is not known from the files).

| | 5bfix7 (run 7 of 5b) | 5c |
|---|---|---|
| rows / columns / nonzeros | 3.68 M / 4.35 M / 20.7 M | 6.67 M / 8.82 M / 36.3 M |
| reduced LP rows / cols | 1.60 M / 2.26 M | 2.37 M / 3.17 M |
| Cholesky nonzeros / FP ops | 440 M / 2.07e12 | 812 M / 4.21e12 |
| barrier iterations | 244 (optimal) | 253 at the snapshot, not converged |
| time per iteration | about 10 s | about 95 s (14:29 start, 6 h 47 min) |
| dual infeasibility at the end | 0.7 | 25 (falling about 2.4x per 80 iterations) |
| primal / dual objective | 1,529,072 / 1,529,068 | 1,526,967 / 1,526,830 |

- Size: expected from the design. About 494 services processes per region (`C_ES-*` by building type, `NRb*`, `COM*`) now
  sit in all 19 regions instead of only in FI (FI 1,585 -> 1,076 processes; each region about +500). Only 12 timeslices.
- Data numerics did not get worse: the magnitudes of NCAP_PASTI, PRC_RESID, COM_PROJ, FLO_SHAR, COM_FR and the UC
  coefficients match 5bfix7 (the 1e-8..1e-6 splits were already in 5bfix7). QA_CHECK has the same categories; the one
  count that grew (`RPC in TOP not found`, 65 -> 713) is the heat-pump COMAHT/COMGHT input, already reported for FI in
  single mode and now copied to the 18 regions.
- `rsum_rhs_scan`: 391 R_SUM UCs, 0 with only regional RHS. `uc_ire_scan`: no missing UC_IRE correction.
- Time per iteration grew 9.5x while the factor work grew 2x: the server was probably paging (the factor alone is about
  6.5 GB, GMO 3.4 GB) or sharing its cores. At the observed rate the barrier would need several hundred more iterations
  and would reach `RESLIM 50000` (about 04:20) with no solution (`solutiontype 2`: no crossover).
- The two objectives differ by 9e-5 (relative) at the snapshot; they lie 0.13 % below 5bfix7, which is the range expected
  from the services moves. This is not a result yet.
