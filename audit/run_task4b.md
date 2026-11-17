# Audit of reg_baseline-sami_2026-11-17_task4b_run3.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,529,745.36 M EUR, reference 1,529,919.88, difference -174.52 (-0.0114%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,870.6 | 144,742.3 | 128.3 |
| INV | 919,898.0 | 919,897.7 | 0.2643 |
| VAR | 464,976.8 | 465,279.9 | -303.1 |

| region | objective share |
|---|---|
| FI | 1,404,454.2 |
| FI196 | 32,624.7 |
| FI1B1 | 17,104.3 |
| FI1D9 | 14,618.8 |
| FI1C5 | 13,025.1 |
| FI1C7 | 11,640.7 |
| FI1D7 | 6,977.7 |
| FI19B | 6,606.2 |
| FI198 | 6,186.9 |
| FI19A | 6,058.0 |
| FI1DB | 3,904.7 |
| FI1C2 | 1,666.3 |
| FI1C6 | 1,499.9 |
| FI1DC | 1,437.0 |
| FI1C1 | 944.6 |
| FI1DA | 407.2 |
| FI199 | 283.4 |
| FI1D5 | 245.2 |
| FI1D8 | 53.31 |
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
| EUHYDDAM00 | 1,374.2 | 1,380.6 | -6.443 |
| ECHP_naturalgas_CCGT | 81.73 | 84.67 | -2.942 |
| EEPP_PV | 42.52 | 45.46 | -2.942 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_coal_thermal | 98.56 | 97.15 | 1.411 |
| EEPP_coal_thermal | 41.06 | 40.22 | 0.8393 |
| EEPP_biomass_thermal | 86.04 | 86.31 | -0.2682 |
| ECHP_HFO_thermal | 8.111 | 8.341 | -0.2302 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05704 |
| EEPP_naturalgas_thermal | 0.07332 | 0.09998 | -0.02666 |
| ECHP_LFO_thermal | 0.01581 | 0.02023 | -0.004415 |
| EEPP_windOFF | 23.58 | 23.59 | -0.003647 |
| ECHP_naturalgas_thermal | 2.226 | 2.229 | -0.003069 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08297 | 0.08335 | -0.0003801 |
| ECHP_lignite_thermal | 29.84 | 29.84 | 1.066e-14 |
| EEPP_HFO_thermal | 2.141 | 2.141 | -8.882e-16 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 0 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | 0 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | 0 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | 0 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | 0 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | 0 |

By class and year: 68 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_naturalgas_CCGT / 2018 | 2.761 | 4.179 | -1.418 |
| ECHP_naturalgas_CCGT / 2020 | 2.761 | 4.179 | -1.418 |
| ECHP_coal_thermal / 2020 | 13.92 | 12.65 | 1.27 |
| EUHYDDAM00 / 2063 | 53.78 | 55.04 | -1.251 |
| EUHYDDAM00 / 2070 | 54.03 | 55.03 | -1.004 |
| EUHYDDAM00 / 2068 | 54.06 | 55.04 | -0.9749 |
| EUHYDDAM00 / 2065 | 54.11 | 55.04 | -0.9223 |
| EEPP_coal_thermal / 2013 | 3.284 | 2.445 | 0.8393 |
| EUHYDDAM00 / 2030 | 54.27 | 55.04 | -0.761 |
| EUHYDDAM00 / 2033 | 54.26 | 54.9 | -0.6445 |
| EUHYDDAM00 / 2060 | 54.4 | 55.04 | -0.6329 |
| EEPP_PV / 2023 | 2.688 | 2.932 | -0.2439 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,284.0 |
| FI198 | 76.55 |
| FI199 | 157.6 |
| FI19A | 269.4 |
| FI19B | 93.97 |
| FI1B1 | 245.3 |
| FI1C1 | 121.4 |
| FI1C2 | 48.83 |
| FI1C5 | 235.5 |
| FI1C6 | 29.83 |
| FI1C7 | 56.02 |
| FI1D5 | 165.0 |
| FI1D7 | 591.2 |
| FI1D8 | 93.25 |
| FI1D9 | 732.6 |
| FI1DA | 72.99 |
| FI1DB | 23.56 |
| FI1DC | 97.55 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.5 | 337.6 | -0.06825 |
| 2013 | 292.8 | 292.1 | 0.7726 |
| 2015 | 319.9 | 320.1 | -0.2059 |
| 2018 | 371.6 | 373.1 | -1.531 |
| 2020 | 314.1 | 314.9 | -0.715 |
| 2023 | 380.0 | 380.3 | -0.2491 |
| 2025 | 422.9 | 423.2 | -0.3622 |
| 2028 | 478.0 | 478.3 | -0.2828 |
| 2030 | 507.1 | 507.3 | -0.2242 |
| 2033 | 442.0 | 442.2 | -0.1484 |
| 2035 | 464.1 | 464.2 | -0.09488 |
| 2038 | 521.4 | 521.6 | -0.2051 |
| 2040 | 573.4 | 573.8 | -0.387 |
| 2043 | 623.1 | 623.9 | -0.7793 |
| 2045 | 643.6 | 644.7 | -1.108 |
| 2048 | 669.3 | 670.5 | -1.177 |
| 2050 | 708.4 | 708.1 | 0.348 |
| 2053 | 719.5 | 719.1 | 0.3974 |
| 2055 | 728.2 | 727.8 | 0.3714 |
| 2058 | 749.2 | 749.1 | 0.04108 |
| 2060 | 764.0 | 763.8 | 0.1938 |
| 2063 | 779.0 | 779.1 | -0.02537 |
| 2065 | 788.8 | 788.8 | -0.00237 |
| 2068 | 805.2 | 805.1 | 0.09784 |
| 2070 | 816.6 | 816.6 | 0.07422 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 198.8 | 200.0 | -1.158 |
| 2013 | 179.7 | 179.3 | 0.341 |
| 2015 | 131.4 | 131.1 | 0.3354 |
| 2018 | 131.5 | 132.5 | -0.9622 |
| 2020 | 146.2 | 145.3 | 0.8137 |
| 2023 | 134.4 | 134.0 | 0.363 |
| 2025 | 124.3 | 124.4 | -0.03125 |
| 2028 | 212.7 | 212.8 | -0.1173 |
| 2030 | 230.6 | 230.4 | 0.1949 |
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
| 2048 | 28.49 | 0.9642 |
| 2055 | 28.19 | 0.9544 |
| 2063 | 29.9 | 1.012 |
| 2070 | 29.21 | 0.9888 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.079 | 0.7157 |
| 2018 | 21.41 | 1.688 |
| 2025 | 247.2 | 19.48 |
| 2033 | 23.7 | 1.868 |
| 2040 | 29.94 | 2.36 |
| 2048 | 16.34 | 1.288 |
| 2055 | 16.84 | 1.227 |
| 2063 | 17.27 | 1.361 |
| 2070 | 17.07 | 1.345 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,115.1 | 0 |
| ELCHIG | 4,402.8 | 0 |
| IPPHTH | 0 | 3,996.3 |
| OILCRD | 0 | 3,850.9 |
| BIOOILFS | 0 | 3,460.0 |
| GreenCert-ELC | 3,342.3 | 0 |
| BIOHVO | 2,986.0 | 0 |
| INDBLQ | 2,550.2 | 0 |
| INDELC | 0 | 2,539.8 |
| OILDST | 1,571.6 | 0 |
| OILGSL | 1,375.8 | 0 |
| ELCHYD | 0 | 1,374.3 |
| ELCWOO | 0 | 1,269.5 |
| ELCWIN | 0 | 1,091.6 |
| MPPWOO | 0 | 771.6 |
| HETHTH | 754.9 | 0 |
| ELCNUC | 0 | 751.8 |
| INDBIO | 497.3 | 174.9 |
| ELCCOH | 0 | 444.5 |
| INDCOK | 0 | 342.9 |
| OILHFO | 323.4 | 5.016 |
| INDRFG | 0 | 289.7 |
| INDCOA | 0 | 275.3 |
| INDGAS | 0 | 239.0 |
| OILKER | 226.9 | 0 |
| SUPRPG | 0 | 219.0 |
| ELCGAS | 0 | 202.4 |
| COALIG | 0 | 189.5 |
| ELCCOL | 0 | 149.0 |
| COACOK | 127.6 | 0 |
| INDHFO | 0 | 120.5 |
| MPPRYC | 0 | 118.4 |
| OILRFG | 106.4 | 0 |
| ICHHTH | 0.02172 | 94.39 |
| OILOTH | 94.31 | 0 |
| BIOGAS | 86.61 | 0 |
| INDHTH | 0 | 85.47 |
| ICLHTH | 42.39 | 42.39 |
| MISSNT | 0 | 65.56 |
| MPPGYP | 0 | 63.92 |
| OILLPG | 60.79 | 0 |
| OILNAP | 55.48 | 0 |
| SUPRPP | 0 | 50.66 |
| ELCSOL | 0 | 45.51 |
| GASCOG | 43.1 | 0 |
| MISRIR | 38.29 | 0 |
| INDLPG | 0 | 31.98 |
| ELCHFO | 0 | 28.38 |
| MISOXY | 0 | 27.68 |
| MISORE | 0 | 20.57 |
| MLMSTN | 0 | 20.19 |
| IIS | 18.42 | 0 |
| SUPGAS | 0 | 16.16 |
| INDCOG | 0 | 15.49 |
| BRFH2 | 0 | 15.12 |
| MPPKAO | 0 | 14.53 |
| OILNEU | 13.69 | 0 |
| MISCST | 7.616 | 3.191 |
| MISSCR | 0 | 9.287 |
| REFHTH | 0 | 7.413 |
| GASBFG | 6.934 | 0 |
| MISBFS | 6.857 | 0 |
| MPPNOH | 0 | 5.741 |
| SUPBIO | 0 | 4.961 |
| INDCOL | 0 | 3.453 |
| MPPOXY | 0 | 3.28 |
| INDMUN | 0 | 2.355 |
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
| INDSLU | 0 | 0.254 |
| ICU | 0.1688 | 0 |
| SUPHTH | 0 | 0.1505 |
| INDCOB | 0 | 0.1388 |
| MCUSCR | 0.006751 | 0 |
| MCUSCU | 0 | 0.001058 |

- Back-and-forth on the same link, year and timeslice: 17 cases, volume 43.3
| link / year / ts | min(imp, exp) |
|---|---|
| TB_ICLHTH_FI_FI1B1 / 2043 / R | 6.8 |
| TB_ICLHTH_FI_FI1B1 / 2040 / F | 6.663 |
| TB_ICLHTH_FI_FI1B1 / 2038 / F | 6.142 |
| TB_ICLHTH_FI_FI1B1 / 2035 / F | 5.361 |
| TB_ICLHTH_FI_FI1B1 / 2033 / R | 4.868 |
| TB_ICLHTH_FI_FI1B1 / 2030 / W | 4.128 |
| TB_ICLHTH_FI_FI1B1 / 2028 / W | 3.677 |
| TB_ICLHTH_FI_FI1B1 / 2045 / R | 1.562 |
| TB_ICLHTH_FI_FI1B1 / 2070 / W | 1.031 |
| TB_MISCST_FI_FI1D9 / 2020 / ANNUAL | 0.86 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 131,070.8, reference 130,244.3 (+0.63%); 19 years differ >0.1 %
- ETSCO2: produced, all years: run 343,489.7, reference 343,808.2 (-0.09%); 14 years differ >0.1 %
- INDCO2N: produced, all years: run 125,806.1, reference 126,331.9 (-0.42%); 23 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,194.8, reference 11,202.8 (-0.07%); 8 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,064.7, reference 6,065.4 (-0.01%); 12 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'GreenCert-ELC': -4.5, 'ELCCO2N': 72344.3, 'ETSCO2': 176809.8} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 0 | 0 |
| FI / ELCHIGG | 300 | 9 | 20.39 |
| FI / ELCLOW | 300 | 1 | 140.5 |
| FI / ELCMED | 300 | 2 | 5.365 |
| FI / HETHTH | 300 | 0 | 0 |

- Peak equations outside the hub: 0 region/commodity pairs (none, as intended)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 264; only in run: 18; only in reference: 22
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
| RS_ACT_SSCDCOKE00_FX | 19.23 |
| RS_ACT_EEHP_DistHeating_LO | 12.48 |
| RS_ACT_SSCDRFLX00_LO | 12.14 |

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

Shadow prices differing by more than 5 %: 149; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_ACT_EEPP_natgas_OCGT | 303,656.6 | 8,790.4 | 294,866.2 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 167,307.8 | 6,902.7 | 160,405.1 |
| UC_VARU_ACT_EEPP_naturalgas_th | 163,495.8 | 8,719.1 | 154,776.6 |
| UC_HydroLakeSupply_CE | 145,140.6 | 35,734.3 | 109,406.3 |
| UC_VARU_ACT_EEPP_HFO_th | 81,792.1 | 10,729.6 | 71,062.5 |
| UC_VARU_CAP_EEPP_naturalgas_th | 34,903.2 | 2,436.8 | 32,466.4 |
| UC_VARU_CAP_EEPP_natgas_CCGT | 30,516.1 | 1,318.7 | 29,197.4 |
| UC_VARU_ACT_EEPP_coal_th | 32,605.7 | 8,298.6 | 24,307.2 |
| UC_VARU_ACT_EEPP_lignite_th | 22,960.1 | 8,299.1 | 14,661.0 |
| UC_VARU_ACT_EUICBGS01 | 26,644.1 | 13,941.5 | 12,702.6 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 12,696.8 | 1,269.5 | 11,427.3 |
| TUC_Istruc_RIR-CYC | 0 | 10,699.4 | -10,699.4 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,675.9 | 0 | 10,675.9 |
| UC_VARU_ACT_EUIGCCWOOCCS01 | 8,104.2 | 1,340.7 | 6,763.4 |
| UC_DCAES-STS_DischLimit | 5,590.5 | 1,051.9 | 4,538.6 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 0 entries differ
- CST_FLOX: 0 entries differ
### investment: 118 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| RSDBATS01 | 10,324.0 | 9,902.3 | 421.7 |
| COMBATS01 | 10,186.1 | 10,588.6 | -402.5 |
| SELCH2EC01 | 11.99 | 135.6 | -123.6 |
| EUIGCCWOO01 | 12,767.5 | 12,884.8 | -117.3 |
| SELCH2PEM01 | 2,462.6 | 2,349.5 | 113.2 |
| R_ES-SH-DH-70_ELC05 | 6,766.5 | 6,877.0 | -110.5 |
| IPPPUPMEC15 | 767.3 | 665.6 | 101.6 |
| ICHSTMBIO01 | 386.0 | 303.9 | 82.15 |
| IOISTMBIO01 | 470.1 | 543.0 | -72.87 |
| R_ES-SH-DH_BIO01 | 5,987.8 | 6,058.0 | -70.21 |
| R_ES-SH-DH-70_ELC07 | 2,959.6 | 3,027.8 | -68.17 |
| R_ES-SH-DH-70_ELC04 | 120.5 | 54.33 | 66.2 |

### fixed O&M: 111 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| ICHSTMBIO01 | 337.0 | 265.3 | 71.71 |
| IISELAFUR01 | 3,566.8 | 3,496.4 | 70.35 |
| IOISTMBIO01 | 410.4 | 474.0 | -63.61 |
| IPPPUPMEC15 | 438.4 | 380.3 | 58.07 |
| SELCH2EC01 | 4.529 | 51.24 | -46.71 |
| SELCH2PEM01 | 928.4 | 885.4 | 43.01 |
| IPPPUPMEC01 | 34.84 | 57.58 | -22.74 |
| R_ES-SH-SD_GAS01 | 120.8 | 142.9 | -22.05 |
| ICHSTMHFO01 | 0 | 20.89 | -20.89 |
| R_ES-SH-DH_BIO01 | 1,481.8 | 1,500.0 | -18.3 |
| IOISTMHFO01 | 50.28 | 32.57 | 17.72 |
| R_ES-SH-DH-70_ELC05 | 1,117.7 | 1,134.7 | -16.94 |

### activity: 565 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IISELAFUR01 | 1,458.4 | 1,428.5 | 29.98 |
| MINBIOCRP41 | 1,598.6 | 1,607.3 | -8.752 |
| TB_INDSCO2N_FI_FI1D9 | 5.823 | 0 | 5.823 |
| SELCH2EC01_LowAF | 0.3269 | 3.418 | -3.092 |
| SELCH2PEM01_LowAF | 63.73 | 60.75 | 2.987 |
| ECHP_naturalgas_CCGT | 71.92 | 74.4 | -2.478 |
| EUIGCCWOO01 | 280.9 | 283.3 | -2.415 |
| ECHP_coal_thermal | 147.6 | 145.5 | 2.069 |
| EUCCGTGAS15 | 113.1 | 111.4 | 1.686 |
| EEPP_coal_thermal | 63.15 | 61.88 | 1.273 |
| S_CCUS_EMIS_H2T | 407.5 | 408.7 | -1.194 |
| CHPIPCSREBLQ015 | 23.95 | 24.84 | -0.8848 |

### flow/import: 36 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EXPCO2-fromFI-coastal | 5,009.7 | 5,133.4 | -123.7 |
| IMPOILCRD | 57,955.4 | 57,840.3 | 115.1 |
| EXPOILDST | -9,832.7 | -9,767.3 | -65.48 |
| IMPELC-SEtoFI | 6,315.0 | 6,367.7 | -52.7 |
| IMPGAS_RU_PIP | 21,949.4 | 21,987.4 | -38 |
| IMPOILGSL | 4,538.3 | 4,570.2 | -31.82 |
| R_ES-SH-DH_BIO01 | 2,574.3 | 2,605.8 | -31.47 |
| IMPCOAHAR | 2,716.4 | 2,686.2 | 30.21 |
| MINMISORE1 | 6,999.7 | 7,029.5 | -29.78 |
| IMPELC-EetoFI | 1,551.1 | 1,528.3 | 22.8 |
| IMPELC-NOtoFI | 251.0 | 230.7 | 20.36 |
| IMPOILHFO | 5,379.3 | 5,397.2 | -17.87 |

### capacity (sum over years): 55 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| R_ES-SH-SD_GAS01 | 534.8 | 632.6 | -97.75 |
| R_ES-SH-SD_ELC01 | 2,202.6 | 2,137.7 | 64.88 |
| R_ES-SH-DH-70_ELC05 | 4,130.5 | 4,193.1 | -62.59 |
| R_ES-SH-DH-70_GAS01 | 827.9 | 775.0 | 52.9 |
| R_ES-SH-DH-70_ELC04 | 79.37 | 35.78 | 43.59 |
| R_ES-SH-DH-70_ELC07 | 1,899.6 | 1,939.9 | -40.34 |
| R_ES-SH-DH_BIO01 | 3,148.7 | 3,187.6 | -38.88 |
| R_ES-SH-FL_GAS01 | 712.3 | 749.8 | -37.52 |
| R_ES-SH-FL_ELC01 | 12,517.2 | 12,484.1 | 33.13 |
| R_ES-SH-DH_ELC07 | 817.1 | 786.7 | 30.45 |
| R_ES-SH-DH-70_BIO01 | 402.8 | 380.6 | 22.23 |
| R_ES-SH-SD_ELC05 | 3,338.4 | 3,320.2 | 18.21 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
