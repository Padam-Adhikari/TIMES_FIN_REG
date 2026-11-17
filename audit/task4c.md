# Task 4c: cement to its sites — audit and design

Status: applied 2026-11-17 (`tools/task4_industry.py --step 4c`, dry run `audit/task4c_dryrun.txt`); server run pending.
Builds on 4a/4b and their lessons (`audit/task4_industry.md` section 9, `audit/task4b.md` sections 6-7).

## 1. The cement chain in the model (Baseline-Sami)

| Part | Processes | Where defined | Data today |
|---|---|---|---|
| Parainen existing plant (Finnsementti, FI1C1) | `ICMFI_PARA_E_DRY` (clinker kiln), `_E_FIN` (cement mill), `_E_FUR_CON` (kiln furnace) | `VT_FINTIMES_IND` / `B-Y ICM Nordics` (tables `~FI_T:FI` at D3 and O49, declarations `~FI_Process` Z3) | stock 1.53 Mt clinker, 1.9 Mt cement, 10 PJ furnace |
| Lappeenranta existing plant (Finnsementti, FI1C5) | `ICMFI_LAPP_E_DRY/_E_FIN/_E_FUR_CON` | same sheet | stock 0; `Scen_Diversified_Cement` sets `NCAP_START 2100` on `*LAPP*` (switched off in this case) |
| New site technologies | `ICMFI_PARA_*`, `ICMFI_LAPP_*` (dry/CaL/oxy kilns, furnaces, LC3, clay, CCS, `DUMMY1/2`) | SubRES_10 (`10_techs_chp_sup_ind.dd`), FI only today | — |
| New generic plants | `ICMFI_GEN_*` (bypass/CCS-ready clinker, furnaces, CCS) | SubRES_10 | `NCAP_START 2025` |
| Emission aggregators | `ICMFI_EMIS` (`ICMFICO2N/P` -> `ICMFICO2`), `ICMFI_CAPTURED` (`ICMFISCO2N/P` -> `ICMFISCO2`) | SubRES_10 | — |
| Cement mix to demand | `ICMFI_ICM` (`ICMPARA`, `ICMLAPP`, `ICMLC3`, `ICMBYF`, `ICMCCSC` -> `ICM`) | SubRES_10 | demand `ICM` (COM_PROJ, FI) |
| Clinker backstop imports | `CLKPARABkStp`, `CLKLAPPBkStp` (IRE, `IRE_PRICE` 918 EUR20/t) | SubRES_10 | external imports |
| Old generic processes | `ICMDRYPRD00`, `ICMWETPRD00`, `ICMFINPRO00`, `ICMPRC*00` | `ICM ILM IGF IGH INM` sheet | stock 0, `NCAP_START 2070` (FI): no activity |

Key `ind_icm` (EU ETS free allocation 2013-2020, `data/keys/ind_icm_2013-2020.csv`): FI1C1 57.9 %, FI1C5 42.1 %
= the two Finnsementti clinker plants (Parainen, Lappeenranta).

Flows that cross the site boundary: clinker between the sites (`ICMFI_PARA_*_FIN` uses `MCMCLKLAPP`, the
Lappeenranta mill `MCMCLKPARA`; `FLO_DELIV` 40 000 EUR/t until 2023, 400 after), blast-furnace slag
`MISBFS` (steel), the five cement products to `ICMFI_ICM`, fuels and electricity, captured CO2
`ICMFISCO2` to the CO2 store `STORAGE_INDS` (hub).

## 2. Constraints and data touching cement

| Item | Now | Treatment |
|---|---|---|
| `cementCO2` (`Scen_Diversified_Cement`): `UC_COMNET` `ICMFICO2` >= 900 / 847 kt | national (`UC_RHSTS`), terms in all 20 regions | unchanged: a net term needs no link correction |
| `UC_DecrCCSICM` (CCS ramp-up, `GROWTH ACT`) | national since 4b, coefficients `AllRegions` | unchanged: follows the processes (as `UC_DecrCCSIND` for pulp and Raahe CCS) |
| `TUC_UP_CHPAUTO-INDCO` term `ICMHTH` | new industrial CHP on the hub | not a cement process; unchanged |
| Scenario data (`ZUESR` FLO_EMIS, `ZUEmisCO2`, `Diversified_Cement`, `ZUILED`, DRATE, coal `FLO_BND` 0) | `AllRegions` tables | follow the processes |
| `BY_Trans` / `ICM NCAP_ACTBND` | `NCAP_BND` interpolation `AllRegions`; `NCAP_START 2070` for `ICMDRY*`, `ICMFUR*`, `ICMFIN*` on FI | follow / old generic stay on the hub |
| `COM_TAXNET` 2000 on `M*` materials, NRG `*PRC` (`BAU-General`, `AllRegions`) | | applies in every region, unchanged |
| `INDCO2` (aggregate `ICMFICO2`, `INDCO2N`, `INDCO2P` -> `INDCO2`) | FI only; `COM_BNDNET LO -9999999` (no bound) | reporting only; step 7 (already true for 4b industry) |

`tools/uc_ire_scan.py` (new, read-only): no national `UC_COMPRD`/`UC_COMCON` term on any commodity that
cement will link (clinkers, slag, products, fuels, electricity) lacks its correction. It finds three older
terms: `UCI_UP_CHPShare-ICL`, `-ICU`, `-IIS` (sector heat linked since 4a; the CHP-share upper limits count
heat imported over `TB_ICLHTH/ICUHTH/IISHTH_*` twice, which loosens them). Corrected in this step (rows
20-22 on `Scen_UC-IND` / `CHPShares`, same pattern as rows 13-14 and 19).

## 3. Design (scientific basis)

1. **Each existing plant to its site** (plant register: Finnsementti Parainen FI1C1, Lappeenranta FI1C5):
   declarations switched; the two mixed `~FI_T:FI` tables (PARA and LAPP rows) are disabled in Reg mode
   and copied per site to a new sheet `Reg_ICM` (`~FI_T:FI1C1`, `~FI_T:FI1C5`, every cell a formula on the
   original). No hub copy (4a lesson). Lappeenranta stays switched off by the scenario (not changed).
2. **New site technologies at their site** (PARA FI1C1, LAPP FI1C5); **new generic plants** and the two
   emission aggregators in the key regions (FI1C1, FI1C5: existing quarries/kiln sites); off on the hub.
3. **Cement demand stays national on the hub** (`ICMFI_ICM` + `ICM`), products linked. Basis: cement is
   sold on a national market and used where construction happens (step 5 spreads demand), unlike pulp
   and paper, whose demand follows the mills (4b). The site chains are distinct processes, so no
   degenerate placement arises.
4. **Links hub <-> FI1C1 / FI1C5**: both clinkers (cross-use between the sites goes via the hub), slag,
   the five products, fuels/electricity as needed, captured CO2 `ICMFISCO2` (store on the hub, as
   `INDSCO2N` for Raahe). Process heat, clay, generic clinkers and site CO2 stay inside the region.
   Emission commodities declared in all regions; cement CO2 counted where emitted (`TOTCO2` in every
   region, `cementCO2` national).
5. Clinker backstop imports stay on the hub (external imports, step 8).
6. CHP-share corrections (section 2).

## 4. Checks

Dry run reviewed first; after apply `tools/regmode_check.py` (0 Reg-only errors), single-mode raw tables
unchanged; after the sync `tools/uc_ire_scan.py` on the new DD files (0 terms), then the server run:
`check_run.py`, `tools/audit_run.py` (incl. K), parameter comparison of every moved process, national
activity of the cement chain vs the single run.

## 5. Applied (2026-11-17)

214 cells in 4 workbooks + new sheet `VT_FINTIMES_IND`/`Reg_ICM` (251 cells) + regenerated link sheet
(394 links = the 376 of 4a/4b + 18 new; the tool stops if any earlier link would be lost).
Two tool fixes found by the dry run: the new-technology finders read every region's topology (after 4b
the 4b technologies are no longer on the hub; without this 26 biogas/4b links would have been dropped),
and `plan_prd_corrections` recognises its own Reg-only header (`RegSum!P7`).
Checks: `tools/regmode_check.py` on the 5 workbooks: 0 Reg-only error cells (`VT_FINTIMES_IND` has 67
error cells in single mode, unchanged from before 4c); single-mode raw tables of the whole model identical
to the last commit (xl2times `--only_read`).
After the sync: `python tools/uc_ire_scan.py` on the new DD files must report nothing.
