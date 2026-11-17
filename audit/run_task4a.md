# Audit of reg_baseline-sami_2026-11-17_task4a_run2.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,529,842.65 M EUR, reference 1,529,919.88, difference -77.23 (-0.0050%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,822.0 | 144,742.3 | 79.71 |
| INV | 919,963.1 | 919,897.7 | 65.36 |
| VAR | 465,057.6 | 465,279.9 | -222.3 |

| region | objective share |
|---|---|
| FI | 1,480,859.4 |
| FI196 | 24,539.6 |
| FI1B1 | 11,278.4 |
| FI1D9 | 8,105.4 |
| FI1C5 | 1,045.9 |
| FI1C1 | 912.4 |
| FI19A | 652.3 |
| FI19B | 540.3 |
| FI1DA | 386.7 |
| FI1C2 | 328.1 |
| FI199 | 283.4 |
| FI1D5 | 245.2 |
| FI198 | 231.2 |
| FI1D7 | 167.0 |
| FI1DB | 84.88 |
| FI1C6 | 57.77 |
| FI1D8 | 53.31 |
| FI1DC | 33.64 |
| FI1C7 | 30.59 |
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
| EUHYDDAM00 | 1,373.8 | 1,380.6 | -6.865 |
| ECHP_naturalgas_CCGT | 81.7 | 84.67 | -2.971 |
| EEPP_PV | 42.52 | 45.46 | -2.942 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_coal_thermal | 98.58 | 97.15 | 1.423 |
| EEPP_coal_thermal | 40.89 | 40.22 | 0.6762 |
| EEPP_biomass_thermal | 86.04 | 86.31 | -0.2712 |
| ECHP_HFO_thermal | 8.112 | 8.341 | -0.2291 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.06279 |
| EEPP_naturalgas_thermal | 0.06909 | 0.09998 | -0.03089 |
| ECHP_LFO_thermal | 0.01581 | 0.02023 | -0.004415 |
| EEPP_windOFF | 23.58 | 23.59 | -0.003647 |
| ECHP_naturalgas_thermal | 2.226 | 2.229 | -0.003069 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08297 | 0.08335 | -0.0003801 |
| ECHP_lignite_thermal | 29.84 | 29.84 | 7.105e-15 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 5.329e-15 |
| EEPP_HFO_thermal | 2.141 | 2.141 | -8.882e-16 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | 0 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | 0 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | 0 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | 0 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | 0 |

By class and year: 72 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_naturalgas_CCGT / 2018 | 2.746 | 4.179 | -1.433 |
| ECHP_naturalgas_CCGT / 2020 | 2.746 | 4.179 | -1.433 |
| ECHP_coal_thermal / 2020 | 13.93 | 12.65 | 1.274 |
| EUHYDDAM00 / 2063 | 53.79 | 55.04 | -1.242 |
| EUHYDDAM00 / 2070 | 54.04 | 55.03 | -0.9935 |
| EUHYDDAM00 / 2068 | 54.07 | 55.04 | -0.963 |
| EUHYDDAM00 / 2065 | 54.13 | 55.04 | -0.9075 |
| EUHYDDAM00 / 2030 | 54.27 | 55.04 | -0.762 |
| EUHYDDAM00 / 2060 | 54.35 | 55.04 | -0.6891 |
| EEPP_coal_thermal / 2013 | 3.121 | 2.445 | 0.6762 |
| EUHYDDAM00 / 2033 | 54.26 | 54.9 | -0.6445 |
| EEPP_PV / 2023 | 2.688 | 2.932 | -0.2439 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,284.2 |
| FI198 | 76.62 |
| FI199 | 157.5 |
| FI19A | 266.6 |
| FI19B | 93.49 |
| FI1B1 | 244.1 |
| FI1C1 | 124.0 |
| FI1C2 | 49.77 |
| FI1C5 | 235.7 |
| FI1C6 | 29.67 |
| FI1C7 | 55.86 |
| FI1D5 | 165.4 |
| FI1D7 | 591.2 |
| FI1D8 | 93.02 |
| FI1D9 | 733.0 |
| FI1DA | 72.99 |
| FI1DB | 23.55 |
| FI1DC | 97.31 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.5 | 337.6 | -0.06813 |
| 2013 | 292.7 | 292.1 | 0.6098 |
| 2015 | 319.9 | 320.1 | -0.2078 |
| 2018 | 371.5 | 373.1 | -1.539 |
| 2020 | 314.1 | 314.9 | -0.7257 |
| 2023 | 380.1 | 380.3 | -0.2224 |
| 2025 | 422.9 | 423.2 | -0.3127 |
| 2028 | 478.1 | 478.3 | -0.193 |
| 2030 | 507.1 | 507.3 | -0.2185 |
| 2033 | 442.0 | 442.2 | -0.2082 |
| 2035 | 464.0 | 464.2 | -0.1553 |
| 2038 | 521.4 | 521.6 | -0.1462 |
| 2040 | 573.6 | 573.8 | -0.2033 |
| 2043 | 623.3 | 623.9 | -0.6258 |
| 2045 | 643.8 | 644.7 | -0.8651 |
| 2048 | 669.8 | 670.5 | -0.6149 |
| 2050 | 707.8 | 708.1 | -0.2661 |
| 2053 | 718.8 | 719.1 | -0.2597 |
| 2055 | 727.8 | 727.8 | -0.00966 |
| 2058 | 749.2 | 749.1 | 0.103 |
| 2060 | 764.2 | 763.8 | 0.4011 |
| 2063 | 779.4 | 779.1 | 0.3556 |
| 2065 | 789.2 | 788.8 | 0.3922 |
| 2068 | 805.2 | 805.1 | 0.1367 |
| 2070 | 816.7 | 816.6 | 0.1015 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 198.8 | 200.0 | -1.157 |
| 2013 | 179.7 | 179.3 | 0.3437 |
| 2015 | 131.5 | 131.1 | 0.3379 |
| 2018 | 131.5 | 132.5 | -0.9644 |
| 2020 | 146.1 | 145.3 | 0.8056 |
| 2023 | 134.4 | 134.0 | 0.3609 |
| 2025 | 124.3 | 124.4 | -0.03125 |
| 2028 | 212.7 | 212.8 | -0.1575 |
| 2030 | 230.5 | 230.4 | 0.1282 |
| 2033 | 168.9 | 168.8 | 0.03722 |
| 2035 | 177.9 | 177.8 | 0.1201 |
| 2038 | 189.9 | 190.0 | -0.03204 |
| 2040 | 204.3 | 204.3 | -0.002001 |
| 2043 | 224.5 | 224.7 | -0.1281 |
| 2045 | 229.5 | 229.2 | 0.2749 |
| 2048 | 235.2 | 235.1 | 0.1623 |
| 2050 | 239.2 | 239.0 | 0.1848 |
| 2053 | 238.5 | 238.4 | 0.06846 |
| 2055 | 243.0 | 242.9 | 0.1304 |
| 2058 | 249.3 | 249.0 | 0.3383 |
| 2060 | 257.9 | 257.1 | 0.8247 |
| 2063 | 262.0 | 262.1 | -0.08721 |
| 2065 | 264.0 | 263.8 | 0.1979 |
| 2068 | 268.7 | 268.4 | 0.232 |
| 2070 | 271.3 | 271.1 | 0.2427 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.609 | 0.4887 |
| 2018 | 12.45 | 0.4215 |
| 2025 | 5.506 | 0.1865 |
| 2033 | 35.55 | 1.203 |
| 2040 | 48.11 | 1.628 |
| 2048 | 28.54 | 0.966 |
| 2055 | 28.2 | 0.9546 |
| 2063 | 29.87 | 1.011 |
| 2070 | 29.21 | 0.9888 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.079 | 0.7157 |
| 2018 | 21.4 | 1.687 |
| 2025 | 246.2 | 19.41 |
| 2033 | 23.7 | 1.868 |
| 2040 | 30.64 | 2.415 |
| 2048 | 16.28 | 1.283 |
| 2055 | 16.54 | 1.067 |
| 2063 | 17.28 | 1.362 |
| 2070 | 17.07 | 1.345 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,114.2 | 0 |
| ELCHIG | 4,402.2 | 0 |
| OILCRD | 0 | 3,846.1 |
| BIOOILFS | 0 | 3,460.0 |
| GreenCert-ELC | 3,324.3 | 0 |
| BIOHVO | 2,986.0 | 0 |
| OILDST | 1,568.3 | 0 |
| OILGSL | 1,376.4 | 0 |
| ELCHYD | 0 | 1,373.9 |
| ELCWOO | 0 | 1,269.5 |
| ELCWIN | 0 | 1,091.6 |
| HETHTH | 754.9 | 0 |
| ELCNUC | 0 | 751.8 |
| ELCCOH | 0 | 444.1 |
| INDCOK | 0 | 342.9 |
| OILHFO | 323.0 | 5.016 |
| INDCOA | 0 | 274.9 |
| OILKER | 226.3 | 0 |
| SUPRPG | 0 | 218.7 |
| ELCGAS | 0 | 202.4 |
| COALIG | 0 | 189.5 |
| ELCCOL | 0 | 149.0 |
| COACOK | 127.6 | 0 |
| INDELC | 0 | 111.0 |
| OILRFG | 106.3 | 0 |
| OILOTH | 94.19 | 0 |
| MISSNT | 0 | 65.56 |
| OILLPG | 59.85 | 0 |
| OILNAP | 55.64 | 0 |
| SUPRPP | 0 | 50.59 |
| ELCSOL | 0 | 45.51 |
| GASCOG | 43.1 | 0 |
| MISRIR | 38.29 | 0 |
| ELCHFO | 0 | 28.38 |
| MISOXY | 0 | 27.68 |
| INDBIO | 0 | 22.56 |
| MISORE | 0 | 20.57 |
| IIS | 18.42 | 0 |
| SUPGAS | 0 | 16.16 |
| INDCOG | 0 | 15.49 |
| BRFH2 | 0 | 15.12 |
| OILNEU | 13.67 | 0 |
| MISCST | 7.616 | 3.191 |
| INDGAS | 0 | 10.07 |
| MISSCR | 0 | 9.287 |
| REFHTH | 0 | 7.404 |
| GASBFG | 6.916 | 0 |
| MISBFS | 6.857 | 0 |
| INDHFO | 0 | 5.141 |
| SUPBIO | 0 | 4.954 |
| IGH | 1.693 | 0 |
| MLMSTN | 0 | 1.277 |
| MGHRYC | 0 | 1.174 |
| MISPLT | 0 | 1.106 |
| INDLPG | 0 | 0.9268 |
| IISHTH | 0.09221 | 0.7988 |
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
| INDLFO | 0 | 0.1115 |
| MCUSCR | 0.006751 | 0 |
| MCUSCU | 0 | 0.001058 |

- Back-and-forth on the same link, year and timeslice: 2 cases, volume 0.91
| link / year / ts | min(imp, exp) |
|---|---|
| TB_MISCST_FI_FI1D7 / 2020 / ANNUAL | 0.86 |
| TB_MISCST_FI_FI1D9 / 2023 / ANNUAL | 0.04999 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 130,600.2, reference 130,244.3 (+0.27%); 19 years differ >0.1 %
- ETSCO2: produced, all years: run 343,291.2, reference 343,808.2 (-0.15%); 13 years differ >0.1 %
- INDCO2N: produced, all years: run 125,888.3, reference 126,331.9 (-0.35%); 17 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,202.9, reference 11,202.8 (+0.00%); 7 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,056.2, reference 6,065.4 (-0.15%); 13 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'ETSCO2': 157935.0, 'ELCCO2N': 72306.6, 'GreenCert-ELC': -4.5} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 15 | 788.6 |
| FI / ELCHIGG | 300 | 7 | 19.66 |
| FI / ELCLOW | 300 | 2 | 157.1 |
| FI / ELCMED | 300 | 7 | 17.44 |
| FI / HETHTH | 300 | 0 | 0 |

- Peak equations outside the hub: 0 region/commodity pairs (none, as intended)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 262; only in run: 20; only in reference: 24
| binding only in run | sum |shadow| |
|---|---|
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,688.1 |
| RS_PRD_RSDFINOIL_LO | 2,357.6 |
| RS_PRD_COMFINOIL_LO | 2,338.5 |
| RS_PRD_RSDBIO_LO | 1,206.4 |
| RS_PRD_COMBIO_LO | 1,151.6 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 653.2 |
| RS_PRD_COMGAS_LO | 412.5 |
| RS_PRD_RSDGAS_LO | 372.4 |
| RS_PRD_COMHET_LO | 78.25 |
| RS_PRD_INDFINGAS_LO | 66.24 |
| RS_ACT_SSCDCOKE00_LO | 39.77 |
| RS_PRD_COMGAS_UP | 30.72 |
| RS_FLO_RSDHET00_HETHTH_UP | 30.04 |
| RS_PRD_RSDGAS_UP | 24.15 |

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
| UC_DecrCCUS4 | 4.653 |
| UC_VARU_CAP_EUGEOORC01 | 3.776 |
| UC_VARU_CAP_EUFBCOH15 | 3.776 |
| UC_VARU_CAP_EUGEOEGS01 | 3.776 |
| UC_VARU_CAP_EUGEOF01 | 3.776 |
| UC_VARU_CAP_EUIGCCCOH15 | 3.776 |
| UC_VARU_CAP_EUIGCCCOL01 | 3.776 |

Shadow prices differing by more than 5 %: 138; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_ACT_EEPP_natgas_OCGT | 124,077.1 | 8,790.4 | 115,286.8 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 81,111.6 | 6,902.7 | 74,208.9 |
| UC_VARU_ACT_EEPP_naturalgas_th | 79,277.0 | 8,719.1 | 70,557.8 |
| UC_VARU_CAP_EEPP_naturalgas_th | 39,552.9 | 2,436.8 | 37,116.1 |
| UC_HydroLakeSupply_CE | 4,423.9 | 35,734.3 | -31,310.4 |
| UC_VARU_ACT_EEPP_HFO_th | 32,487.3 | 10,729.6 | 21,757.6 |
| UC_VARU_CAP_EEPP_natgas_CCGT | 18,650.2 | 1,318.7 | 17,331.5 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 11,971.6 | 1,269.5 | 10,702.1 |
| TUC_Istruc_RIR-CYC | 0 | 10,699.4 | -10,699.4 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,688.1 | 0 | 10,688.1 |
| UC_R_SPLBoiler_CHP_SD_GAS | 5,100.3 | 72.69 | 5,027.6 |
| UC_R_SPLBoiler_CHP_DH-70_GAS | 5,097.4 | 90.91 | 5,006.5 |
| UC_R_SPLBoiler_CHP_SD_H2 | 5,136.0 | 150.4 | 4,985.6 |
| UC_R_SPLBoiler_CHP_FL_GAS | 5,124.1 | 148.8 | 4,975.4 |
| UC_R_SPLBoiler_CHP_DH_GAS | 5,098.7 | 202.5 | 4,896.2 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 0 entries differ
- CST_FLOX: 0 entries differ
### investment: 109 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 11,500.7 | 9,902.3 | 1,598.4 |
| COMBATS01 | 8,992.9 | 10,588.6 | -1,595.7 |
| SELCH2EC01 | 2.356 | 135.6 | -133.3 |
| SELCH2PEM01 | 2,459.8 | 2,349.5 | 110.3 |
| R_ES-SH-DH-70_ELC05 | 6,770.7 | 6,877.0 | -106.3 |
| R_ES-SH-DH-70_ELC07 | 2,964.3 | 3,027.8 | -63.48 |
| R_ES-SH-DH-70_ELC04 | 113.1 | 54.33 | 58.77 |
| R_ES-SH-DH_BIO01 | 6,000.7 | 6,058.0 | -57.34 |
| R_ES-SH-DH_ELC05 | 2,949.4 | 2,896.3 | 53.12 |
| EUWINOFH01 | 2,996.6 | 2,948.8 | 47.8 |
| R_ES-SH-SD_GAS01 | 247.5 | 291.5 | -44.03 |
| R_ES-SH-DH-70_BIO01 | 755.8 | 713.4 | 42.43 |

### fixed O&M: 107 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IISELAFUR01 | 3,566.8 | 3,496.4 | 70.35 |
| P_RSDBATS01 | 462.4 | 397.7 | 64.69 |
| P_COMBATS01 | 308.2 | 372.8 | -64.61 |
| SELCH2EC01 | 0.8903 | 51.24 | -50.35 |
| SELCH2PEM01 | 927.3 | 885.4 | 41.93 |
| R_ES-SH-SD_GAS01 | 120.9 | 142.9 | -21.96 |
| IOISTMBIO01 | 456.8 | 474.0 | -17.18 |
| R_ES-SH-DH-70_ELC05 | 1,118.4 | 1,134.7 | -16.27 |
| R_ES-SH-DH_BIO01 | 1,484.9 | 1,500.0 | -15.19 |
| IOISTMHFO01 | 46.48 | 32.57 | 13.91 |
| ICHSTMBIO01 | 278.9 | 265.3 | 13.69 |
| ICHSTMHFO01 | 7.519 | 20.89 | -13.37 |

### activity: 303 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IISELAFUR01 | 1,458.4 | 1,428.5 | 29.98 |
| MINBIOCRP41 | 1,598.6 | 1,607.3 | -8.752 |
| TB_INDSCO2N_FI_FI1D9 | 5.823 | 0 | 5.823 |
| SELCH2EC01_LowAF | 0.06425 | 3.418 | -3.354 |
| SELCH2PEM01_LowAF | 63.55 | 60.75 | 2.802 |
| ECHP_naturalgas_CCGT | 71.91 | 74.4 | -2.495 |
| ECHP_coal_thermal | 147.6 | 145.5 | 2.087 |
| EUCCGASCCSpos20 | 198.4 | 199.6 | -1.18 |
| EEPP_coal_thermal | 62.91 | 61.88 | 1.026 |
| EUIGCCWOO01 | 284.1 | 283.3 | 0.8057 |
| TB_OILCRD_FI_FI1B1 | 0.7692 | 0 | 0.7692 |
| INDIPPLFOHTH06 | 12.49 | 13.25 | -0.759 |

### flow/import: 32 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EXPOILGSL | -16,434.8 | -16,267.1 | -167.7 |
| IMPOILGSL | 4,664.6 | 4,570.2 | 94.44 |
| EXPOILDST | -9,847.4 | -9,767.3 | -80.13 |
| IMPOILDST | 15,157.1 | 15,101.9 | 55.22 |
| MINMISORE1 | 6,999.7 | 7,029.5 | -29.78 |
| IMPGAS_RU_PIP | 21,958.6 | 21,987.4 | -28.79 |
| IMPCOAHAR | 2,714.6 | 2,686.2 | 28.36 |
| R_ES-SH-DH_BIO01 | 2,579.8 | 2,605.8 | -26.03 |
| IMPELC-EetoFI | 1,544.7 | 1,528.3 | 16.35 |
| MINMISSCR1 | 7,754.6 | 7,738.4 | 16.2 |
| IMPOILHFO | 5,412.8 | 5,397.2 | 15.66 |
| R_ES-SH-DH-70_BIO01 | 238.0 | 224.3 | 13.74 |

### capacity (sum over years): 57 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| R_ES-SH-SD_GAS01 | 535.4 | 632.6 | -97.19 |
| RSDBATS01 | 432.2 | 371.0 | 61.24 |
| COMBATS01 | 295.6 | 356.8 | -61.15 |
| R_ES-SH-DH-70_ELC05 | 4,133.0 | 4,193.1 | -60.14 |
| R_ES-SH-SD_ELC01 | 2,197.8 | 2,137.7 | 60.01 |
| R_ES-SH-DH-70_GAS01 | 826.2 | 775.0 | 51.25 |
| R_ES-SH-DH-70_ELC04 | 74.47 | 35.78 | 38.7 |
| R_ES-SH-FL_GAS01 | 712.3 | 749.8 | -37.47 |
| R_ES-SH-DH-70_ELC07 | 1,902.7 | 1,939.9 | -37.23 |
| R_ES-SH-FL_ELC01 | 12,516.8 | 12,484.1 | 32.74 |
| R_ES-SH-DH_BIO01 | 3,155.3 | 3,187.6 | -32.28 |
| R_ES-SH-DH_ELC05 | 1,631.5 | 1,601.4 | 30.02 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
