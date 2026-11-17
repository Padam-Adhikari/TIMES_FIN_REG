# Audit of baseline-sami.gdx vs baseline-new.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,540,391.58 M EUR, reference 1,529,919.88, difference +10,471.69 (+0.6845%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 145,908.3 | 144,742.3 | 1,166.0 |
| INV | 925,384.6 | 919,897.7 | 5,486.9 |
| VAR | 468,633.1 | 465,279.9 | 3,353.2 |
| VARX | 465.6 | 0 | 465.6 |

| region | objective share |
|---|---|
| FI | 1,496,985.2 |
| FI196 | 24,602.1 |
| FI1D9 | 8,076.6 |
| FI1B1 | 6,131.0 |
| FI1C1 | 883.4 |
| FI1C5 | 692.8 |
| FI19A | 628.7 |
| FI19B | 488.8 |
| FI1DA | 386.7 |
| FI1C2 | 329.7 |
| FI199 | 283.3 |
| FI1D5 | 245.2 |
| FI198 | 225.0 |
| FI1D7 | 164.6 |
| FI1DB | 85.03 |
| FI1C6 | 64.19 |
| FI1D8 | 53.31 |
| FI1C7 | 30.64 |
| FI1DC | 28.22 |
| FI200 | 7.076 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| EUHYDDAM00 | 1,327.9 | 1,380.6 | -52.71 |
| ECHP_naturalgas_CCGT | 73.65 | 84.67 | -11.02 |
| ECHP_coal_thermal | 88.16 | 97.15 | -8.992 |
| EEPP_coal_thermal | 44.3 | 40.22 | 4.088 |
| EEPP_PV | 42.52 | 45.46 | -2.94 |
| ECHP_HFO_thermal | 10.17 | 8.341 | 1.831 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_lignite_thermal | 28.7 | 29.84 | -1.145 |
| EEPP_biomass_thermal | 86.04 | 86.31 | -0.2654 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05515 |
| EEPP_naturalgas_thermal | 0.07253 | 0.09998 | -0.02745 |
| ECHP_LFO_thermal | 0.01304 | 0.02023 | -0.007191 |
| EEPP_windOFF | 23.58 | 23.59 | -0.003647 |
| ECHP_naturalgas_thermal | 2.227 | 2.229 | -0.002229 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08297 | 0.08335 | -0.0003801 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 5.329e-15 |
| EEPP_HFO_thermal | 2.141 | 2.141 | -8.882e-16 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | 0 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | 0 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | 0 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | 0 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | 0 |

By class and year: 78 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_coal_thermal / 2018 | 30.43 | 38.11 | -7.679 |
| EUHYDDAM00 / 2030 | 50.65 | 55.04 | -4.382 |
| EEPP_coal_thermal / 2013 | 6.533 | 2.445 | 4.088 |
| EUHYDDAM00 / 2060 | 51.04 | 55.04 | -3.999 |
| EUHYDDAM00 / 2065 | 51.1 | 55.04 | -3.935 |
| EUHYDDAM00 / 2058 | 51.1 | 55.04 | -3.935 |
| EUHYDDAM00 / 2050 | 51.1 | 55.04 | -3.934 |
| EUHYDDAM00 / 2063 | 51.1 | 55.04 | -3.934 |
| EUHYDDAM00 / 2068 | 51.1 | 55.04 | -3.934 |
| EUHYDDAM00 / 2055 | 51.1 | 55.04 | -3.934 |
| EUHYDDAM00 / 2070 | 51.1 | 55.03 | -3.929 |
| EUHYDDAM00 / 2053 | 51.1 | 54.99 | -3.887 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,279.9 |
| FI198 | 75.13 |
| FI199 | 156.3 |
| FI19A | 260.6 |
| FI19B | 87.04 |
| FI1B1 | 239.6 |
| FI1C1 | 120.8 |
| FI1C2 | 50.07 |
| FI1C5 | 229.8 |
| FI1C6 | 29.44 |
| FI1C7 | 53.78 |
| FI1D5 | 160.3 |
| FI1D7 | 585.2 |
| FI1D8 | 89.52 |
| FI1D9 | 726.0 |
| FI1DA | 72.85 |
| FI1DB | 22.61 |
| FI1DC | 95.09 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 336.6 | 337.6 | -1.021 |
| 2013 | 292.4 | 292.1 | 0.3838 |
| 2015 | 315.1 | 320.1 | -4.987 |
| 2018 | 365.1 | 373.1 | -7.936 |
| 2020 | 315.0 | 314.9 | 0.1801 |
| 2023 | 385.0 | 380.3 | 4.724 |
| 2025 | 428.8 | 423.2 | 5.601 |
| 2028 | 491.8 | 478.3 | 13.54 |
| 2030 | 521.4 | 507.3 | 14.09 |
| 2033 | 452.3 | 442.2 | 10.07 |
| 2035 | 478.2 | 464.2 | 14.03 |
| 2038 | 535.3 | 521.6 | 13.68 |
| 2040 | 587.8 | 573.8 | 14.02 |
| 2043 | 633.9 | 623.9 | 9.982 |
| 2045 | 652.3 | 644.7 | 7.619 |
| 2048 | 676.6 | 670.5 | 6.128 |
| 2050 | 713.7 | 708.1 | 5.607 |
| 2053 | 724.3 | 719.1 | 5.186 |
| 2055 | 732.4 | 727.8 | 4.586 |
| 2058 | 755.5 | 749.1 | 6.365 |
| 2060 | 772.0 | 763.8 | 8.228 |
| 2063 | 787.0 | 779.1 | 7.915 |
| 2065 | 797.0 | 788.8 | 8.204 |
| 2068 | 811.2 | 805.1 | 6.125 |
| 2070 | 822.1 | 816.6 | 5.484 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 190.3 | 200.0 | -9.676 |
| 2013 | 176.6 | 179.3 | -2.694 |
| 2015 | 125.5 | 131.1 | -5.594 |
| 2018 | 125.8 | 132.5 | -6.626 |
| 2020 | 141.6 | 145.3 | -3.744 |
| 2023 | 133.8 | 134.0 | -0.2382 |
| 2025 | 134.2 | 124.4 | 9.838 |
| 2028 | 218.2 | 212.8 | 5.346 |
| 2030 | 232.4 | 230.4 | 2.075 |
| 2033 | 172.0 | 168.8 | 3.137 |
| 2035 | 184.0 | 177.8 | 6.194 |
| 2038 | 190.8 | 190.0 | 0.8016 |
| 2040 | 204.9 | 204.3 | 0.6053 |
| 2043 | 226.9 | 224.7 | 2.248 |
| 2045 | 230.8 | 229.2 | 1.617 |
| 2048 | 236.4 | 235.1 | 1.366 |
| 2050 | 239.4 | 239.0 | 0.4395 |
| 2053 | 240.8 | 238.4 | 2.383 |
| 2055 | 243.8 | 242.9 | 0.9055 |
| 2058 | 249.7 | 249.0 | 0.7488 |
| 2060 | 256.9 | 257.1 | -0.1822 |
| 2063 | 262.1 | 262.1 | -0.02085 |
| 2065 | 264.7 | 263.8 | 0.8347 |
| 2068 | 268.4 | 268.4 | -0.00604 |
| 2070 | 271.2 | 271.1 | 0.07422 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 18.65 | 1.5 |
| 2018 | 13.04 | 0.4417 |
| 2025 | 9.509 | 0.322 |
| 2033 | 34.79 | 1.178 |
| 2040 | 48.76 | 1.65 |
| 2048 | 28.94 | 0.9797 |
| 2055 | 27.71 | 1.512 |
| 2063 | 29.95 | 1.86 |
| 2070 | 28.98 | 1.363 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 11.91 | 0.9385 |
| 2018 | 20.88 | 1.646 |
| 2025 | 293.6 | 25.12 |
| 2033 | 21.57 | 169.4 |
| 2040 | 31.08 | 2.659 |
| 2048 | 16.35 | 167.5 |
| 2055 | 16.43 | 167.6 |
| 2063 | 17.24 | 335.6 |
| 2070 | 17.03 | 1.457 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,120.8 | 0 |
| ELCHIG | 4,196.3 | 0 |
| GreenCert-ELC | 3,278.4 | 0 |
| ELCHYD | 0 | 1,328.0 |
| ELCWOO | 0 | 1,269.5 |
| ELCWIN | 0 | 1,091.6 |
| ELCNUC | 0 | 751.8 |
| HETHTH | 669.9 | 0 |
| ELCCOH | 0 | 416.0 |
| INDCOK | 0 | 311.7 |
| INDCOA | 0 | 274.8 |
| ELCGAS | 0 | 180.7 |
| ELCCOL | 0 | 144.1 |
| MISSNT | 0 | 82.77 |
| MISRIR | 53.92 | 0 |
| ELCSOL | 0 | 45.51 |
| ELCHFO | 0 | 34.09 |
| MISOXY | 0 | 23.78 |
| INDBIO | 0 | 22.9 |
| INDBFG | 8.863 | 8.914 |
| INDELC | 0 | 13.27 |
| MISBFS | 6.325 | 0 |
| MISPLT | 0 | 2.342 |
| ELCDST | 0 | 0.3796 |
| INDHFO | 0 | 0.0003054 |

- Back-and-forth on the same link, year and timeslice: 1 cases, volume 8.863
| link / year / ts | min(imp, exp) |
|---|---|
| TB_INDBFG_FI_FI1D9 / 2025 / ANNUAL | 8.863 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 127,307.2, reference 130,244.3 (-2.26%); 24 years differ >0.1 %
- ETSCO2: produced, all years: run 342,577.9, reference 343,808.2 (-0.36%); 21 years differ >0.1 %
- INDCO2N: produced, all years: run 128,692.0, reference 126,331.9 (+1.87%); 24 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,358.1, reference 11,202.8 (+1.39%); 25 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,087.7, reference 6,065.4 (+0.37%); 22 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'ELCCO2N': 68280.4, 'GreenCert-ELC': -4.5, 'ETSCO2': 128870.4} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 0 | 0 |
| FI / ELCHIGG | 300 | 7 | 11.17 |
| FI / ELCLOW | 300 | 0 | 0 |
| FI / ELCMED | 300 | 3 | 10.36 |
| FI / HETHTH | 300 | 0 | 0 |
| FI196 / ELCHIG | 300 | 1 | 2.861 |
| FI196 / HETHTH | 300 | 0 | 0 |
| FI198 / ELCHIG | 300 | 0 | 0 |
| FI198 / HETHTH | 300 | 2 | 4,265.8 |
| FI199 / ELCHIG | 300 | 5 | 37.36 |
| FI199 / HETHTH | 300 | 0 | 0 |
| FI19A / ELCHIG | 300 | 5 | 37.37 |
| FI19A / HETHTH | 300 | 0 | 0 |
| FI19B / ELCHIG | 300 | 0 | 0 |
| FI19B / HETHTH | 300 | 5 | 7,571.6 |
| FI1B1 / ELCHIG | 300 | 8 | 23.52 |
| FI1B1 / HETHTH | 300 | 2 | 3,478.8 |
| FI1C1 / ELCHIG | 300 | 7 | 39.17 |
| FI1C1 / HETHTH | 300 | 1 | 1,996.4 |
| FI1C2 / ELCHIG | 300 | 19 | 69.68 |
| FI1C2 / HETHTH | 300 | 0 | 0 |
| FI1C5 / ELCHIG | 300 | 6 | 37.55 |
| FI1C5 / HETHTH | 300 | 0 | 0 |
| FI1C6 / ELCHIG | 300 | 3 | 22.53 |
| FI1C6 / HETHTH | 300 | 0 | 0 |
| FI1C7 / ELCHIG | 300 | 9 | 63.53 |
| FI1C7 / HETHTH | 300 | 0 | 0 |
| FI1D5 / ELCHIG | 300 | 12 | 66.78 |
| FI1D5 / HETHTH | 300 | 1 | 3,263.5 |
| FI1D7 / ELCHIG | 300 | 0 | 0 |
| FI1D7 / HETHTH | 300 | 1 | 3,265.8 |
| FI1D8 / ELCHIG | 300 | 0 | 0 |
| FI1D9 / ELCHIG | 300 | 13 | 71.36 |
| FI1D9 / HETHTH | 300 | 2 | 5,206.8 |
| FI1DA / ELCHIG | 300 | 4 | 6.55 |
| FI1DA / HETHTH | 300 | 2 | 4,240.1 |
| FI1DB / ELCHIG | 300 | 6 | 40.67 |
| FI1DB / HETHTH | 300 | 0 | 0 |
| FI1DC / ELCHIG | 300 | 0 | 0 |
| FI1DC / HETHTH | 300 | 0 | 0 |
| FI200 / ELCHIG | 300 | 0 | 0 |

- Peak equations outside the hub: 36 region/commodity pairs (expected none in the hub design)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 264; only in run: 22; only in reference: 22
| binding only in run | sum |shadow| |
|---|---|
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,418.2 |
| RS_PRD_RSDFINOIL_LO | 2,368.5 |
| RS_PRD_COMFINOIL_LO | 2,365.7 |
| RS_PRD_RSDBIO_LO | 1,269.2 |
| RS_PRD_COMBIO_LO | 1,203.8 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 751.0 |
| RS_PRD_COMGAS_LO | 404.7 |
| RS_PRD_RSDGAS_LO | 350.1 |
| UC_Growth_wind_OFF | 115.5 |
| RS_PRD_COMHET_LO | 71.42 |
| RS_FLO_RSDHET00_HETHTH_UP | 47.44 |
| RS_PRD_COMGAS_UP | 43.67 |
| RS_ACT_SSCDCOKE00_LO | 43.21 |
| RS_ACT_SSCDCOKE00_FX | 25.32 |

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

Shadow prices differing by more than 5 %: 207; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_HydroLakeSupply_CE | 349,420.2 | 35,734.3 | 313,685.9 |
| UC_VARU_ACT_EEPP_natgas_OCGT | 257,414.0 | 8,790.4 | 248,623.6 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 158,048.0 | 6,902.7 | 151,145.3 |
| UC_VARU_ACT_EEPP_naturalgas_th | 139,603.1 | 8,719.1 | 130,883.9 |
| UC_VARU_ACT_EEPP_HFO_th | 89,554.9 | 10,729.6 | 78,825.2 |
| UC_VARU_CAP_EEPP_naturalgas_th | 46,097.7 | 2,436.8 | 43,660.9 |
| UC_VARU_CAP_EEPP_natgas_CCGT | 31,495.5 | 1,318.7 | 30,176.8 |
| UC_VARU_ACT_EEPP_lignite_th | 26,390.0 | 8,299.1 | 18,090.9 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 17,157.3 | 1,269.5 | 15,887.8 |
| UC_ACAES-STG_DischLimit | 16,374.5 | 1,094.8 | 15,279.7 |
| UC_VARU_ACT_EEPP_coal_th | 23,558.8 | 8,298.6 | 15,260.2 |
| UC_VARU_CAP_EUICGAS01 | 12,827.6 | 1,969.4 | 10,858.2 |
| TUC_Istruc_RIR-CYC | 0 | 10,699.4 | -10,699.4 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,418.2 | 0 | 10,418.2 |
| UC_VARU_ACT_EUIGCCWOOCCS01 | 9,599.8 | 1,340.7 | 8,259.1 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 1 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI / 2025 / MPPPUP | 334.0 | 0 | 334.0 |

- CST_FLOX: 0 entries differ
### investment: 216 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EUWINOFH01 | 6,237.0 | 2,948.8 | 3,288.2 |
| COMBATS01 | 12,457.8 | 10,588.6 | 1,869.1 |
| RSDBATS01 | 8,046.7 | 9,902.3 | -1,855.6 |
| R_ES-SH-DH_ELC05 | 1,930.0 | 2,896.3 | -966.3 |
| R_ES-SH-DH_ELC04 | 829.6 | 0 | 829.6 |
| EUWINONM01 | 42,718.7 | 43,385.6 | -666.9 |
| TRA_Car_Dis_Sma_41 | 3,635.9 | 3,162.2 | 473.7 |
| EUICGAS01 | 2,652.9 | 2,292.1 | 360.8 |
| R_ES-SH-DH-70_ELC04 | 365.8 | 54.33 | 311.5 |
| TRA_Car_Elc_Sma_10 | 16,810.0 | 17,093.1 | -283.1 |
| TRA_Car_Gas_LoM_91 | 5,137.4 | 4,869.1 | 268.3 |
| EUIGCCWOO01 | 13,152.9 | 12,884.8 | 268.2 |

### fixed O&M: 202 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EUWINOFH01 | 893.0 | 420.9 | 472.0 |
| R_ES-SH-FL_GAS01 | 338.8 | 164.9 | 173.8 |
| R_ES-SH-DH_ELC05 | 290.2 | 433.3 | -143.1 |
| R_ES-SH-DH_ELC04 | 122.3 | 0 | 122.3 |
| TRA_Car_Dis_Sma_41 | 826.4 | 718.7 | 107.7 |
| SELCH2PEM01 | 980.3 | 885.4 | 94.95 |
| EUWINONM01 | 5,978.9 | 6,072.1 | -93.19 |
| TRA_Car_Elc_Sma_10 | 4,766.6 | 4,849.0 | -82.41 |
| P_COMBATS01 | 450.7 | 372.8 | 77.95 |
| P_RSDBATS01 | 320.1 | 397.7 | -77.55 |
| SBIOH2GCC01 | 2,131.7 | 2,202.4 | -70.66 |
| TRA_Car_Gas_LoM_91 | 1,167.6 | 1,106.7 | 60.99 |

### activity: 260 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EUWINOFH01 | 64.39 | 30.59 | 33.8 |
| ICLADVPRO05 | 161.2 | 129.2 | 31.96 |
| IGHRECYCL10 | 575.2 | 543.2 | 31.95 |
| ICLADVPRO01 | 26.58 | 55.7 | -29.12 |
| IMPBIOETH | 2,885.6 | 2,858.3 | 27.31 |
| IPPPUPCHE01 | 2,955.8 | 2,934.4 | 21.4 |
| EUHYDLAKELC01 | 59.69 | 39.42 | 20.27 |
| IGHRECYCL05 | 99.04 | 118.8 | -19.74 |
| ECHP_coal_thermal | 132.2 | 145.5 | -13.28 |
| IISELAFUR01 | 1,439.8 | 1,428.5 | 11.36 |
| ECHP_naturalgas_CCGT | 64.72 | 74.4 | -9.68 |
| IISSINTERBIO | 370.0 | 360.9 | 9.169 |

### flow/import: 67 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EXPOILGSL | -14,961.8 | -16,267.1 | 1,305.3 |
| MINMPPWOO1 | 116,338.1 | 115,521.8 | 816.2 |
| IMPOILCRD | 57,259.9 | 57,840.3 | -580.5 |
| IMPOILGSL | 4,164.5 | 4,570.2 | -405.6 |
| EXPOILKER | -1,525.3 | -1,176.6 | -348.7 |
| EXPOILDST | -9,467.2 | -9,767.3 | 300.1 |
| IMPOILKER | 3,835.9 | 3,597.7 | 238.3 |
| MINMPPRYC1 | 17,601.3 | 17,755.0 | -153.7 |
| IMPOILLPG | 4,790.8 | 4,659.9 | 130.8 |
| IMPGAS_RU_PIP | 22,108.7 | 21,987.4 | 121.3 |
| EXPOILHFO | -1,980.0 | -1,871.8 | -108.2 |
| IMPOILDST | 15,201.2 | 15,101.9 | 99.29 |

### capacity (sum over years): 75 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| R_ES-SH-FL_ELC01 | 11,692.7 | 12,484.1 | -791.4 |
| R_ES-SH-FL_GAS01 | 1,541.0 | 749.8 | 791.2 |
| R_ES-SH-DH_ELC05 | 1,072.6 | 1,601.4 | -528.8 |
| R_ES-SH-DH_ELC04 | 497.1 | 0 | 497.1 |
| R_ES-SH-DH-70_GAS01 | 515.0 | 775.0 | -260.0 |
| R_ES-SH-SD_GAS01 | 835.8 | 632.6 | 203.2 |
| R_ES-SH-DH-70_ELC04 | 236.6 | 35.78 | 200.8 |
| R_ES-SH-SD_ELC01 | 2,001.1 | 2,137.7 | -136.6 |
| TRA_Car_Elc_Sma_10 | 7,876.9 | 8,012.9 | -135.9 |
| R_ES-SH-FL_ELC07 | 452.4 | 582.2 | -129.8 |
| R_ES-SH-SD_HET01 | 7,836.8 | 7,714.3 | 122.5 |
| TRA_Car_PIH_LoM_20pct | 11,692.0 | 11,590.1 | 101.9 |

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
