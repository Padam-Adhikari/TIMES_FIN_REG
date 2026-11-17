# Reference runs (kept outside GAMS_WrkTIMES, which is replaced on every server sync)

| File | Run | Objective (M EUR) |
|---|---|---|
| single_baseline-sami_2026-11-16.gdx (.lst) | single-region Baseline (FI), same scenarios as the regional case; identical to baseline-new (2026-11-11) | 1,529,919.8846 |
| reg_baseline-sami_2026-11-16_run2.gdx | regional FI + 19, task 3 before the loss/link-emission fix (+0.68 %) | 1,540,391.5762 |
| reg_baseline-sami_2026-11-16_run3_final.gdx | regional FI + 19, task 3 final (passes) | 1,529,550.8204 |
| reg_baseline-sami_2026-11-16_task4a.gdx (.lst) | regional FI + 19, task 4a first run (+0.35 %; six defects, audit/task4_industry.md section 9) | 1,535,236.4238 |
| reg_baseline-sami_2026-11-17_task4a_run2.gdx (.lst) | regional FI + 19, task 4a with the six corrections (passes, -0.005 %) | 1,529,842.6527 |
| reg_baseline-sami_2026-11-17_task4b_run3.gdx (.lst) | regional FI + 19, task 4b with fixes 0d2894e + 7d34394 (passes, -0.011 %) | 1,529,745.3598 |

Compare a regional run only with the single-region run of the same scenario group:
`python tools/audit_run.py <regional>.gdx --ref runs/single_baseline-sami_2026-11-16.gdx --out audit/run_<name>.md`
