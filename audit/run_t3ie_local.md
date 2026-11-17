# Audit of t3ie.gdx vs baseline-new.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,529,551.00 M EUR, reference 1,529,919.88, difference -368.88 (-0.0241%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,719.8 | 144,742.3 | -22.48 |
| INV | 919,682.9 | 919,897.7 | -214.8 |
| VAR | 465,148.3 | 465,279.9 | -131.6 |
| VARX | 0.002296 | 0 | 0.002296 |

| region | objective share |
|---|---|
| FI | 1,486,020.7 |
| FI196 | 24,525.6 |
| FI1D9 | 8,102.7 |
| FI1B1 | 6,210.9 |
| FI1C1 | 900.0 |
| FI1C5 | 694.5 |
| FI19A | 644.5 |
| FI19B | 535.6 |
| FI1DA | 386.7 |
| FI1C2 | 329.1 |
| FI199 | 283.4 |
| FI1D5 | 245.2 |
| FI198 | 231.2 |
| FI1D7 | 167.4 |
| FI1DB | 84.92 |
| FI1C6 | 64.01 |
| FI1D8 | 53.32 |
| FI1DC | 33.63 |
| FI1C7 | 30.61 |
| FI200 | 7.078 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| EUHYDDAM00 | 1,374.3 | 1,380.6 | -6.339 |
| EEPP_PV | 42.5 | 45.46 | -2.962 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_coal_thermal | 96.73 | 97.15 | -0.4263 |
| EEPP_biomass_thermal | 86.03 | 86.31 | -0.2743 |
| ECHP_naturalgas_CCGT | 84.42 | 84.67 | -0.2479 |
| EEPP_coal_thermal | 40.14 | 40.22 | -0.07279 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05749 |
| EEPP_naturalgas_thermal | 0.06448 | 0.09998 | -0.0355 |
| ECHP_HFO_thermal | 8.316 | 8.341 | -0.02578 |
| ECHP_LFO_thermal | 0.006176 | 0.02023 | -0.01405 |
| ECHP_naturalgas_thermal | 2.223 | 2.229 | -0.005654 |
| EEPP_windOFF | 23.59 | 23.59 | -0.00195 |
| ECHP_lignite_thermal | 29.84 | 29.84 | -0.00131 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08296 | 0.08335 | -0.0003844 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | -7.081e-06 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | -4.598e-08 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | -4.488e-08 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | -4.304e-08 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | -3.127e-08 |
| EEPP_HFO_thermal | 2.141 | 2.141 | 2.215e-09 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 2.287e-10 |

By class and year: 67 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| EUHYDDAM00 / 2063 | 53.8 | 55.04 | -1.236 |
| EUHYDDAM00 / 2070 | 54.07 | 55.03 | -0.9606 |
| EUHYDDAM00 / 2068 | 54.08 | 55.04 | -0.9543 |
| EUHYDDAM00 / 2065 | 54.14 | 55.04 | -0.8976 |
| EUHYDDAM00 / 2030 | 54.27 | 55.04 | -0.7604 |
| EUHYDDAM00 / 2033 | 54.21 | 54.9 | -0.6945 |
| EUHYDDAM00 / 2060 | 54.44 | 55.04 | -0.5988 |
| ECHP_coal_thermal / 2018 | 37.85 | 38.11 | -0.2556 |
| EEPP_PV / 2023 | 2.688 | 2.932 | -0.2439 |
| EEPP_PV / 2040 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2038 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2035 | 3.564 | 3.796 | -0.2319 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,283.0 |
| FI198 | 76.78 |
| FI199 | 157.5 |
| FI19A | 265.0 |
| FI19B | 93.23 |
| FI1B1 | 248.7 |
| FI1C1 | 121.4 |
| FI1C2 | 50 |
| FI1C5 | 237.2 |
| FI1C6 | 30.59 |
| FI1C7 | 56.22 |
| FI1D5 | 165.0 |
| FI1D7 | 591.0 |
| FI1D8 | 92.91 |
| FI1D9 | 732.3 |
| FI1DA | 73.02 |
| FI1DB | 23.46 |
| FI1DC | 97.6 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.5 | 337.6 | -0.1253 |
| 2013 | 291.9 | 292.1 | -0.1832 |
| 2015 | 319.8 | 320.1 | -0.2633 |
| 2018 | 372.6 | 373.1 | -0.5154 |
| 2020 | 314.3 | 314.9 | -0.5347 |
| 2023 | 379.7 | 380.3 | -0.6089 |
| 2025 | 423.0 | 423.2 | -0.2598 |
| 2028 | 478.2 | 478.3 | -0.1085 |
| 2030 | 507.2 | 507.3 | -0.1262 |
| 2033 | 442.3 | 442.2 | 0.07696 |
| 2035 | 464.2 | 464.2 | 0.02391 |
| 2038 | 521.6 | 521.6 | 0.03162 |
| 2040 | 573.6 | 573.8 | -0.1624 |
| 2043 | 623.3 | 623.9 | -0.6108 |
| 2045 | 643.7 | 644.7 | -0.9604 |
| 2048 | 669.6 | 670.5 | -0.8468 |
| 2050 | 707.9 | 708.1 | -0.1698 |
| 2053 | 719.0 | 719.1 | -0.04313 |
| 2055 | 727.9 | 727.8 | 0.106 |
| 2058 | 749.3 | 749.1 | 0.1733 |
| 2060 | 763.9 | 763.8 | 0.1316 |
| 2063 | 778.9 | 779.1 | -0.1336 |
| 2065 | 788.7 | 788.8 | -0.137 |
| 2068 | 805.2 | 805.1 | 0.03993 |
| 2070 | 816.7 | 816.6 | 0.1303 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 200.0 | 200.0 | 0.03802 |
| 2013 | 180.5 | 179.3 | 1.114 |
| 2015 | 132.2 | 131.1 | 1.094 |
| 2018 | 133.2 | 132.5 | 0.7341 |
| 2020 | 146.2 | 145.3 | 0.8836 |
| 2023 | 133.8 | 134.0 | -0.18 |
| 2025 | 134.0 | 124.4 | 9.665 |
| 2028 | 212.4 | 212.8 | -0.4656 |
| 2030 | 230.9 | 230.4 | 0.4912 |
| 2033 | 168.9 | 168.8 | 0.04806 |
| 2035 | 177.7 | 177.8 | -0.09245 |
| 2038 | 189.9 | 190.0 | -0.1097 |
| 2040 | 203.8 | 204.3 | -0.4996 |
| 2043 | 224.4 | 224.7 | -0.2836 |
| 2045 | 229.2 | 229.2 | -0.0008702 |
| 2048 | 234.9 | 235.1 | -0.161 |
| 2050 | 239.3 | 239.0 | 0.3348 |
| 2053 | 238.8 | 238.4 | 0.3623 |
| 2055 | 243.2 | 242.9 | 0.3856 |
| 2058 | 249.5 | 249.0 | 0.4995 |
| 2060 | 257.3 | 257.1 | 0.217 |
| 2063 | 262.5 | 262.1 | 0.3701 |
| 2065 | 264.3 | 263.8 | 0.4471 |
| 2068 | 268.9 | 268.4 | 0.4555 |
| 2070 | 271.5 | 271.1 | 0.4519 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 4.663 | 4.663 |
| 2018 | 12.39 | 0.4194 |
| 2025 | 4.559 | 0.1545 |
| 2033 | 35.63 | 1.206 |
| 2040 | 48.52 | 1.642 |
| 2048 | 28.62 | 0.9687 |
| 2055 | 28.24 | 0.9334 |
| 2063 | 29.89 | 0.9869 |
| 2070 | 29.21 | 0.9627 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.111 | 9.111 |
| 2018 | 21.41 | 21.41 |
| 2025 | 266.9 | 266.9 |
| 2033 | 23.79 | 23.79 |
| 2040 | 31.13 | 31.13 |
| 2048 | 16.28 | 16.28 |
| 2055 | 16.56 | 16.56 |
| 2063 | 17.27 | 17.27 |
| 2070 | 17.07 | 17.07 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,102.3 | 0 |
| ELCHIG | 4,403.1 | 0.002809 |
| GreenCert-ELC | 3,325.1 | 0.3327 |
| ELCHYD | 0.3951 | 1,374.8 |
| ELCWOO | 0.4381 | 1,269.9 |
| ELCWIN | 0.6747 | 1,092.3 |
| HETHTH | 754.9 | 0.002451 |
| ELCNUC | 0 | 751.8 |
| ELCCOH | 0.02058 | 435.8 |
| INDCOK | 0.0004998 | 310.9 |
| INDCOA | 2.49e-07 | 274.0 |
| ELCGAS | 2.415 | 210.5 |
| ELCCOL | 0.05971 | 149.0 |
| MISSNT | 0 | 82.73 |
| MISRIR | 53.91 | 0 |
| ELCSOL | 0.7261 | 46.25 |
| ELCHFO | 0.7766 | 29.74 |
| INDBIO | 0.04049 | 25.56 |
| MISOXY | 0 | 23.74 |
| INDBFG | 10.75 | 10.84 |
| INDELC | 0.02933 | 13.36 |
| MISBFS | 6.376 | 0.02585 |
| MISPLT | 0 | 2.387 |
| ELCDST | 0.7894 | 1.208 |
| ETSCO2 | 0.8031 | 0.803 |
| ELCCO2N | 0.0004472 | 1.491 |
| IISHTH | 0.06479 | 0.06479 |
| GreenCert-FIN | 0.0347 | 0.09455 |
| GASBFG | 0.05215 | 0.05318 |
| GASIIS | 0.04573 | 0.0525 |
| INDHFO | 0.047 | 0.04753 |
| GASCOP | 0.04248 | 0.04248 |

- Back-and-forth on the same link, year and timeslice: 4941 cases, volume 18.55
| link / year / ts | min(imp, exp) |
|---|---|
| TB_INDBFG_FI_FI1D9 / 2025 / ANNUAL | 10.75 |
| TB_ETSCO2_FI_FI1D9 / 2070 / ANNUAL | 0.009291 |
| TB_ETSCO2_FI_FI1C2 / 2070 / ANNUAL | 0.009289 |
| TB_ETSCO2_FI_FI1C5 / 2070 / ANNUAL | 0.009289 |
| TB_ETSCO2_FI_FI1C6 / 2070 / ANNUAL | 0.009289 |
| TB_ETSCO2_FI_FI1B1 / 2070 / ANNUAL | 0.009289 |
| TB_ETSCO2_FI_FI1C1 / 2070 / ANNUAL | 0.009289 |
| TB_ETSCO2_FI_FI199 / 2070 / ANNUAL | 0.009289 |
| TB_ETSCO2_FI_FI1DB / 2070 / ANNUAL | 0.009289 |
| TB_ETSCO2_FI_FI19A / 2070 / ANNUAL | 0.009289 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 131,224.1, reference 130,244.3 (+0.75%); 19 years differ >0.1 %
- ETSCO2: produced, all years: run 343,326.2, reference 343,808.2 (-0.14%); 16 years differ >0.1 %
- INDCO2N: produced, all years: run 125,038.5, reference 126,331.9 (-1.02%); 22 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,210.6, reference 11,202.8 (+0.07%); 11 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,065.9, reference 6,065.4 (+0.01%); 18 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'ETSCO2': 132295.0, 'GreenCert-ELC': -4.5, 'ELCCO2N': 71853.6} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 59 | 790.9 |
| FI / ELCHIGG | 300 | 39 | 33.29 |
| FI / ELCLOW | 300 | 15 | 134.4 |
| FI / ELCMED | 300 | 33 | 11.84 |
| FI / HETHTH | 300 | 0 | 0 |

- Peak equations outside the hub: 0 region/commodity pairs (none, as intended)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 264; only in run: 35; only in reference: 22
| binding only in run | sum |shadow| |
|---|---|
| UCI_UP_CHPShare-ICL | 85,384.6 |
| UCI_UP_CHPShare-ICU | 71,386.6 |
| UCI_UP_CHPShare-IAL | 26,014.0 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,674.6 |
| RS_PRD_RSDFINOIL_LO | 2,368.6 |
| RS_PRD_COMFINOIL_LO | 2,348.6 |
| RS_PRD_RSDBIO_LO | 1,200.4 |
| RS_PRD_COMBIO_LO | 1,145.5 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 688.2 |
| RS_PRD_COMGAS_LO | 390.0 |
| RS_PRD_RSDGAS_LO | 345.7 |
| RS_PRD_COMHET_LO | 76.88 |
| UC_DecrCCSIND | 75.66 |
| RS_ACT_SSCDCOKE00_LO | 39.34 |

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

Shadow prices differing by more than 5 %: 173; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_CAP_EEPP_natgas_CCGT | 661,969.4 | 1,318.7 | 660,650.7 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 630,759.3 | 1,269.5 | 629,489.8 |
| UC_VARU_CAP_EEPP_naturalgas_th | 624,789.6 | 2,436.8 | 622,352.7 |
| UC_HydroLakeSupply_CE | 463,963.3 | 35,734.3 | 428,229.0 |
| UC_VARU_CAP_EEPP_HFO_th | 249,258.1 | 702.2 | 248,555.8 |
| UC_VARU_ACT_EEPP_natgas_OCGT | 132,465.3 | 8,790.4 | 123,674.9 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 105,596.2 | 6,902.7 | 98,693.5 |
| UC_VARU_ACT_EEPP_naturalgas_th | 102,903.3 | 8,719.1 | 94,184.2 |
| UCI_UP_CHPShare-ICL | 85,384.6 | 0 | 85,384.6 |
| UC_VARU_ACT_EEPP_HFO_th | 83,255.8 | 10,729.6 | 72,526.1 |
| UCI_UP_CHPShare-ICU | 71,386.6 | 0 | 71,386.6 |
| UCI_UP_CHPShare-IAL | 26,014.0 | 0 | 26,014.0 |
| UC_VARU_ACT_EEPP_lignite_th | 28,975.2 | 8,299.1 | 20,676.1 |
| UC_VARU_CAP_EEPP_lignite_th | 20,189.7 | 630.4 | 19,559.3 |
| UC_VARU_CAP_EEPP_coal_th | 20,194.9 | 1,060.7 | 19,134.3 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 47 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI / 2070 / MCMCLKBYF | 0.000477 | 0 | 0.000477 |
| FI / 2070 / MCMCLKCCSC | 0.0004706 | 0 | 0.0004706 |
| FI / 2070 / ICLHTH | 0.0002453 | 0 | 0.0002453 |
| FI / 2070 / ILMHTH | 0.0002319 | 0 | 0.0002319 |
| FI / 2070 / INFOTH | 0.0001989 | 0 | 0.0001989 |
| FI / 2065 / MCMCLKBYF | 0.0001915 | 0 | 0.0001915 |
| FI / 2065 / MCMCLKCCSC | 0.0001877 | 0 | 0.0001877 |
| FI / 2070 / IGHHTH | 0.0001678 | 0 | 0.0001678 |
| FI / 2060 / MCMCLKBYF | 0.0001557 | 0 | 0.0001557 |
| FI / 2060 / MCMCLKCCSC | 0.0001522 | 0 | 0.0001522 |

- CST_FLOX: 0 entries differ
### investment: 780 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 14,330.3 | 9,902.3 | 4,428.1 |
| COMBATS01 | 6,163.7 | 10,588.6 | -4,424.9 |
| SELCH2PEM01 | 1,219.3 | 2,349.5 | -1,130.1 |
| SELCH2EC01 | 1,219.4 | 135.6 | 1,083.8 |
| TRA_Hdt_ELC_01 | 56,528.1 | 56,662.1 | -134.0 |
| TRA_Car_PIH_LoM_20pct | 29,552.1 | 29,648.3 | -96.2 |
| HHTHHFO001 | 249.6 | 342.3 | -92.73 |
| EUCCGASCCSpos20 | 6,713.9 | 6,799.3 | -85.45 |
| EUIGCCWOO01 | 12,966.6 | 12,884.8 | 81.86 |
| TRA_Car_Gas_LoM_71 | 4,313.0 | 4,233.6 | 79.42 |
| TRA_Car_Dis_Sma_31 | 389.0 | 462.6 | -73.63 |
| EUWINOFH01 | 3,018.5 | 2,948.8 | 69.72 |

### fixed O&M: 603 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| SELCH2PEM01 | 459.7 | 885.4 | -425.7 |
| SELCH2EC01 | 459.7 | 51.24 | 408.5 |
| P_RSDBATS01 | 515.2 | 397.7 | 117.6 |
| P_COMBATS01 | 255.3 | 372.8 | -117.5 |
| ICLADVPRO05 | 160.7 | 130.1 | 30.51 |
| ICLADVPRO01 | 25.36 | 54.36 | -29.01 |
| TRA_Car_PIH_LoM_20pct | 6,839.1 | 6,861.4 | -22.3 |
| IPPPUPMEC15 | 402.2 | 380.3 | 21.89 |
| HHTHHFO001 | 52.36 | 72.62 | -20.26 |
| TRA_Hdt_ELC_01 | 8,149.0 | 8,168.3 | -19.32 |
| IOISTMLPG01 | 18.76 | 0 | 18.76 |
| TRA_Car_Gas_LoM_71 | 980.3 | 962.2 | 18.05 |

### activity: 349 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| ICLADVPRO05 | 160.9 | 129.2 | 31.71 |
| ICLADVPRO01 | 25.82 | 55.7 | -29.88 |
| SELCH2PEM01_LowAF | 31.55 | 60.75 | -29.19 |
| SELCH2EC01_LowAF | 31.55 | 3.418 | 28.14 |
| TB_INDSCO2N_FI_FI1D9 | 5.82 | 0 | 5.82 |
| MINBIOCRP41 | 1,602.0 | 1,607.3 | -5.267 |
| EUCCGASCCSpos20 | 196.9 | 199.6 | -2.663 |
| ICLSTDPRO01 | 11.87 | 14.01 | -2.138 |
| EUIGCCWOO01 | 285.1 | 283.3 | 1.828 |
| IISSINTERBIO | 359.2 | 360.9 | -1.677 |
| IISELAFUR01 | 1,429.9 | 1,428.5 | 1.486 |
| IISSINTER01 | 16.44 | 15.05 | 1.391 |

### flow/import: 89 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IMPELC-SEtoFI | 6,025.2 | 6,367.7 | -342.5 |
| IMPELC-EetoFI | 1,826.0 | 1,528.3 | 297.6 |
| EXPOILGSL | -16,529.8 | -16,267.1 | -262.7 |
| IMPOILGSL | 4,721.1 | 4,570.2 | 151.0 |
| IMPOILDST | 15,209.5 | 15,101.9 | 107.6 |
| EXPOILDST | -9,839.4 | -9,767.3 | -72.13 |
| IMPELC-NOtoFI | 279.4 | 230.7 | 48.68 |
| EXPOILHFO | -1,912.7 | -1,871.8 | -40.9 |
| IMPCOAHAR | 2,713.7 | 2,686.2 | 27.46 |
| EXPOILKER | -1,190.2 | -1,176.6 | -13.59 |
| IMPOILHFO | 5,410.5 | 5,397.2 | 13.33 |
| TRABAT_ChgStn | 10,512.3 | 10,525.0 | -12.69 |

### capacity (sum over years): 265 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 480.1 | 371.0 | 109.1 |
| COMBATS01 | 247.8 | 356.8 | -109.0 |
| TRA_Car_PIH_LoM_20pct | 11,552.3 | 11,590.1 | -37.74 |
| R_ES-SH-SD_GAS01 | 663.1 | 632.6 | 30.51 |
| R_ES-SH-FL_ELC01 | 12,514.4 | 12,484.1 | 30.34 |
| TRA_Car_Elc_Sma_10 | 8,041.5 | 8,012.9 | 28.6 |
| P_RSDBATS01 | 120.0 | 92.74 | 27.27 |
| P_COMBATS01 | 61.94 | 89.2 | -27.26 |
| R_ES-SH-FL_GAS01 | 722.7 | 749.8 | -27.13 |
| TRABAT_ChgStn | 54.47 | 33.34 | 21.13 |
| R_ES-SH-DH-70_GAS01 | 755.2 | 775.0 | -19.82 |
| R_ES-SH-DH-70_ELC07 | 1,959.6 | 1,939.9 | 19.7 |

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
