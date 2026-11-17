# Audit of reg_baseline-sami_2026-11-17_task4c.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,529,746.95 M EUR, reference 1,529,919.88, difference -172.94 (-0.0113%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,870.6 | 144,742.3 | 128.3 |
| INV | 919,898.0 | 919,897.7 | 0.2643 |
| VAR | 464,978.4 | 465,279.9 | -301.5 |

| region | objective share |
|---|---|
| FI | 1,402,621.9 |
| FI196 | 32,750.1 |
| FI1B1 | 16,934.9 |
| FI1D9 | 14,619.1 |
| FI1C5 | 13,010.9 |
| FI1C7 | 11,680.8 |
| FI19B | 6,657.0 |
| FI1D7 | 6,601.0 |
| FI198 | 6,262.8 |
| FI19A | 6,240.8 |
| FI1DB | 3,808.3 |
| FI1C1 | 2,893.7 |
| FI1C2 | 1,592.9 |
| FI1C6 | 1,580.1 |
| FI1DC | 1,496.3 |
| FI1DA | 407.2 |
| FI199 | 283.4 |
| FI1D5 | 245.2 |
| FI1D8 | 53.32 |
| FI200 | 7.076 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved
- PRC_RESID national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| EUHYDDAM00 | 1,374.2 | 1,380.6 | -6.443 |
| EEPP_PV | 42.52 | 45.46 | -2.946 |
| ECHP_naturalgas_CCGT | 81.73 | 84.67 | -2.945 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_coal_thermal | 98.56 | 97.15 | 1.411 |
| EEPP_coal_thermal | 41.06 | 40.22 | 0.8393 |
| EEPP_biomass_thermal | 86.04 | 86.31 | -0.2656 |
| ECHP_HFO_thermal | 8.111 | 8.341 | -0.2308 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05895 |
| EEPP_naturalgas_thermal | 0.0681 | 0.09998 | -0.03188 |
| ECHP_LFO_thermal | 0.01581 | 0.02023 | -0.004415 |
| EEPP_windOFF | 23.58 | 23.59 | -0.003647 |
| ECHP_naturalgas_thermal | 2.226 | 2.229 | -0.003069 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| ECHP_lignite_thermal | 29.84 | 29.84 | -0.0005673 |
| EEPP_LFO_thermal | 0.08297 | 0.08335 | -0.0003801 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 5.329e-15 |
| EEPP_HFO_thermal | 2.141 | 2.141 | -8.882e-16 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | 0 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | 0 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | 0 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | 0 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | 0 |

By class and year: 68 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_naturalgas_CCGT / 2020 | 2.758 | 4.179 | -1.421 |
| ECHP_naturalgas_CCGT / 2018 | 2.758 | 4.179 | -1.421 |
| ECHP_coal_thermal / 2020 | 13.92 | 12.65 | 1.27 |
| EUHYDDAM00 / 2063 | 53.78 | 55.04 | -1.251 |
| EUHYDDAM00 / 2070 | 54.02 | 55.03 | -1.006 |
| EUHYDDAM00 / 2068 | 54.06 | 55.04 | -0.9749 |
| EUHYDDAM00 / 2065 | 54.11 | 55.04 | -0.9223 |
| EEPP_coal_thermal / 2013 | 3.284 | 2.445 | 0.8393 |
| EUHYDDAM00 / 2030 | 54.27 | 55.04 | -0.761 |
| EUHYDDAM00 / 2033 | 54.26 | 54.9 | -0.6445 |
| EUHYDDAM00 / 2060 | 54.4 | 55.04 | -0.6329 |
| EEPP_PV / 2023 | 2.688 | 2.932 | -0.2439 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,283.8 |
| FI198 | 76.54 |
| FI199 | 157.8 |
| FI19A | 269.4 |
| FI19B | 91.39 |
| FI1B1 | 244.4 |
| FI1C1 | 122.4 |
| FI1C2 | 50.06 |
| FI1C5 | 236.2 |
| FI1C6 | 30.61 |
| FI1C7 | 55.81 |
| FI1D5 | 165.0 |
| FI1D7 | 591.3 |
| FI1D8 | 93.44 |
| FI1D9 | 732.9 |
| FI1DA | 73.01 |
| FI1DB | 23.44 |
| FI1DC | 97.05 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.5 | 337.6 | -0.06759 |
| 2013 | 292.8 | 292.1 | 0.772 |
| 2015 | 319.9 | 320.1 | -0.2089 |
| 2018 | 371.5 | 373.1 | -1.536 |
| 2020 | 314.1 | 314.9 | -0.7181 |
| 2023 | 380.0 | 380.3 | -0.2492 |
| 2025 | 422.9 | 423.2 | -0.3611 |
| 2028 | 478.0 | 478.3 | -0.2827 |
| 2030 | 507.1 | 507.3 | -0.2215 |
| 2033 | 442.0 | 442.2 | -0.1484 |
| 2035 | 464.1 | 464.2 | -0.09488 |
| 2038 | 521.4 | 521.6 | -0.2051 |
| 2040 | 573.4 | 573.8 | -0.387 |
| 2043 | 623.1 | 623.9 | -0.7847 |
| 2045 | 643.6 | 644.7 | -1.109 |
| 2048 | 669.3 | 670.5 | -1.177 |
| 2050 | 708.4 | 708.1 | 0.348 |
| 2053 | 719.5 | 719.1 | 0.3973 |
| 2055 | 728.2 | 727.8 | 0.3714 |
| 2058 | 749.2 | 749.1 | 0.04173 |
| 2060 | 764.0 | 763.8 | 0.1938 |
| 2063 | 779.0 | 779.1 | -0.02537 |
| 2065 | 788.8 | 788.8 | -0.00237 |
| 2068 | 805.2 | 805.1 | 0.09784 |
| 2070 | 816.6 | 816.6 | 0.07269 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 198.8 | 200.0 | -1.157 |
| 2013 | 179.7 | 179.3 | 0.3415 |
| 2015 | 131.4 | 131.1 | 0.334 |
| 2018 | 131.5 | 132.5 | -0.9654 |
| 2020 | 146.2 | 145.3 | 0.8104 |
| 2023 | 134.4 | 134.0 | 0.362 |
| 2025 | 124.3 | 124.4 | -0.03125 |
| 2028 | 212.7 | 212.8 | -0.1167 |
| 2030 | 230.6 | 230.4 | 0.1972 |
| 2033 | 168.3 | 168.8 | -0.5018 |
| 2035 | 177.4 | 177.8 | -0.3306 |
| 2038 | 189.8 | 190.0 | -0.171 |
| 2040 | 203.6 | 204.3 | -0.6864 |
| 2043 | 223.9 | 224.7 | -0.7907 |
| 2045 | 228.8 | 229.2 | -0.4215 |
| 2048 | 234.6 | 235.1 | -0.5134 |
| 2050 | 239.1 | 239.0 | 0.1338 |
| 2053 | 238.5 | 238.4 | 0.09289 |
| 2055 | 242.7 | 242.9 | -0.1845 |
| 2058 | 248.7 | 249.0 | -0.251 |
| 2060 | 257.2 | 257.1 | 0.1411 |
| 2063 | 262.0 | 262.1 | -0.09641 |
| 2065 | 264.0 | 263.8 | 0.1261 |
| 2068 | 268.6 | 268.4 | 0.1413 |
| 2070 | 271.2 | 271.1 | 0.1506 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.418 | 0.3021 |
| 2018 | 12.47 | 0.4221 |
| 2025 | 5.506 | 0.1865 |
| 2033 | 35.53 | 1.203 |
| 2040 | 47.55 | 1.609 |
| 2048 | 28.48 | 0.9642 |
| 2055 | 28.2 | 0.9544 |
| 2063 | 29.9 | 1.012 |
| 2070 | 29.21 | 0.9888 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.079 | 0.7157 |
| 2018 | 21.58 | 1.701 |
| 2025 | 247.2 | 19.48 |
| 2033 | 23.7 | 1.868 |
| 2040 | 29.94 | 2.019 |
| 2048 | 16.34 | 0.9346 |
| 2055 | 16.84 | 0.9537 |
| 2063 | 17.27 | 0.7791 |
| 2070 | 17.07 | 0.5965 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,115.1 | 0 |
| ICMFISCO2 | 10,396.2 | 0 |
| ELCHIG | 4,402.8 | 0 |
| IPPHTH | 0 | 3,996.3 |
| OILCRD | 0 | 3,850.9 |
| BIOOILFS | 0 | 3,460.0 |
| GreenCert-ELC | 3,342.3 | 0 |
| BIOHVO | 2,986.0 | 0 |
| INDELC | 0 | 2,567.7 |
| INDBLQ | 2,550.2 | 0 |
| OILDST | 1,571.6 | 0 |
| OILGSL | 1,375.8 | 0 |
| ELCHYD | 0 | 1,374.3 |
| ELCWOO | 0 | 1,269.5 |
| ELCWIN | 0 | 1,091.6 |
| MPPWOO | 0 | 771.6 |
| HETHTH | 754.9 | 0 |
| ELCNUC | 0 | 751.8 |
| INDBIO | 466.4 | 138.9 |
| ELCCOH | 0 | 444.5 |
| INDCOK | 0 | 342.9 |
| OILHFO | 323.4 | 5.016 |
| INDRFG | 0 | 289.7 |
| INDCOA | 0 | 284.4 |
| INDGAS | 0 | 265.9 |
| OILKER | 226.9 | 0 |
| SUPRPG | 0 | 219.0 |
| ELCGAS | 0 | 202.4 |
| ICHHTH | 28.03 | 166.7 |
| COALIG | 0 | 189.5 |
| ELCCOL | 0 | 149.0 |
| INDHFO | 0 | 130.7 |
| COACOK | 127.6 | 0 |
| MPPRYC | 0 | 118.4 |
| OILRFG | 106.4 | 0 |
| OILOTH | 94.31 | 0 |
| BIOGAS | 86.61 | 0 |
| INDHTH | 0 | 81.45 |
| MISSNT | 0 | 65.56 |
| MPPGYP | 0 | 63.92 |
| OILLPG | 60.79 | 0 |
| OILNAP | 55.48 | 0 |
| SUPRPP | 0 | 50.66 |
| ELCSOL | 0 | 45.51 |
| GASCOG | 43.1 | 0 |
| MISRIR | 38.29 | 0 |
| ICMPARA | 37.66 | 0 |
| INDLPG | 0 | 31.98 |
| ELCHFO | 0 | 28.38 |
| MISOXY | 0 | 27.68 |
| MISORE | 0 | 20.57 |
| MLMSTN | 0 | 20.19 |
| IIS | 18.42 | 0 |
| INDSLU | 0 | 17.02 |
| SUPGAS | 0 | 16.16 |
| INDCOG | 0 | 15.49 |
| BRFH2 | 0 | 15.12 |
| MPPKAO | 0 | 14.53 |
| MISBFS | 6.857 | 6.893 |
| OILNEU | 13.69 | 0 |
| MISCST | 7.616 | 3.191 |
| MISSCR | 0 | 9.287 |
| REFHTH | 0 | 7.413 |
| GASBFG | 6.934 | 0 |
| MPPNOH | 0 | 5.741 |
| SUPBIO | 0 | 4.961 |
| INDCOL | 0 | 3.453 |
| MPPOXY | 0 | 3.28 |
| INDMUN | 0 | 2.563 |
| INDLFO | 0 | 2.094 |
| IGH | 1.693 | 0 |
| MGHRYC | 0 | 1.174 |
| MISPLT | 0 | 1.106 |
| IISHTH | 0.09221 | 0.7988 |
| INDHH2 | 0 | 0.7987 |
| BRFCA3 | 0 | 0.7166 |
| SUPELC | 0 | 0.6686 |
| INDBFG | 0 | 0.6324 |
| ICUHTH | 0 | 0.4682 |
| ELCDST | 0 | 0.3796 |
| MCUORE | 0 | 0.3679 |
| MISQLI | 0 | 0.2985 |
| ICU | 0.1688 | 0 |
| SUPHTH | 0 | 0.1505 |
| INDCOB | 0 | 0.1388 |
| MCUSCR | 0.006751 | 0 |
| MCUSCU | 0 | 0.001058 |

- Back-and-forth on the same link, year and timeslice: 2 cases, volume 0.91
| link / year / ts | min(imp, exp) |
|---|---|
| TB_MISCST_FI_FI1D7 / 2020 / ANNUAL | 0.86 |
| TB_MISCST_FI_FI1D7 / 2023 / ANNUAL | 0.04999 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 131,070.8, reference 130,244.3 (+0.63%); 19 years differ >0.1 %
- ETSCO2: produced, all years: run 343,201.4, reference 343,808.2 (-0.18%); 14 years differ >0.1 %
- INDCO2N: produced, all years: run 125,806.1, reference 126,331.9 (-0.42%); 23 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,194.8, reference 11,202.8 (-0.07%); 8 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,064.7, reference 6,065.4 (-0.01%); 12 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'GreenCert-ELC': -4.5, 'ETSCO2': 180733.9, 'ELCCO2N': 72344.3} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 0 | 0 |
| FI / ELCHIGG | 300 | 8 | 16.8 |
| FI / ELCLOW | 300 | 5 | 270.8 |
| FI / ELCMED | 300 | 4 | 3.844 |
| FI / HETHTH | 300 | 0 | 0 |

- Peak equations outside the hub: 0 region/commodity pairs (none, as intended)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 262; only in run: 19; only in reference: 24
| binding only in run | sum |shadow| |
|---|---|
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,675.9 |
| RS_PRD_RSDFINOIL_LO | 2,362.2 |
| RS_PRD_COMFINOIL_LO | 2,343.1 |
| RS_PRD_RSDBIO_LO | 1,208.0 |
| RS_PRD_COMBIO_LO | 1,153.4 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 654.5 |
| RS_PRD_COMGAS_LO | 413.4 |
| RS_PRD_RSDGAS_LO | 373.0 |
| RS_PRD_COMHET_LO | 78.27 |
| RS_PRD_INDFINGAS_LO | 66.49 |
| RS_ACT_SSCDCOKE00_LO | 39.88 |
| RS_PRD_COMGAS_UP | 30.67 |
| UCI_UP_CHPShare-IIS | 25.44 |
| RS_PRD_RSDGAS_UP | 24.15 |

| binding only in reference | sum |shadow| |
|---|---|
| TUC_Istruc_RIR-CYC | 10,699.4 |
| UC_AUCoalWithoutCCS | 323.5 |
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

Shadow prices differing by more than 5 %: 152; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_ACT_EEPP_natgas_OCGT | 222,608.0 | 8,790.4 | 213,817.6 |
| UC_VARU_ACT_EEPP_naturalgas_th | 154,258.9 | 8,719.1 | 145,539.7 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 142,762.7 | 6,902.7 | 135,860.0 |
| UC_HydroLakeSupply_CE | 169,826.3 | 35,734.3 | 134,092.0 |
| UC_VARU_ACT_EEPP_HFO_th | 81,155.7 | 10,729.6 | 70,426.0 |
| UC_VARU_CAP_EUCCGASCCSpos20 | 4,230.1 | 56,904.4 | -52,674.3 |
| UC_VARU_CAP_EEPP_natgas_CCGT | 39,703.1 | 1,318.7 | 38,384.4 |
| UC_VARU_CAP_EEPP_naturalgas_th | 40,514.0 | 2,436.8 | 38,077.2 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 24,864.3 | 1,269.5 | 23,594.8 |
| UC_VARU_ACT_EEPP_coal_th | 24,373.7 | 8,298.6 | 16,075.2 |
| UC_VARU_ACT_EEPP_lignite_th | 23,058.1 | 8,299.1 | 14,759.1 |
| TUC_TRA_Lcv-Lpg | 21,926.4 | 32,707.9 | -10,781.6 |
| TUC_Istruc_RIR-CYC | 0 | 10,699.4 | -10,699.4 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,675.9 | 0 | 10,675.9 |
| UC_ACAES-STG_DischLimit | 11,608.7 | 1,094.8 | 10,513.9 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 0 entries differ
- CST_FLOX: 0 entries differ
### investment: 123 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 16,961.7 | 9,902.3 | 7,059.5 |
| COMBATS01 | 3,548.4 | 10,588.6 | -7,040.3 |
| SELCH2EC01 | 11.99 | 135.6 | -123.6 |
| EUIGCCWOO01 | 12,767.5 | 12,884.8 | -117.3 |
| SELCH2PEM01 | 2,462.6 | 2,349.5 | 113.2 |
| R_ES-SH-DH-70_ELC05 | 6,766.5 | 6,877.0 | -110.5 |
| IPPPUPMEC15 | 767.3 | 665.6 | 101.6 |
| R_ES-SH-DH_BIO01 | 5,987.8 | 6,058.0 | -70.21 |
| R_ES-SH-DH-70_ELC07 | 2,959.6 | 3,027.8 | -68.17 |
| R_ES-SH-DH-70_ELC04 | 120.5 | 54.33 | 66.2 |
| IPPPUPMEC01 | 86.89 | 143.6 | -56.72 |
| R_ES-SH-DH_ELC07 | 1,309.0 | 1,257.3 | 51.72 |

### fixed O&M: 115 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| P_RSDBATS01 | 628.4 | 397.7 | 230.7 |
| P_COMBATS01 | 142.9 | 372.8 | -229.9 |
| IISELAFUR01 | 3,566.8 | 3,496.4 | 70.35 |
| IPPPUPMEC15 | 438.4 | 380.3 | 58.07 |
| SELCH2EC01 | 4.529 | 51.24 | -46.71 |
| SELCH2PEM01 | 928.4 | 885.4 | 43.01 |
| IPPPUPMEC01 | 34.84 | 57.58 | -22.74 |
| R_ES-SH-SD_GAS01 | 120.8 | 142.9 | -22.05 |
| ICHSTMHFO01 | 0 | 20.89 | -20.89 |
| IOISTMHFO01 | 50.98 | 32.57 | 18.41 |
| R_ES-SH-DH_BIO01 | 1,481.8 | 1,500.0 | -18.3 |
| R_ES-SH-DH-70_ELC05 | 1,117.7 | 1,134.7 | -16.94 |

### activity: 567 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IISELAFUR01 | 1,458.4 | 1,428.5 | 29.98 |
| MINBIOCRP41 | 1,598.6 | 1,607.3 | -8.752 |
| TB_INDSCO2N_FI_FI1D9 | 5.823 | 0 | 5.823 |
| SELCH2EC01_LowAF | 0.3269 | 3.418 | -3.092 |
| SELCH2PEM01_LowAF | 63.73 | 60.75 | 2.987 |
| ECHP_naturalgas_CCGT | 71.92 | 74.4 | -2.478 |
| EUIGCCWOO01 | 280.9 | 283.3 | -2.415 |
| TB_ICMFISCO2_FI_FI1C1 | 2.079 | 0 | 2.079 |
| ECHP_coal_thermal | 147.6 | 145.5 | 2.069 |
| EUCCGTGAS15 | 113.1 | 111.4 | 1.686 |
| EEPP_coal_thermal | 63.15 | 61.88 | 1.273 |
| S_CCUS_EMIS_H2T | 407.5 | 408.7 | -1.194 |

### flow/import: 36 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EXPCO2-fromFI-coastal | 5,009.7 | 5,133.4 | -123.7 |
| IMPOILCRD | 57,955.4 | 57,840.3 | 115.1 |
| EXPOILDST | -9,832.7 | -9,767.3 | -65.48 |
| IMPGAS_RU_PIP | 21,949.4 | 21,987.4 | -38 |
| IMPOILGSL | 4,538.3 | 4,570.2 | -31.82 |
| R_ES-SH-DH_BIO01 | 2,574.3 | 2,605.8 | -31.47 |
| IMPCOAHAR | 2,716.4 | 2,686.2 | 30.21 |
| MINMISORE1 | 6,999.7 | 7,029.5 | -29.78 |
| IMPOILHFO | 5,379.3 | 5,397.2 | -17.87 |
| MINMISSCR1 | 7,754.6 | 7,738.4 | 16.2 |
| R_ES-SH-DH-70_BIO01 | 237.5 | 224.3 | 13.17 |
| IMPELC-SEtoFI | 6,355.5 | 6,367.7 | -12.27 |

### capacity (sum over years): 55 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 601.4 | 371.0 | 230.4 |
| COMBATS01 | 127.2 | 356.8 | -229.6 |
| R_ES-SH-SD_GAS01 | 534.8 | 632.6 | -97.75 |
| R_ES-SH-SD_ELC01 | 2,202.6 | 2,137.7 | 64.88 |
| R_ES-SH-DH-70_ELC05 | 4,130.5 | 4,193.1 | -62.59 |
| P_RSDBATS01 | 150.3 | 92.74 | 57.6 |
| P_COMBATS01 | 31.8 | 89.2 | -57.4 |
| R_ES-SH-DH-70_GAS01 | 827.9 | 775.0 | 52.9 |
| R_ES-SH-DH-70_ELC04 | 79.37 | 35.78 | 43.59 |
| R_ES-SH-DH-70_ELC07 | 1,899.6 | 1,939.9 | -40.34 |
| R_ES-SH-DH_BIO01 | 3,148.7 | 3,187.6 | -38.88 |
| R_ES-SH-FL_GAS01 | 712.3 | 749.8 | -37.52 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
