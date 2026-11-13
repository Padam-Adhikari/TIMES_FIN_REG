# Regionalising the Finland TIMES model (Reg-FINTIMES)

## Goal
Turn the single-region Finland model (JRC-EU-TIMES adapted for Finland) into a model with
19 Finnish regions (NUTS-3 / maakunta) plus FI as a national hub. Work one sector at a time;
the model must solve, with no dummy imports, after every step.

## Model and repository
- VEDA2.0 model folder: `Reg-FINTIMES/`. One VEDA book, `FINTIMES` (`VT_FINTIMES_*.xlsx`), plus
  `SubRES_TMPL/`, `SuppXLS/`, `SuppXLS/Trades/`, `SysSettings.xlsx`, `BY_Trans.xlsx`.
- Regions (see `SysSettings.xlsx` → `Region_selection`): FI (national hub) and
  FI196 Satakunta, FI198 Keski-Suomi, FI199 Etelä-Pohjanmaa, FI19A Pohjanmaa, FI19B Pirkanmaa,
  FI1B1 Helsinki-Uusimaa, FI1C1 Varsinais-Suomi, FI1C2 Kanta-Häme, FI1C5 Etelä-Karjala,
  FI1C6 Päijät-Häme, FI1C7 Kymenlaakso, FI1D5 Keski-Pohjanmaa, FI1D7 Lappi, FI1D8 Kainuu,
  FI1D9 Pohjois-Pohjanmaa, FI1DA Etelä-Savo, FI1DB Pohjois-Savo, FI1DC Pohjois-Karjala, FI200 Åland.
- Model switch: every workbook whose tables depend on the model has a `Region_selection` sheet;
  cell B8 = `FINTIMES` (single region) or `Reg-FINTIMES` (multi-region). `select_model.xlsm`
  flips it in all files. Region-dependent cells use
  `=IF(Region_selection!$B$8=Region_selection!$D$8, <FI value>, <regional value>)`.
  **Single-region mode must keep working and give the same result as before every change.**
- VEDA cases: `Baseline` (region group FI), `Baseline-Sami`, `Baseline-Reg` (test group
  Reg-FI-Copy = FI, FI1B1, FI1D9). Full group: `Reg-FI`.
- Runs are made by Jack on a server (VEDA sync + GAMS/CPLEX), not on this machine.
  Solved runs are saved as `Reg-FINTIMES/AppData/GAMSSAVE/<case>.gdx`.

## Design: hub and spokes
- FI stays as a national hub during the transition. Things are moved out of FI into regions
  sector by sector; FI ends up holding only imports/exports with other countries and national
  constraints.
- Regions exchange commodities with FI (and later with each other) through internal trade links
  defined in `SuppXLS/Trades/ScenTrade__Trade_Links.xlsx` (sheet `FI internal trades`,
  `~TradeLinks_DINS`, link names `TB_<COMM>_<R1>_<R2>`) and parameters in
  `SuppXLS/Trades/ScenTrade_TradeParameters.xlsx`.
- Done so far (pilot): iron and steel blast furnace route (IISBLAFUR00, IISCOREXP00, IISCYCFUR00)
  moved to FI1D9 with its data; 15 links FI↔FI1D9 for its commodities.

## Rules for every attribute (apply these, do not improvise)
| Rule | Attributes | How |
|---|---|---|
| Split | COM_PROJ, NCAP_PASTI, PRC_RESID, STOCK, regional resource potentials | National value × regional share from `FIR_Keys.xlsx` or a plant register. The sum over regions must equal the national value exactly. Never copy these. |
| Sum | Non-zero national bounds (CAP_BND, NCAP_BND, ACT_BND, FLO_BND, COM_BNDPRD, COM_BNDNET, FLO_CUM, RCAP_BND) and user constraints with a non-zero RHS (UC_RHSRT/RTS/RHST/RHSTS) | One constraint summed over FI + all regions (`UC_R_SUM`) with the national value. Must be done **before** the sector it covers moves, otherwise moved processes escape it. Split only if Jack says the limit is physically regional (e.g. hydro sites, wind potential). |
| Copy | Zero bounds and zero RHS; costs, efficiencies, lifetimes, discount rates, emission factors, FLO_SHAR, ACT_EFF, PRC_ACTFLO, COM_IE, COM_FR, NCAP_PKCNT | Same value in every region. `AllRegions` tables already do this. |
| Regional data | NCAP_AF/AFC of wind, solar, hydro; CAP_BND of reV wind classes | From reV / ENSPRESO / plant data supplied by Jack. |
| Link | Trade with other countries, IMPEXP and MINRNW | Each external link gets a home region (decided by Jack). |

Traps found in the audit of the Baseline-Sami case (968 tables in 99 workbooks):
- ~419 tables address `FI` only; ~112 use `AllRegions`; ~178 have no region (SubRES tables
  apply to every region). A national quantity in an `AllRegions` or no-region table is
  applied once **per region** when regions are added → 19× too much.
- `~TFM_INS` with `AllRegions` applies to all regions; `~TFM_DINS` needs explicit region columns.
- Known issue to fix first: `ScenTrade_TradeParameters` sets `ACTCOST 10` on all `TB_*` links.
  With costs in M€ and energy in PJ that is ~10 €/GJ (~36 €/MWh on INDELC) — far from "small".
  Use about 0.001–0.01 unless Jack says otherwise.

## Excel safety (strict)
- Never write model workbooks with openpyxl (it damages formulas, named ranges, VBA).
  Read with openpyxl (`read_only=True, data_only=True`) or xlwings; write only with xlwings.
- Every change is made by a script in `tools/`, never by hand, so it can be re-run and reviewed.
- Every script has `--dry-run` (default) that prints exactly what it would write; write only
  with `--apply` after Jack approves the dry-run output.
- Keep formulas and the `Region_selection` switch working; prefer adding the regional value
  through the existing IF pattern or a new `~TFM_INS`/`~TFM_DINS` table over overwriting values.
- One git branch per task (`reg/<task>`); small commits; never commit to `main`.
- **Colour every cell a tool writes** (fill colour, so changes can be reviewed in Excel later):
  | Colour | Meaning |
  |---|---|
  | light blue `#DDEBF7` | `Region_selection` switch formula (single value kept, regional value added) |
  | light orange `#FCE4D6` | value computed from a regional key (split; check against `audit/keys.md`) |
  | light green `#E2EFDA` | new Reg-only table or sheet (e.g. `RegSum`, new `~TFM_AVA`, new links) |
  | light yellow `#FFF2CC` | value that still needs a decision or better data (listed in `audit/<task>.md`) |
  Each touched workbook gets the legend on its `Region_selection` sheet.

## Work loop (per task)
1. Read-only audit of the tables the task touches → write `audit/<task>.md` (file, sheet, cell,
   tag, attribute, current regions, rule to apply).
2. Write `tools/<task>.py`; run the dry run; show Jack the summary.
3. Apply, commit, push the branch.
4. Jack runs on the server: (a) single-region `Baseline`, (b) the regional case, and pushes the GDX files.
5. Run `python tools/check_run.py <regional>.gdx --ref <single-region>.gdx --out checks/<task>.md`.
   - Dummy imports must be zero; COM_PROJ and NCAP_PASTI totals must be conserved (hard checks).
   - Single-region run must equal the previous single-region run (regression).
   - Explain any objective change (link costs, regional limits).
6. Fix on the same branch until checks pass; then Jack merges.

## Target: a fully regional model
All 19 regions carry their own plants, demand, stocks and resources, linked by real
transmission/transport links; FI is only the national hub (national constraints, trade with
other countries). Åland (FI200) is a normal region **connected** to the mainland (and, through
FI, to Sweden) by links - not modelled separately. Full region group: `Reg-FI`.

## Task list (in order; do not start the next before the current one passes)
0. Fix the internal link cost; convert national bounds and non-zero-RHS UCs to `UC_R_SUM`;
   make the regional case (Reg-FI-Copy) solve.
1. Validate the steel pilot (FI vs FI+FI1D9); add the missing links (e.g. GASBFT).
2. Power and CHP plants, nuclear, hydro, existing wind/solar to their sites (Energy Authority
   power plant register); links region<->FI hub. Pass: objective ~ single-region run.
3. Grid between neighbouring regions with real capacities (Fingrid), Åland links; reV/ENSPRESO
   wind and solar per region.
4. Other single sites: Porvoo refinery (FI1B1), pulp and paper, chemicals, cement, LNG terminals
   (EU ETS / E-PRTR facility registers) - like steel.
5. Spread demand and stocks: residential and services buildings, district heat, transport,
   agriculture, with keys from `data/keys/` (`tools/regional_keys.py`).
6. Resources: biomass, peat, waste, CO2 storage split by region (Luke, GTK); the task-0 national
   sums of `MIN*` potentials are replaced by the Split rule.
7. Fix every constraint that only sees FI (zero-RHS shares with FI-only coefficients:
   `UC-IIS`, `RCUC-*`, `UC_CO2_Cars`, ...) and every `AllRegions` national quantity.
8. FI becomes a pure hub; external links get their home regions; run the full group `Reg-FI`.

## Regional keys
`tools/regional_keys.py` fetches every key from its public source (Statistics Finland PxWeb,
Traficom, Luke, Energy Authority, ...), maps it to NUTS-3, checks that the 19 shares sum to
exactly 1 and that the regional total equals the national figure, and writes `data/keys/*.csv`
plus `audit/keys.md` (source, table, values, checks). Model scripts read only these files.

## Decisions to confirm with Jack/Padam (ask when the data do not settle them)
Plant locations not in public registers; home regions of external links; which bounds are
physically regional; link capacities and costs where Fingrid data are missing.

## Tools
- `check_run.py` (repo root) — checks a solved GDX against a reference (needs gdxdump: GAMS on PATH or
  `pip install gamspy_base`).
- xl2times can give a quick headless DD check, but VEDA is authoritative: xl2times skips
  `~COMAGG_R1C2`, `~PRCCOMEMI`, `~TFM_TOPINS`, `~TFM_UPD-N` and formula-bearing `~TFM_INS`.
