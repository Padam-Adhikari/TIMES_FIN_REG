"""Renders audit/task0.md from the classified entries of tools/task0.py (read-only)."""
import collections
import datetime
import os

CLASS_TEXT = {
    "SUM": "**Sum** -> `RS_*` UC_R_SUM (Reg mode)",
    "LINK": "Link: external trade, stays on FI hub - no change",
    "POT": "**Sum** (resource potential) -> `RS_*` UC_R_SUM; Split rule replaces it when regional resource data exist",
    "KEEP": "No change: cumulative UP bound on an FI-hub process",
    "NONBIND": "No change: sentinel, not a limit",
    "SKIP": "No change: not a quantity",
    "COPY": "Copy (zero)",
}


def _b(path):
    return path.replace("Reg-FINTIMES/", "")


def _vals(es):
    pairs = sorted({(str(e.year or "-"), e.value) for e in es}, key=lambda x: x[0])
    s = ", ".join(f"{y}: {v:g}" for y, v in pairs)
    return s if len(s) < 260 else s[:250] + f" ... ({len(pairs)} values)"


def _items(e):
    i = e.ident
    for k in ("techname", "pset_pn", "pset: pn", "pset:pn"):
        if k in i:
            base = str(i[k])
            break
    else:
        base = ""
    extra = [f"{k}={i[k]}" for k in ("pset_ci", "pset_co", "pset_pd", "pset_set", "cset_cn",
                                     "commname", "comm-in", "comm-out") if k in i]
    s = " ".join(x for x in [base] + extra if x)
    if e.items and len(e.items) > 1:
        s += f" ({len(e.items)} processes)"
    return s.replace("|", "/")


def render(scan, entries, inactive, uc_report, ucs, plan, actcost, topo, CASE):
    out = []
    w = out.append
    nz_b = [e for e in entries if e.value != 0 and not e.attr.startswith("UC_RHS")]
    nz_u = [e for e in entries if e.value != 0 and e.attr.startswith("UC_RHS")]
    w(INTRO.format(case=CASE, date=datetime.date.today().isoformat(), nbooks=len(scan),
                   ntables=sum(len(x["tables"]) for x in scan), actcost=actcost))

    # ---- bounds inventory
    w("\n## 2. Non-zero national bounds\n\n")
    c = collections.Counter(e.cls for e in nz_b)
    w("Counts of non-zero bound values: " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())) + ".\n\n")
    w("One line per table x attribute x limit x item. `Region` is the column the value sits in "
      "(`-` = no region column: SubRES/VT rows apply to every region where the process exists; "
      "today that is FI only, because every SubRES `~TFM_AVA` sets `AllRegions 0, FI 1`).\n\n")
    groups = collections.OrderedDict()
    for e in nz_b:
        k = (e.book, e.sheet, e.tagcell, e.tag, e.attr, e.lim, _items(e), e.region, e.cls)
        groups.setdefault(k, []).append(e)
    for cls in ("SUM", "POT", "LINK", "KEEP", "NONBIND", "SKIP"):
        sel = [(k, v) for k, v in groups.items() if k[8] == cls]
        if not sel:
            continue
        w(f"\n### 2.{['SUM','POT','LINK','KEEP','NONBIND','SKIP'].index(cls)+1} {CLASS_TEXT[cls]}\n\n")
        w("| File | Sheet | Table | Attribute | Lim | Item(s) | Region | Values (year: value) | Cells |\n")
        w("|---|---|---|---|---|---|---|---|---|\n")
        for k, es in sel:
            book, sheet, cell, tag, attr, lim, items, reg, _ = k
            cells = ", ".join(sorted({e.coord() for e in es}))[:80]
            w(f"| {_b(book)} | {sheet} | {cell} `~{tag}` | {attr} | {lim} | {items} | {reg or '-'} | "
              f"{_vals(es)} | {cells} |\n")

    # ---- UC inventory
    w("\n## 3. User constraints with a non-zero RHS\n\n")
    w("| File | Sheet | Table | UC_N | Region set now | RHS attribute | Lim | Values (year: value) |\n")
    w("|---|---|---|---|---|---|---|---|\n")
    rset = {(r["book"], r["sheet"], r["table"]): r["rset"] for r in uc_report}
    ug = collections.OrderedDict()
    for e in nz_u:
        k = (e.book, e.sheet, e.tagcell, str(e.ident.get("uc_n")), e.attr, e.lim)
        ug.setdefault(k, []).append(e)
    for (book, sheet, cell, ucn, attr, lim), es in ug.items():
        rs = rset.get((book, sheet, cell), "?")
        w(f"| {_b(book)} | {sheet} | {cell} | {ucn} | {rs} | {attr} | {lim} | {_vals(es)} |\n")
    w("\nZero-RHS UC tables that share a `~UC_Sets` line with a table above and therefore switch "
      "with it:\n\n")
    for r in uc_report:
        if not r["nonzero"] and r.get("co_table"):
            w(f"- {_b(r['book'])} / {r['sheet']} / {r['table']} {', '.join(r['ucs'])}: {r['co_table']}"
              f"{' (UP, coefficients >= 0, so R_S <= 0 is the same as R_E <= 0)' if r['co_table']=='safe' else ''}\n")

    # ---- inactive
    w("\n## 4. Disabled tables (tag without `~` in the current mode) holding bounds/RHS\n\n")
    seen = set()
    for wb, t in inactive:
        key = (wb["file"], t["sheet"], t["cell"])
        if key in seen:
            continue
        hdr = " ".join(t["header"]).upper()
        if any(x in hdr or x in (t["params"] or "").upper() for x in ("BND", "RHS", "CUM")):
            seen.add(key)
            w(f"- {_b(wb['file'])} / {t['sheet']} / {t['cell']} `{t['tag']}: {t['params']}`"
              f"{' (tag is a formula: ' + t['tag_formula'] + ')' if t['tag_formula'] else ''}\n")

    # ---- proposal
    w(PROPOSAL)
    w("\n### 5.6 What the change does\n\n")
    w(f"- Cell edits: {sum(len(v) for v in plan.edits.values())} in {len(plan.edits)} workbooks "
      "(all `=IF(Region_selection...)` switches; single-region values unchanged).\n")
    w(f"- New `RS_*` constraints (Reg mode only): {len(ucs)}.\n")
    have = {x["file"] for x in scan if x["mode"]}
    need = sorted(b for b in plan.need_rs if b not in have)
    w(f"- Workbooks that need a `Region_selection` sheet first ({len(need)}): "
      + ", ".join(_b(b) for b in need) + ".\n")
    if plan.blocked:
        w("\nNot handled automatically:\n\n" + "".join(f"- {x}\n" for x in plan.blocked))
    w(TRAPS)
    return "".join(out)


INTRO = """# Task 0 audit: internal link cost, national bounds, non-zero-RHS user constraints

Case: **{case}** | generated {date} by `tools/task0.py --write-audit` (read-only) |
{nbooks} workbooks, {ntables} tagged tables (incl. `~UC_Sets` lines and disabled tags).

Method: every workbook of the case (from `AppData/Cases.json` + `Groups.json`: BASE `VT_*`,
`BY_Trans`, the SubRES pairs, SysSettings, TradeParameters, the 55 checked SuppXLS scenarios and
the trade links) was read with openpyxl `read_only=True` - cached values and formulas. Values are
the ones VEDA sees with the switch at **FINTIMES** (all files are saved in single-region mode).
VEDA aliases were resolved (`BNDACT`/`ACTBND` = ACT_BND, `CUM` = ACT_CUM, ...), `\\I:` rows and
columns, `*` comment columns and year-`0` interpolation cells were skipped, and the FI_T
`TechName` / UC_T `UC_N` carry-forward was applied. Cross-check: every non-zero FI bound in
`AppData/GAMSSAVE/baseline.gdx` maps to one of the tables below, except items that no longer
exist in the files (that GDX is older than the current workbooks).

## 1. Internal link cost

| File | Sheet | Table | Value now | Proposed |
|---|---|---|---|---|
| SuppXLS/Trades/ScenTrade_TradeParameters.xlsx | FI internal trades | C2 `~TFM_INS` (AllRegions, `Pset_PN = TB_*`) | ACTCOST **10** | **{actcost}** |

- Units are M EUR / PJ, so 10 = 10 EUR/GJ = 36 EUR/MWh on every PJ that crosses a link
  (`TB_INDELC_FI_FI1D9` etc.), both directions. That is a real cost, not an anti-stalling tie
  breaker; it penalises the regional run against the single-region run.
- The tag cell is `=IF(Region_selection!$B$8=Region_selection!$D$9,"~TFM_INS","TFM_INS")`, so
  the table is only read in Reg-FINTIMES mode: single-region runs are not affected by the change.
- **Choice: {actcost} M EUR/PJ** (= 0.36 EUR/GWh). On the hub links the cost has only one job: break
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
"""

PROPOSAL = """
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
- RHS = the national value, at the same years, same LimType.
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
  FX bounds are switched off at source in Reg mode (row: `Attribute` cell -> `\\I:`; column: header
  -> `\\I:<header>`; otherwise the value cell -> blank), because an FI-only LO/FX would pin moved
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
  region-less (UC_RHST/UC_RHSTS only), the 185 `RS_*` constraints are active, and the only LO/FX
  bounds still read from FI are the 101 external-trade bounds (Link rule).
"""

TRAPS = """
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
"""
