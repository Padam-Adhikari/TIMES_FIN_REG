# Audit of reg_baseline-sami_2026-11-19_task5b_run3.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,532,000.46 M EUR, reference 1,529,919.88, difference +2,080.57 (+0.1360%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,722.3 | 144,742.3 | -20.05 |
| INV | 918,103.8 | 919,897.7 | -1,793.9 |
| VAR | 469,174.4 | 465,279.9 | 3,894.5 |
| VARX | 0.03851 | 0 | 0.03851 |

| region | objective share |
|---|---|
| FI | 1,022,675.6 |
| FI1B1 | 109,493.6 |
| FI196 | 52,517.1 |
| FI19B | 41,429.6 |
| FI1D9 | 41,224.0 |
| FI1C1 | 37,986.0 |
| FI198 | 25,095.3 |
| FI1C7 | 24,611.3 |
| FI1DB | 22,439.4 |
| FI1C5 | 22,393.8 |
| FI1D7 | 20,899.6 |
| FI19A | 20,194.2 |
| FI199 | 18,968.3 |
| FI1C6 | 16,586.1 |
| FI1C2 | 15,721.2 |
| FI1DC | 13,666.7 |
| FI1DA | 11,302.8 |
| FI1D5 | 5,951.9 |
| FI1D8 | 5,874.1 |
| FI200 | 2,969.9 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved
- PRC_RESID national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| EEPP_PV | 42.5 | 45.46 | -2.962 |
| ECHP_coal_thermal | 99.1 | 97.15 | 1.946 |
| EUHYDDAM00 | 1,378.7 | 1,380.6 | -1.876 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| EEPP_coal_thermal | 41.01 | 40.22 | 0.7943 |
| ECHP_naturalgas_CCGT | 84.28 | 84.67 | -0.394 |
| EEPP_biomass_thermal | 86.03 | 86.31 | -0.2743 |
| ECHP_HFO_thermal | 8.107 | 8.341 | -0.2348 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05788 |
| EEPP_naturalgas_thermal | 0.06301 | 0.09998 | -0.03697 |
| ECHP_LFO_thermal | 0 | 0.02023 | -0.02023 |
| ECHP_naturalgas_thermal | 2.22 | 2.229 | -0.009128 |
| ECHP_lignite_thermal | 29.84 | 29.84 | -0.002604 |
| EEPP_windOFF | 23.59 | 23.59 | -0.001945 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08295 | 0.08335 | -0.0003948 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | -3.314e-05 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | -1.546e-07 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | -1.509e-07 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | -1.448e-07 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | -1.062e-07 |
| EEPP_HFO_thermal | 2.141 | 2.141 | 7.379e-09 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 7.619e-10 |

By class and year: 59 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_coal_thermal / 2020 | 14.07 | 12.65 | 1.421 |
| EUHYDDAM00 / 2033 | 54.03 | 54.9 | -0.8706 |
| EEPP_coal_thermal / 2013 | 3.239 | 2.445 | 0.7943 |
| EUHYDDAM00 / 2030 | 54.28 | 55.04 | -0.7541 |
| ECHP_coal_thermal / 2018 | 38.63 | 38.11 | 0.5252 |
| EEPP_PV / 2023 | 2.688 | 2.932 | -0.2439 |
| EEPP_PV / 2040 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2038 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2035 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2033 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2028 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2025 | 3.564 | 3.796 | -0.2319 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,284.4 |
| FI198 | 76.91 |
| FI199 | 157.7 |
| FI19A | 265.8 |
| FI19B | 93.32 |
| FI1B1 | 249.4 |
| FI1C1 | 122.2 |
| FI1C2 | 49.97 |
| FI1C5 | 237.6 |
| FI1C6 | 30.81 |
| FI1C7 | 56.56 |
| FI1D5 | 165.4 |
| FI1D7 | 591.5 |
| FI1D8 | 93.29 |
| FI1D9 | 732.8 |
| FI1DA | 73.04 |
| FI1DB | 23.56 |
| FI1DC | 98.03 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.6 | 337.6 | -0.04416 |
| 2013 | 292.8 | 292.1 | 0.7712 |
| 2015 | 319.9 | 320.1 | -0.1897 |
| 2018 | 373.1 | 373.1 | 0.06399 |
| 2020 | 315.5 | 314.9 | 0.648 |
| 2023 | 381.6 | 380.3 | 1.329 |
| 2025 | 423.3 | 423.2 | 0.0826 |
| 2028 | 478.9 | 478.3 | 0.655 |
| 2030 | 507.9 | 507.3 | 0.6588 |
| 2033 | 443.2 | 442.2 | 1.028 |
| 2035 | 465.2 | 464.2 | 0.9855 |
| 2038 | 522.4 | 521.6 | 0.8154 |
| 2040 | 574.9 | 573.8 | 1.069 |
| 2043 | 622.5 | 623.9 | -1.435 |
| 2045 | 641.5 | 644.7 | -3.178 |
| 2048 | 668.6 | 670.5 | -1.872 |
| 2050 | 705.9 | 708.1 | -2.123 |
| 2053 | 717.0 | 719.1 | -2.121 |
| 2055 | 728.1 | 727.8 | 0.2702 |
| 2058 | 749.2 | 749.1 | 0.03918 |
| 2060 | 764.6 | 763.8 | 0.8559 |
| 2063 | 780.5 | 779.1 | 1.401 |
| 2065 | 790.3 | 788.8 | 1.536 |
| 2068 | 805.4 | 805.1 | 0.273 |
| 2070 | 816.9 | 816.6 | 0.3777 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 198.6 | 200.0 | -1.307 |
| 2013 | 179.6 | 179.3 | 0.2452 |
| 2015 | 131.3 | 131.1 | 0.2133 |
| 2018 | 133.4 | 132.5 | 0.9368 |
| 2020 | 147.6 | 145.3 | 2.297 |
| 2023 | 134.4 | 134.0 | 0.427 |
| 2025 | 122.5 | 124.4 | -1.88 |
| 2028 | 212.5 | 212.8 | -0.3276 |
| 2030 | 232.7 | 230.4 | 2.306 |
| 2033 | 169.1 | 168.8 | 0.2439 |
| 2035 | 177.5 | 177.8 | -0.2418 |
| 2038 | 189.0 | 190.0 | -0.9436 |
| 2040 | 203.1 | 204.3 | -1.187 |
| 2043 | 223.0 | 224.7 | -1.72 |
| 2045 | 230.5 | 229.2 | 1.247 |
| 2048 | 234.2 | 235.1 | -0.8875 |
| 2050 | 236.3 | 239.0 | -2.649 |
| 2053 | 237.4 | 238.4 | -1.055 |
| 2055 | 242.9 | 242.9 | 0.009815 |
| 2058 | 249.5 | 249.0 | 0.505 |
| 2060 | 257.9 | 257.1 | 0.8385 |
| 2063 | 261.5 | 262.1 | -0.5593 |
| 2065 | 264.6 | 263.8 | 0.7225 |
| 2068 | 268.9 | 268.4 | 0.5033 |
| 2070 | 271.7 | 271.1 | 0.6616 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 4.725 | 4.729 |
| 2018 | 12.9 | 0.4351 |
| 2025 | 8.316 | 0.2816 |
| 2033 | 35.65 | 1.207 |
| 2040 | 47.98 | 1.624 |
| 2048 | 27.65 | 0.9359 |
| 2055 | 29.08 | 0.957 |
| 2063 | 30.75 | 1.015 |
| 2070 | 29.74 | 0.9795 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.092 | 0.7168 |
| 2018 | 21.61 | 1.703 |
| 2025 | 238.6 | 18.8 |
| 2033 | 23.6 | 1.592 |
| 2040 | 30.43 | 1.75 |
| 2048 | 15.07 | 0.7754 |
| 2055 | 16.37 | 0.7779 |
| 2063 | 16.86 | 0.8026 |
| 2070 | 16.38 | 0.6784 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,103.3 | 0.0744 |
| ICMFISCO2 | 10,396.0 | 0 |
| ELCHIG | 4,410.4 | 0.009343 |
| INDELC | 2.041 | 4,068.4 |
| IPPHTH | 4.914 | 4,000.1 |
| OILCRD | 0.08255 | 3,890.0 |
| BIOOILFS | 0.2959 | 3,460.7 |
| GreenCert-ELC | 3,348.9 | 1.589 |
| BIOHVO | 2,986.6 | 0.2961 |
| INDBLQ | 2,544.8 | 1.111 |
| OILDST | 1,568.9 | 515.6 |
| TRADST | 1.633 | 1,691.9 |
| OILGSL | 1,399.3 | 0.08337 |
| ELCHYD | 1.46 | 1,380.4 |
| ELCWOO | 1.51 | 1,271.0 |
| ELCWIN | 2.361 | 1,094.0 |
| ELCLOW | 0.0007218 | 1,080.2 |
| INDBIO | 258.3 | 642.5 |
| MPPWOO | 0.009513 | 771.0 |
| HETHTH | 758.8 | 0.009016 |
| ELCNUC | 0.003054 | 751.8 |
| TRAGSLSP95 | 1.804 | 667.3 |
| ELCCOH | 0.07124 | 446.3 |
| INDHTH | 0.5951 | 443.4 |
| OILHFO | 257.1 | 165.5 |
| OILNEU | 0.0838 | 411.3 |
| INDCOK | 2.652 | 346.7 |
| INDLFO | 1.796 | 304.2 |
| INDCOA | 1.977 | 297.3 |
| OILNAP | 0.1159 | 290.1 |
| INDRFG | 0.08406 | 289.8 |
| INDGAS | 7.898 | 281.9 |
| INDHFO | 1.888 | 268.8 |
| ELCGAS | 8.315 | 216.2 |
| SUPRPG | 0.08639 | 221.3 |
| IOIHTH | 12.59 | 207.3 |
| OILKER | 206.6 | 0.08697 |
| COALIG | 0.07737 | 189.6 |
| OILOTH | 33.49 | 118.6 |
| BIOWOO | 0 | 151.4 |
| ELCCOL | 0.207 | 149.2 |
| OILLPG | 12.76 | 120.4 |
| COACOK | 127.7 | 0.08777 |
| ICHHTH | 2.936 | 122.1 |
| MPPRYC | 0.01031 | 118.6 |
| TRAGSLE85 | 1.833 | 109.4 |
| BIOGAS | 97 | 8.033 |
| OILRFG | 62.26 | 37.24 |
| INDHH2 | 37.63 | 37.4 |
| GASNAT | 9.774 | 64.2 |
| ELCHIGG | 36.96 | 36.96 |
| TRALH2 | 36.96 | 36.96 |
| SYNH2CT | 40.15 | 32.7 |
| MISSNT | 0.01907 | 65.57 |
| MPPGYP | 0 | 63.92 |
| INFHTH | 23.42 | 39.33 |
| SUPRPP | 0.09133 | 51.3 |
| ELCSOL | 2.583 | 48.15 |
| INDLPG | 2.891 | 43.93 |
| GASCOG | 43.21 | 0.09284 |
| MISRIR | 38.28 | 0 |
| ICMPARA | 37.75 | 0.08844 |
| ELCHFO | 2.693 | 31.08 |
| MISOXY | 0 | 27.68 |
| TRAHFO | 27.33 | 0 |
| INDCOG | 0.1695 | 26.74 |
| GASP2GB | 11.07 | 15.83 |
| INMHTH | 12.75 | 13.45 |
| AGRGAS | 12.91 | 12.91 |
| GASP2G | 12.32 | 12.32 |
| COAHAR | 0.1051 | 22.53 |
| MISORE | 0 | 20.57 |
| MLMSTN | 0 | 20.19 |
| IIS | 18.46 | 0.04466 |
| INDSLU | 2.964 | 15.19 |
| SUPGAS | 0.4363 | 16.6 |
| BRFH2 | 0.2991 | 15.42 |
| MISBFS | 7.71 | 7.607 |
| MPPKAO | 0 | 14.53 |
| ELCMED | 0.0007355 | 14.38 |
| INDMUN | 2.132 | 9.52 |
| MISCST | 7.682 | 3.257 |
| INDCOL | 2.754 | 6.596 |
| MISSCR | 0 | 9.287 |
| GASBFG | 7.237 | 0.3242 |
| REFHTH | 0 | 7.488 |
| TRAGSLSP95E10 | 3.06 | 3.06 |
| ELCDST | 2.745 | 3.129 |
| MPPNOH | 0 | 5.736 |
| ETSCO2 | 2.789 | 2.789 |
| SUPBIO | 0.1065 | 5.117 |
| ELCCO2N | 0.001546 | 5.169 |
| IALHTH | 0.7984 | 2.801 |
| MPPOXY | 0 | 3.278 |
| IGH | 1.715 | 0.02196 |
| IISHTH | 0.3744 | 1.081 |
| SUPELC | 0.2567 | 0.9254 |
| MISPLT | 0.03428 | 1.141 |
| MGHRYC | 0 | 1.174 |
| MALBAU | 0.1296 | 1.015 |
| BRFCA3 | 0 | 0.7167 |
| BIOPROP | 0.3719 | 0.3109 |
| INDBFG | 0.02107 | 0.6534 |
| RENGEO | 0 | 0.6626 |
| ICMLC3 | 0.3242 | 0.3242 |
| INDCOB | 0.2524 | 0.3911 |
| ICLHTH | 0.1218 | 0.3472 |
| ICUHTH | 0 | 0.4682 |
| MALSCR | 0 | 0.4548 |
| MCUORE | 0 | 0.3679 |
| GASIIS | 0.1574 | 0.1779 |
| GreenCert-FIN | 0.1558 | 0.1746 |
| OILFDS | 0.1589 | 0.1654 |
| MISQLI | 0 | 0.2985 |
| GASCOP | 0.1458 | 0.1458 |
| ICU | 0.193 | 0.02419 |
| SUPHTH | 0 | 0.1505 |
| RENSOL | 0 | 0.111 |
| MCUSCR | 0.0383 | 0.03155 |
| MCUSCU | 0.0339 | 0.03496 |
| MISRFC | 0.03428 | 0.03428 |

- Back-and-forth on the same link, year and timeslice: 54641 cases, volume 307.5
| link / year / ts | min(imp, exp) |
|---|---|
| TB_MISCST_FI_FI1C5 / 2020 / ANNUAL | 0.2759 |
| TB_MISCST_FI_FI1D9 / 2020 / ANNUAL | 0.2301 |
| TB_MISCST_FI_FI1D7 / 2020 / ANNUAL | 0.2144 |
| TB_MISCST_FI_FI1C2 / 2020 / ANNUAL | 0.142 |
| TB_INDCOL_FI_FI200 / 2070 / ANNUAL | 0.03297 |
| TB_INDCOL_FI_FI1D5 / 2070 / ANNUAL | 0.03297 |
| TB_INDCOL_FI_FI1D7 / 2070 / ANNUAL | 0.03297 |
| TB_INDCOL_FI_FI1C5 / 2070 / ANNUAL | 0.03297 |
| TB_INDCOL_FI_FI1C7 / 2070 / ANNUAL | 0.03297 |
| TB_INDCOL_FI_FI1DA / 2070 / ANNUAL | 0.03297 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 130,531.8, reference 130,244.3 (+0.22%); 25 years differ >0.1 %
- ETSCO2: produced, all years: run 343,434.6, reference 343,808.2 (-0.11%); 19 years differ >0.1 %
- INDCO2N: produced, all years: run 125,129.1, reference 126,331.9 (-0.95%); 24 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,153.4, reference 11,202.8 (-0.44%); 21 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,091.0, reference 6,065.4 (+0.42%); 20 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'ELCCO2N': 72831.9, 'ETSCO2': 181261.5, 'GreenCert-ELC': -4.5} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 78 | 792.7 |
| FI / ELCHIGG | 300 | 91 | 33.36 |
| FI / ELCLOW | 300 | 60 | 118.0 |
| FI / ELCMED | 300 | 86 | 12.1 |
| FI / HETHTH | 300 | 1 | 1.025e-06 |
| FI196 / ELCHIGG | 300 | 65 | 2,882.1 |
| FI196 / ELCLOW | 300 | 115 | 6,499.2 |
| FI196 / ELCMED | 300 | 217 | 10,080.6 |
| FI198 / ELCHIGG | 300 | 0 | 0 |
| FI198 / ELCLOW | 300 | 106 | 5,697.9 |
| FI198 / ELCMED | 300 | 148 | 7,924.3 |
| FI199 / ELCHIGG | 300 | 86 | 2,272.4 |
| FI199 / ELCLOW | 300 | 128 | 6,308.5 |
| FI199 / ELCMED | 300 | 89 | 2,743.3 |
| FI19A / ELCHIGG | 300 | 74 | 3,215.1 |
| FI19A / ELCLOW | 300 | 125 | 7,204.6 |
| FI19A / ELCMED | 300 | 121 | 2,380.9 |
| FI19B / ELCHIGG | 300 | 35 | 1,874.7 |
| FI19B / ELCLOW | 300 | 91 | 5,796.5 |
| FI19B / ELCMED | 300 | 278 | 11,954.1 |
| FI1B1 / ELCHIGG | 300 | 5 | 212.4 |
| FI1B1 / ELCLOW | 300 | 187 | 8,323.9 |
| FI1B1 / ELCMED | 300 | 241 | 11,449.9 |
| FI1C1 / ELCHIGG | 300 | 57 | 844.4 |
| FI1C1 / ELCLOW | 300 | 177 | 8,650.6 |
| FI1C1 / ELCMED | 300 | 52 | 2,980.4 |
| FI1C2 / ELCHIGG | 300 | 198 | 7,441.1 |
| FI1C2 / ELCLOW | 300 | 41 | 2,863.0 |
| FI1C2 / ELCMED | 300 | 178 | 6,452.1 |
| FI1C5 / ELCHIGG | 300 | 170 | 7,757.1 |
| FI1C5 / ELCLOW | 300 | 90 | 5,646.1 |
| FI1C5 / ELCMED | 300 | 116 | 3,170.0 |
| FI1C6 / ELCHIGG | 300 | 0 | 0 |
| FI1C6 / ELCLOW | 300 | 206 | 9,084.7 |
| FI1C6 / ELCMED | 300 | 265 | 12,378.7 |
| FI1C7 / ELCHIGG | 300 | 11 | 101.1 |
| FI1C7 / ELCLOW | 300 | 178 | 8,459.0 |
| FI1C7 / ELCMED | 300 | 103 | 6,285.2 |
| FI1D5 / ELCHIGG | 300 | 154 | 5,738.0 |
| FI1D5 / ELCLOW | 300 | 120 | 4,980.2 |
| FI1D5 / ELCMED | 300 | 43 | 2,664.8 |
| FI1D7 / ELCHIGG | 300 | 237 | 8,445.7 |
| FI1D7 / ELCLOW | 300 | 160 | 7,290.4 |
| FI1D7 / ELCMED | 300 | 63 | 3,850.9 |
| FI1D8 / ELCHIGG | 300 | 289 | 10,463.9 |
| FI1D8 / ELCLOW | 300 | 80 | 4,236.5 |
| FI1D8 / ELCMED | 300 | 169 | 8,775.6 |
| FI1D9 / ELCHIGG | 300 | 173 | 8,752.9 |
| FI1D9 / ELCLOW | 300 | 141 | 6,532.1 |
| FI1D9 / ELCMED | 300 | 159 | 7,288.2 |
| FI1DA / ELCHIGG | 300 | 67 | 1,164.0 |
| FI1DA / ELCLOW | 300 | 81 | 2,580.9 |
| FI1DA / ELCMED | 300 | 44 | 684.9 |
| FI1DB / ELCHIGG | 300 | 151 | 5,485.1 |
| FI1DB / ELCLOW | 300 | 96 | 3,544.0 |
| FI1DB / ELCMED | 300 | 129 | 5,483.2 |
| FI1DC / ELCHIGG | 300 | 110 | 3,757.8 |
| FI1DC / ELCLOW | 300 | 178 | 6,717.4 |
| FI1DC / ELCMED | 300 | 172 | 7,847.2 |
| FI200 / ELCHIGG | 300 | 52 | 1,508.9 |
| FI200 / ELCLOW | 300 | 252 | 10,895.3 |
| FI200 / ELCMED | 300 | 74 | 4,427.2 |

- Peak equations outside the hub: 57 region/commodity pairs (expected none in the hub design)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 264; only in run: 55; only in reference: 22
| binding only in run | sum |shadow| |
|---|---|
| UCI_UP_CHPShare-IAL | 176,632.1 |
| UCI_UP_CHPShare-ICL | 125,257.4 |
| UCI_UP_CHPShare-ICU | 66,245.5 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,758.6 |
| RS_PRD_RSDFINOIL_LO | 2,363.6 |
| RS_PRD_COMFINOIL_LO | 2,345.6 |
| RS_PRD_RSDBIO_LO | 1,191.4 |
| RS_PRD_COMBIO_LO | 1,139.9 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 638.3 |
| RS_PRD_COMGAS_LO | 408.9 |
| RS_PRD_RSDGAS_LO | 372.9 |
| UCI_UP_CHPShare-IIS | 90.8 |
| RS_PRD_COMHET_LO | 78.59 |
| RS_PRD_INDFINGAS_LO | 63.64 |

| binding only in reference | sum |shadow| |
|---|---|
| TUC_Istruc_RIR-CYC | 10,699.4 |
| UC_DecrCCUS7 | 181.2 |
| UC_DecrCCUS3 | 34.77 |
| UC_VARU_CAP_EUFBCOL01 | 7.551 |
| UC_VARU_CAP_EUSTCOHcon01 | 7.551 |
| UC_VARU_CAP_EUSTCOHsup01 | 7.551 |
| UC_VARU_CAP_EUSTCOLsup01 | 7.551 |
| UC_VARU_CAP_EUIGCOLCCSpre20 | 4.828 |
| UC_VARU_CAP_EUGEOORC01 | 3.776 |
| UC_VARU_CAP_EUFBCOH15 | 3.776 |
| UC_VARU_CAP_EUGEOEGS01 | 3.776 |
| UC_VARU_CAP_EUGEOF01 | 3.776 |
| UC_VARU_CAP_EUIGCCCOH15 | 3.776 |
| UC_VARU_CAP_EUIGCCCOL01 | 3.776 |
| UC_VARU_CAP_EUPCCOLCCSpos20 | 3.776 |

Shadow prices differing by more than 5 %: 206; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_CAP_EEPP_natgas_CCGT | 627,809.2 | 1,318.7 | 626,490.5 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 596,918.8 | 1,269.5 | 595,649.3 |
| UC_VARU_CAP_EEPP_naturalgas_th | 592,156.3 | 2,436.8 | 589,719.5 |
| UC_VARU_CAP_EEPP_HFO_th | 237,466.0 | 702.2 | 236,763.8 |
| UCI_UP_CHPShare-IAL | 176,632.1 | 0 | 176,632.1 |
| UCI_UP_CHPShare-ICL | 125,257.4 | 0 | 125,257.4 |
| UC_VARU_ACT_EEPP_natgas_OCGT | 131,929.3 | 8,790.4 | 123,138.9 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 105,087.0 | 6,902.7 | 98,184.3 |
| UC_VARU_ACT_EEPP_naturalgas_th | 102,331.4 | 8,719.1 | 93,612.3 |
| UC_VARU_ACT_EEPP_HFO_th | 80,648.2 | 10,729.6 | 69,918.5 |
| UCI_UP_CHPShare-ICU | 66,245.5 | 0 | 66,245.5 |
| UC_HydroLakeSupply_CE | 63,421.7 | 35,734.3 | 27,687.4 |
| UC_VARU_ACT_EEPP_lignite_th | 27,703.9 | 8,299.1 | 19,404.8 |
| UC_VARU_CAP_EEPP_lignite_th | 19,229.3 | 630.4 | 18,598.9 |
| UC_VARU_CAP_EEPP_coal_th | 19,243.4 | 1,060.7 | 18,182.7 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 410 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI1C5 / 2070 / MCMCLKBYF | 0.001646 | 0 | 0.001646 |
| FI1C1 / 2070 / MCMCLKBYF | 0.001645 | 0 | 0.001645 |
| FI1C5 / 2070 / MCMCLKCCSC | 0.001626 | 0 | 0.001626 |
| FI1C1 / 2070 / MCMCLKCCSC | 0.001623 | 0 | 0.001623 |
| FI1C5 / 2070 / MCMCLKLAPP | 0.001498 | 0 | 0.001498 |
| FI / 2070 / ILMHTH | 0.0007762 | 0 | 0.0007762 |
| FI1B1 / 2070 / INFOTH | 0.0006888 | 0 | 0.0006888 |
| FI200 / 2070 / INFOTH | 0.0006888 | 0 | 0.0006888 |
| FI1D5 / 2070 / INFOTH | 0.0006888 | 0 | 0.0006888 |
| FI199 / 2070 / INFOTH | 0.0006888 | 0 | 0.0006888 |

- CST_FLOX: 0 entries differ
### investment: 867 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| COMBATS01 | 0 | 10,588.6 | -10,588.6 |
| RSDBATS01 | 18,393.7 | 9,902.3 | 8,491.4 |
| SELCH2PEM01 | 1,105.6 | 2,349.5 | -1,243.9 |
| SELCH2EC01 | 1,105.6 | 135.6 | 970.0 |
| EUIGCCWOO01 | 13,367.5 | 12,884.8 | 482.8 |
| EUWINONM01 | 43,022.3 | 43,385.6 | -363.3 |
| TRA_Hdt_ELC_01 | 56,331.2 | 56,662.1 | -330.9 |
| EUCCGASCCSpos20 | 7,079.4 | 6,799.3 | 280.1 |
| EUWINOFH01 | 3,194.8 | 2,948.8 | 246.0 |
| R_ES-SH-DH-70_ELC05 | 6,686.1 | 6,877.0 | -190.9 |
| CHPINDSPWOO101 | 44.96 | 230.4 | -185.4 |
| EUPVSOLL101 | 4,359.8 | 4,174.7 | 185.0 |

### fixed O&M: 720 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| SELCH2PEM01 | 417.5 | 885.4 | -467.9 |
| P_COMBATS01 | 0 | 372.8 | -372.8 |
| SELCH2EC01 | 417.5 | 51.24 | 366.2 |
| P_RSDBATS01 | 694.3 | 397.7 | 296.6 |
| IISELAFUR01 | 3,568.1 | 3,496.4 | 71.61 |
| CHPINDSPWOO101 | 16.17 | 82.85 | -66.68 |
| IPPPUPMEC15 | 438.4 | 380.3 | 58.07 |
| EUCCGASCCSpos20 | 1,308.6 | 1,256.3 | 52.26 |
| EUWINONM01 | 6,021.3 | 6,072.1 | -50.8 |
| EUCCGTGAS15 | 1,231.9 | 1,281.9 | -50 |
| TRA_Hdt_ELC_01 | 8,120.6 | 8,168.3 | -47.7 |
| EUPVSOLL101 | 1,084.0 | 1,037.4 | 46.66 |

### activity: 1368 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| SELCH2PEM01_LowAF | 28.75 | 60.75 | -32 |
| ICLADVPRO01 | 25.37 | 55.7 | -30.33 |
| IISELAFUR01 | 1,458.8 | 1,428.5 | 30.33 |
| ICLADVPRO05 | 159.3 | 129.2 | 30.09 |
| SELCH2EC01_LowAF | 28.75 | 3.418 | 25.33 |
| EUIGCCWOO01 | 293.4 | 283.3 | 10.08 |
| MINBIOCRP41 | 1,598.6 | 1,607.3 | -8.752 |
| EUHYDLAKELC01 | 47.64 | 39.42 | 8.221 |
| TB_INDSCO2N_FI_FI1D9 | 5.821 | 0 | 5.821 |
| IPPPUPCHE01 | 2,929.7 | 2,934.4 | -4.636 |
| EUCCGTGAS15 | 107.2 | 111.4 | -4.266 |
| EUWINONM01 | 451.7 | 455.5 | -3.741 |

### flow/import: 156 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TB_ELCLOW_FI_FI1B1 | 1,393.1 | 0 | 1,393.1 |
| EXPOILGSL | -16,972.6 | -16,267.1 | -705.4 |
| IMPOILCRD | 58,526.2 | 57,840.3 | 685.8 |
| TB_ELCLOW_FI_FI1C1 | 527.8 | 0 | 527.8 |
| TB_ELCLOW_FI_FI19B | 511.2 | 0 | 511.2 |
| TB_ELCLOW_FI_FI1D9 | 401.4 | 0 | 401.4 |
| IMPELC-SEtoFI | 6,045.1 | 6,367.7 | -322.6 |
| IMPELC-EetoFI | 1,843.1 | 1,528.3 | 314.7 |
| TB_ELCLOW_FI_FI196 | 296.1 | 0 | 296.1 |
| TB_ELCLOW_FI_FI199 | 294.6 | 0 | 294.6 |
| TB_ELCLOW_FI_FI1DB | 284.3 | 0 | 284.3 |
| TB_ELCLOW_FI_FI198 | 273.0 | 0 | 273.0 |

### capacity (sum over years): 300 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| COMBATS01 | 0 | 356.8 | -356.8 |
| RSDBATS01 | 656.7 | 371.0 | 285.7 |
| R_ES-SH-FL_ELC01 | 12,667.2 | 12,484.1 | 183.1 |
| R_ES-SH-FL_GAS01 | 606.3 | 749.8 | -143.5 |
| R_ES-SH-DH-70_ELC05 | 4,069.8 | 4,193.1 | -123.3 |
| P_COMBATS01 | 0 | 89.2 | -89.2 |
| R_ES-SH-SD_GAS01 | 558.0 | 632.6 | -74.6 |
| P_RSDBATS01 | 164.2 | 92.74 | 71.44 |
| R_ES-SH-DH-70_ELC04 | 100.7 | 35.78 | 64.95 |
| R_ES-SH-FL_ELC05 | 207.6 | 261.9 | -54.32 |
| R_ES-SH-DH-70_ELC07 | 1,983.8 | 1,939.9 | 43.85 |
| TRA_Car_Elc_Sma_10 | 8,045.4 | 8,012.9 | 32.52 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## L. Output without inputs
- Processes running with less than 20 % of their reference inputs per unit of activity: none

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
