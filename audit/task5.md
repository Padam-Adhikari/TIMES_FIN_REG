# Step 5: demand and stocks to the regions — audit and phasing

Status: read-only audit 2026-11-17 on the DD files of the passing 4c run
(`runs/reg_baseline-sami_2026-11-17_task4c.gdx`). Nothing changed yet.

## 1. What is still on the hub (Baseline-Sami, 2010)

| Sector | Demand commodities (COM_PROJ 2010) | Existing stock on the hub | Notes |
|---|---|---|---|
| Residential | `R_DetH` 792, `R_SDetH` 599, `R_Flat` 1,108 (building services), `RLIG` 95, `ROEL` 18, `RREF` 8.7, `RCDR` 3.3, `RCWA` 4.5, `RDWA` 2.9 | 65 `R_E*` heating/appliance techs, 4 `Rdw*` building processes, `RSD*` | building-stock module `Scen_NewHouses_and_retrofits` (`Bldg_*`, old-stock UCs), retrofit setup |
| Services | 13 `NR_*` (offices, shops, hotels/restaurants, hospitals, sport, lighting, ventilation, refrigeration, ICT, street lighting) | 90 `C_E*`, 12 `NRb*`, `COM*` | |
| Transport | cars 132, heavy trucks 96, buses 17, vans 5.3, motorcycles 4.8, mopeds 2.6, rail freight 19 / passenger 5.1 + 4.0 + metro 1.0, aviation (domestic 6.3, intra/extra-EU), navigation 9.2, bunkers 101 | 28 `TRA*` | aviation, international shipping and bunkers are international: stay on the hub (external links, step 8) |
| Agriculture | `AGR_Agr_For_Fis` 79 | 1 | |
| Generic industry | `IOI` 158, `INF` 20, `INM` 14, `IAL` 0.04, `ICL` 0.19; non-energy use `NEU` 103 | `IOI*` 14, `INM*` 12, `INF*` 11, `IAL*` 2, `ICL*` 2 | 4a/4b left these on the hub (no ETS proxy) |

Energy carriers to these sectors are produced on the hub: electricity distribution
`ELCHIG -> ELCMED -> ELCLOW -> RSDELC/COMELC` (hub only), district heat `HETHTH` (17 regional CHPs send
heat to the hub over `TB_HETHTH_*`: a copper plate for heat) and its distribution to `RSDHET`/`COMHET`.

## 2. Constraints on these sectors

| Family | Source | Now | Treatment when the sector moves |
|---|---|---|---|
| End-use shares `RCUC-Lo/Up_R/C_ES-*` (min. electricity, max. district heat per end use), boiler limits `UC_R_SPLBoiler*`, `UC_R_UnitBoiler*` | `Scen_UC_RSD-COM` | `R_E: AllRegions`, coefficients in an `FI` column (~80 UCs) | national (`R_S`), coefficients `AllRegions` (4b mechanism `plan_ucs_general`); `uc_ire_scan` for link corrections |
| Heat-pump caps / minimum capacities `UC_RSD_*HPCAP*` | `Scen_UC_HeatPumps_MaxCAP/MinCAP_Lo` | national (task 0), `FI` coefficients | coefficients `AllRegions` |
| Old building stock `UCR_OldStock-*` | `Scen_NewHouses_and_retrofits` | national, `FI` coefficients | coefficients `AllRegions`; module studied in 5d |
| Calibration sums `RS_PRD_RSD*/COM*/TRA*`, `RS_FLO_*HETHTH*`, `RS_ACT_EEHP_DistHeating_LO` | `Scen_ZATEMP_Calibration`, `RegSum_Base` | national (task 0) | stay national; `UC_IRE` corrections where the carriers cross links (`uc_ire_scan`) |
| Transport shares `TUC_TRA_Car/Bus/Lcv-*`, EV/H2 sales `UC_*EV*`, `UC_CO2_Cars`, diesel min/max, vehicle batteries | `Scen_UC_TRA`, `Scen_TRA_EVPHEV_NewSalesBase`, `Scen_TRA_CO2_target` (`R_E: FI`), `Scen_TRA_SCENARIOS` | regional, `FI` coefficients | national, coefficients `AllRegions` (EU car CO2 standard and national sales targets are national) |
| Generic-industry shares `S_INFM/INMM/IOIM`, `TUC_LO_INMPRC/IOIPRC-*`, `TUC_UP_INMHET/IOIHET-INDCO`, `UCI_UP_CHPShare-INF/INM/IOI/IAL`, `TUC_Istruc_ALU-*` | `Scen_UC-IND` | national, `FI` coefficients | coefficients `AllRegions` + corrections (as 4b) |
| CO2 targets `CO2TargetESR2030`, `CO2TargetAllSectors2030FI` | | national, all regions | unchanged |
| Demand-side flexibility / storage `UC_VAR*`, `UC_*Batt*` | `Scen_SepDb-ZIET_VAR*`, `Scen_UC_STORAGE` | variable-RES module restricted to the hub in Reg mode (task 0) | rebuilt per region with step 3 wind/solar; batteries with their sector |

Lesson from 4b (`audit/task4b.md` section 7): before each move run `tools/uc_ire_scan.py --extra <carriers>`.

## 3. Regional keys (all public; `tools/regional_keys.py`, PxWeb)

| Key | Source | Use |
|---|---|---|
| floor area by region x building class x heat source, 2010 | Statistics Finland `raku/15f7` (Building stock: buildings and floor area by region, intended use, heat source, 2005-2025) | residential demand `R_DetH` (one/two-dwelling), `R_SDetH` (terraced), `R_Flat` (blocks of flats); services `NR_*` by use (commercial, office, care, assembly, education); existing heating systems `R_E*`/`C_E*` by heat source; district-heat demand |
| population 2010/2015/2020/2024 | `vaerak/11ra` (done) | appliances, lighting (`RLIG`, `ROEL`, ...), passenger rail, ICT, street lighting |
| vehicle stock by region and class | Traficom via Statistics Finland `mkan/11ic` (2011-2025; 2011 is the first year: documented) | cars, vans, lorries > 3.5 t, buses, motorcycles, mopeds (demand and `TRA*` stock) |
| value added by industry (TOL) and region | Statistics Finland `alyr/13x2` (2018-2024) | `IOI`, `INF`, `INM`, `IAL`, `ICL` (cross-check: `tene/12bw` energy use in manufacturing by region) |
| agriculture | Luke statistics (utilised agricultural area / greenhouse area by region) | `AGR` |
| special cases | metro: Helsinki (FI1B1) only; non-energy use `NEU`: petrochemical feedstock at Porvoo (key `ind_ich`) | |

## 4. Proposed phasing (one group per server run, as in step 4)

| Part | Content | Why in this order |
|---|---|---|
| **5a** | generic industry (`IOI`, `INF`, `INM`, `IAL`, `ICL`), `NEU`, agriculture | small, few constraints (`Scen_UC-IND` mechanism of 4b); finishes industry |
| **5b** | road transport (cars, vans, trucks, buses, two-wheelers) by vehicle stock; rail by population (metro FI1B1); aviation, navigation, bunkers stay on the hub | self-contained chain (`SUBRES_20`), ~30 constraints; carriers (fuels, electricity, hydrogen) linked from the hub |
| **5c** | services buildings (`NR_*`, `C_E*`, `NRb*`) by floor area and heat source | uses the `raku/15f7` key; end-use carriers `COMELC`/`COMHET` linked from the hub |
| **5d** | residential buildings (`R_*`, `R_E*`, `Rdw*`, appliances) incl. the building-stock and retrofit module | largest: own audit of `Scen_NewHouses_and_retrofits` before the dry run |
| **5e** | district heat local: each region's buildings served by its own CHP/heat-only boilers; the hub `HETHTH` copper plate removed | physically required (heat is not transported between regions); objective will rise and must be explained |

Transitional (documented in each part): electricity distribution stays on the hub and end-use carriers
(`RSDELC`, `COMELC`, `TRAELC`, fuels) reach the regions over hub links, as industry fuels in step 4.
Regional distribution follows with the grid work (step 3 grid / step 8).

## 5. Next actions

1. Extend `tools/regional_keys.py` with the keys of section 3 (checks: 19 shares sum to 1, regional total
   = national figure), write `data/keys/*.csv` and `audit/keys.md`.
2. Start 5a: audit of the generic-industry tables (`VT_FINTIMES_IND`), dry run.
