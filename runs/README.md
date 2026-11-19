# Reference runs (kept outside GAMS_WrkTIMES, which is replaced on every server sync)

| File | Run | Objective (M EUR) |
|---|---|---|
| single_baseline-sami_2026-11-16.gdx (.lst) | single-region Baseline (FI), same scenarios as the regional case; identical to baseline-new (2026-11-11) | 1,529,919.8846 |
| reg_baseline-sami_2026-11-16_run2.gdx | regional FI + 19, task 3 before the loss/link-emission fix (+0.68 %) | 1,540,391.5762 |
| reg_baseline-sami_2026-11-16_run3_final.gdx | regional FI + 19, task 3 final (passes) | 1,529,550.8204 |
| reg_baseline-sami_2026-11-16_task4a.gdx (.lst) | regional FI + 19, task 4a first run (+0.35 %; six defects, audit/task4_industry.md section 9) | 1,535,236.4238 |
| reg_baseline-sami_2026-11-17_task4a_run2.gdx (.lst) | regional FI + 19, task 4a with the six corrections (passes, -0.005 %) | 1,529,842.6527 |
| reg_baseline-sami_2026-11-17_task4b_run3.gdx (.lst) | regional FI + 19, task 4b with fixes 0d2894e + 7d34394 (passes, -0.011 %) | 1,529,745.3598 |
| reg_baseline-sami_2026-11-17_task4c.gdx (.lst) | regional FI + 19, task 4c cement (passes, -0.011 %; crossover 39 min) | 1,529,746.9452 |
| reg_baseline-sami_2026-11-18_task5a.gdx (.lst) | regional FI + 19, task 5a first run (FAIL -5.2 %: agriculture efficiency lost, audit/task5a.md section 6) | 1,450,307.0889 |
| reg_baseline-sami_2026-11-18_task5a_run2.gdx (.lst) | regional FI + 19, task 5a with 5afix (passes, -0.038 %; solutiontype 2) | 1,529,334.3737 |
| reg_baseline-sami_2026-11-19_task5b.gdx (.lst) | regional FI + 19, task 5b run 2 (FAIL +47.9 %: vans/trucks undeclared, 5bfix3; GDX local only) | 2,262,896 |
| reg_baseline-sami_2026-11-19_task5b_run2.gdx (.lst) | regional FI + 19, task 5b run 3 (FAIL +29.5 %: Fill-R header, 5bfix4; GDX local only) | 1,980,800.2142 |
| reg_baseline-sami_2026-11-19_task5b_run3.gdx (.lst) | regional FI + 19, task 5b run 4 (hard checks pass, +0.136 %: DELIV on ELCLOW links, 5bfix5; GDX local only) | 1,532,000.4587 |
| reg_baseline-sami_2026-11-19_task5b_run4.gdx (.lst) | regional FI + 19, task 5b run 5 (hard checks pass, -0.152 %: EV electricity outside the variable-RES adequacy UC, 5bfix6; GDX local only) | 1,527,592.9076 |
| reg_baseline-sami_2026-11-19_task5b_run5.gdx (.lst) | regional FI + 19, task 5b run 6 (NOT SOLVED: numerical, status 7; R_S UCs with regional RHS became R_EACH, 5bfix7; GDX local only) | (1.24e10, not optimal) |

Compare a regional run only with the single-region run of the same scenario group:
`python tools/audit_run.py <regional>.gdx --ref runs/single_baseline-sami_2026-11-16.gdx --out audit/run_<name>.md`
