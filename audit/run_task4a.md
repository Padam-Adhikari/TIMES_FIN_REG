# Audit of reg_baseline-sami_2026-11-16_task4a.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,535,236.42 M EUR, reference 1,529,919.88, difference +5,316.54 (+0.3475%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 141,362.6 | 144,742.3 | -3,379.7 |
| INV | 925,200.0 | 919,897.7 | 5,302.3 |
| VAR | 466,250.7 | 465,279.9 | 970.8 |
| VARX | 2,423.0 | 0 | 2,423.0 |

| region | objective share |
|---|---|
| FI | 1,485,308.7 |
| FI196 | 24,482.5 |
| FI1B1 | 11,726.9 |
| FI1D9 | 8,758.0 |
| FI1C5 | 1,069.0 |
| FI1C1 | 890.8 |
| FI19A | 628.6 |
| FI19B | 487.2 |
| FI1DA | 386.6 |
| FI1C2 | 317.6 |
| FI199 | 283.4 |
| FI1D5 | 245.2 |
| FI198 | 230.9 |
| FI1D7 | 167.0 |
| FI1DB | 84.76 |
| FI1D8 | 53.31 |
| FI1C6 | 44.8 |
| FI1DC | 33.58 |
| FI1C7 | 30.55 |
| FI200 | 7.081 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved
- PRC_RESID national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| ECHP_naturalgas_CCGT | 70.7 | 84.67 | -13.98 |
| EUHYDDAM00 | 1,370.8 | 1,380.6 | -9.817 |
| ECHP_coal_thermal | 90.41 | 97.15 | -6.743 |
| EEPP_PV | 42.52 | 45.46 | -2.942 |
| EEPP_coal_thermal | 37.77 | 40.22 | -2.445 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_HFO_thermal | 7.029 | 8.341 | -1.313 |
| EEPP_biomass_thermal | 86.05 | 86.31 | -0.2619 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05949 |
| EEPP_naturalgas_thermal | 0.07258 | 0.09998 | -0.0274 |
| ECHP_LFO_thermal | 0.01304 | 0.02023 | -0.007191 |
| EEPP_windOFF | 23.58 | 23.59 | -0.003647 |
| ECHP_naturalgas_thermal | 2.226 | 2.229 | -0.003069 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08297 | 0.08335 | -0.0003801 |
| ECHP_lignite_thermal | 29.84 | 29.84 | 3.553e-15 |
| EEPP_lignite_thermal | 8.505 | 8.505 | -1.776e-15 |
| EEPP_HFO_thermal | 2.141 | 2.141 | -8.882e-16 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | 0 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | 0 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | 0 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | 0 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | 0 |

By class and year: 73 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_coal_thermal / 2018 | 32.49 | 38.11 | -5.618 |
| ECHP_naturalgas_CCGT / 2015 | 23.57 | 28.22 | -4.658 |
| ECHP_naturalgas_CCGT / 2013 | 19.39 | 24.04 | -4.655 |
| ECHP_naturalgas_CCGT / 2010 | 19.39 | 24.04 | -4.654 |
| EEPP_coal_thermal / 2013 | 0 | 2.445 | -2.445 |
| ECHP_HFO_thermal / 2028 | 1.263 | 2.641 | -1.378 |
| EUHYDDAM00 / 2055 | 53.72 | 55.04 | -1.318 |
| EUHYDDAM00 / 2053 | 53.7 | 54.99 | -1.284 |
| EUHYDDAM00 / 2058 | 53.77 | 55.04 | -1.261 |
| EUHYDDAM00 / 2030 | 53.86 | 55.04 | -1.172 |
| ECHP_coal_thermal / 2020 | 11.53 | 12.65 | -1.125 |
| EUHYDDAM00 / 2050 | 54.03 | 55.04 | -1.006 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,281.4 |
| FI198 | 76.29 |
| FI199 | 157.3 |
| FI19A | 261.2 |
| FI19B | 88.23 |
| FI1B1 | 240.6 |
| FI1C1 | 122.0 |
| FI1C2 | 48.81 |
| FI1C5 | 237.0 |
| FI1C6 | 27.36 |
| FI1C7 | 56.1 |
| FI1D5 | 164.4 |
| FI1D7 | 591.2 |
| FI1D8 | 92.44 |
| FI1D9 | 732.4 |
| FI1DA | 72.97 |
| FI1DB | 23.4 |
| FI1DC | 94.61 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 335.0 | 337.6 | -2.596 |
| 2013 | 284.9 | 292.1 | -7.131 |
| 2015 | 315.3 | 320.1 | -4.826 |
| 2018 | 367.2 | 373.1 | -5.876 |
| 2020 | 313.5 | 314.9 | -1.4 |
| 2023 | 383.9 | 380.3 | 3.626 |
| 2025 | 426.6 | 423.2 | 3.337 |
| 2028 | 483.7 | 478.3 | 5.419 |
| 2030 | 514.3 | 507.3 | 7.02 |
| 2033 | 445.3 | 442.2 | 3.072 |
| 2035 | 478.4 | 464.2 | 14.28 |
| 2038 | 536.4 | 521.6 | 14.81 |
| 2040 | 585.1 | 573.8 | 11.31 |
| 2043 | 629.1 | 623.9 | 5.177 |
| 2045 | 648.4 | 644.7 | 3.724 |
| 2048 | 673.5 | 670.5 | 3.024 |
| 2050 | 712.9 | 708.1 | 4.865 |
| 2053 | 722.9 | 719.1 | 3.781 |
| 2055 | 733.1 | 727.8 | 5.276 |
| 2058 | 756.4 | 749.1 | 7.319 |
| 2060 | 771.7 | 763.8 | 7.912 |
| 2063 | 787.1 | 779.1 | 8.017 |
| 2065 | 797.4 | 788.8 | 8.59 |
| 2068 | 814.3 | 805.1 | 9.175 |
| 2070 | 824.8 | 816.6 | 8.209 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 198.0 | 200.0 | -1.982 |
| 2013 | 175.7 | 179.3 | -3.625 |
| 2015 | 122.3 | 131.1 | -8.79 |
| 2018 | 118.9 | 132.5 | -13.59 |
| 2020 | 138.8 | 145.3 | -6.502 |
| 2023 | 116.7 | 134.0 | -17.29 |
| 2025 | 110.4 | 124.4 | -14 |
| 2028 | 214.7 | 212.8 | 1.901 |
| 2030 | 225.8 | 230.4 | -4.563 |
| 2033 | 175.7 | 168.8 | 6.86 |
| 2035 | 193.5 | 177.8 | 15.76 |
| 2038 | 190.9 | 190.0 | 0.916 |
| 2040 | 206.0 | 204.3 | 1.766 |
| 2043 | 229.8 | 224.7 | 5.154 |
| 2045 | 234.8 | 229.2 | 5.589 |
| 2048 | 239.7 | 235.1 | 4.658 |
| 2050 | 243.1 | 239.0 | 4.141 |
| 2053 | 245.2 | 238.4 | 6.83 |
| 2055 | 247.9 | 242.9 | 5.097 |
| 2058 | 255.0 | 249.0 | 6.066 |
| 2060 | 262.4 | 257.1 | 5.277 |
| 2063 | 267.4 | 262.1 | 5.287 |
| 2065 | 269.2 | 263.8 | 5.338 |
| 2068 | 274.5 | 268.4 | 6.055 |
| 2070 | 275.3 | 271.1 | 4.19 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.528 | 0.3056 |
| 2018 | 11.78 | 0.3988 |
| 2025 | 11.53 | 0.3905 |
| 2033 | 39.01 | 1.32 |
| 2040 | 43.06 | 1.457 |
| 2048 | 29.5 | 0.9985 |
| 2055 | 27.29 | 0.9238 |
| 2063 | 29.68 | 1.005 |
| 2070 | 28.77 | 0.9739 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 7.668 | 0.6045 |
| 2018 | 19.69 | 1.552 |
| 2025 | 427.1 | 33.66 |
| 2033 | 22.61 | 1.782 |
| 2040 | 26.92 | 1.614 |
| 2048 | 16.6 | 0.7411 |
| 2055 | 16.41 | 0.7233 |
| 2063 | 17.01 | 0.3188 |
| 2070 | 16.79 | 0.3503 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 41,562.0 | 0 |
| ELCHIG | 4,375.8 | 0 |
| OILCRD | 0 | 4,291.9 |
| GreenCert-ELC | 3,321.3 | 0 |
| BIOOILFS | 0 | 2,912.3 |
| BIOHVO | 2,513.3 | 0 |
| OILDST | 1,942.1 | 0 |
| OILGSL | 1,584.6 | 0 |
| ELCHYD | 0 | 1,370.9 |
| ELCWOO | 0 | 1,269.5 |
| ELCWIN | 0 | 1,091.6 |
| ELCNUC | 0 | 751.8 |
| HETHTH | 726.7 | 0 |
| ELCCOH | 0 | 407.8 |
| INDCOK | 0 | 354.6 |
| INDCOA | 0 | 307.4 |
| OILKER | 290.3 | 0 |
| OILHFO | 247.2 | 3.927 |
| SUPRPG | 0 | 244.1 |
| COALIG | 0 | 184.1 |
| ELCGAS | 0 | 173.2 |
| ELCCOL | 0 | 149.0 |
| OILRFG | 97.27 | 0 |
| MISSNT | 0 | 94.63 |
| COACOK | 89.17 | 0 |
| OILLPG | 77.22 | 0 |
| MISRIR | 61.87 | 0 |
| SUPRPP | 0 | 56.46 |
| INDBIO | 0 | 53.7 |
| ELCSOL | 0 | 45.51 |
| INDELC | 0 | 44.66 |
| OILNAP | 35.61 | 0 |
| GASCOG | 34.08 | 0 |
| MISOXY | 0 | 27.45 |
| ELCHFO | 0 | 25.34 |
| SUPGAS | 0 | 15.7 |
| BRFH2 | 0 | 12.73 |
| REFHTH | 0 | 8.262 |
| INDGAS | 0 | 6.188 |
| SUPBIO | 0 | 5.529 |
| OILNEU | 4.766 | 0 |
| MISBFS | 4.219 | 0 |
| INDHFO | 0 | 4.127 |
| MISPLT | 0 | 3.857 |
| IGH | 1.587 | 0 |
| INDBFG | 0 | 1.331 |
| MGHRYC | 0 | 1.063 |
| BRFCA3 | 0 | 0.6032 |
| SUPELC | 0 | 0.5628 |
| INDLPG | 0 | 0.4726 |
| ICUHTH | 0 | 0.4112 |
| ELCDST | 0 | 0.3796 |
| MCUORE | 0 | 0.3231 |
| ICU | 0.1688 | 0 |
| SUPHTH | 0 | 0.1267 |
| INDLFO | 0 | 0.09792 |
| MCUSCU | 0 | 0.01802 |
| MCUSCR | 0.006751 | 0 |

- Back-and-forth on the same link, year and timeslice: 0 cases, volume 0
## F. Emissions and certificates
- ELCCO2N: produced, all years: run 118,801.6, reference 130,244.3 (-8.79%); 25 years differ >0.1 %
- ETSCO2: produced, all years: run 364,623.6, reference 343,808.2 (+6.05%); 24 years differ >0.1 %
- INDCO2N: produced, all years: run 131,603.2, reference 126,331.9 (+4.17%); 25 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,248.2, reference 11,202.8 (+0.41%); 25 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,131.8, reference 6,065.4 (+1.09%); 25 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'ELCCO2N': 66862.0, 'GreenCert-ELC': -4.5, 'ETSCO2': 157115.1} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 0 | 0 |
| FI / ELCHIGG | 300 | 5 | 12.39 |
| FI / ELCLOW | 300 | 1 | 16.82 |
| FI / ELCMED | 300 | 4 | 11.25 |
| FI / HETHTH | 300 | 0 | 0 |

- Peak equations outside the hub: 0 region/commodity pairs (none, as intended)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 260; only in run: 24; only in reference: 26
| binding only in run | sum |shadow| |
|---|---|
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 12,784.8 |
| RS_PRD_COMFINOIL_LO | 3,106.7 |
| RS_PRD_RSDFINOIL_LO | 3,100.5 |
| RS_PRD_RSDBIO_LO | 1,433.8 |
| RS_PRD_COMBIO_LO | 1,392.8 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 898.3 |
| RS_PRD_INDFINSOLID_LO | 799.8 |
| RS_PRD_COMGAS_LO | 578.6 |
| RS_PRD_RSDGAS_LO | 540.6 |
| RS_ACT_SSCDCOKE00_LO | 93.91 |
| RS_PRD_COMHET_LO | 74.63 |
| TUC_UP_IOIHET-INDCO | 39.74 |
| RS_PRD_RSDGAS_UP | 36.99 |
| UC_DecrBECCS1 | 26.91 |

| binding only in reference | sum |shadow| |
|---|---|
| TUC_Istruc_COP_PRD | 33,064.1 |
| TUC_Istruc_RIR-CYC | 10,699.4 |
| TUC_Istruc_CST-SSTEEL | 364.6 |
| UC_DecrCCUS7 | 181.2 |
| UC_DecrCCUS3 | 34.77 |
| UC_VARU_CAP_EUFBCOL01 | 7.551 |
| UC_VARU_CAP_EUSTCOHcon01 | 7.551 |
| UC_VARU_CAP_EUSTCOHsup01 | 7.551 |
| UC_VARU_CAP_EUSTCOLsup01 | 7.551 |
| UC_NonDecrWinONCAP | 5.666 |
| UC_VARU_CAP_EUIGCOLCCSpre20 | 4.828 |
| UC_DecrCCUS4 | 4.653 |
| UC_VARU_CAP_EUGEOORC01 | 3.776 |
| UC_VARU_CAP_EUFBCOH15 | 3.776 |
| UC_VARU_CAP_EUGEOEGS01 | 3.776 |

Shadow prices differing by more than 5 %: 263; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_HydroLakeSupply_CE | 819,009.4 | 35,734.3 | 783,275.2 |
| UC_VARU_ACT_EEPP_natgas_OCGT | 364,204.5 | 8,790.4 | 355,414.1 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 250,360.2 | 6,902.7 | 243,457.4 |
| UC_VARU_ACT_EEPP_naturalgas_th | 200,541.2 | 8,719.1 | 191,822.1 |
| UC_VARU_ACT_EEPP_HFO_th | 104,668.6 | 10,729.6 | 93,939.0 |
| UC_VARU_CAP_EEPP_naturalgas_th | 53,039.8 | 2,436.8 | 50,603.0 |
| TUC_Istruc_COP_PRD | 0 | 33,064.1 | -33,064.1 |
| UC_VARU_CAP_EEPP_natgas_CCGT | 27,812.8 | 1,318.7 | 26,494.1 |
| UC_VARU_ACT_EEPP_lignite_th | 33,541.7 | 8,299.1 | 25,242.6 |
| UC_VARU_ACT_EEPP_coal_th | 31,843.2 | 8,298.6 | 23,544.6 |
| UC_ACAES-STG_DischLimit | 17,231.0 | 1,094.8 | 16,136.2 |
| TUC_Istruc_CST-SCR | 26,155.0 | 11,096.4 | 15,058.6 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 12,784.8 | 0 | 12,784.8 |
| TUC_Istruc_RIR-CYC | 0 | 10,699.4 | -10,699.4 |
| UC_VARU_ACT_EUICBGS01 | 24,547.9 | 13,941.5 | 10,606.4 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 1 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI / 2025 / MPPPUP | 1,738.4 | 0 | 1,738.4 |

- CST_FLOX: 0 entries differ
### investment: 249 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Hdt_ELC_01 | 60,833.1 | 56,662.1 | 4,171.0 |
| TRA_Hdt_Dis_01 | 16,134.4 | 19,113.7 | -2,979.4 |
| EUWINOFH01 | 5,034.4 | 2,948.8 | 2,085.6 |
| IISELAFUR01 | 0 | 1,637.5 | -1,637.5 |
| SELCH2EC01 | 1,660.8 | 135.6 | 1,525.2 |
| R_ES-SH-DH_ELC05 | 1,507.0 | 2,896.3 | -1,389.3 |
| IISBLAFURTGRCS20 | 3,912.0 | 2,715.7 | 1,196.3 |
| SELCH2PEM01 | 1,245.2 | 2,349.5 | -1,104.3 |
| EUIGCCWOO01 | 13,884.0 | 12,884.8 | 999.3 |
| TRA_Car_Dis_LoM_81 | 1,348.6 | 350.7 | 997.9 |
| TRA_Car_Elc_LoM_10 | 6,751.4 | 5,867.2 | 884.2 |
| R_ES-SH-DH_ELC04 | 864.6 | 0 | 864.6 |

### fixed O&M: 230 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IISELAFUR01 | 0 | 3,496.4 | -3,496.4 |
| IISFINPRO01 | 0 | 911.1 | -911.1 |
| IISBOXFUR01 | 0 | 887.6 | -887.6 |
| IISDRIH2 | 687.1 | 10.76 | 676.3 |
| TRA_Hdt_ELC_01 | 8,769.6 | 8,168.3 | 601.3 |
| SELCH2EC01 | 627.5 | 51.24 | 576.3 |
| IISBLAFURTGRCS20 | 1,622.7 | 1,126.5 | 496.2 |
| TRA_Hdt_Dis_01 | 2,558.5 | 3,031.0 | -472.5 |
| SELCH2PEM01 | 468.6 | 885.4 | -416.8 |
| IISBLAFURTGR10 | 231.7 | 561.7 | -330.0 |
| EUWINOFH01 | 720.3 | 420.9 | 299.4 |
| TRA_Car_Dis_LoM_81 | 306.5 | 79.71 | 226.8 |

### activity: 320 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IISELAFUR01 | 0 | 1,428.5 | -1,428.5 |
| IISBOXFUR01 | 0 | 1,422.9 | -1,422.9 |
| IISDRIH2 | 401.1 | 6.199 | 394.9 |
| IISBLAFURTGRCS20 | 334.0 | 234.2 | 99.82 |
| IISFINPRO01 | 0 | 98.31 | -98.31 |
| IISSINTERBIO | 458.0 | 360.9 | 97.13 |
| IPPPUPCHE01 | 3,007.9 | 2,934.4 | 73.48 |
| IMPBIOEMHV | 246.2 | 308.2 | -62.06 |
| IISBLAFURTGR10 | 22.86 | 70.09 | -47.23 |
| ICLADVPRO05 | 173.9 | 129.2 | 44.66 |
| ICLADVPRO01 | 12.71 | 55.7 | -43 |
| SELCH2EC01_LowAF | 43.79 | 3.418 | 40.38 |

### flow/import: 72 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IMPOILCRD | 67,853.1 | 57,840.3 | 10,012.8 |
| IMPOILDST | 10,518.0 | 15,101.9 | -4,583.8 |
| MINMISSCR1 | 4,662.0 | 7,738.4 | -3,076.4 |
| EXPOILGSL | -18,975.5 | -16,267.1 | -2,708.3 |
| EXPOILDST | -12,210.6 | -9,767.3 | -2,443.4 |
| MINMISORE1 | 9,267.8 | 7,029.5 | 2,238.3 |
| IMPOILGSL | 2,713.5 | 4,570.2 | -1,856.6 |
| MINMPPWOO1 | 117,298.5 | 115,521.8 | 1,776.6 |
| EXPOILKER | -2,337.2 | -1,176.6 | -1,160.6 |
| IMPOILHFO | 6,232.7 | 5,397.2 | 835.6 |
| IMPGASNATBkStp | 775.0 | 0 | 775.0 |
| EXPCO2-fromFI-coastal | 5,829.2 | 5,133.4 | 695.8 |

### capacity (sum over years): 72 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| R_ES-SH-DH_ELC05 | 828.0 | 1,601.4 | -773.4 |
| R_ES-SH-FL_ELC01 | 11,725.0 | 12,484.1 | -759.1 |
| R_ES-SH-FL_GAS01 | 1,418.9 | 749.8 | 669.1 |
| R_ES-SH-DH_ELC04 | 518.1 | 0 | 518.1 |
| TRA_Car_Elc_LoM_10 | 1,869.0 | 1,552.4 | 316.6 |
| R_ES-SH-DH-70_GAS01 | 466.5 | 775.0 | -308.5 |
| R_ES-SH-SD_GAS01 | 899.4 | 632.6 | 266.8 |
| TRA_Car_Elc_Sma_10 | 7,780.9 | 8,012.9 | -232.0 |
| R_ES-SH-SD_ELC05 | 3,095.6 | 3,320.2 | -224.5 |
| TRA_Car_PIH_Sma_20pct | 3,340.2 | 3,545.9 | -205.7 |
| R_ES-SH-DH-70_ELC07 | 2,104.1 | 1,939.9 | 164.2 |
| TRA_Car_PIH_LoM_20pct | 11,428.7 | 11,590.1 | -161.4 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: 8
| region / process | activity (all years) |
|---|---|
| FI / IISFINPRO00 | 89.01 |
| FI / IISBOXFUR00 | 68.75 |
| FI / IISSINTER00 | 8.276 |
| FI / IISPELLET00 | 3.857 |
| FI / IISELAFUR00 | 3.485 |
| FI / IISAODFUR00 | 0.7377 |
| FI / IISFECRFR00 | 0.1623 |
| FI / INDIISHTH00 | 0.1461 |


## Verdict
FAIL: activity without capacity
