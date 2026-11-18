# Run check: reg_baseline-sami_2026-11-19_task5b.gdx

Regions (20): FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200

## 1. Dummy imports: PASS


## 2. Objective

Run: 2.2629e+06

Reference: 1.52992e+06  ·  difference +732,976 (+47.9094%)

## 3. National totals (sum over regions vs reference)

### COM_PROJ demand by year, commodity: PASS (0 of 1375 keys differ)


### NCAP_PASTI existing capacity by process: FAIL (6 of 340 keys differ)

| key | run | reference | difference |
|---|---|---|---|
| TRA_Lcv_Dis | 0 | 175.848 | -175.848 |
| TRA_Mop_Gas | 0 | 146.188 | -146.188 |
| TRA_Mot_Gas | 0 | 127.618 | -127.618 |
| TRA_Hdt_Dis | 0 | 62.2285 | -62.2285 |
| TRA_Lcv_Gas | 0 | 11.846 | -11.846 |
| TRA_Hdt_Gas | 0 | 1.44507 | -1.44507 |

### PRC_RESID residual (base-year) capacity by process, year: FAIL (34 of 3241 keys differ)

| key | run | reference | difference |
|---|---|---|---|
| TRA_Lcv_Dis / 2010 | 0 | 321.674 | -321.674 |
| TRA_Mop_Gas / 2010 | 0 | 259.889 | -259.889 |
| TRA_Lcv_Dis / 2013 | 0 | 257.339 | -257.339 |
| TRA_Mot_Gas / 2010 | 0 | 226.877 | -226.877 |
| TRA_Lcv_Dis / 2015 | 0 | 214.449 | -214.449 |
| TRA_Mop_Gas / 2013 | 0 | 194.917 | -194.917 |
| TRA_Mot_Gas / 2013 | 0 | 170.158 | -170.158 |
| TRA_Mop_Gas / 2015 | 0 | 151.602 | -151.602 |
| TRA_Lcv_Dis / 2018 | 0 | 150.114 | -150.114 |
| TRA_Mot_Gas / 2015 | 0 | 132.345 | -132.345 |
| TRA_Hdt_Dis / 2010 | 0 | 113.833 | -113.833 |
| TRA_Lcv_Dis / 2020 | 0 | 107.225 | -107.225 |
| TRA_Hdt_Dis / 2013 | 0 | 91.0661 | -91.0661 |
| TRA_Mop_Gas / 2018 | 0 | 86.6297 | -86.6297 |
| TRA_Hdt_Dis / 2015 | 0 | 75.8884 | -75.8884 |
| TRA_Mot_Gas / 2018 | 0 | 75.6257 | -75.6257 |
| TRA_Hdt_Dis / 2018 | 0 | 53.1219 | -53.1219 |
| TRA_Mop_Gas / 2020 | 0 | 43.3148 | -43.3148 |
| TRA_Lcv_Dis / 2023 | 0 | 42.8898 | -42.8898 |
| TRA_Hdt_Dis / 2020 | 0 | 37.9442 | -37.9442 |
| TRA_Mot_Gas / 2020 | 0 | 37.8128 | -37.8128 |
| TRA_Lcv_Gas / 2010 | 0 | 21.6695 | -21.6695 |
| TRA_Lcv_Gas / 2013 | 0 | 17.3356 | -17.3356 |
| TRA_Hdt_Dis / 2023 | 0 | 15.1777 | -15.1777 |
| TRA_Lcv_Gas / 2015 | 0 | 14.4463 | -14.4463 |

… 9 more

### VAR_CAP installed capacity by year, process (result): DIFF (5743 of 9752 keys differ)

| key | run | reference | difference |
|---|---|---|---|
| 2040 / TRA_Car_PIH_UpM_20pct | 65.1551 | 449.746 | -384.591 |
| 2045 / TRA_Car_PIH_UpM_20pct | 105.887 | 455.389 | -349.502 |
| 2043 / TRA_Car_PIH_UpM_20pct | 113.065 | 449.746 | -336.681 |
| 2048 / TRA_Car_PIH_LoM_20pct | 945.067 | 622.079 | +322.988 |
| 2043 / TRA_Car_Elc_Sma_10 | 1018.39 | 1335.48 | -317.089 |
| 2045 / TRA_Car_Elc_Sma_10 | 1018.39 | 1335.48 | -317.088 |
| 2048 / TRA_Car_Elc_Sma_10 | 1018.39 | 1335.48 | -317.088 |
| 2048 / TRA_Car_PIH_UpM_20pct | 156.552 | 464.233 | -307.68 |
| 2070 / TRA_Car_PIH_UpM_20pct | 228.254 | 532.325 | -304.071 |
| 2068 / TRA_Car_PIH_UpM_20pct | 225.995 | 529.149 | -303.154 |
| 2058 / TRA_Car_PIH_UpM_20pct | 224.116 | 513.673 | -289.557 |
| 2065 / TRA_Car_PIH_UpM_20pct | 236.621 | 524.385 | -287.764 |
| 2053 / TRA_Car_PIH_UpM_20pct | 218.212 | 504.811 | -286.599 |
| 2060 / TRA_Car_PIH_UpM_20pct | 230.22 | 516.672 | -286.452 |
| 2063 / TRA_Car_PIH_UpM_20pct | 235.043 | 521.3 | -286.256 |
| 2055 / TRA_Car_PIH_UpM_20pct | 225.286 | 507.406 | -282.121 |
| 2050 / TRA_Car_PIH_LoM_20pct | 958.125 | 677.215 | +280.91 |
| 2045 / TRA_Car_PIH_LoM_20pct | 864.775 | 588.162 | +276.613 |
| 2050 / TRA_Car_PIH_UpM_20pct | 202.069 | 470.129 | -268.06 |
| 2053 / TRA_Car_PIH_LoM_20pct | 1101.08 | 842.662 | +258.418 |
| 2048 / TRA_Car_Elc_Exe_10 | 774.245 | 516.054 | +258.192 |
| 2038 / TRA_Car_PIH_LoM_20pct | 461.922 | 210.515 | +251.408 |
| 2035 / TRA_Car_PIH_LoM_20pct | 461.916 | 210.515 | +251.401 |
| 2038 / TRA_Car_Elc_Sma_10 | 393.573 | 603.886 | -210.313 |
| 2040 / TRA_Car_Elc_Sma_10 | 393.573 | 603.886 | -210.313 |

… 5718 more

### Emissions (VAR_COMNET) by year, commodity (result): DIFF (213 of 225 keys differ)

| key | run | reference | difference |
|---|---|---|---|
| 2023 / TRACO2N | 2226.03 | 16068.2 | -13842.2 |
| 2020 / TRACO2N | 2116.05 | 15157.3 | -13041.3 |
| 2025 / TRACO2N | 2299.35 | 15334.4 | -13035 |
| 2018 / TRACO2N | 2179.78 | 14808.7 | -12629 |
| 2015 / TRACO2N | 2275.37 | 14452.7 | -12177.4 |
| 2010 / TRACO2N | 2484.24 | 14640.5 | -12156.2 |
| 2013 / TRACO2N | 2358.92 | 14456.2 | -12097.3 |
| 2028 / TRACO2N | 2405.84 | 14103.2 | -11697.4 |
| 2030 / TRACO2N | 2476.83 | 12356.3 | -9879.42 |
| 2033 / TRACO2N | 2589.1 | 12063.9 | -9474.84 |
| 2035 / TRACO2N | 2663.94 | 10986.8 | -8322.84 |
| 2038 / TRACO2N | 2769.31 | 10620.6 | -7851.26 |
| 2020 / ELCCO2N | 16476.1 | 9331.04 | +7145.04 |
| 2040 / TRACO2N | 2839.55 | 8991.75 | -6152.2 |
| 2043 / TRACO2N | 2931.29 | 8745.17 | -5813.88 |
| 2045 / TRACO2N | 2992.45 | 8533.93 | -5541.48 |
| 2048 / TRACO2N | 3083.42 | 7379.98 | -4296.56 |
| 2020 / ETSCO2 | 24127.6 | 19855.3 | +4272.23 |
| 2023 / ELCCO2N | 8870.03 | 4707.59 | +4162.44 |
| 2023 / ETSCO2 | 15974.1 | 12042.6 | +3931.42 |
| 2018 / ELCCO2N | 18487.7 | 14868.2 | +3619.5 |
| 2025 / ETSCO2 | 12501 | 8917.76 | +3583.25 |
| 2020 / INDCO2N | 7812.34 | 11352.5 | -3540.16 |
| 2050 / TRACO2N | 3144.07 | 6341.76 | -3197.69 |
| 2060 / TRACO2N | 3449.83 | 6133.37 | -2683.53 |

… 188 more

## 4. Internal trade (exports on TB_* links, summed over years)

| from region | link | commodity | flow |
|---|---|---|---|
| FI1D9 | TB_INDSCO2N_FI_FI1D9 | INDSCO2N | 28446.3 |
| FI1C1 | TB_ICMFISCO2_FI_FI1C1 | ICMFISCO2 | 10455.8 |
| FI | TB_OILCRD_FI_FI1B1 | OILCRD | 6038.91 |
| FI1B1 | TB_OILDST_FI_FI1B1 | OILDST | 2412.68 |
| FI1B1 | TB_OILGSL_FI_FI1B1 | OILGSL | 2194.9 |
| FI | TB_BIOOILFS_FI_FI1B1 | BIOOILFS | 1686.89 |
| FI1B1 | TB_BIOHVO_FI_FI1B1 | BIOHVO | 1455.82 |
| FI196 | TB_ELCHIG_FI_FI196 | ELCHIG | 1287.19 |
| FI | TB_INDELC_FI_FI1B1 | INDELC | 886.526 |
| FI1D9 | TB_GreenCert-ELC_FI_FI1D9 | GreenCert-ELC | 776.262 |
| FI1D9 | TB_ELCHIG_FI_FI1D9 | ELCHIG | 734.544 |
| FI | TB_ELCNUC_FI_FI196 | ELCNUC | 665.399 |
| FI | TB_IPPHTH_FI_FI1C5 | IPPHTH | 597.306 |
| FI1D7 | TB_GreenCert-ELC_FI_FI1D7 | GreenCert-ELC | 595.035 |
| FI1D7 | TB_ELCHIG_FI_FI1D7 | ELCHIG | 591.534 |
| FI | TB_IPPHTH_FI_FI1C7 | IPPHTH | 587.329 |
| FI | TB_ELCHYD_FI_FI1D7 | ELCHYD | 520.381 |
| FI | TB_IPPHTH_FI_FI196 | IPPHTH | 432.972 |
| FI | TB_BIOOILFS_FI_FI1C5 | BIOOILFS | 422.844 |
| FI1B1 | TB_OILHFO_FI_FI1B1 | OILHFO | 420.13 |
| FI | TB_INDELC_FI_FI196 | INDELC | 415.08 |
| FI | TB_ELCWIN_FI_FI1D9 | ELCWIN | 381.027 |
| FI | TB_TRADST_FI_FI1B1 | TRADST | 379.058 |
| FI1B1 | TB_OILKER_FI_FI1B1 | OILKER | 373.134 |
| FI | TB_IPPHTH_FI_FI19B | IPPHTH | 367.471 |
| FI1C5 | TB_BIOHVO_FI_FI1C5 | BIOHVO | 364.955 |
| FI | TB_IPPHTH_FI_FI1D9 | IPPHTH | 351.896 |
| FI | TB_SUPRPG_FI_FI1B1 | SUPRPG | 343.615 |
| FI | TB_ELCWOO_FI_FI1C5 | ELCWOO | 342.991 |
| FI | TB_INDELC_FI_FI1C5 | INDELC | 335.663 |
| FI | TB_INDELC_FI_FI1C7 | INDELC | 331.647 |
| FI196 | TB_INDBLQ_FI_FI196 | INDBLQ | 330.519 |
| FI | TB_INDELC_FI_FI19B | INDELC | 329.847 |
| FI | TB_INDCOK_FI_FI1D9 | INDCOK | 325.345 |
| FI1C5 | TB_GreenCert-ELC_FI_FI1C5 | GreenCert-ELC | 324.823 |
| FI | TB_IPPHTH_FI_FI1D7 | IPPHTH | 324.674 |
| FI | TB_IPPHTH_FI_FI198 | IPPHTH | 323.997 |
| FI | TB_OILNEU_FI_FI1B1 | OILNEU | 308.965 |
| FI | TB_IPPHTH_FI_FI19A | IPPHTH | 300.094 |
| FI | TB_INDELC_FI_FI1D9 | INDELC | 298.167 |

## Verdict: FAIL
