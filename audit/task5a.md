# Task 5a: generic industry, non-energy use and agriculture — audit and design

Status: applied 2026-11-17 (`tools/task4_industry.py --step 5a`, dry run `audit/task5a_dryrun.txt`); server run pending.

## 1. What moves

| Sector | Processes (where) | Demand 2010 (PJ) | Key (`data/keys/`) | Basis |
|---|---|---|---|---|
| Other industries `IOI*` (energy-service chain -> `IOIDEMAND00`) | 27 + `IOIOTH-NRG` (`VT_FINTIMES_IND`/`IOI`), new `IOI*01` (SubRES_10) | `IOI` 158 | `emp_ioi_2010`: employment by workplace, manufacturing excl. paper 17, refining 19, chemicals 20, minerals 23, basic metals 24 | the residual manufacturing (food, wood products, machinery, electronics, ...) is many sites; employment is the standard downscaling proxy where energy by branch and region is not published (ETS covers only a few large IOI plants: `ind_ioi` puts 85 % in five regions) |
| Non-ferrous metals `INF*` | 27 + `INFOTH-NRG` (`IAL ICU INF`), new `INF*01` | `INF` 20 | `emp_24nonsteel_2010`: basic metals 24 without the steel towns Raahe, Tornio, Imatra, Hameenlinna | nickel Harjavalta, cobalt/zinc Kokkola, Terrafame, Pori are not all ETS metal installations; steel is modelled as IIS at its sites |
| Aluminium `IAL*` | 5 (`IAL ICU INF`), new `IAL*01..10` | `IAL` 0.04 | `emp_24nonsteel_2010` | secondary aluminium / foundries with the other non-ferrous metals |
| Other non-metallic minerals `INM*` | 27 + `INMOTH-NRG` (`ICM ILM IGF IGH INM`), new `INM*01` | `INM` 14 | `emp_23_2010` | cement, lime, glass moved in step 4 are a small part of TOL 23 employment |
| Chlor-alkali `ICL*` | 4 (`IAM ICL ICH`), new `ICL*01/05` | `ICL` 0.19 | `emp_20_2010` (chemicals) | no production register; tiny demand (yellow in step 4, resolved with the chemicals branch) |
| Non-energy use `NEUDEMAND00` | `NEU` sheet | `NEU` 103 | `ind_ich_2013-2020` (Porvoo 78 %) | petrochemical feedstock (steam cracker) and refinery products used as feedstock |
| Agriculture, forestry, fishing `AGR_*-Tech`, fuel techs `AGR*00` | `VT_FINTIMES_AGR` | `AGR_Agr_For_Fis` 79 | `emp_A_2010` | employment in agriculture, forestry and fishing by workplace |

Keys: `tools/regional_keys.py` (`audit/keys.md`): employment by workplace municipality (Statistics Finland
tyokay/115h) summed to regions with the official 2026 municipality-region correspondence; regional totals
equal the national totals.

## 2. Mechanism (as 4b)

- Existing processes declared only in their key regions, data copied per region on `Reg_IND` / new `Reg_AGR`
  (stock x share), generic values of copied rows blank in Reg mode with Reg-only helpers for the formulas
  that read them (4b lesson, now in the same pass).
- Demand `COM_PROJ` split by the key on `Scen_ZUDemand_REF2016`/`Reg_Demand` (hub 0), 4b demands kept.
- New SubRES_10 technologies available in the key regions, off on the hub.
- Commodities declared in the regions; hub links for fuels, electricity and sector heat; links of 4a-4c kept
  (the tool stops if one would be lost).
- Sector heat (`IOIHTH`, `INFHTH`, `INMHTH`, `IALHTH`) crosses links while the autoproducer and new
  industrial CHPs stay on the hub (transitional, as 4b): `UC_IRE` corrections for the CHP-share limits
  `UCI_UP_CHPShare-IOI/INF/INM/IAL` (new Reg-only table on `CHPShares`). Other constraints of these sectors
  (`S_INFM/INMM/IOIM`, `TUC_LO_INMPRC/IOIPRC-*`, `TUC_UP_INMHET/IOIHET-INDCO`, `TUC_Istruc_ALU-*`) are
  already national with `AllRegions` coefficients and fills over all regions (4a/4b).
- `UC_VARI_ELE_Cons_Cap` (variable-RES module, hub only since task 0) loses agriculture's electricity
  as it lost industry's in step 4: rebuilt per region with step 3 wind/solar (step 7 list).

## 3. Repair of a 4b slip (no effect on results)

`plan_generic` re-wrapped 9 generic cells on `IIS` that 4a had already blanked
(`IF(single, IF(single, v, ""), "")`), and their 4bfix helpers (`IIS!Y71..Y135`) took the inner expression,
so they are empty in Reg mode. The formulas that read them (`IIS!P71..P130`) use the helper only when the
calibrated FI value in column G is empty, and it is filled on all these rows: no effect on any run. 5a
restores the single switch and the helpers' original values, and `plan_generic` skips cells that are already
switched.

## 4. Checks

Dry run; after apply `regmode_check` (0 Reg-only errors), single-mode raw tables unchanged, value check of
the regional copies; after the sync `uc_ire_scan` (0); server run: hard checks, audit (incl. K), parameter
comparison of the moved processes, national activity vs the single run.

## 5. Applied (2026-11-17)

7 workbooks: `VT_FINTIMES_IND` (declarations, regenerated `Reg_IND` with the 4a/4b rows + 5a, blanks with
helpers, 18 repaired 4b cells), `VT_FINTIMES_AGR` (new `Reg_AGR`, `Region_selection` sheet added - picked up
by `select_model.xlsm`, which switches every workbook with that sheet), `Scen_ZUDemand_REF2016`
(`Reg_Demand`: 4b + 5a demands, 156 rows), SubRES_10 `_Trans` (65 availability rows), `SysSettings`
(declarations), trade links (394 -> 893), `Scen_UC-IND` (`CHPShares` rows 28-33).

Apply problems and fixes (the model workbooks were restored from git before every retry; each successful
book was re-applied in the final single pass):
1. Excel crashed while saving `SysSettings` after four books in one session; one Excel instance per
   workbook (`apply_per_book`) showed the real error: "Save method failed" - Excel's temporary file was
   complete, the swap with the original was refused.
2. Cause: `tools/veda_tables.read_tables` left its read-only openpyxl workbooks open; the planning phase of
   the same Python process still held `SysSettings.xlsx` (Windows refuses to replace an open file). Fixed:
   `read_tables` closes both workbooks; the engine saves a copy (`SaveCopyAs`) and swaps it in after Excel
   has quit (`tools/task3_power.apply`), retrying while the lock clears.

Checks: `regmode_check` on the 7 workbooks: 0 Reg-only errors; single-mode raw tables of the whole model
identical to the last commit (xl2times); Reg-mode value of every cell on `Reg_IND` (260 rows), `Reg_AGR`
(23) and `Reg_Demand` (156) equals its single-mode source expression (copies and key shares).
