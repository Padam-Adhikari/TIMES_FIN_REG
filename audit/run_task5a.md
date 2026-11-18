# Audit of reg_baseline-sami_2026-11-18_task5a_run2.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,529,334.37 M EUR, reference 1,529,919.88, difference -585.51 (-0.0383%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,778.1 | 144,742.3 | 35.76 |
| INV | 919,250.4 | 919,897.7 | -647.3 |
| VAR | 465,305.8 | 465,279.9 | 25.95 |
| VARX | 0.05595 | 0 | 0.05595 |

| region | objective share |
|---|---|
| FI | 1,397,480.6 |
| FI196 | 33,049.9 |
| FI1B1 | 18,179.1 |
| FI1D9 | 14,795.6 |
| FI1C5 | 12,615.3 |
| FI1C7 | 11,448.6 |
| FI19B | 7,569.9 |
| FI1D7 | 6,761.5 |
| FI198 | 6,588.3 |
| FI19A | 6,508.2 |
| FI1DB | 4,118.6 |
| FI1C1 | 3,356.7 |
| FI1C2 | 1,876.7 |
| FI1C6 | 1,873.5 |
| FI1DC | 1,625.1 |
| FI1DA | 501.5 |
| FI199 | 478.7 |
| FI1D5 | 393.0 |
| FI1D8 | 87.38 |
| FI200 | 26.34 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved
- PRC_RESID national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| EUHYDDAM00 | 1,372.1 | 1,380.6 | -8.553 |
| EEPP_PV | 42.5 | 45.46 | -2.962 |
| ECHP_coal_thermal | 99.19 | 97.15 | 2.035 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_naturalgas_CCGT | 84.14 | 84.67 | -0.529 |
| EEPP_biomass_thermal | 86.03 | 86.31 | -0.2772 |
| ECHP_HFO_thermal | 8.106 | 8.341 | -0.2358 |
| EEPP_coal_thermal | 40.33 | 40.22 | 0.114 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05847 |
| EEPP_naturalgas_thermal | 0.06166 | 0.09998 | -0.03832 |
| ECHP_LFO_thermal | 0 | 0.02023 | -0.02023 |
| ECHP_naturalgas_thermal | 2.218 | 2.229 | -0.01054 |
| ECHP_lignite_thermal | 29.84 | 29.84 | -0.003839 |
| EEPP_windOFF | 23.58 | 23.59 | -0.002007 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08294 | 0.08335 | -0.0004046 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | -1.849e-05 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | -2.806e-07 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | -2.707e-07 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | -2.541e-07 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | -1.867e-07 |
| EEPP_HFO_thermal | 2.141 | 2.141 | 1.994e-08 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 2.057e-09 |

By class and year: 68 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_coal_thermal / 2020 | 14.07 | 12.65 | 1.419 |
| EUHYDDAM00 / 2063 | 53.97 | 55.04 | -1.065 |
| EUHYDDAM00 / 2068 | 54.02 | 55.04 | -1.016 |
| EUHYDDAM00 / 2070 | 54.06 | 55.03 | -0.9654 |
| EUHYDDAM00 / 2065 | 54.08 | 55.04 | -0.9557 |
| EUHYDDAM00 / 2030 | 54.29 | 55.04 | -0.749 |
| EUHYDDAM00 / 2060 | 54.36 | 55.04 | -0.6704 |
| EUHYDDAM00 / 2033 | 54.26 | 54.9 | -0.6457 |
| ECHP_coal_thermal / 2018 | 38.72 | 38.11 | 0.6169 |
| EUHYDDAM00 / 2058 | 54.46 | 55.04 | -0.5736 |
| EUHYDDAM00 / 2050 | 54.47 | 55.04 | -0.5664 |
| EUHYDDAM00 / 2055 | 54.47 | 55.04 | -0.5645 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,282.9 |
| FI198 | 76.63 |
| FI199 | 157.4 |
| FI19A | 265.7 |
| FI19B | 92.99 |
| FI1B1 | 249.2 |
| FI1C1 | 122.2 |
| FI1C2 | 49.98 |
| FI1C5 | 237.0 |
| FI1C6 | 30.53 |
| FI1C7 | 56.05 |
| FI1D5 | 164.8 |
| FI1D7 | 590.8 |
| FI1D8 | 92.73 |
| FI1D9 | 732.1 |
| FI1DA | 73 |
| FI1DB | 23.37 |
| FI1DC | 97.42 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.6 | 337.6 | -0.03609 |
| 2013 | 292.2 | 292.1 | 0.09899 |
| 2015 | 319.9 | 320.1 | -0.1835 |
| 2018 | 373.2 | 373.1 | 0.07409 |
| 2020 | 315.4 | 314.9 | 0.564 |
| 2023 | 381.6 | 380.3 | 1.347 |
| 2025 | 423.2 | 423.2 | -0.01846 |
| 2028 | 478.7 | 478.3 | 0.4804 |
| 2030 | 507.8 | 507.3 | 0.4775 |
| 2033 | 443.1 | 442.2 | 0.9187 |
| 2035 | 464.9 | 464.2 | 0.7679 |
| 2038 | 522.2 | 521.6 | 0.5712 |
| 2040 | 573.8 | 573.8 | 0.03936 |
| 2043 | 623.5 | 623.9 | -0.4148 |
| 2045 | 643.6 | 644.7 | -1.097 |
| 2048 | 669.8 | 670.5 | -0.6736 |
| 2050 | 708.5 | 708.1 | 0.4848 |
| 2053 | 719.7 | 719.1 | 0.6627 |
| 2055 | 728.4 | 727.8 | 0.5697 |
| 2058 | 750.1 | 749.1 | 0.9312 |
| 2060 | 763.4 | 763.8 | -0.3556 |
| 2063 | 780.0 | 779.1 | 0.9802 |
| 2065 | 789.4 | 788.8 | 0.6606 |
| 2068 | 805.7 | 805.1 | 0.542 |
| 2070 | 817.3 | 816.6 | 0.7128 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 198.1 | 200.0 | -1.866 |
| 2013 | 179.6 | 179.3 | 0.2994 |
| 2015 | 131.4 | 131.1 | 0.2699 |
| 2018 | 133.5 | 132.5 | 1.054 |
| 2020 | 147.6 | 145.3 | 2.247 |
| 2023 | 134.5 | 134.0 | 0.4803 |
| 2025 | 122.5 | 124.4 | -1.88 |
| 2028 | 212.3 | 212.8 | -0.5161 |
| 2030 | 232.3 | 230.4 | 1.921 |
| 2033 | 168.9 | 168.8 | 0.07774 |
| 2035 | 177.4 | 177.8 | -0.4083 |
| 2038 | 189.3 | 190.0 | -0.7226 |
| 2040 | 203.6 | 204.3 | -0.7038 |
| 2043 | 223.5 | 224.7 | -1.222 |
| 2045 | 230.7 | 229.2 | 1.503 |
| 2048 | 235.2 | 235.1 | 0.1246 |
| 2050 | 238.6 | 239.0 | -0.4047 |
| 2053 | 238.1 | 238.4 | -0.3195 |
| 2055 | 243.4 | 242.9 | 0.5463 |
| 2058 | 249.8 | 249.0 | 0.7995 |
| 2060 | 257.6 | 257.1 | 0.5493 |
| 2063 | 262.9 | 262.1 | 0.7964 |
| 2065 | 264.8 | 263.8 | 0.9614 |
| 2068 | 269.4 | 268.4 | 0.9263 |
| 2070 | 272.0 | 271.1 | 0.9143 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 4.708 | 4.705 |
| 2018 | 12.93 | 0.4363 |
| 2025 | 8.181 | 0.2771 |
| 2033 | 35.57 | 1.204 |
| 2040 | 48.96 | 1.657 |
| 2048 | 28.54 | 0.966 |
| 2055 | 28.39 | 0.9388 |
| 2063 | 30.06 | 0.9925 |
| 2070 | 29.13 | 0.9601 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.116 | 0.7187 |
| 2018 | 21.62 | 1.704 |
| 2025 | 239.1 | 18.84 |
| 2033 | 23.63 | 1.591 |
| 2040 | 31.03 | 1.785 |
| 2048 | 15.54 | 0.7982 |
| 2055 | 16.67 | 0.7897 |
| 2063 | 17.25 | 0.8194 |
| 2070 | 17.02 | 0.7046 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,105.1 | 0.128 |
| ICMFISCO2 | 10,394.2 | 0 |
| ELCHIG | 4,403.0 | 0.01566 |
| INDELC | 3.393 | 4,069.8 |
| IPPHTH | 9.159 | 4,004.4 |
| OILCRD | 0.1429 | 3,857.5 |
| BIOOILFS | 0.5031 | 3,460.9 |
| GreenCert-ELC | 3,343.4 | 2.824 |
| BIOHVO | 2,986.9 | 0.5034 |
| INDBLQ | 2,546.3 | 1.963 |
| OILDST | 1,560.0 | 515.6 |
| OILGSL | 1,386.1 | 0.1455 |
| ELCHYD | 2.62 | 1,374.9 |
| ELCWOO | 2.571 | 1,272.0 |
| ELCWIN | 4.068 | 1,095.8 |
| INDBIO | 259.2 | 643.4 |
| MPPWOO | 0.01685 | 771.0 |
| HETHTH | 758.8 | 0.01499 |
| ELCNUC | 0.00527 | 751.8 |
| OILHFO | 281.6 | 165.4 |
| ELCCOH | 0.1219 | 445.0 |
| INDHTH | 1.072 | 443.5 |
| OILNEU | 0.1467 | 411.5 |
| INDCOK | 4.565 | 348.6 |
| INDLFO | 3.247 | 305.9 |
| INDCOA | 3.674 | 299.0 |
| INDGAS | 13.88 | 287.7 |
| OILNAP | 0.2046 | 290.8 |
| INDRFG | 0.1474 | 289.8 |
| INDHFO | 3.425 | 270.0 |
| ELCGAS | 14.14 | 221.8 |
| IOIHTH | 20.56 | 214.9 |
| SUPRPG | 0.1536 | 219.5 |
| OILKER | 202.1 | 0.1553 |
| COALIG | 0.1384 | 189.7 |
| OILOTH | 33.72 | 119.6 |
| BIOWOO | 0 | 151.4 |
| ELCCOL | 0.3546 | 149.3 |
| OILLPG | 13.04 | 121.2 |
| ICHHTH | 4.597 | 124.6 |
| COACOK | 127.7 | 0.157 |
| INDHH2 | 63.4 | 63.17 |
| MPPRYC | 0.01867 | 118.6 |
| BIOGAS | 102.3 | 13.73 |
| OILRFG | 62.33 | 38.21 |
| GASNAT | 17.69 | 72.1 |
| INFHTH | 30.58 | 46.95 |
| MISSNT | 0.03359 | 65.58 |
| MPPGYP | 0 | 63.92 |
| ELCSOL | 4.479 | 50.09 |
| SUPRPP | 0.1645 | 50.97 |
| INDLPG | 4.948 | 45.46 |
| ELCMED | 0.001268 | 45.4 |
| GASP2GB | 19.57 | 24.35 |
| INMHTH | 21.48 | 22.22 |
| GASCOG | 43.29 | 0.1676 |
| AGRGAS | 21.35 | 21.35 |
| GASP2G | 20.92 | 20.92 |
| MISRIR | 38.28 | 0 |
| ICMPARA | 37.82 | 0.1586 |
| ELCHFO | 4.583 | 32.97 |
| MISOXY | 0 | 27.68 |
| INDCOG | 0.3061 | 26.88 |
| ELCLOW | 0.001339 | 26.51 |
| COAHAR | 0.1911 | 22.61 |
| INDSLU | 5.074 | 17.43 |
| MISORE | 0 | 20.57 |
| MLMSTN | 0 | 20.19 |
| IIS | 18.5 | 0.08069 |
| SUPGAS | 0.7976 | 16.96 |
| MISBFS | 8.252 | 8.084 |
| BRFH2 | 0.5108 | 15.63 |
| INDMUN | 3.653 | 11.1 |
| MPPKAO | 0 | 14.53 |
| INDCOL | 4.762 | 8.604 |
| MISCST | 7.736 | 3.311 |
| ELCDST | 4.627 | 5.242 |
| ETSCO2 | 4.759 | 4.761 |
| MISSCR | 0 | 9.287 |
| ELCCO2N | 0.002606 | 8.781 |
| GASBFG | 7.924 | 0.5496 |
| SYNH2CT | 7.464 | 0 |
| REFHTH | 0 | 7.425 |
| MPPNOH | 0 | 5.736 |
| SUPBIO | 0.1948 | 5.164 |
| IALHTH | 1.43 | 3.433 |
| MPPOXY | 0 | 3.278 |
| IISHTH | 0.5764 | 1.283 |
| IGH | 1.732 | 0.03939 |
| SUPELC | 0.4019 | 1.071 |
| MALBAU | 0.2393 | 1.125 |
| MISPLT | 0.05828 | 1.165 |
| MGHRYC | 0 | 1.174 |
| BIOPROP | 0.6278 | 0.5287 |
| ICMLC3 | 0.5506 | 0.5506 |
| INDCOB | 0.42 | 0.5588 |
| RENGEO | 0 | 0.7303 |
| BRFCA3 | 0 | 0.7167 |
| ICLHTH | 0.2385 | 0.4638 |
| INDBFG | 0.02295 | 0.6553 |
| GreenCert-FIN | 0.2591 | 0.311 |
| GASIIS | 0.268 | 0.3 |
| OILFDS | 0.2699 | 0.281 |
| GASCOP | 0.2476 | 0.2476 |
| ICUHTH | 0 | 0.4682 |
| MALSCR | 0 | 0.4548 |
| MCUORE | 0 | 0.3679 |
| MISQLI | 0 | 0.2985 |
| ICU | 0.2134 | 0.04466 |
| SUPHTH | 0 | 0.1505 |
| MCUSCR | 0.06225 | 0.0555 |
| MCUSCU | 0.05789 | 0.05895 |
| MISRFC | 0.05828 | 0.05828 |
| RENSOL | 0 | 0.1153 |
| IGF | 0 | 1.165e-08 |

- Back-and-forth on the same link, year and timeslice: 36776 cases, volume 335.9
| link / year / ts | min(imp, exp) |
|---|---|
| TB_MISCST_FI_FI1C5 / 2020 / ANNUAL | 0.2767 |
| TB_MISCST_FI_FI1D9 / 2020 / ANNUAL | 0.231 |
| TB_MISCST_FI_FI1D7 / 2020 / ANNUAL | 0.2154 |
| TB_MISCST_FI_FI1C2 / 2020 / ANNUAL | 0.1423 |
| TB_INDCOL_FI_FI200 / 2070 / ANNUAL | 0.05845 |
| TB_INDCOL_FI_FI1D5 / 2070 / ANNUAL | 0.05845 |
| TB_INDCOL_FI_FI1D7 / 2070 / ANNUAL | 0.05845 |
| TB_INDCOL_FI_FI1C5 / 2070 / ANNUAL | 0.05845 |
| TB_INDCOL_FI_FI1DA / 2070 / ANNUAL | 0.05845 |
| TB_INDCOL_FI_FI1C7 / 2070 / ANNUAL | 0.05845 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 131,224.6, reference 130,244.3 (+0.75%); 25 years differ >0.1 %
- ETSCO2: produced, all years: run 343,269.7, reference 343,808.2 (-0.16%); 18 years differ >0.1 %
- INDCO2N: produced, all years: run 124,834.1, reference 126,331.9 (-1.19%); 25 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,166.6, reference 11,202.8 (-0.32%); 21 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,083.4, reference 6,065.4 (+0.30%); 19 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'ELCCO2N': 72685.3, 'ETSCO2': 180822.5, 'GreenCert-ELC': -4.5} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 78 | 792.2 |
| FI / ELCHIGG | 300 | 92 | 32.29 |
| FI / ELCLOW | 300 | 62 | 133.4 |
| FI / ELCMED | 300 | 86 | 11.78 |
| FI / HETHTH | 300 | 2 | 2.061e-06 |
| FI196 / ELCLOW | 300 | 200 | 8,459.8 |
| FI196 / ELCMED | 300 | 169 | 5,498.5 |
| FI198 / ELCLOW | 300 | 246 | 11,277.1 |
| FI198 / ELCMED | 300 | 246 | 10,422.7 |
| FI199 / ELCLOW | 300 | 140 | 6,142.4 |
| FI199 / ELCMED | 300 | 150 | 6,102.8 |
| FI19A / ELCLOW | 300 | 160 | 8,367.5 |
| FI19A / ELCMED | 300 | 152 | 7,394.5 |
| FI19B / ELCLOW | 300 | 182 | 9,228.7 |
| FI19B / ELCMED | 300 | 200 | 8,860.8 |
| FI1B1 / ELCLOW | 300 | 83 | 4,595.2 |
| FI1B1 / ELCMED | 300 | 77 | 3,642.6 |
| FI1C1 / ELCLOW | 300 | 75 | 2,795.5 |
| FI1C1 / ELCMED | 300 | 71 | 2,147.2 |
| FI1C2 / ELCLOW | 300 | 175 | 8,148.0 |
| FI1C2 / ELCMED | 300 | 161 | 6,811.1 |
| FI1C5 / ELCLOW | 300 | 133 | 5,361.3 |
| FI1C5 / ELCMED | 300 | 113 | 4,624.8 |
| FI1C6 / ELCLOW | 300 | 167 | 6,140.6 |
| FI1C6 / ELCMED | 300 | 150 | 5,285.6 |
| FI1C7 / ELCLOW | 300 | 190 | 9,280.2 |
| FI1C7 / ELCMED | 300 | 188 | 8,080.3 |
| FI1D5 / ELCLOW | 300 | 203 | 9,536.1 |
| FI1D5 / ELCMED | 300 | 202 | 8,356.6 |
| FI1D7 / ELCLOW | 300 | 291 | 13,675.9 |
| FI1D7 / ELCMED | 300 | 294 | 12,848.3 |
| FI1D8 / ELCLOW | 300 | 153 | 9,587.8 |
| FI1D8 / ELCMED | 300 | 150 | 9,329.0 |
| FI1D9 / ELCLOW | 300 | 107 | 4,304.8 |
| FI1D9 / ELCMED | 300 | 83 | 4,101.4 |
| FI1DA / ELCLOW | 300 | 127 | 7,537.3 |
| FI1DA / ELCMED | 300 | 122 | 6,154.0 |
| FI1DB / ELCLOW | 300 | 250 | 11,362.4 |
| FI1DB / ELCMED | 300 | 250 | 10,719.9 |
| FI1DC / ELCLOW | 300 | 186 | 8,138.2 |
| FI1DC / ELCMED | 300 | 188 | 6,937.4 |
| FI200 / ELCLOW | 300 | 43 | 2,648.2 |
| FI200 / ELCMED | 300 | 45 | 2,747.1 |

- Peak equations outside the hub: 38 region/commodity pairs (expected none in the hub design)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 264; only in run: 53; only in reference: 22
| binding only in run | sum |shadow| |
|---|---|
| UCI_UP_CHPShare-IAL | 92,956.3 |
| UCI_UP_CHPShare-ICL | 73,200.5 |
| UCI_UP_CHPShare-ICU | 43,232.9 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,730.4 |
| RS_PRD_RSDFINOIL_LO | 2,359.2 |
| RS_PRD_COMFINOIL_LO | 2,341.5 |
| RS_PRD_RSDBIO_LO | 1,192.1 |
| RS_PRD_COMBIO_LO | 1,140.0 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 639.2 |
| RS_PRD_COMGAS_LO | 409.2 |
| RS_PRD_RSDGAS_LO | 373.1 |
| UCI_UP_CHPShare-IIS | 92.12 |
| RS_PRD_COMHET_LO | 78.7 |
| RS_PRD_INDFINGAS_LO | 63.8 |

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

Shadow prices differing by more than 5 %: 196; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_CAP_EEPP_natgas_CCGT | 380,749.3 | 1,318.7 | 379,430.6 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 353,523.0 | 1,269.5 | 352,253.6 |
| UC_VARU_CAP_EEPP_naturalgas_th | 353,945.9 | 2,436.8 | 351,509.0 |
| UC_HydroLakeSupply_CE | 273,004.8 | 35,734.3 | 237,270.5 |
| UC_VARU_CAP_EEPP_HFO_th | 154,470.3 | 702.2 | 153,768.0 |
| UC_VARU_ACT_EEPP_natgas_OCGT | 132,086.3 | 8,790.4 | 123,295.9 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 105,392.5 | 6,902.7 | 98,489.7 |
| UC_VARU_ACT_EEPP_naturalgas_th | 102,780.8 | 8,719.1 | 94,061.6 |
| UCI_UP_CHPShare-IAL | 92,956.3 | 0 | 92,956.3 |
| UCI_UP_CHPShare-ICL | 73,200.5 | 0 | 73,200.5 |
| UC_VARU_ACT_EEPP_HFO_th | 80,657.9 | 10,729.6 | 69,928.2 |
| UCI_UP_CHPShare-ICU | 43,232.9 | 0 | 43,232.9 |
| UC_VARU_ACT_EEPP_lignite_th | 26,909.2 | 8,299.1 | 18,610.1 |
| UC_VARU_CAP_EEPP_lignite_th | 12,491.2 | 630.4 | 11,860.8 |
| UC_VARU_CAP_EEPP_coal_th | 12,497.1 | 1,060.7 | 11,436.4 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 403 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI1C5 / 2070 / MCMCLKBYF | 0.002735 | 0 | 0.002735 |
| FI1C1 / 2070 / MCMCLKBYF | 0.002733 | 0 | 0.002733 |
| FI1C5 / 2070 / MCMCLKCCSC | 0.002697 | 0 | 0.002697 |
| FI1C1 / 2070 / MCMCLKCCSC | 0.002693 | 0 | 0.002693 |
| FI1C5 / 2070 / MCMCLKLAPP | 0.002495 | 0 | 0.002495 |
| FI / 2070 / ILMHTH | 0.001206 | 0 | 0.001206 |
| FI1C5 / 2065 / MCMCLKBYF | 0.001081 | 0 | 0.001081 |
| FI1C1 / 2065 / MCMCLKBYF | 0.001079 | 0 | 0.001079 |
| FI1B1 / 2070 / INFOTH | 0.001078 | 0 | 0.001078 |
| FI200 / 2070 / INFOTH | 0.001078 | 0 | 0.001078 |

- CST_FLOX: 0 entries differ
### investment: 896 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| COMBATS01 | 0 | 10,588.6 | -10,588.6 |
| RSDBATS01 | 20,282.8 | 9,902.3 | 10,380.6 |
| SELCH2PEM01 | 1,138.3 | 2,349.5 | -1,211.2 |
| SELCH2EC01 | 1,138.3 | 135.6 | 1,002.7 |
| EUIGCCWOO01 | 13,355.4 | 12,884.8 | 470.6 |
| EUCCGASCCSpos20 | 6,456.5 | 6,799.3 | -342.8 |
| TRA_Hdt_ELC_01 | 56,365.1 | 56,662.1 | -297.0 |
| TRA_Car_PIH_LoM_20pct | 29,380.3 | 29,648.3 | -268.0 |
| TRA_Car_Dis_Sma_41 | 2,909.2 | 3,162.2 | -253.1 |
| TRA_Car_Elc_Sma_10 | 17,344.0 | 17,093.1 | 250.9 |
| TRA_Car_Gas_LoM_91 | 4,627.0 | 4,869.1 | -242.1 |
| TRA_Car_Dis_LoM_51 | 570.0 | 334.9 | 235.1 |

### fixed O&M: 736 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| SELCH2PEM01 | 429.5 | 885.4 | -455.9 |
| SELCH2EC01 | 429.5 | 51.24 | 378.2 |
| P_COMBATS01 | 0 | 372.8 | -372.8 |
| P_RSDBATS01 | 762.7 | 397.7 | 365.0 |
| TRA_Car_Elc_Sma_10 | 4,922.1 | 4,849.0 | 73.1 |
| IISELAFUR01 | 3,567.9 | 3,496.4 | 71.42 |
| CHPINDSPWOO101 | 15.83 | 82.85 | -67.01 |
| EUCCGASCCSpos20 | 1,193.0 | 1,256.3 | -63.37 |
| TRA_Car_PIH_LoM_20pct | 6,799.5 | 6,861.4 | -61.9 |
| IPPPUPMEC15 | 438.4 | 380.3 | 58.07 |
| TRA_Car_Dis_Sma_41 | 661.2 | 718.7 | -57.51 |
| TRA_Car_Gas_LoM_91 | 1,051.6 | 1,106.7 | -55.02 |

### activity: 1239 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| SELCH2PEM01_LowAF | 29.45 | 60.75 | -31.3 |
| IISELAFUR01 | 1,458.7 | 1,428.5 | 30.28 |
| ICLADVPRO01 | 25.62 | 55.7 | -30.09 |
| ICLADVPRO05 | 159.1 | 129.2 | 29.85 |
| SELCH2EC01_LowAF | 29.45 | 3.418 | 26.03 |
| EUCCGASCCSpos20 | 189.3 | 199.6 | -10.3 |
| EUIGCCWOO01 | 293.4 | 283.3 | 10.04 |
| MINBIOCRP41 | 1,598.6 | 1,607.3 | -8.751 |
| TB_INDSCO2N_FI_FI1D9 | 5.821 | 0 | 5.821 |
| IPPPUPCHE01 | 2,929.6 | 2,934.4 | -4.735 |
| ECHP_coal_thermal | 148.5 | 145.5 | 2.991 |
| TB_ICMFISCO2_FI_FI1C1 | 2.079 | 0 | 2.079 |

### flow/import: 158 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EXPOILGSL | -16,759.5 | -16,267.1 | -492.4 |
| IMPELC-SEtoFI | 6,084.6 | 6,367.7 | -283.2 |
| IMPELC-EetoFI | 1,792.1 | 1,528.3 | 263.7 |
| IMPOILGSL | 4,793.3 | 4,570.2 | 223.1 |
| IMPOILDST | 15,273.2 | 15,101.9 | 171.3 |
| IMPOILCRD | 58,009.2 | 57,840.3 | 168.9 |
| EXPOILDST | -9,895.8 | -9,767.3 | -128.5 |
| MINMPPWOO1 | 115,399.5 | 115,521.8 | -122.3 |
| EXPCO2-fromFI-coastal | 5,011.6 | 5,133.4 | -121.7 |
| IMPELC-NOtoFI | 280.7 | 230.7 | 49.99 |
| CHPINDSPWOO101 | 9.759 | 54.86 | -45.1 |
| EXPOILKER | -1,209.0 | -1,176.6 | -32.37 |

### capacity (sum over years): 322 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| COMBATS01 | 0 | 356.8 | -356.8 |
| RSDBATS01 | 720.3 | 371.0 | 349.3 |
| R_ES-SH-FL_ELC01 | 12,704.3 | 12,484.1 | 220.3 |
| R_ES-SH-FL_GAS01 | 565.5 | 749.8 | -184.3 |
| R_ES-SH-DH-70_ELC05 | 4,071.3 | 4,193.1 | -121.8 |
| TRA_Car_Elc_Sma_10 | 8,133.4 | 8,012.9 | 120.5 |
| TRA_Car_PIH_LoM_20pct | 11,485.7 | 11,590.1 | -104.4 |
| P_COMBATS01 | 0 | 89.2 | -89.2 |
| P_RSDBATS01 | 180.1 | 92.74 | 87.33 |
| R_ES-SH-DH-70_ELC07 | 2,002.5 | 1,939.9 | 62.54 |
| TRA_Car_Elc_Exe_10 | 14,357.8 | 14,414.0 | -56.27 |
| R_ES-SH-FL_ELC05 | 207.7 | 261.9 | -54.18 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## L. Output without inputs
- Processes running with less than 20 % of their reference inputs per unit of activity: none

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
