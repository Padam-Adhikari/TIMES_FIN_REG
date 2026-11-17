# Audit of baseline-sami.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,529,550.82 M EUR, reference 1,529,919.88, difference -369.06 (-0.0241%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,713.7 | 144,742.3 | -28.63 |
| INV | 919,666.6 | 919,897.7 | -231.2 |
| VAR | 465,170.6 | 465,279.9 | -109.3 |

| region | objective share |
|---|---|
| FI | 1,486,021.8 |
| FI196 | 24,524.8 |
| FI1D9 | 8,102.7 |
| FI1B1 | 6,246.4 |
| FI1C1 | 913.7 |
| FI1C5 | 693.8 |
| FI19A | 652.8 |
| FI19B | 488.1 |
| FI1DA | 386.7 |
| FI1C2 | 329.7 |
| FI199 | 283.4 |
| FI1D5 | 245.2 |
| FI198 | 231.2 |
| FI1D7 | 167.0 |
| FI1DB | 84.9 |
| FI1C6 | 53.99 |
| FI1D8 | 53.31 |
| FI1DC | 33.65 |
| FI1C7 | 30.6 |
| FI200 | 7.081 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| EUHYDDAM00 | 1,373.9 | 1,380.6 | -6.673 |
| EEPP_PV | 42.52 | 45.46 | -2.942 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_coal_thermal | 96.7 | 97.15 | -0.4536 |
| EEPP_biomass_thermal | 86.04 | 86.31 | -0.2674 |
| ECHP_naturalgas_CCGT | 84.43 | 84.67 | -0.246 |
| EEPP_coal_thermal | 40.08 | 40.22 | -0.1351 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05928 |
| EEPP_naturalgas_thermal | 0.06931 | 0.09998 | -0.03067 |
| ECHP_HFO_thermal | 8.323 | 8.341 | -0.01877 |
| ECHP_LFO_thermal | 0.01515 | 0.02023 | -0.005077 |
| EEPP_windOFF | 23.58 | 23.59 | -0.003647 |
| ECHP_naturalgas_thermal | 2.226 | 2.229 | -0.003069 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | -0.0008354 |
| EEPP_LFO_thermal | 0.08297 | 0.08335 | -0.0003801 |
| ECHP_lignite_thermal | 29.84 | 29.84 | 1.421e-14 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 5.329e-15 |
| EEPP_HFO_thermal | 2.141 | 2.141 | 8.882e-16 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | 0 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | 0 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | 0 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | 0 |

By class and year: 70 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| EUHYDDAM00 / 2063 | 53.79 | 55.04 | -1.249 |
| EUHYDDAM00 / 2070 | 54.05 | 55.03 | -0.9835 |
| EUHYDDAM00 / 2068 | 54.08 | 55.04 | -0.9599 |
| EUHYDDAM00 / 2065 | 54.13 | 55.04 | -0.9061 |
| EUHYDDAM00 / 2030 | 54.27 | 55.04 | -0.7618 |
| EUHYDDAM00 / 2033 | 54.2 | 54.9 | -0.7009 |
| EUHYDDAM00 / 2060 | 54.39 | 55.04 | -0.6421 |
| ECHP_coal_thermal / 2018 | 37.85 | 38.11 | -0.2566 |
| EEPP_PV / 2023 | 2.688 | 2.932 | -0.2439 |
| EEPP_PV / 2033 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2028 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2025 | 3.564 | 3.796 | -0.2319 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,283.7 |
| FI198 | 76.62 |
| FI199 | 157.4 |
| FI19A | 266.8 |
| FI19B | 88.51 |
| FI1B1 | 250.5 |
| FI1C1 | 124.4 |
| FI1C2 | 50.06 |
| FI1C5 | 235.1 |
| FI1C6 | 28.83 |
| FI1C7 | 56.07 |
| FI1D5 | 165.4 |
| FI1D7 | 591.2 |
| FI1D8 | 93.03 |
| FI1D9 | 733.0 |
| FI1DA | 72.99 |
| FI1DB | 23.54 |
| FI1DC | 97.2 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.5 | 337.6 | -0.113 |
| 2013 | 291.8 | 292.1 | -0.2441 |
| 2015 | 319.8 | 320.1 | -0.2515 |
| 2018 | 372.6 | 373.1 | -0.517 |
| 2020 | 314.3 | 314.9 | -0.5568 |
| 2023 | 379.7 | 380.3 | -0.5976 |
| 2025 | 422.9 | 423.2 | -0.3508 |
| 2028 | 478.0 | 478.3 | -0.2857 |
| 2030 | 507.0 | 507.3 | -0.2962 |
| 2033 | 442.1 | 442.2 | -0.08198 |
| 2035 | 464.0 | 464.2 | -0.1794 |
| 2038 | 521.4 | 521.6 | -0.1662 |
| 2040 | 573.4 | 573.8 | -0.3473 |
| 2043 | 623.3 | 623.9 | -0.6073 |
| 2045 | 643.8 | 644.7 | -0.8716 |
| 2048 | 669.6 | 670.5 | -0.807 |
| 2050 | 707.8 | 708.1 | -0.2895 |
| 2053 | 718.9 | 719.1 | -0.171 |
| 2055 | 727.9 | 727.8 | 0.09237 |
| 2058 | 749.3 | 749.1 | 0.1807 |
| 2060 | 763.9 | 763.8 | 0.1708 |
| 2063 | 779.0 | 779.1 | -0.09234 |
| 2065 | 788.7 | 788.8 | -0.08507 |
| 2068 | 805.2 | 805.1 | 0.06644 |
| 2070 | 816.7 | 816.6 | 0.1643 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 199.9 | 200.0 | -0.09438 |
| 2013 | 180.4 | 179.3 | 1.09 |
| 2015 | 132.2 | 131.1 | 1.077 |
| 2018 | 133.2 | 132.5 | 0.7086 |
| 2020 | 146.2 | 145.3 | 0.8178 |
| 2023 | 133.8 | 134.0 | -0.1726 |
| 2025 | 134.1 | 124.4 | 9.761 |
| 2028 | 212.4 | 212.8 | -0.4123 |
| 2030 | 230.8 | 230.4 | 0.4019 |
| 2033 | 168.8 | 168.8 | -0.05285 |
| 2035 | 177.6 | 177.8 | -0.2002 |
| 2038 | 189.9 | 190.0 | -0.1178 |
| 2040 | 203.7 | 204.3 | -0.6005 |
| 2043 | 224.4 | 224.7 | -0.2845 |
| 2045 | 229.2 | 229.2 | -0.03063 |
| 2048 | 234.9 | 235.1 | -0.1916 |
| 2050 | 239.2 | 239.0 | 0.249 |
| 2053 | 238.8 | 238.4 | 0.3439 |
| 2055 | 243.2 | 242.9 | 0.3735 |
| 2058 | 249.5 | 249.0 | 0.4776 |
| 2060 | 257.2 | 257.1 | 0.1376 |
| 2063 | 262.5 | 262.1 | 0.3583 |
| 2065 | 264.2 | 263.8 | 0.4074 |
| 2068 | 268.8 | 268.4 | 0.4172 |
| 2070 | 271.5 | 271.1 | 0.4111 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 8.636 | 0.7005 |
| 2018 | 12.38 | 0.4193 |
| 2025 | 4.597 | 0.1558 |
| 2033 | 35.63 | 1.206 |
| 2040 | 48.52 | 1.642 |
| 2048 | 28.61 | 0.9686 |
| 2055 | 28.23 | 0.9083 |
| 2063 | 29.88 | 1.011 |
| 2070 | 29.21 | 0.9888 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.105 | 0.7178 |
| 2018 | 21.38 | 1.685 |
| 2025 | 266.9 | 21.04 |
| 2033 | 23.8 | 1.876 |
| 2040 | 31.13 | 2.454 |
| 2048 | 16.28 | 1.195 |
| 2055 | 16.56 | 0.67 |
| 2063 | 17.28 | 1.156 |
| 2070 | 17.07 | 1.345 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,102.3 | 0 |
| ELCHIG | 4,402.6 | 0 |
| GreenCert-ELC | 3,324.4 | 0 |
| ELCHYD | 0 | 1,374.0 |
| ELCWOO | 0 | 1,269.5 |
| ELCWIN | 0 | 1,091.6 |
| HETHTH | 754.9 | 0 |
| ELCNUC | 0 | 751.8 |
| ELCCOH | 0 | 435.5 |
| INDCOK | 0 | 310.9 |
| INDCOA | 0 | 274.0 |
| ELCGAS | 0 | 208.1 |
| ELCCOL | 0 | 149.0 |
| MISSNT | 0 | 82.73 |
| MISRIR | 53.91 | 0 |
| ELCSOL | 0 | 45.51 |
| ELCHFO | 0 | 28.97 |
| INDBIO | 0 | 25.52 |
| MISOXY | 0 | 23.74 |
| INDBFG | 10.68 | 10.76 |
| INDELC | 0 | 13.33 |
| MISBFS | 6.309 | 0 |
| MISPLT | 0 | 2.387 |
| ELCDST | 0 | 0.3796 |
| INDHFO | 0 | 0.0005275 |

- Back-and-forth on the same link, year and timeslice: 1 cases, volume 10.68
| link / year / ts | min(imp, exp) |
|---|---|
| TB_INDBFG_FI_FI1D9 / 2025 / ANNUAL | 10.68 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 131,158.7, reference 130,244.3 (+0.70%); 18 years differ >0.1 %
- ETSCO2: produced, all years: run 343,214.7, reference 343,808.2 (-0.17%); 14 years differ >0.1 %
- INDCO2N: produced, all years: run 125,124.2, reference 126,331.9 (-0.96%); 21 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,211.5, reference 11,202.8 (+0.08%); 11 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,064.9, reference 6,065.4 (-0.01%); 17 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'GreenCert-ELC': -4.5, 'ETSCO2': 132270.4, 'ELCCO2N': 71827.5} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 7 | 333.8 |
| FI / ELCHIGG | 300 | 4 | 6.312 |
| FI / ELCLOW | 300 | 1 | 16.78 |
| FI / ELCMED | 300 | 0 | 0 |
| FI / HETHTH | 300 | 0 | 0 |

- Peak equations outside the hub: 0 region/commodity pairs (none, as intended)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 269; only in run: 24; only in reference: 17
| binding only in run | sum |shadow| |
|---|---|
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,674.7 |
| RS_PRD_RSDFINOIL_LO | 2,368.5 |
| RS_PRD_COMFINOIL_LO | 2,348.5 |
| RS_PRD_RSDBIO_LO | 1,200.4 |
| RS_PRD_COMBIO_LO | 1,145.4 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 688.1 |
| RS_PRD_COMGAS_LO | 390.0 |
| RS_PRD_RSDGAS_LO | 345.8 |
| RS_PRD_COMHET_LO | 76.87 |
| RS_ACT_SSCDCOKE00_LO | 39.34 |
| RS_PRD_COMGAS_UP | 32.4 |
| RS_ACT_SSCDCOKE00_FX | 19.24 |
| RS_FLO_RSDHET00_HETHTH_UP | 18.02 |
| RS_ACT_SSCDRFLX00_LO | 13.96 |

| binding only in reference | sum |shadow| |
|---|---|
| TUC_TRA_Lcv-Lpg | 32,707.9 |
| TUC_Istruc_RIR-CYC | 10,699.4 |
| UC_VARU_CAP_EUSTCOHcon01 | 7.551 |
| UC_VARU_CAP_EUSTCOHsup01 | 7.551 |
| UC_VARU_CAP_EUSTCOLsup01 | 7.551 |
| UC_VARU_CAP_EUGEOORC01 | 3.776 |
| UC_VARU_CAP_EUGEOEGS01 | 3.776 |
| UC_VARU_CAP_EUGEOF01 | 3.776 |
| UC_VARU_CAP_EUIGCCCOH15 | 3.776 |
| UC_VARU_CAP_EUPCCOLCCSpos20 | 3.776 |
| UC_VARU_CAP_EUSTCOLcon01 | 3.776 |
| UC_VARU_CAP_EUPCCOHCCSpos20 | 3.776 |
| UC_VARU_CAP_EUIGCOHCCSpre20 | 3.776 |
| UC_VARU_CAP_EUPCCOHCCSoxy20 | 3.776 |
| UC_VARU_CAP_EUNUC4th40 | 1.992 |

Shadow prices differing by more than 5 %: 150; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_ACT_EEPP_natgas_OCGT | 135,998.7 | 8,790.4 | 127,208.3 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 91,982.4 | 6,902.7 | 85,079.6 |
| UC_VARU_ACT_EEPP_naturalgas_th | 84,928.0 | 8,719.1 | 76,208.9 |
| UC_VARU_CAP_EUCCGASCCSpos20 | 3,253.8 | 56,904.4 | -53,650.7 |
| UC_VARU_CAP_EEPP_naturalgas_th | 36,205.8 | 2,436.8 | 33,769.0 |
| TUC_TRA_Lcv-Lpg | 0 | 32,707.9 | -32,707.9 |
| UC_VARU_ACT_EEPP_HFO_th | 34,759.8 | 10,729.6 | 24,030.1 |
| UC_VARU_CAP_EEPP_natgas_CCGT | 23,342.7 | 1,318.7 | 22,024.0 |
| UC_HydroLakeSupply_CE | 23,472.2 | 35,734.3 | -12,262.1 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 12,580.2 | 1,269.5 | 11,310.8 |
| TUC_Istruc_RIR-CYC | 0 | 10,699.4 | -10,699.4 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,674.7 | 0 | 10,674.7 |
| TUC_TRA_Car-Lpg | 787.2 | 5,644.3 | -4,857.1 |
| UC_VARU_CAP_EUNUCLifeExt | 12,994.9 | 10,551.1 | 2,443.8 |
| RS_PRD_RSDFINOIL_LO | 2,368.5 | 0 | 2,368.5 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 0 entries differ
- CST_FLOX: 0 entries differ
### investment: 111 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 17,097.2 | 9,902.3 | 7,195.0 |
| COMBATS01 | 3,396.6 | 10,588.6 | -7,192.1 |
| SELCH2EC01 | 0 | 135.6 | -135.6 |
| TRA_Hdt_ELC_01 | 56,542.9 | 56,662.1 | -119.2 |
| TRA_Car_PIH_LoM_20pct | 29,552.1 | 29,648.3 | -96.24 |
| SELCH2PEM01 | 2,444.6 | 2,349.5 | 95.12 |
| HHTHHFO001 | 251.7 | 342.3 | -90.63 |
| TRA_Car_Gas_LoM_71 | 4,313.1 | 4,233.6 | 79.51 |
| TRA_Car_Dis_Sma_31 | 388.9 | 462.6 | -73.66 |
| EUIGCCWOO01 | 12,955.2 | 12,884.8 | 70.44 |
| EUCCGASCCSpos20 | 6,731.7 | 6,799.3 | -67.57 |
| TRA_Car_Elc_Sma_10 | 17,156.2 | 17,093.1 | 63.09 |

### fixed O&M: 109 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| P_RSDBATS01 | 627.5 | 397.7 | 229.8 |
| P_COMBATS01 | 143.0 | 372.8 | -229.7 |
| SELCH2EC01 | 0 | 51.24 | -51.24 |
| SELCH2PEM01 | 921.6 | 885.4 | 36.17 |
| IOISTMBIO01 | 446.3 | 474.0 | -27.67 |
| TRA_Car_PIH_LoM_20pct | 6,839.1 | 6,861.4 | -22.31 |
| HHTHHFO001 | 52.82 | 72.62 | -19.8 |
| ICHSTMBIO01 | 284.0 | 265.3 | 18.72 |
| IPPPUPMEC15 | 398.8 | 380.3 | 18.51 |
| TRA_Car_Gas_LoM_71 | 980.3 | 962.2 | 18.07 |
| TRA_Hdt_ELC_01 | 8,151.2 | 8,168.3 | -17.19 |
| TRA_Car_Elc_Sma_10 | 4,866.2 | 4,849.0 | 17.15 |

### activity: 236 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| ICLADVPRO05 | 138.8 | 129.2 | 9.613 |
| ICLADVPRO01 | 47.47 | 55.7 | -8.237 |
| TB_INDSCO2N_FI_FI1D9 | 5.82 | 0 | 5.82 |
| MINBIOCRP41 | 1,602.9 | 1,607.3 | -4.369 |
| SELCH2EC01_LowAF | 0 | 3.418 | -3.418 |
| SELCH2PEM01_LowAF | 63.26 | 60.75 | 2.511 |
| EUCCGASCCSpos20 | 197.4 | 199.6 | -2.144 |
| ICLSTDPRO01 | 12.32 | 14.01 | -1.688 |
| EUIGCCWOO01 | 284.9 | 283.3 | 1.598 |
| IISELAFUR01 | 1,429.9 | 1,428.5 | 1.486 |
| INDIPPGASHTH06 | 6.749 | 8.115 | -1.366 |
| HHTHCOH001 | 8.5 | 7.438 | 1.062 |

### flow/import: 34 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EXPOILGSL | -16,542.7 | -16,267.1 | -275.5 |
| IMPOILGSL | 4,725.5 | 4,570.2 | 155.3 |
| IMPELC-SEtoFI | 6,240.5 | 6,367.7 | -127.2 |
| IMPELC-EetoFI | 1,652.8 | 1,528.3 | 124.5 |
| IMPOILDST | 15,205.4 | 15,101.9 | 103.5 |
| EXPOILDST | -9,837.0 | -9,767.3 | -69.72 |
| EXPOILHFO | -1,906.9 | -1,871.8 | -35.09 |
| IMPCOAHAR | 2,712.0 | 2,686.2 | 25.81 |
| EXPOILKER | -1,190.9 | -1,176.6 | -14.37 |
| IMPOILHFO | 5,409.7 | 5,397.2 | 12.57 |
| TRABAT_ChgStn | 10,513.6 | 10,525.0 | -11.42 |
| IMPELC-NOtoFI | 238.6 | 230.7 | 7.875 |

### capacity (sum over years): 54 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 588.9 | 371.0 | 217.9 |
| COMBATS01 | 139.0 | 356.8 | -217.8 |
| P_RSDBATS01 | 147.2 | 92.74 | 54.47 |
| P_COMBATS01 | 34.74 | 89.2 | -54.46 |
| R_ES-SH-FL_ELC01 | 12,528.4 | 12,484.1 | 44.28 |
| R_ES-SH-SD_GAS01 | 673.5 | 632.6 | 40.94 |
| TRA_Car_PIH_LoM_20pct | 11,552.3 | 11,590.1 | -37.76 |
| R_ES-SH-FL_GAS01 | 712.4 | 749.8 | -37.44 |
| TRA_Car_Elc_Sma_10 | 8,041.5 | 8,012.9 | 28.63 |
| R_ES-SH-DH-70_GAS01 | 748.4 | 775.0 | -26.6 |
| R_ES-SH-SD_ELC01 | 2,112.8 | 2,137.7 | -24.97 |
| R_ES-SH-DH-70_ELC07 | 1,960.4 | 1,939.9 | 20.49 |

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
