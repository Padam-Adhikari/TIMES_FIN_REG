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
