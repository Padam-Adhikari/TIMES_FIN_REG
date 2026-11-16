# Task 4 (industry): single industrial sites to their regions — audit and design

Status: audit and keys done (read-only); tool `tools/task4_industry.py` next. Nothing in the model changed yet.

## 1. Data

| What | Source | Tool / file |
|---|---|---|
| Industrial installations (111): name, address, activity, NACE, coordinates, verified emissions and free allocation 2008-2024 | EU Transaction Log (EUTL) via the open EUETS.INFO API (J. Abrell) | `tools/industry_register.py` -> `data/sources/eutl_FI_industry.csv` |
| Region of each installation | coordinates in the official maakunta polygons (`data/sources/maakunta_2026_wgs84.geojson`); checked against the postal town; 3 geocoding errors corrected by hand (Porvoo refinery, Metsä Board Kaskinen, Sotkamo) | same |
| Regional keys | free allocation 2013-2020 (EU product benchmark x historical production) per region and sector | `tools/industry_keys.py` -> `data/keys/ind_*.csv`, `audit/industry_keys.md` |
| Autoproducer CHP / power keys | Energy Authority power plant register (step 3) | `data/keys/power_CHPAUTOGEN*.csv` |

Why free allocation: within a sector it is proportional to production, and it also covers pulp and paper,
whose verified emissions are mostly biogenic (not reported). Each key has 19 shares >= 0 summing to exactly 1.

## 2. Where the industry data sit in the model

- `VT_FINTIMES_IND.xlsx`: 207 processes declared on `Processes` (+ AutoProd-CHP/ElcOnly, B-Y ICM Nordics),
  Region `FI`; data in long `~FI_T` tables (TechName, Attribute, CommName, generic `2010` column, calibrated
  `FI` column). The `FI` column holds the Finnish calibration (input coefficients) and the base-year stock
  (`STOCK` -> `PRC_RESID`).
- `VT_FINTIMES_SUP.xlsx`: refinery `SSCDRFLX00`, coke oven `SSCDCOKE00`, refinery heat `SUPREFHTH00`
  (`ProcComm`, `VEDA Tables`, `Flexible Refinery`; activity bounds on FI, national sums since task 0).
- `SubRES_22_TECHS_BIOREFINERIES`: HVO unit `BRF1_HVO` (Neste Porvoo, UPM Lappeenranta).
- Steel pilot (task 1): `IISBLAFUR00`, `IISCOREXP00`, `IISCYCFUR00` in FI1D9 (Region cells + table header switch).

## 3. Design

For a process that moves:
1. **Declaration**: its `~FI_Process` Region cell becomes, in Reg mode, the list of its regions — plus FI for
   processes split over several regions (FI keeps the calibrated coefficients, stock 0), only the site
   region for single sites.
2. **Data**: a Reg-only sheet `Reg_IND` (green) with one `~FI_T` table, one row per calibrated `FI` cell of a
   moved process and one column per region. Every value is a formula on the original `FI` cell:
   coefficients copied (Copy rule), `STOCK` x regional share (Split rule, orange). The original tables stay
   the single source; single-region mode reads nothing new.
3. **FI stock** of split processes -> 0 in Reg mode (switch formula, blue); single sites: the table's `FI`
   header switches to the site (as in the steel pilot) when the table holds only that site's processes.
4. **Product demand** (COM_PROJ of the sector's products) split with the same key (Split rule): production
   of Finnish heavy industry is where the mills are; a single national demand on the hub would make the
   regional distribution of future production arbitrary (equal-cost alternatives).
5. **Links** hub <-> region for every fuel/material the moved processes use and for products that are not
   split, read from the DD files after a sync; commodity declarations in the regions checked first
   (lesson of task 3: VEDA silently drops topology on undeclared commodities).
6. **Constraints**: industry UCs (`Scen_UC-IND`, route shares, CCS limits, ...) checked with
   `tools/regional_scan.py` (FI-only constraints over moved processes) and made national (R_S AllRegions)
   where needed; attributes that spread with the commodity declarations (COM_IE, COM_TAXNET, FLO_EMIS by fuel,
   PeakTS) checked as in task 3.

## 4. Treatment by process

| Processes | Stock (base year) | Region(s) | Basis |
|---|---|---|---|
| Refinery `SSCDRFLX00`, refinery heat `SUPREFHTH00`, refinery-gas CHP/power `CHPAUTOGENRFG00`, `EAUTOGENRFGD00` | activity bounds | FI1B1 Porvoo | Neste Porvoo; Naantali (FI1C1, ~10 % of phase-3 refinery allocation) closed 2021 — **decision: all in Porvoo** (yellow) |
| HVO `BRF1_HVO` | PASTI | FI1B1 / FI1C5 | Neste Porvoo NEXBTL and UPM Lappeenranta by vintage (yellow: capacities from company data) |
| Coke oven `SSCDCOKE00` | activity bounds | FI1D9 | SSAB Raahe |
| Steel BOF `IISBOXFUR00`, `IISBOXSCR00`, sinter `IISSINTER00`, pellets `IISPELLET00`, DRI/cupola (stock 0) | 2.75 / 3.71 / 1.86 Mt | FI1D9 | SSAB Raahe integrated works (with the pilot BF route) |
| Ferrochrome `IISFECRFR00`, AOD `IISAODFUR00` | 0.28 / 1.27 Mt | FI1D7 | Outokumpu Tornio |
| EAF `IISELAFUR00` | 0.25 Mt | key `ind_iis_eaf`: FI1D7 93.5 %, FI1C5 6.5 % | Tornio, Ovako Imatra |
| Finishing `IISFINPRO00`, steel heat `INDIISHTH00` | 4.23 Mt | key `ind_iis`: FI1D9 79.9, FI1D7 16.9, FI1C2 2.1, FI1C5 1.2 % | Raahe, Tornio, Hämeenlinna, Imatra |
| Cement `ICMFI_PARA_*` / `ICMFI_LAPP_*` | 10 Mt-scale kiln | FI1C1 / FI1C5 | Finnsementti Parainen / Lappeenranta (site-named processes) |
| Generic cement `ICM*` (stock 0) | 0 | key `ind_icm` | |
| Lime `ILM*` | 0.35 Mt | key `ind_ilm`: FI1D9 35, FI1D7 34, FI1B1 13.5, FI1C1 9.8, FI1DA 5.1, FI1C5 2.4 % | Nordkalk, SMA Mineral sites |
| Copper `ICU*` | 0.05 Mt | FI196 | Boliden Harjavalta (and Pori) |
| Hollow glass `IGH*` | 0.30 Mt | FI1C7 | Karhula packaging glass (closed 2021) — yellow |
| Chemicals `ICH*` | | key `ind_ich`: FI1B1 77.7, FI196 19.7, FI1C5 2.4, FI1DC 0.2 % | Porvoo petrochemicals, Harjavalta, ... |
| Ammonia / fertiliser `IAM*` | 0.004 Mt | key `ind_iam`: FI1C1 52, FI1DB 48 % | Yara Uusikaupunki, Siilinjärvi |
| Pulp and paper `IPP*`, pulp-mill heat `INDIPPHTH00`, black-liquor CHP `CHPAUTOGENBLQ00` | 11.8 Mt paper, 9.5 Mt chem. pulp | key `ind_ipp` (49 mills): FI1C5 15.9, FI1C7 15.8, FI196 10.1, FI1D7 8.8, FI1D9 8.5, FI19B 8.4, FI198 8.2, FI19A 7.4, FI1B1 5.7, FI1DB 5.1, ... | |
| Autoproducer CHP / power `CHPAUTOGEN*`, `EAUTOGEN*` | | keys `power_CHPAUTOGEN*` (step 3 register) | |
| **Stays on the hub (step 5)**: generic sectors `INF*`, `INM*`, `IOI*`, aluminium recycling `IAL*` | | key from regional manufacturing statistics | mostly small non-ETS sites; ETS installations are not representative |
| **Stays on the hub**: chlor-alkali `ICL*` (0.1 Mt) | | | no production proxy in the register (yellow) |
| **Stays on the hub**: industrial fuel techs `IND*00`, non-energy use `NEU*` | | | supply side; fuels reach regions over links |
| **Step 8**: LNG terminals (Inkoo, Hamina, Pori, Tornio) | | | LNG is an import (external link): home regions decided with the other external links; no effect while gas is a national copper plate |

## 5. Checks planned

- Local first: emulate the VEDA output on the server's DD files, solve, `tools/audit_run.py` vs the
  single-region run (objective, PRC_RESID / NCAP_PASTI / COM_PROJ conserved, production by sector,
  emissions, no dummy imports), `tools/regional_scan.py` on the DD files after the sync.
- `check_run.py` and `tools/audit_run.py` now also conserve `PRC_RESID` (base-year stock), the attribute
  that carries almost all industry capacity.

## 6. Open points (yellow)

1. Naantali refinery (closed 2021) placed with Porvoo.
2. HVO capacities by site (Neste Porvoo / UPM Lappeenranta) from company reports.
3. Karhula hollow glass (closed 2021) — the base-year stock stays there; decline follows the model.
4. Chlor-alkali (`ICL*`) on the hub until a production proxy is found.
5. Generic industry (`INF*`, `INM*`, `IOI*`, `IAL*`) in step 5 with regional manufacturing statistics.

## 7. Phasing (one sector group per server run)

| Part | Content | Status |
|---|---|---|
| 4a | rest of steel (Raahe FI1D9, Tornio FI1D7, EAF Tornio/Imatra, finishing by site), refinery + refinery heat + refinery-gas CHP (Porvoo FI1B1), coke oven (Raahe), HVO (Porvoo / Lappeenranta by vintage), copper (Harjavalta FI196), glass (Karhula FI1C7) | applied (`tools/task4_industry.py`), checks below; server run pending |
| 4b | pulp and paper, lime, chemicals, fertiliser, black-liquor CHP; product demand split with the same keys together with the regional availability of the sectors' new technologies | next |
| 4c | cement site chains (incl. SubRES 10 new site technologies, `diversified_cement`) | after 4b |

In 4a the product demands (steel, copper, glass, refinery products) stay on the hub and products are linked:
the sectors' new technologies are still available on the hub only, so a split demand could not grow.

## 8. 4a implementation (`tools/task4_industry.py`, dry run `audit/task4a_dryrun.txt`)

- **switch** (whole data table belongs to one site; process declared only there): copper `IAL ICU INF`!G188 -> FI196,
  glass `ICM ILM IGF IGH INM`!G236 -> FI1C7, coke oven SUP `VEDA Tables`!I39 -> FI1D9, refinery SUP
  `Flexible Refinery`!K25 -> FI1B1 (+ refinery heat). The activity bounds move with the data; the national
  sums `RS_ACT_SSCD*` (task 0) stay consistent.
- **copy** (steel table `IIS`!E52/E219 holds processes for several regions; refinery-gas CHP shares a table
  with hub processes): declared on FI + regions; new sheet `VT_FINTIMES_IND`!`Reg_IND` with one row per
  calibrated FI cell (formulas on the original cell; stock x share in orange). FI's own stock row becomes a
  VEDA comment row in Reg mode (TechName `*...`): the stock cells are chained formulas (e.g. AOD stock =
  finishing stock x share), so they are not modified; where a comment row is followed by continuation rows
  the process name is repeated in Reg mode.
- **HVO**: `SubRES_22_TECHS_BIOREFINERIES_Trans`!`Reg_HVO`: AVA FI 0, FI1B1 1, FI1C5 1; NCAP_PASTI 2007/2009
  200 kt in FI1B1, 2015 120 kt in FI1C5 (vintages of the SubRES = Neste NEXBTL 1/2, UPM BioVerno).
- **UCs national** (R_E FI -> R_S AllRegions, UC_RHSRT* -> UC_RHST*, FI coefficient columns -> AllRegions):
  `Scen_UC-IND` UC-IIS (steel route shares), CHPShares (autoproducer CHP shares), `Scen_REFINERIES_Lim` UCT4.
- **Commodities**: 52 commodities used by the moved processes declared in every region (SysSettings Comms,
  switch formula). Their spreading attributes checked: COM_TAXNET surplus penalties (equivalent), COM_PROJ
  stays on FI, COM_AGG of IND fuels (see next point).
- **Links**: 101 new (sheet `FI internal trades industry`), 9 already defined by the pilot / power links skipped.
- **Double counting fixed (also an existing pilot issue)**: INDCOA, INDCOB, INDCOG, INDCOK, INDGAS, INDBFG
  have an FX balance; their aggregates INDFINSOLID / INDFINGAS count gross production (VAR_COMPRD, which
  includes internal imports, eqcombal.mod). The national production sums RS_PRD_INDFINSOLID_* and
  RS_PRD_INDFINGAS_* (task 0) therefore counted fuel sent to FI1D9 twice. `Scen_ZATEMP_Calibration`!RegSum
  rows 87-110: UC_IRE-I = -UC_COMPRD x COM_AGG on TB_<component>_* (24 rows).

Checks after writing: every HEAD formula unchanged in the 8 workbooks (52,000+), no external links;
single-region mode: xl2times reads identical tables from all 138 workbooks (0 changed).
Regional check (copy flipped to Reg-FINTIMES, xl2times DD for FI + 19): stocks at their sites and split
exactly (finishing FI1D9 3.379 / FI1D7 0.716 / FI1C2 0.087 / FI1C5 0.050 = 4.2315; EAF FI1D7 0.234 /
FI1C5 0.016; AOD, ferrochrome FI1D7; BOF FI1D9; copper FI196; glass FI1C7); FI copies without stock
(comment rows work); refinery, refinery heat and coke oven declared only at their site. Not verifiable
with xl2times (checked in VEDA's DD files after the sync): topology of the IND-table processes (xl2times
shows none, also for the validated pilot blast furnace) and the HVO vintage split (formula-bearing
~TFM_INS is skipped by xl2times).

## 9. First 4a server run (2026-11-16) and the corrections

Server run `runs/reg_baseline-sami_2026-11-16_task4a.gdx`: optimal, no dummy imports, COM_PROJ /
NCAP_PASTI / PRC_RESID conserved, objective 1,535,236.42 = **+0.35 %** vs the single run
1,529,919.88 (before 4a: -0.024 %). Audit `audit/run_task4a.md`. Diagnosed by comparing every
parameter of every moved process (single FI vs its site) and by local solves of the server DD files
with each correction (TIMES 4.8.3, CPLEX barrier):

| # | Defect (4a) | Effect | Correction (`tools/task4_industry.py --step insert`, `--step fix`) |
|---|---|---|---|
| 1 | Copy-mode plants (13 `*00` steel processes + refinery-gas CHP) kept a declaration on the hub without stock or capacity cost. TIMES (`pp_reduce.red`, REDUCE=YES) gives such a process **no capacity variable** | free, unlimited converter/finishing/sinter/cupola/CHP on the hub (new audit check K) | declared only at their sites |
| 2 | Route-share fills `FILL-IIS` (crude steel) and `FILL-IALICU` (copper) read stocks of region FI only | all shares 0: scrap route capped at 0 (no new EAF), copper >= 99 % primary lost | fills read every region (as the pilot's MISRIR table), shares from the sum; copper constraint national; `UC_IRE-I` corrections on `TB_MISCST_*`, `TB_MCUSCU_*` |
| 3 | Aggregates `INDFINSOLID`, `INDFINGAS` declared on the hub only, so `COM_AGG` and the `RS_PRD_*` production term existed only there, while the 4a `UC_IRE-I` corrections subtracted regional imports | coke delivered to Raahe penalised by the LO dual (121 EUR/unit in 2015): sinter, pellets, FeCr idle at their sites | aggregates declared in every region (SysSettings) |
| 4 | VEDA lets the original table's generic `2010` value beat the `Reg_IND` copy of the calibrated FI value | AOD, EAF, FeCr at their sites with generic coefficients | generic cells of copied rows blank in Reg mode (9 cells) |
| 5 | Refinery table column `FI~LO` (lower output shares) not switched | Porvoo free to choose its product mix: 2-7x activity 2030-2050, +21,000 MEUR crude imports | header `FI1B1~LO` in Reg mode |
| 6 | `NETSCO2` (non-ETS CO2) not declared in the regions | copper's non-ETS emissions dropped | Reg-only declaration row (as ELCCO2N/ETSCO2 in task 3) |

Not losses (checked): `FLO_BND` UP 0 on `INDCOL` (no such input), `FLO_PKCOI` of refinery heat (heat
peak only on the hub since task 3), `ACT_BND` (national-sum UCs since task 0). Pending for step 7:
`UC_DecrCCSIND` (hub-only zero-RHS constraint on industrial CCS; lost the Raahe CCS blast furnace;
not binding in either run).

Local emulations of the corrections on the server DD files (objective vs single):
1 alone -0.47 %; 1+2 +0.69 %; 1+2+3 (aggregates declared only) +0.69 %; + RS_PRD terms in the
regions and 4: +0.27 %; + 5 and 6: +0.43 %. Steel 2010-2025 and the refinery now match the single
run; still open: after 2030 hydrogen DRI replaces EAF and BF-CCS (being diagnosed by fixing the
single-run steel activity and asking CPLEX for the conflict).

Applied 2026-11-17 (with approval): `--step insert` (10 empty rows at `Scen_UC-IND` `UC-IIS` row 24,
the UP table moves to rows 37-42) and `--step fix` (206 cells in 4 workbooks: Scen_UC-IND 176,
SysSettings 7, VT_FINTIMES_IND 22, VT_FINTIMES_SUP 1; dry run `audit/task4a_fix_dryrun.txt`).
Checks: every edited cell keeps its single-region value after recalculation; single-mode raw tables
of the whole model (xl2times) identical to the last commit (only the moved `UC-IIS` table changed its
address, content identical); no formula lost or changed outside the plan in the 4 workbooks.

Not yet in the workbooks (no effect in the local tests, kept for step 7): `UC_DecrCCSIND` as a
national sum (tested: objective unchanged); `UC_IRE-I` corrections for `UCI_UP_CHPShare-*` and
`TUC_MinShareofCenELCinINDELC` (not binding). Growth constraints `UC_Growth_*` are R_S with FI only.
