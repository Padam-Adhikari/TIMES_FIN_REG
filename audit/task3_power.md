# Task 3 (power): existing power and CHP plants, hydro, wind, PV and nuclear to their regions

Tool: `tools/task3_power.py` (dry run by default, `--apply` writes with xlwings).
Dry-run output with every cell: `audit/task3_power_dryrun.txt`; apply log: `audit/task3_power_apply.log`.

## 1. Validation before the workbooks were touched

The design was first tested on the server's own DD files (`tools/dd_regionalise.py --step3`, the
19 regions added to the regional Baseline-Sami DD files, solved locally with TIMES 4.8.3 + CPLEX):

| Run | Content | Objective (M EUR) |
|---|---|---|
| r20 | skeleton: FI hub + 19 empty regions | 1,529,541.78 |
| s4 | + power sector in the regions (this design) | 1,529,544.94 (+0.0002 %) |

- 33 processes moved (20 classes, 7 nuclear units, 6 LowAF twins); every `NCAP_PASTI` and
  `PRC_RESID` total conserved (1,303 entries checked).
- No dummy imports beyond the base model's own (`ICMFI_PARA_DUMMY*` are identical in r20 and s4).
- The other differences are small re-allocations between equivalent options, e.g. storage, hydro dispatch and
  biomass steam (e.g. `STGHTH01` -49 PJ, `SELCH2PEM01_LowAF` +42 PJ summed over all years).
- An earlier variant that **traded** the LowAF pseudo commodities was 3.9 % cheaper (wrong):
  utilisation is a per-plant property, so the LowAF_* commodities now close inside each region.

## 2. What the tool writes (Reg-FINTIMES mode only; single-region values unchanged)

| Workbook | Sheet / cell | Rule | Change |
|---|---|---|---|
| VT_FINTIMES_ELC | ELC_ExistingStock P3:P28 (`~FI_Process` Region) | Split (declaration) | 20 existing classes declared in the regions with a non-zero key share (comma list) |
| Scen_Power_from_JRC-IDEES-2015 | CHP_VEDA!B1, ELE_VEDA!B1 | Split | national `~TFM_DINS-TS` PASTI tables off in Reg mode |
| " | **Reg_PASTI** (new, green) | Split | 172 region x class rows = national value x share (orange); year-0 codes copied |
| " | **Reg_Keys** (new) | Split | 16 keys x 19 regions (orange), sum check column (= 1) |
| " | Other charact G/H (48 cells) | Copy | AFA / EFF / CHPR written for FI copied to AllRegions |
| BY_Trans | HYDRO_CAP_ACTBND I4:X14 | Split | EUHYDDAM00 STOCK split over 16 regions (orange); Reg_Keys sheet |
| " | SolWin-AF E4, E34; HYDRO_CAP_ACTBND H31 | Copy (yellow) | wind, PV, hydro AF profiles national in every region |
| SubRes_00_Nuc-EU_Trans | NUC D5, E3:G8 | site | ENFI* off the hub; Loviisa FI1B1, Olkiluoto FI196, Pyhajoki FI1D9 |
| " | Updates B25 | site | OL3 firm commitment (NCAP_BND N) in FI196 |
| SubRes_12_TECHS_PowerLowAF_Trans | AVA rows 21-28, F3:Q3 | follow plant | 6 twins in their plants' regions, not on FI; LowAF_DumBase/DumPeak in the 12 regions |
| Scen_SepDb-ZIET_VAR | Variables B17, CapIntermitt C13/C26 + RHS headers | Sum | VAR system balances R_S AllRegions, UC_RHSRT(S) -> UC_RHST(S) |
| " | Variables D43 | Link | UC_VAR4_IMP (variable import) excludes internal links `-TB_*` |
| " | Utilisation (2) B2 | per plant | UC_VARU_* identities R_E AllRegions (was R_E FI after reg_feasible) |
| Scen_SepDb-ZIET_VAR_Stor | UC_VAR2_EXC B7, D122; UC_StorageCompetition C32 + RHS headers | Sum | excess/utilisation/storage balances R_S |
| " | UC_VAR2_EXC column O (22 cells) | Copy | coefficients written in the FI column (nuclear `EN*` PASTI etc.) to Allregions |
| " | UC_VAR2_EXC P104 | Copy | CEFF of the LowAF twins in every region |
| Scen_UC-ELC | DESERTEC B3 + RHS | Sum | non-decreasing RES capacity national |
| " | Coal ELC Share A2, H4 + RHS; **A24:E26** (green) | Sum + link | coal share national; `UC_IRE-I` = -UC_COMPRD on `TB_ELCHIG_*` (internal imports are not production) |
| ScenTrade__Trade_Links | **FI internal trades power** (new) | Link | 220 links FI <-> region (ELCHIG 19, ELCSOL 19, GreenCert-ELC 19, ELCWIN 18, ELCCO2N/ETSCO2/ELCDST/ELCHFO/HETHTH 17, ELCHYD 16, ELCCOL/ELCGAS 13, ELCWOO 10, ELCCOH 5, ELCNUC 3) |

`tools/reg_feasible.py` no longer re-switches UC_Sets lines that already carry a switch.

Colours: blue = switch; orange = key split; green = Reg-only table/rows; yellow = needs better data.
Legend on each touched workbook's `Region_selection` sheet (B30:C34). Five workbooks received a
`Region_selection` sheet (copied from ScenTrade_TradeParameters, mode FINTIMES), so
`select_model.xlsm` flips them too.

## 2b. Checks after writing (local, headless)

| Check | Result |
|---|---|
| Single-region mode, every table xl2times reads from the 99 workbooks (before vs after, `x_old`/`x_new` raw tables) | **identical** (0 tables changed) |
| Every formula of the HEAD version still present and unchanged outside the planned cells (`tools/formula_diff.py`) | 8/8 workbooks OK, no new external links |
| `select_model` flip of a copy to Reg-FINTIMES (`tools/model_mode.py set`), xl2times DD of the full group (FI + 19) | PRC_MAP: `EEPP_windOFF` only in FI196 and FI1D7; nuclear units only at their sites; 238 `TB_*` links (220 new + 18 pilot) |
| NCAP_PASTI summed over regions vs single-region FI (253 entries) | **conserved exactly** |
| UC region sets | VAR/VAR2/VAR3/utilisation/NonDecr/coal share: UC_R_SUM; UC_VARU_*: UC_R_EACH in every region |
| LowAF twins / dummies | twins only in their plants' regions; LowAF_DumBase/DumPeak in FI + 12 regions |

xl2times limitations (not model errors): it resolves AllRegions-vs-region columns at random (it
already drops hydro STOCK years in the unchanged single-region model, while VEDA's DD files have
every year), and it writes no `UC_IRE` terms (also none for the steel pilot's MISRIR correction
that VEDA writes) and no UC terms with `Attrib_Cond`. These parts are checked in the VEDA DD
files of the server run.

Incident while applying (fixed): the hydro split formulas were first written before their
`Reg_Keys` sheet existed (Excel turned the name into an external link). A cleanup step then also
broke BY_Trans' own links and turned 48 formulas into values. BY_Trans was restored from git and
re-applied, with new sheets now written before cell edits and only stray links removed.
`tools/formula_diff.py` confirms no formula was lost.

## 3. Keys (Split rule)

`data/keys/power_<key>.csv` from the Energy Authority power plant register (2026; 2019 for
retired plants), sited by municipality and OSM, mapped to the official NUTS-3 polygons
(`tools/power_register.py`, `tools/power_keys.py`, documented in `audit/power_keys.md`). Each key
has 19 shares that sum to exactly 1; the `Reg_Keys` sheets repeat them with a sum column.

| Class | Key | Regions |
|---|---|---|
| EUHYDDAM00 | hydro capacity | 16 |
| EEPP_windON / windOFF / PV | wind onshore / offshore / solar capacity | 19 / 2 / 19 |
| ECHP_* (coal, lignite = peat, biomass, HFO, LFO) | CHP capacity by fuel | 4-17 |
| ECHP_naturalgas_* | gas CHP | 5 |
| EEPP_coal / lignite (peat) | condensing plants | 1 (FI196) / 1 (FI1D9) |
| EEPP_naturalgas_*, EEPP_HFO, EEPP_LFO, EEPP_biomass | condensing / reserve plants | 3-12 |
| Nuclear | site | Loviisa FI1B1, Olkiluoto FI196, Pyhajoki FI1D9 |

## 4. Open points (yellow) and what Jack/Padam should check in the first VEDA sync

1. **AF profiles** of wind, PV and hydro are national profiles copied to every region (step 7:
   reV/ENSPRESO capacity factors per region).
2. **VEDA syntax to confirm in the DD files after the sync** (xl2times cannot check these):
   - `~FI_Process` Region cell with a comma-separated region list (e.g. `FI196,FI1D7`):
     `base.dd` must contain `PRC_MAP`/`TOP` lines for `EEPP_windOFF` in FI196 and FI1D7 and none in FI;
   - region header cells that are `""` in FINTIMES mode end the table there (same pattern as
     task 0 and the steel pilot).
3. `UC_VARI_ELE_Cons_Cap` stays an FI identity. Its UC_COMCON at FI counts exports to the regions,
   which are close to zero while demand stays in FI. It must become national with link corrections
   when demand moves (step 5).
4. Existing classes have no investment cost and only the year-0 code on NCAP_BND (same in the
   single-region model). Investment there is not blocked explicitly in either model.

## 6. First server run (2026-11-16, Baseline-Reg, FI + 19): infeasible -> fixed (`tools/task3_vedafix.py`)

Diagnosed by solving the server's DD files locally (CPLEX conflict refiner) and comparing every
regional DD entry with the prototype s4:

| Finding | Cause | Fix |
|---|---|---|
| Conflict: `RS_NCAP_ENFI_OLKILUOTO-3_FX` (2023) needs 1.6 GW, but OL3 cannot be built in FI196 | ELCNUC, ELCHIG, ELCCOL, ELCGAS, HETHTH, ... declared only in FI (SysSettings `Comms`, Region = `FI`). VEDA drops every TOP, PRC_ACTUNT, FLO_EMIS and trade link that names a commodity the region lacks: none of the moved plants had inputs or outputs, and 186 of the 220 new links were missing | 12 Region cells -> `=IF(SEL,"FI",TEXTJOIN(all regions))` (blue), same formula the model already uses for ELCCO2N, INDCOA, ... |
| ELCCO2N, ETSCO2 (and GreenCert-ELC once declared) had no balance in the regions (ENV, LimType N) | a region could keep its CO2 / certificates instead of sending them to the hub, where caps, taxes and certificate rules sit | hub rows `FI` only in Reg mode (blue); Reg-only rows Comms!V75:AA77 (green) declare them in the 19 regions with LimType FX |
| 2030 coal phase-out (`Scen_KILL_CoalPhaseOut2030`, CAP_BND UP 0) only in FI | value written in the FI column | O4, O6 = FI value in Reg mode (AllRegions, Copy rule); Region_selection sheet added |
| `tradeparameters.dd` not in the run; `demand_com-fr` instead of `demand_com-fr_sami` | case Baseline-Reg uses a different scenario list than the single-region `baseline-new` | run the regional case with the same scenarios as the single-region case (incl. TradeParameters, RegSum_Base) |

Check before writing: the fix was emulated in the server's DD files (declarations in the regions,
the moved plants' TOP / activity groups / FLO_EMIS, the 186 links, FX for the regional ENV
balances, coal phase-out, link costs, and the moved plants' terms in the national UCs that VEDA
had dropped with the commodities: UC_VARI_MINDISP, UC_VAR2/3_*, UC_CoalBANforHEATING,
UELC_UpShare-CoalELC, AU_ELC_HYD) and solved locally with the same scenarios as the single run
(demand_com-fr_sami, TradeParameters): barrier objective **1,529,545.6 M EUR** vs single-region
1,529,919.9 (-0.024 %, the same gap as the empty-region skeleton before step 3, 1,529,541.8);
no dummy imports, COM_PROJ and NCAP_PASTI conserved. Without those UC terms the emulation was
1.6 % too cheap, i.e. VEDA must write them after the fix: check `UC_FLO` lines of
UC_VARI_MINDISP for regional plants and `UC_R_SUM` with all regions in the next DD files. `check_run.py` now ignores year 0 of NCAP_PASTI
(interpolation code, was counted once per region).

## 5. Server run

1. Pull branch `reg/full`. Open `select_model.xlsm` and switch to Reg-FINTIMES, then
   **sync all files** in VEDA.
2. Run the regional case with the full group (FI + 19 regions, scenario `RegSum_Base` included).
3. Switch back to FINTIMES, sync, and run `Baseline`. It must reproduce the previous single-region objective.
4. Push both GDX files and the `GAMS_WrkTIMES` folder. The checks: `check_run.py`, the DD
   comparison with the prototype (`tools/dd_regionalise.py --step3`), and point 2 above.
