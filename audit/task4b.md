# Task 4b: pulp and paper, lime, chemicals, fertiliser to their regions — audit and design

Status: applied 2026-11-17 (`tools/task4_industry.py --step 4b`, dry run `audit/task4b_dryrun.txt`); server run pending.
Builds on 4a (passed 2026-11-17, -0.005 %) and its lessons (`audit/task4_industry.md` section 9).

## 1. What moves

| Sector | Existing processes (stock in the FI column) | Key (EU ETS free allocation 2013-2020) | New technologies |
|---|---|---|---|
| Pulp and paper `IPP*`, pulp-mill heat `INDIPPHTH00`, black-liquor CHP `CHPAUTOGENBLQ00` | 11 processes, 27 with stock in all 4b sectors (paper 11.8 Mt, chemical pulp 9.5 Mt, process heat 12 + 5.1 PJ, mill heat 4.7 PJ, BLQ CHP 0.13 GW) | `ind_ipp`, 13 regions: FI1C5 15.9, FI1C7 15.8, FI196 10.1, FI1D7 8.8, FI1D9 8.5, FI19B 8.4, FI198 8.2, FI19A 7.4, FI1B1 5.7, FI1DB 5.1, FI1C6 2.1, FI1DC 1.9, FI1C2 1.8 % | SubRES_10: 17 (pulping, process heat by fuel, black-liquor biorefineries `BBLQ*`) |
| Lime `ILM*` | 5 (0.34 Mt kilns, kiln fuels) | `ind_ilm`, 6 regions: FI1D9 35.2, FI1D7 34.0, FI1B1 13.5, FI1C1 9.8, FI1DA 5.1, FI1C5 2.4 % | SubRES_10: 2 |
| Chemicals `ICH*` (energy-service chain: process heat, machine drive, steam, electrolysis by fuel -> `ICHDEMAND00`) | 27 | `ind_ich`: FI1B1 77.7, FI196 19.7, FI1C5 2.4, FI1DC 0.2 % | SubRES_10: 18 |
| Fertiliser `IAM*` | 4 (0.0044 Mt) | `ind_iam`: FI1C1 52.2, FI1DB 47.8 % | SubRES_10: 5 |
| Industrial CHP and boilers serving these sectors | (new only) | union of the sector keys' regions | SubRES_13: `CHPIND*`, `CHPIP*`, `INDIPP*HTH06` |

## 2. Design decisions (scientific basis)

1. **Product demand split with the sector key** (Split rule: `COM_PROJ` of `IPL`, `IPH`, `ICH`, `ILM`,
   `IAM` x share, exact sums). Basis: with a copper-plate grid every region has the same costs, so a
   national demand on the hub would place future capacity arbitrarily (degenerate LP). Production of
   Finnish heavy industry is where the mills are; the key is production-proportional (EU benchmark x
   historical activity). Same as the design approved for step 4 (`audit/task4_industry.md` sections 3, 7).
2. **The whole sector chain moves** (existing stock split by key; new sector technologies of SubRES_10
   available in the key regions; on the hub they are switched off in Reg mode). Commodities touched only
   by the chains stay inside the region and get no link: pulp `MPPPUP`, process heat `IPPPRC`/`ICHPRC`/
   `ILMPRC`, machine drive `ICHMCH`, demand products `IPL`/`IPH`/`ICH`/`ILM`/`IAM`, biorefinery fuels.
   **Transitional (documented):** the existing multi-sector autoproducer CHPs (`CHPAUTOGEN*`, step-3 keys
   are by fuel, not sector) and the new industrial CHP/boiler technologies (SubRES_13) stay on the hub,
   so sector heat (`IPPHTH`, `ICHHTH`) and black liquor (`INDBLQ`) cross links, as steel heat in 4a.
   This ends when the autoproducers move to their plants (with step 5).
3. **Existing plants only in their regions**, never a hub copy (4a lesson: a hub copy without stock or
   capacity cost has no capacity variable and runs for free).
4. **Share constraints national** (`R_S: AllRegions`, as the steel shares in 4a): `TUC_Istruc_PUP-*`,
   `TUC_LO_*PRC-*`, `TUC_UP_*HET-INDCO` (`INDPRC`), `S_ICHM` (`FI` sheet), `TUC_UP_IPP_COA`, and the
   whole CCS growth table (`GROWTH ACT`, incl. `UC_DecrCCSIND`). A national sum keeps the single-region
   meaning exactly, which per-region copies would not once sector heat crosses links. Their stock fills
   (`FILL-PUP`, `INDPRC`) read every region and sum them (4a lesson). `UC_IRE-I` corrections on the heat
   links (`TB_IPPHTH_*`, `TB_ICHHTH_*`) in `INDPRC`, `CHPShares` and `UC_IPPCOA`.
5. **Generic `2010` values blanked** in Reg mode for copied rows with a calibrated FI value (4a lesson);
   region-qualified headers (`FI~..`) checked.
6. **Commodities** of the moved chains declared in their regions (SysSettings), links hub <-> region for
   fuels/materials only, read from the DD files.

## 3. Constraints touching 4b processes (DD of the passing 4a run)

| Constraint | Now | Terms | Treatment |
|---|---|---|---|
| `TUC_Istruc_PUP-CHE/MEC/RYC` | R_E, FI coefficients | pulp route shares (fill `FILL-PUP`, FI only) | R_E AllRegions, fill all regions |
| `TUC_LO_IPPPRC-INDEL/INDGA`, `TUC_LO_ICHPRC-INDEL/INDGA` | R_E, FI | min. electricity/gas share in process heat (fill `INDPRC`, FI only) | R_E AllRegions, fill all regions |
| `TUC_UP_IPPHET-INDCO`, `TUC_UP_ICHHET-INDCO` | R_E, FI | coal cap in sector heat | R_E AllRegions |
| `TUC_UP_IPP_COA` (`Scen_UC_LimitCOAL`) | R_E AllRegions, FI column | coal in IPP heat | AllRegions column |
| `S_ICHM` | R_E FI | chemicals machine-drive fuel mix | R_E AllRegions |
| `UCI_UP_CHPShare-IPP` | R_S (FI terms) | CHP share of pulp heat | regional terms follow the commodity |
| `TUC_UP_CHPAUTO-INDCO` | R_S FI+FI1B1 | coal in autoproducer CHP | unchanged (national) |
| `UC_DecrCCSIND` | R_E FI | CCS growth (pulp CCS `IPPPUPMEC15`, Raahe CCS) | R_S AllRegions |

## 4. Checks

Dry run reviewed first; after the sync: `check_run.py` (dummy imports, COM_PROJ / NCAP_PASTI /
PRC_RESID conserved), `tools/audit_run.py` (incl. K: no activity without capacity), parameter
comparison of every moved process single vs regional, `tools/regional_scan.py`. Pass: objective close
to the single run; a small rise is expected from per-region shares and fixed regional demand
(documented when it appears).

## 5. Applied (2026-11-17)

881 cells in 9 workbooks + regenerated/new sheets (`Reg_IND` with the 4a rows unchanged + 4b rows;
link sheet with the 101 4a links + 275 new; `Reg_Demand`). The first apply pass refused the two
tool-made sheets (marker check of the shared engine); those workbooks were not saved, the other seven
were restored from git and the whole step was applied again in one pass.
Checks: single-mode raw tables of the whole model identical to the last commit (xl2times); no formula
lost or changed outside the plan in the 9 workbooks; all 4a formulas and links present on the
regenerated sheets.
