# Audit of 5bfix7.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,529,070.30 M EUR, reference 1,529,919.88, difference -849.59 (-0.0555%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,791.6 | 144,742.3 | 49.3 |
| INV | 919,524.3 | 919,897.7 | -373.4 |
| VAR | 464,754.4 | 465,279.9 | -525.5 |
| VARX | 0.02769 | 0 | 0.02769 |

| region | objective share |
|---|---|
| FI | 1,021,827.2 |
| FI1B1 | 109,075.5 |
| FI196 | 52,408.1 |
| FI19B | 41,199.9 |
| FI1D9 | 41,066.8 |
| FI1C1 | 37,760.5 |
| FI198 | 24,997.3 |
| FI1C7 | 24,530.3 |
| FI1DB | 22,335.6 |
| FI1C5 | 22,330.9 |
| FI1D7 | 20,827.4 |
| FI19A | 20,121.1 |
| FI199 | 18,862.6 |
| FI1C6 | 16,507.2 |
| FI1C2 | 15,654.2 |
| FI1DC | 13,600.0 |
| FI1DA | 11,243.4 |
| FI1D5 | 5,923.7 |
| FI1D8 | 5,844.9 |
| FI200 | 2,953.7 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved
- PRC_RESID national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| EUHYDDAM00 | 1,372.7 | 1,380.6 | -7.949 |
| EEPP_PV | 42.5 | 45.46 | -2.962 |
| ECHP_coal_thermal | 99.14 | 97.15 | 1.984 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| EEPP_coal_thermal | 40.86 | 40.22 | 0.6464 |
| ECHP_naturalgas_CCGT | 84.17 | 84.67 | -0.5022 |
| EEPP_biomass_thermal | 86.03 | 86.31 | -0.2763 |
| ECHP_HFO_thermal | 8.107 | 8.341 | -0.2344 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05784 |
| EEPP_naturalgas_thermal | 0.06313 | 0.09998 | -0.03685 |
| ECHP_LFO_thermal | 0 | 0.02023 | -0.02023 |
| ECHP_naturalgas_thermal | 2.221 | 2.229 | -0.008115 |
| ECHP_lignite_thermal | 29.84 | 29.84 | -0.002244 |
| EEPP_windOFF | 23.59 | 23.59 | -0.001945 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08295 | 0.08335 | -0.000392 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | -6.281e-05 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | -1.276e-07 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | -1.24e-07 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | -1.179e-07 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | -8.705e-08 |
| EEPP_HFO_thermal | 2.141 | 2.141 | 7.32e-09 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 7.563e-10 |

By class and year: 68 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_coal_thermal / 2020 | 14.25 | 12.65 | 1.6 |
| EUHYDDAM00 / 2063 | 53.88 | 55.04 | -1.151 |
| EUHYDDAM00 / 2068 | 53.98 | 55.04 | -1.06 |
| EUHYDDAM00 / 2070 | 53.99 | 55.03 | -1.038 |
| EUHYDDAM00 / 2065 | 54.03 | 55.04 | -1.003 |
| EUHYDDAM00 / 2060 | 54.26 | 55.04 | -0.7756 |
| EUHYDDAM00 / 2030 | 54.28 | 55.04 | -0.756 |
| EUHYDDAM00 / 2033 | 54.22 | 54.9 | -0.6783 |
| EEPP_coal_thermal / 2013 | 3.091 | 2.445 | 0.6464 |
| ECHP_coal_thermal / 2018 | 38.49 | 38.11 | 0.3842 |
| EUHYDDAM00 / 2058 | 54.71 | 55.04 | -0.3203 |
| EUHYDDAM00 / 2050 | 54.72 | 55.04 | -0.3182 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,283.5 |
| FI198 | 76.68 |
| FI199 | 157.5 |
| FI19A | 265.7 |
| FI19B | 93.03 |
| FI1B1 | 249.3 |
| FI1C1 | 122.2 |
| FI1C2 | 49.98 |
| FI1C5 | 237.0 |
| FI1C6 | 30.54 |
| FI1C7 | 56.1 |
| FI1D5 | 164.9 |
| FI1D7 | 590.8 |
| FI1D8 | 92.78 |
| FI1D9 | 732.1 |
| FI1DA | 73 |
| FI1DB | 23.39 |
| FI1DC | 97.47 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.5 | 337.6 | -0.06228 |
| 2013 | 292.7 | 292.1 | 0.6051 |
| 2015 | 319.9 | 320.1 | -0.2055 |
| 2018 | 373.0 | 373.1 | -0.1041 |
| 2020 | 315.7 | 314.9 | 0.8002 |
| 2023 | 381.7 | 380.3 | 1.426 |
| 2025 | 423.2 | 423.2 | -0.0253 |
| 2028 | 478.7 | 478.3 | 0.4464 |
| 2030 | 507.7 | 507.3 | 0.4502 |
| 2033 | 442.6 | 442.2 | 0.4118 |
| 2035 | 464.9 | 464.2 | 0.7618 |
| 2038 | 522.2 | 521.6 | 0.6533 |
| 2040 | 573.9 | 573.8 | 0.1069 |
| 2043 | 623.7 | 623.9 | -0.2114 |
| 2045 | 643.8 | 644.7 | -0.8486 |
| 2048 | 670.8 | 670.5 | 0.3044 |
| 2050 | 707.3 | 708.1 | -0.8081 |
| 2053 | 718.4 | 719.1 | -0.6689 |
| 2055 | 729.1 | 727.8 | 1.302 |
| 2058 | 750.0 | 749.1 | 0.8256 |
| 2060 | 765.2 | 763.8 | 1.438 |
| 2063 | 780.1 | 779.1 | 1.037 |
| 2065 | 789.7 | 788.8 | 0.9046 |
| 2068 | 805.9 | 805.1 | 0.807 |
| 2070 | 817.3 | 816.6 | 0.7192 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 198.8 | 200.0 | -1.132 |
| 2013 | 179.9 | 179.3 | 0.579 |
| 2015 | 131.7 | 131.1 | 0.5489 |
| 2018 | 133.5 | 132.5 | 1.009 |
| 2020 | 148.3 | 145.3 | 2.941 |
| 2023 | 134.8 | 134.0 | 0.7432 |
| 2025 | 122.5 | 124.4 | -1.878 |
| 2028 | 212.3 | 212.8 | -0.5339 |
| 2030 | 232.2 | 230.4 | 1.859 |
| 2033 | 168.5 | 168.8 | -0.2805 |
| 2035 | 177.4 | 177.8 | -0.4128 |
| 2038 | 189.2 | 190.0 | -0.733 |
| 2040 | 203.6 | 204.3 | -0.6743 |
| 2043 | 223.6 | 224.7 | -1.059 |
| 2045 | 231.0 | 229.2 | 1.782 |
| 2048 | 234.7 | 235.1 | -0.3405 |
| 2050 | 239.2 | 239.0 | 0.1809 |
| 2053 | 238.1 | 238.4 | -0.3047 |
| 2055 | 243.4 | 242.9 | 0.5124 |
| 2058 | 249.7 | 249.0 | 0.7153 |
| 2060 | 257.1 | 257.1 | -0.02791 |
| 2063 | 262.4 | 262.1 | 0.2938 |
| 2065 | 264.6 | 263.8 | 0.721 |
| 2068 | 269.1 | 268.4 | 0.7169 |
| 2070 | 271.8 | 271.1 | 0.7055 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 4.725 | 4.724 |
| 2018 | 13.17 | 0.4445 |
| 2025 | 8.223 | 0.2785 |
| 2033 | 35.43 | 1.199 |
| 2040 | 48.7 | 1.648 |
| 2048 | 28.57 | 0.967 |
| 2055 | 28.46 | 0.9414 |
| 2063 | 30.03 | 0.9913 |
| 2070 | 29.18 | 0.9617 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.096 | 0.7171 |
| 2018 | 21.72 | 1.712 |
| 2025 | 240.2 | 18.93 |
| 2033 | 23.34 | 1.578 |
| 2040 | 30.7 | 1.768 |
| 2048 | 15.64 | 0.8046 |
| 2055 | 16.61 | 0.7876 |
| 2063 | 17.27 | 0.8195 |
| 2070 | 17.06 | 0.7066 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,115.1 | 0.06032 |
| ICMFISCO2 | 10,402.0 | 0 |
| ELCHIG | 4,404.1 | 0.007599 |
| INDELC | 18.27 | 4,084.4 |
| IPPHTH | 3.979 | 3,999.2 |
| OILCRD | 0.06705 | 3,855.1 |
| BIOOILFS | 0.2396 | 3,460.7 |
| GreenCert-ELC | 3,342.5 | 1.286 |
| BIOHVO | 2,986.6 | 0.2397 |
| INDBLQ | 2,545.2 | 0.9013 |
| OILDST | 1,559.8 | 515.6 |
| TRADST | 1.297 | 1,690.3 |
| OILGSL | 1,385.3 | 0.06776 |
| ELCHYD | 1.18 | 1,374.0 |
| ELCWOO | 1.222 | 1,270.7 |
| ELCLOW | 19.05 | 1,099.4 |
| ELCWIN | 1.91 | 1,093.6 |
| INDBIO | 257.8 | 642.2 |
| MPPWOO | 0.007722 | 770.9 |
| HETHTH | 758.7 | 0.007172 |
| ELCNUC | 0.002478 | 751.8 |
| TRAGSLSP95 | 1.421 | 667.9 |
| ELCCOH | 0.05771 | 446.1 |
| INDHTH | 0.4802 | 443.5 |
| OILHFO | 255.0 | 165.6 |
| OILNEU | 0.06806 | 411.4 |
| INDCOK | 2.04 | 346.1 |
| INDLFO | 1.445 | 304.0 |
| INDCOA | 1.494 | 296.9 |
| OILNAP | 0.09397 | 290.7 |
| INDRFG | 0.06827 | 289.8 |
| INDGAS | 6.202 | 280.8 |
| INDHFO | 1.514 | 268.0 |
| ELCGAS | 6.729 | 214.4 |
| SUPRPG | 0.07011 | 219.3 |
| IOIHTH | 10.98 | 205.7 |
| OILKER | 201.4 | 0.07066 |
| COALIG | 0.06271 | 189.6 |
| OILOTH | 33.43 | 119.4 |
| BIOWOO | 0 | 151.3 |
| ELCCOL | 0.1676 | 149.1 |
| OILLPG | 12.32 | 120.8 |
| COACOK | 127.6 | 0.07109 |
| ICHHTH | 2.58 | 121.0 |
| MPPRYC | 0.0083 | 118.6 |
| TRAGSLE85 | 1.441 | 108.9 |
| BIOGAS | 94.97 | 6.504 |
| OILRFG | 62.24 | 38.19 |
| GASNAT | 7.867 | 62.07 |
| ELCMED | 26.22 | 40.61 |
| MISSNT | 0.01546 | 65.57 |
| MPPGYP | 0 | 63.92 |
| INDHH2 | 30.61 | 30.38 |
| SYNH2CT | 33.7 | 26.25 |
| ELCHIGG | 29.91 | 29.91 |
| TRALH2 | 29.91 | 29.91 |
| INFHTH | 20.6 | 37.15 |
| SUPRPP | 0.07374 | 50.82 |
| ELCSOL | 2.084 | 47.64 |
| INDLPG | 2.338 | 43.44 |
| GASCOG | 43.19 | 0.07472 |
| MISRIR | 38.29 | 0 |
| ICMPARA | 37.73 | 0.07158 |
| ELCHFO | 2.18 | 30.57 |
| MISOXY | 0 | 27.68 |
| INDCOG | 0.1018 | 26.68 |
| TRAHFO | 26.44 | 0 |
| GASP2GB | 8.855 | 13.85 |
| COAHAR | 0.08413 | 22.5 |
| INMHTH | 10.41 | 11.17 |
| AGRGAS | 10.35 | 10.35 |
| MISORE | 0 | 20.57 |
| MLMSTN | 0 | 20.19 |
| GASP2G | 9.971 | 9.971 |
| IIS | 18.45 | 0.03594 |
| SUPGAS | 0.3497 | 16.51 |
| INDSLU | 2.395 | 14.34 |
| BRFH2 | 0.2421 | 15.37 |
| MISBFS | 7.53 | 7.46 |
| MPPKAO | 0 | 14.53 |
| MISCST | 7.669 | 3.244 |
| INDMUN | 1.724 | 8.782 |
| MISSCR | 0 | 9.287 |
| INDCOL | 2.123 | 5.965 |
| REFHTH | 0 | 7.421 |
| GASBFG | 7.154 | 0.2639 |
| MPPNOH | 0 | 5.735 |
| SUPBIO | 0.08566 | 5.052 |
| TRAGSLSP95E10 | 2.448 | 2.448 |
| ELCDST | 2.2 | 2.676 |
| ETSCO2 | 2.26 | 2.26 |
| ELCCO2N | 0.001243 | 4.19 |
| IALHTH | 0.6399 | 2.642 |
| MPPOXY | 0 | 3.277 |
| IGH | 1.71 | 0.01766 |
| IISHTH | 0.32 | 1.027 |
| MGHRYC | 0 | 1.174 |
| MISPLT | 0.02775 | 1.134 |
| MALBAU | 0.1026 | 0.9881 |
| INDBFG | 0.04886 | 0.6812 |
| BRFCA3 | 0 | 0.7167 |
| SUPELC | 0 | 0.6687 |
| RENGEO | 0 | 0.6464 |
| BIOPROP | 0.3009 | 0.2517 |
| ICMLC3 | 0.2624 | 0.2624 |
| INDCOB | 0.1912 | 0.3299 |
| ICUHTH | 0 | 0.4682 |
| MALSCR | 0 | 0.4548 |
| ICLHTH | 0.1093 | 0.3347 |
| MCUORE | 0 | 0.3679 |
| MISQLI | 0 | 0.2985 |
| GASIIS | 0.1274 | 0.1441 |
| GreenCert-FIN | 0.1264 | 0.1412 |
| OILFDS | 0.1286 | 0.1339 |
| GASCOP | 0.118 | 0.118 |
| ICU | 0.188 | 0.01928 |
| SUPHTH | 0 | 0.1505 |
| RENSOL | 0 | 0.1098 |
| MCUSCR | 0.03189 | 0.02514 |
| MCUSCU | 0.02739 | 0.02845 |
| MISRFC | 0.02775 | 0.02775 |

- Back-and-forth on the same link, year and timeslice: 69704 cases, volume 309.4
| link / year / ts | min(imp, exp) |
|---|---|
| TB_MISCST_FI_FI1C5 / 2020 / ANNUAL | 0.2758 |
| TB_MISCST_FI_FI1D9 / 2020 / ANNUAL | 0.23 |
| TB_MISCST_FI_FI1D7 / 2020 / ANNUAL | 0.2143 |
| TB_MISCST_FI_FI1C2 / 2020 / ANNUAL | 0.1418 |
| TB_INMHTH_FI_FI199 / 2070 / R | 0.02634 |
| TB_INMHTH_FI_FI199 / 2070 / F | 0.02634 |
| TB_INMHTH_FI_FI199 / 2070 / S | 0.02633 |
| TB_INMHTH_FI_FI199 / 2070 / W | 0.02633 |
| TB_INMHTH_FI_FI1DA / 2070 / R | 0.0262 |
| TB_INMHTH_FI_FI1DA / 2070 / F | 0.02619 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 131,578.9, reference 130,244.3 (+1.02%); 24 years differ >0.1 %
- ETSCO2: produced, all years: run 343,312.2, reference 343,808.2 (-0.14%); 17 years differ >0.1 %
- INDCO2N: produced, all years: run 124,830.0, reference 126,331.9 (-1.19%); 25 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,166.3, reference 11,202.8 (-0.33%); 20 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,085.1, reference 6,065.4 (+0.33%); 19 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'ETSCO2': 181030.0, 'GreenCert-ELC': -4.5, 'ELCCO2N': 72794.2} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 77 | 792.5 |
| FI / ELCHIGG | 300 | 90 | 32.03 |
| FI / ELCLOW | 300 | 50 | 126.7 |
| FI / ELCMED | 300 | 84 | 11.82 |
| FI / HETHTH | 300 | 0 | 0 |
| FI196 / ELCHIGG | 300 | 300 | 11,014.5 |
| FI196 / ELCLOW | 300 | 149 | 5,534.3 |
| FI196 / ELCMED | 300 | 196 | 8,767.4 |
| FI198 / ELCHIGG | 300 | 145 | 5,764.1 |
| FI198 / ELCLOW | 300 | 161 | 6,060.2 |
| FI198 / ELCMED | 300 | 121 | 2,443.0 |
| FI199 / ELCHIGG | 300 | 60 | 2,293.1 |
| FI199 / ELCLOW | 300 | 139 | 6,058.2 |
| FI199 / ELCMED | 300 | 241 | 8,684.3 |
| FI19A / ELCHIGG | 300 | 20 | 618.1 |
| FI19A / ELCLOW | 300 | 153 | 7,131.0 |
| FI19A / ELCMED | 300 | 247 | 9,734.0 |
| FI19B / ELCHIGG | 300 | 3 | 79.27 |
| FI19B / ELCLOW | 300 | 175 | 8,296.5 |
| FI19B / ELCMED | 300 | 263 | 10,239.4 |
| FI1B1 / ELCHIGG | 300 | 69 | 1,534.5 |
| FI1B1 / ELCLOW | 300 | 172 | 7,595.7 |
| FI1B1 / ELCMED | 300 | 127 | 4,870.5 |
| FI1C1 / ELCHIGG | 300 | 249 | 8,787.9 |
| FI1C1 / ELCLOW | 300 | 253 | 10,193.4 |
| FI1C1 / ELCMED | 300 | 257 | 10,490.5 |
| FI1C2 / ELCHIGG | 300 | 296 | 10,822.3 |
| FI1C2 / ELCLOW | 300 | 79 | 3,569.0 |
| FI1C2 / ELCMED | 300 | 52 | 2,361.1 |
| FI1C5 / ELCHIGG | 300 | 300 | 11,014.5 |
| FI1C5 / ELCLOW | 300 | 221 | 8,279.7 |
| FI1C5 / ELCMED | 300 | 126 | 4,191.4 |
| FI1C6 / ELCHIGG | 300 | 266 | 10,627.4 |
| FI1C6 / ELCLOW | 300 | 75 | 2,439.5 |
| FI1C6 / ELCMED | 300 | 263 | 10,462.9 |
| FI1C7 / ELCHIGG | 300 | 143 | 4,726.9 |
| FI1C7 / ELCLOW | 300 | 189 | 7,558.0 |
| FI1C7 / ELCMED | 300 | 291 | 10,639.8 |
| FI1D5 / ELCHIGG | 300 | 202 | 6,297.6 |
| FI1D5 / ELCLOW | 300 | 211 | 8,838.3 |
| FI1D5 / ELCMED | 300 | 248 | 10,257.0 |
| FI1D7 / ELCHIGG | 300 | 276 | 9,459.2 |
| FI1D7 / ELCLOW | 300 | 133 | 5,518.7 |
| FI1D7 / ELCMED | 300 | 71 | 3,550.1 |
| FI1D8 / ELCHIGG | 300 | 286 | 10,053.9 |
| FI1D8 / ELCLOW | 300 | 249 | 9,863.1 |
| FI1D8 / ELCMED | 300 | 69 | 1,229.1 |
| FI1D9 / ELCHIGG | 300 | 130 | 4,050.1 |
| FI1D9 / ELCLOW | 300 | 90 | 5,230.6 |
| FI1D9 / ELCMED | 300 | 77 | 1,514.6 |
| FI1DA / ELCHIGG | 300 | 162 | 6,645.6 |
| FI1DA / ELCLOW | 300 | 187 | 8,789.5 |
| FI1DA / ELCMED | 300 | 211 | 8,979.9 |
| FI1DB / ELCHIGG | 300 | 96 | 4,002.4 |
| FI1DB / ELCLOW | 300 | 252 | 11,055.0 |
| FI1DB / ELCMED | 300 | 213 | 7,109.8 |
| FI1DC / ELCHIGG | 300 | 181 | 5,743.9 |
| FI1DC / ELCLOW | 300 | 273 | 9,964.7 |
| FI1DC / ELCMED | 300 | 222 | 9,279.1 |
| FI200 / ELCHIGG | 300 | 284 | 10,113.1 |
| FI200 / ELCLOW | 300 | 259 | 10,230.2 |
| FI200 / ELCMED | 300 | 61 | 3,052.4 |

- Peak equations outside the hub: 57 region/commodity pairs (expected none in the hub design)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 264; only in run: 55; only in reference: 22
| binding only in run | sum |shadow| |
|---|---|
| UCI_UP_CHPShare-IAL | 129,910.3 |
| UCI_UP_CHPShare-ICL | 94,029.0 |
| UCI_UP_CHPShare-ICU | 54,667.4 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,748.9 |
| RS_PRD_RSDFINOIL_LO | 2,362.6 |
| RS_PRD_COMFINOIL_LO | 2,345.4 |
| RS_PRD_RSDBIO_LO | 1,194.4 |
| RS_PRD_COMBIO_LO | 1,142.1 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 640.5 |
| RS_PRD_COMGAS_LO | 409.2 |
| RS_PRD_RSDGAS_LO | 372.7 |
| UCI_UP_CHPShare-IIS | 91.28 |
| RS_PRD_COMHET_LO | 78.47 |
| RS_PRD_INDFINGAS_LO | 64.09 |

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

Shadow prices differing by more than 5 %: 199; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_CAP_EEPP_natgas_CCGT | 504,031.0 | 1,318.7 | 502,712.3 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 474,794.9 | 1,269.5 | 473,525.4 |
| UC_VARU_CAP_EEPP_naturalgas_th | 472,524.7 | 2,436.8 | 470,087.8 |
| UC_VARU_CAP_EEPP_HFO_th | 196,227.0 | 702.2 | 195,524.8 |
| UC_HydroLakeSupply_CE | 217,967.0 | 35,734.3 | 182,232.7 |
| UCI_UP_CHPShare-IAL | 129,910.3 | 0 | 129,910.3 |
| UC_VARU_ACT_EEPP_natgas_OCGT | 132,196.8 | 8,790.4 | 123,406.4 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 105,618.9 | 6,902.7 | 98,716.2 |
| UC_VARU_ACT_EEPP_naturalgas_th | 102,966.1 | 8,719.1 | 94,247.0 |
| UCI_UP_CHPShare-ICL | 94,029.0 | 0 | 94,029.0 |
| UC_VARU_ACT_EEPP_HFO_th | 80,902.3 | 10,729.6 | 70,172.7 |
| UCI_UP_CHPShare-ICU | 54,667.4 | 0 | 54,667.4 |
| UC_VARU_ACT_EEPP_lignite_th | 27,533.9 | 8,299.1 | 19,234.8 |
| UC_VARU_CAP_EEPP_lignite_th | 15,885.4 | 630.4 | 15,255.0 |
| UC_VARU_CAP_EEPP_coal_th | 15,883.1 | 1,060.7 | 14,822.4 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 359 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI1C5 / 2070 / MCMCLKBYF | 0.001319 | 0 | 0.001319 |
| FI1C1 / 2070 / MCMCLKBYF | 0.001318 | 0 | 0.001318 |
| FI1C5 / 2070 / MCMCLKCCSC | 0.001302 | 0 | 0.001302 |
| FI1C1 / 2070 / MCMCLKCCSC | 0.0013 | 0 | 0.0013 |
| FI1C5 / 2070 / MCMCLKLAPP | 0.001202 | 0 | 0.001202 |
| FI / 2070 / ILMHTH | 0.0006505 | 0 | 0.0006505 |
| FI1B1 / 2070 / INFOTH | 0.0005384 | 0 | 0.0005384 |
| FI200 / 2070 / INFOTH | 0.0005384 | 0 | 0.0005384 |
| FI1D5 / 2070 / INFOTH | 0.0005384 | 0 | 0.0005384 |
| FI199 / 2070 / INFOTH | 0.0005384 | 0 | 0.0005384 |

- CST_FLOX: 0 entries differ
### investment: 866 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 20,500.9 | 9,902.3 | 10,598.6 |
| COMBATS01 | 0 | 10,588.6 | -10,588.6 |
| SELCH2PEM01 | 1,144.4 | 2,349.5 | -1,205.0 |
| SELCH2EC01 | 1,144.5 | 135.6 | 1,008.9 |
| EUIGCCWOO01 | 13,330.3 | 12,884.8 | 445.5 |
| EUCCGASCCSpos20 | 6,466.4 | 6,799.3 | -332.9 |
| TRA_Hdt_ELC_01 | 56,386.8 | 56,662.1 | -275.3 |
| TRA_Car_PIH_LoM_20pct | 29,379.9 | 29,648.3 | -268.4 |
| R_ES-SH-DH-70_ELC05 | 6,618.7 | 6,877.0 | -258.3 |
| TRA_Car_Dis_Sma_41 | 2,908.0 | 3,162.2 | -254.2 |
| TRA_Car_Elc_Sma_10 | 17,341.9 | 17,093.1 | 248.8 |
| TRA_Car_Gas_LoM_91 | 4,629.5 | 4,869.1 | -239.6 |

### fixed O&M: 711 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| SELCH2PEM01 | 431.8 | 885.4 | -453.6 |
| SELCH2EC01 | 431.8 | 51.24 | 380.6 |
| P_RSDBATS01 | 770.8 | 397.7 | 373.1 |
| P_COMBATS01 | 0 | 372.8 | -372.8 |
| TRA_Car_Elc_Sma_10 | 4,921.5 | 4,849.0 | 72.46 |
| IISELAFUR01 | 3,566.8 | 3,496.4 | 70.35 |
| CHPINDSPWOO101 | 15.74 | 82.85 | -67.11 |
| TRA_Car_PIH_LoM_20pct | 6,799.4 | 6,861.4 | -61.99 |
| EUCCGASCCSpos20 | 1,194.8 | 1,256.3 | -61.52 |
| IPPPUPMEC15 | 438.4 | 380.3 | 58.07 |
| TRA_Car_Dis_Sma_41 | 660.9 | 718.7 | -57.78 |
| TRA_Car_Gas_LoM_91 | 1,052.2 | 1,106.7 | -54.46 |

### activity: 1355 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| SELCH2PEM01_LowAF | 29.7 | 60.75 | -31.05 |
| ICLADVPRO01 | 25.5 | 55.7 | -30.21 |
| IISELAFUR01 | 1,458.4 | 1,428.5 | 29.98 |
| ICLADVPRO05 | 159.2 | 129.2 | 29.97 |
| SELCH2EC01_LowAF | 29.7 | 3.418 | 26.29 |
| EUCCGASCCSpos20 | 189.4 | 199.6 | -10.15 |
| EUIGCCWOO01 | 292.9 | 283.3 | 9.546 |
| MINBIOCRP41 | 1,598.6 | 1,607.3 | -8.752 |
| TB_INDSCO2N_FI_FI1D9 | 5.823 | 0 | 5.823 |
| IPPPUPCHE01 | 2,929.2 | 2,934.4 | -5.23 |
| ECHP_coal_thermal | 148.4 | 145.5 | 2.912 |
| TB_ICMFISCO2_FI_FI1C1 | 2.08 | 0 | 2.08 |

### flow/import: 119 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EXPOILGSL | -16,733.0 | -16,267.1 | -465.8 |
| IMPELC-SEtoFI | 6,015.9 | 6,367.7 | -351.9 |
| IMPELC-EetoFI | 1,859.9 | 1,528.3 | 331.5 |
| IMPOILGSL | 4,780.6 | 4,570.2 | 210.4 |
| IMPOILDST | 15,269.4 | 15,101.9 | 167.5 |
| EXPOILDST | -9,920.4 | -9,767.3 | -153.1 |
| MINMPPWOO1 | 115,386.7 | 115,521.8 | -135.2 |
| IMPOILCRD | 57,974.6 | 57,840.3 | 134.2 |
| EXPCO2-fromFI-coastal | 5,006.4 | 5,133.4 | -127.0 |
| IMPELC-NOtoFI | 285.7 | 230.7 | 55.01 |
| CHPINDSPWOO101 | 9.694 | 54.86 | -45.16 |
| IMPCOAHAR | 2,726.1 | 2,686.2 | 39.86 |

### capacity (sum over years): 300 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 728.0 | 371.0 | 357.0 |
| COMBATS01 | 0 | 356.8 | -356.8 |
| R_ES-SH-FL_ELC01 | 12,678.8 | 12,484.1 | 194.7 |
| R_ES-SH-DH-70_ELC05 | 4,030.3 | 4,193.1 | -162.8 |
| R_ES-SH-FL_GAS01 | 592.3 | 749.8 | -157.5 |
| TRA_Car_Elc_Sma_10 | 8,132.4 | 8,012.9 | 119.5 |
| TRA_Car_PIH_LoM_20pct | 11,485.6 | 11,590.1 | -104.5 |
| P_RSDBATS01 | 182.0 | 92.74 | 89.25 |
| P_COMBATS01 | 0 | 89.2 | -89.2 |
| R_ES-SH-SD_GAS01 | 550.4 | 632.6 | -82.2 |
| R_ES-SH-DH-70_ELC07 | 2,015.4 | 1,939.9 | 75.47 |
| R_ES-SH-DH-70_ELC04 | 102.3 | 35.78 | 66.54 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## L. Output without inputs
- Processes running with less than 20 % of their reference inputs per unit of activity: none

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
