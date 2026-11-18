# Audit of reg_baseline-sami_2026-11-18_task5a.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,450,307.09 M EUR, reference 1,529,919.88, difference -79,612.80 (-5.2037%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 133,356.0 | 144,742.3 | -11,386.3 |
| INV | 880,261.7 | 919,897.7 | -39,636.0 |
| VAR | 436,689.4 | 465,279.9 | -28,590.4 |

| region | objective share |
|---|---|
| FI | 1,319,610.6 |
| FI196 | 33,010.8 |
| FI1B1 | 19,260.8 |
| FI1D9 | 14,822.0 |
| FI1C5 | 12,010.1 |
| FI1C7 | 10,835.1 |
| FI19B | 7,463.0 |
| FI19A | 6,589.5 |
| FI198 | 6,313.7 |
| FI1D7 | 6,269.0 |
| FI1DB | 3,978.9 |
| FI1C1 | 3,211.7 |
| FI1C6 | 1,936.5 |
| FI1C2 | 1,893.6 |
| FI1DC | 1,649.1 |
| FI1DA | 490.6 |
| FI199 | 471.8 |
| FI1D5 | 393.8 |
| FI1D8 | 80.9 |
| FI200 | 15.67 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: 2 keys differ
| key | run | reference | diff |
|---|---|---|---|
| AGRGAS00 | 0 | 0.01616 | -0.01616 |
| ICLSTDPRO01 | 0.01897 | 0.01872 | 0.0002481 |

- PRC_RESID national totals: 29 keys differ
| key | run | reference | diff |
|---|---|---|---|
| AGRGAS00 / 2010 | 0 | 0.03143 | -0.03143 |
| AGRGAS00 / 2013 | 0 | 0.02955 | -0.02955 |
| AGRGAS00 / 2015 | 0 | 0.02829 | -0.02829 |
| AGRGAS00 / 2018 | 0 | 0.0264 | -0.0264 |
| AGRGAS00 / 2020 | 0 | 0.02515 | -0.02515 |
| AGRGAS00 / 2023 | 0 | 0.02326 | -0.02326 |
| AGRGAS00 / 2025 | 0 | 0.022 | -0.022 |
| AGRGAS00 / 2028 | 0 | 0.02012 | -0.02012 |
| AGRGAS00 / 2030 | 0 | 0.01886 | -0.01886 |
| AGRGAS00 / 2033 | 0 | 0.01697 | -0.01697 |
| AGRGAS00 / 2035 | 0 | 0.01572 | -0.01572 |
| AGRGAS00 / 2038 | 0 | 0.01383 | -0.01383 |
| AGRGAS00 / 2040 | 0 | 0.01257 | -0.01257 |
| AGRGAS00 / 2043 | 0 | 0.01069 | -0.01069 |
| AGRGAS00 / 2045 | 0 | 0.009429 | -0.009429 |


## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| ECHP_naturalgas_CCGT | 50.66 | 84.67 | -34.02 |
| ECHP_biomass_thermal | 327.0 | 313.6 | 13.43 |
| ECHP_coal_thermal | 105.8 | 97.15 | 8.604 |
| EEPP_HFO_thermal | 6.187 | 2.141 | 4.046 |
| EEPP_coal_thermal | 43.55 | 40.22 | 3.334 |
| EEPP_PV | 42.59 | 45.46 | -2.877 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_lignite_thermal | 31.21 | 29.84 | 1.37 |
| EUHYDDAM00 | 1,379.4 | 1,380.6 | -1.177 |
| EEPP_biomass_thermal | 86.04 | 86.31 | -0.2693 |
| ECHP_HFO_thermal | 8.296 | 8.341 | -0.04518 |
| EEPP_naturalgas_thermal | 0.07068 | 0.09998 | -0.0293 |
| ECHP_LFO_thermal | 0.01304 | 0.02023 | -0.007191 |
| EEPP_windOFF | 23.58 | 23.59 | -0.003647 |
| ECHP_naturalgas_thermal | 2.226 | 2.229 | -0.003221 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08297 | 0.08335 | -0.0003801 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 5.329e-15 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | 0 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | 0 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | 0 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | 0 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | 0 |

By class and year: 73 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_naturalgas_CCGT / 2015 | 19.67 | 28.22 | -8.555 |
| ECHP_naturalgas_CCGT / 2013 | 15.49 | 24.04 | -8.551 |
| ECHP_naturalgas_CCGT / 2010 | 15.49 | 24.04 | -8.551 |
| ECHP_coal_thermal / 2020 | 20.55 | 12.65 | 7.895 |
| ECHP_biomass_thermal / 2035 | 4.498 | 0 | 4.498 |
| ECHP_biomass_thermal / 2038 | 4.498 | 0 | 4.498 |
| ECHP_biomass_thermal / 2033 | 4.498 | 0 | 4.498 |
| ECHP_naturalgas_CCGT / 2020 | 0 | 4.179 | -4.179 |
| ECHP_naturalgas_CCGT / 2018 | 0 | 4.179 | -4.179 |
| EEPP_coal_thermal / 2013 | 5.779 | 2.445 | 3.334 |
| ECHP_lignite_thermal / 2018 | 1.37 | 0 | 1.37 |
| EUHYDDAM00 / 2030 | 53.76 | 55.04 | -1.271 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,288.0 |
| FI198 | 76.9 |
| FI199 | 157.8 |
| FI19A | 270.7 |
| FI19B | 84.77 |
| FI1B1 | 236.4 |
| FI1C1 | 123.1 |
| FI1C2 | 49.92 |
| FI1C5 | 240.5 |
| FI1C6 | 30.9 |
| FI1C7 | 56.69 |
| FI1D5 | 165.5 |
| FI1D7 | 590.6 |
| FI1D8 | 93.44 |
| FI1D9 | 734.9 |
| FI1DA | 74.7 |
| FI1DB | 23.56 |
| FI1DC | 99.32 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 329.0 | 337.6 | -8.59 |
| 2013 | 288.0 | 292.1 | -4.062 |
| 2015 | 311.9 | 320.1 | -8.173 |
| 2018 | 370.7 | 373.1 | -2.356 |
| 2020 | 318.2 | 314.9 | 3.335 |
| 2023 | 379.2 | 380.3 | -1.062 |
| 2025 | 417.7 | 423.2 | -5.535 |
| 2028 | 467.3 | 478.3 | -10.93 |
| 2030 | 488.1 | 507.3 | -19.2 |
| 2033 | 433.2 | 442.2 | -8.987 |
| 2035 | 463.5 | 464.2 | -0.6553 |
| 2038 | 504.9 | 521.6 | -16.63 |
| 2040 | 551.5 | 573.8 | -22.27 |
| 2043 | 574.3 | 623.9 | -49.57 |
| 2045 | 609.8 | 644.7 | -34.87 |
| 2048 | 651.4 | 670.5 | -19.07 |
| 2050 | 685.1 | 708.1 | -22.96 |
| 2053 | 700.1 | 719.1 | -18.97 |
| 2055 | 712.1 | 727.8 | -15.77 |
| 2058 | 728.1 | 749.1 | -20.99 |
| 2060 | 738.0 | 763.8 | -25.74 |
| 2063 | 752.5 | 779.1 | -26.54 |
| 2065 | 761.1 | 788.8 | -27.64 |
| 2068 | 777.8 | 805.1 | -27.32 |
| 2070 | 790.2 | 816.6 | -26.33 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 209.3 | 200.0 | 9.353 |
| 2013 | 191.0 | 179.3 | 11.7 |
| 2015 | 137.7 | 131.1 | 6.537 |
| 2018 | 148.0 | 132.5 | 15.57 |
| 2020 | 176.0 | 145.3 | 30.68 |
| 2023 | 139.1 | 134.0 | 5.112 |
| 2025 | 118.8 | 124.4 | -5.57 |
| 2028 | 185.4 | 212.8 | -27.49 |
| 2030 | 202.7 | 230.4 | -27.7 |
| 2033 | 152.0 | 168.8 | -16.81 |
| 2035 | 167.8 | 177.8 | -10.01 |
| 2038 | 188.7 | 190.0 | -1.299 |
| 2040 | 202.2 | 204.3 | -2.085 |
| 2043 | 222.7 | 224.7 | -1.99 |
| 2045 | 225.6 | 229.2 | -3.657 |
| 2048 | 228.9 | 235.1 | -6.141 |
| 2050 | 232.8 | 239.0 | -6.203 |
| 2053 | 235.8 | 238.4 | -2.662 |
| 2055 | 236.6 | 242.9 | -6.301 |
| 2058 | 240.8 | 249.0 | -8.175 |
| 2060 | 245.2 | 257.1 | -11.91 |
| 2063 | 247.9 | 262.1 | -14.15 |
| 2065 | 249.0 | 263.8 | -14.85 |
| 2068 | 250.0 | 268.4 | -18.46 |
| 2070 | 251.6 | 271.1 | -19.5 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.243 | 0.2965 |
| 2018 | 8.557 | 0.2898 |
| 2025 | 11.53 | 0.3905 |
| 2033 | 31.94 | 1.081 |
| 2040 | 45.63 | 1.544 |
| 2048 | 29.83 | 1.01 |
| 2055 | 25.48 | 0.8626 |
| 2063 | 31.55 | 1.068 |
| 2070 | 30.29 | 1.025 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.247 | 0.729 |
| 2018 | 15.73 | 1.24 |
| 2025 | 124.7 | 9.829 |
| 2033 | 22.24 | 1.753 |
| 2040 | 29.88 | 1.792 |
| 2048 | 17.7 | 0.8107 |
| 2055 | 17.34 | 0.7812 |
| 2063 | 17.92 | 0.5437 |
| 2070 | 17.3 | 0.5187 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,091.9 | 0 |
| ICMFISCO2 | 10,411.7 | 0 |
| OILCRD | 0 | 6,799.3 |
| ELCHIG | 4,405.8 | 0 |
| INDELC | 0 | 4,073.0 |
| IPPHTH | 0 | 3,983.6 |
| GreenCert-ELC | 3,370.5 | 0 |
| OILDST | 2,789.9 | 0 |
| BIOOILFS | 0 | 2,777.2 |
| INDBLQ | 2,567.9 | 0 |
| OILGSL | 2,459.6 | 0 |
| BIOHVO | 2,396.7 | 0 |
| ELCHYD | 0 | 1,379.5 |
| ELCWOO | 0 | 1,309.6 |
| ELCWIN | 0 | 1,091.6 |
| INDBIO | 221.0 | 696.8 |
| MPPWOO | 0 | 755.3 |
| HETHTH | 753.7 | 0 |
| ELCNUC | 0 | 751.8 |
| OILHFO | 506.1 | 13.65 |
| ELCCOH | 0 | 475.9 |
| INDHTH | 0 | 454.1 |
| OILKER | 407.2 | 0 |
| OILNEU | 0 | 400.9 |
| SUPRPG | 0 | 386.7 |
| INDCOK | 0 | 345.7 |
| INDLFO | 0 | 302.8 |
| INDCOA | 0 | 294.5 |
| INDRFG | 0 | 289.7 |
| INDGAS | 0 | 277.3 |
| INDHFO | 0 | 250.2 |
| OILNAP | 0 | 243.0 |
| COALIG | 0 | 189.9 |
| IOIHTH | 0.515 | 174.8 |
| ELCCOL | 0 | 154.8 |
| OILRFG | 123.8 | 18.4 |
| COACOK | 127.9 | 0 |
| ELCGAS | 0 | 126.5 |
| MPPRYC | 0 | 122.5 |
| ICHHTH | 0.1426 | 107.4 |
| OILOTH | 38.91 | 52.74 |
| SUPRPP | 0 | 89.44 |
| OILLPG | 12.7 | 74.55 |
| MISSNT | 0 | 65.55 |
| MPPGYP | 0 | 63.92 |
| BIOGAS | 45.85 | 0 |
| ELCSOL | 0 | 45.6 |
| GASCOG | 42.86 | 0 |
| ELCHFO | 0 | 40.59 |
| MISRIR | 38.32 | 0 |
| ICMPARA | 37.66 | 0 |
| GASNAT | 0 | 34.5 |
| MISOXY | 0 | 28.01 |
| INDCOG | 0 | 26.57 |
| INDSLU | 0 | 21.93 |
| GASBFG | 21.56 | 0 |
| MISORE | 0 | 21.01 |
| MLMSTN | 0 | 20.2 |
| IIS | 18.42 | 0 |
| INDLPG | 0 | 16.77 |
| SUPGAS | 0 | 16.19 |
| MPPKAO | 0 | 14.53 |
| MISBFS | 6.882 | 6.919 |
| REFHTH | 0 | 13.09 |
| INFHTH | 1.417 | 11.09 |
| BRFH2 | 0 | 12.14 |
| MISSCR | 0 | 10.18 |
| MISCST | 7.232 | 1.983 |
| SUPBIO | 0 | 8.759 |
| SYNH2CT | 6.895 | 0 |
| MPPNOH | 0 | 5.616 |
| INDMUN | 0 | 4.451 |
| INDCOL | 0 | 3.82 |
| MPPOXY | 0 | 3.209 |
| IALHTH | 0 | 2.002 |
| IGH | 1.852 | 0 |
| INDHH2 | 0.8015 | 0.6119 |
| MGHRYC | 0 | 1.277 |
| INMHTH | 0.2244 | 0.9214 |
| MISPLT | 0 | 1.107 |
| IISHTH | 0.09221 | 0.9618 |
| MALBAU | 0 | 0.8853 |
| INDBFG | 0 | 0.741 |
| BRFCA3 | 0 | 0.5752 |
| SUPELC | 0 | 0.5367 |
| ICUHTH | 0 | 0.4682 |
| MALSCR | 0 | 0.4547 |
| ELCDST | 0 | 0.3796 |
| MCUORE | 0 | 0.3679 |
| MISQLI | 0 | 0.3026 |
| ICU | 0.1688 | 0 |
| INDCOB | 0 | 0.1388 |
| SUPHTH | 0 | 0.1208 |
| MCUSCR | 0.006751 | 0 |
| MCUSCU | 0 | 0.001058 |

- Back-and-forth on the same link, year and timeslice: 1 cases, volume 0.1335
| link / year / ts | min(imp, exp) |
|---|---|
| TB_INMHTH_FI_FI1DB / 2013 / W | 0.1335 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 146,291.7, reference 130,244.3 (+12.32%); 25 years differ >0.1 %
- ETSCO2: produced, all years: run 362,702.2, reference 343,808.2 (+5.50%); 25 years differ >0.1 %
- INDCO2N: produced, all years: run 133,221.6, reference 126,331.9 (+5.45%); 24 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 10,843.9, reference 11,202.8 (-3.20%); 25 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 5,661.4, reference 6,065.4 (-6.66%); 25 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'ETSCO2': 192641.9, 'GreenCert-ELC': -4.5, 'ELCCO2N': 72715.9} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 0 | 0 |
| FI / ELCHIGG | 300 | 17 | 31.8 |
| FI / ELCLOW | 300 | 3 | 64.62 |
| FI / ELCMED | 300 | 3 | 11.69 |
| FI / HETHTH | 300 | 0 | 0 |
| FI196 / ELCLOW | 300 | 172 | 5,769.1 |
| FI196 / ELCMED | 300 | 160 | 4,640.2 |
| FI198 / ELCLOW | 300 | 223 | 8,304.5 |
| FI198 / ELCMED | 300 | 221 | 7,511.0 |
| FI199 / ELCLOW | 300 | 154 | 5,743.2 |
| FI199 / ELCMED | 300 | 157 | 4,584.0 |
| FI19A / ELCLOW | 300 | 168 | 6,697.5 |
| FI19A / ELCMED | 300 | 182 | 6,393.5 |
| FI19B / ELCLOW | 300 | 139 | 4,789.1 |
| FI19B / ELCMED | 300 | 150 | 4,027.2 |
| FI1B1 / ELCLOW | 300 | 85 | 3,194.2 |
| FI1B1 / ELCMED | 300 | 85 | 3,817.8 |
| FI1C1 / ELCLOW | 300 | 103 | 3,945.5 |
| FI1C1 / ELCMED | 300 | 102 | 3,552.4 |
| FI1C2 / ELCLOW | 300 | 90 | 3,580.2 |
| FI1C2 / ELCMED | 300 | 90 | 2,853.6 |
| FI1C5 / ELCLOW | 300 | 119 | 3,701.6 |
| FI1C5 / ELCMED | 300 | 103 | 2,823.8 |
| FI1C6 / ELCLOW | 300 | 157 | 5,388.0 |
| FI1C6 / ELCMED | 300 | 176 | 5,726.5 |
| FI1C7 / ELCLOW | 300 | 76 | 2,732.1 |
| FI1C7 / ELCMED | 300 | 64 | 2,407.0 |
| FI1D5 / ELCLOW | 300 | 93 | 3,446.1 |
| FI1D5 / ELCMED | 300 | 118 | 3,773.4 |
| FI1D7 / ELCLOW | 300 | 193 | 8,402.8 |
| FI1D7 / ELCMED | 300 | 201 | 8,177.2 |
| FI1D8 / ELCLOW | 300 | 0 | 0 |
| FI1D8 / ELCMED | 300 | 0 | 0 |
| FI1D9 / ELCLOW | 300 | 166 | 5,300.0 |
| FI1D9 / ELCMED | 300 | 172 | 4,687.0 |
| FI1DA / ELCLOW | 300 | 283 | 10,320.8 |
| FI1DA / ELCMED | 300 | 281 | 9,184.8 |
| FI1DB / ELCLOW | 300 | 300 | 11,003.8 |
| FI1DB / ELCMED | 300 | 300 | 9,930.2 |
| FI1DC / ELCLOW | 300 | 160 | 5,597.6 |
| FI1DC / ELCMED | 300 | 172 | 5,680.9 |
| FI200 / ELCLOW | 300 | 102 | 4,463.2 |
| FI200 / ELCMED | 300 | 103 | 4,579.6 |

- Peak equations outside the hub: 38 region/commodity pairs (expected none in the hub design)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 257; only in run: 23; only in reference: 29
| binding only in run | sum |shadow| |
|---|---|
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 7,185.7 |
| UCI_UP_CHPShare-ICL | 2,720.8 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDBIO_LO | 751.5 |
| RS_PRD_COMBIO_LO | 712.5 |
| RS_PRD_RSDFINOIL_LO | 611.4 |
| RS_PRD_COMFINOIL_LO | 606.6 |
| RS_PRD_RSDHET_LO | 395.9 |
| RS_PRD_COMGAS_LO | 240.7 |
| UCI_UP_CHPShare-IIS | 233.5 |
| RS_PRD_RSDGAS_LO | 199.0 |
| RS_PRD_COMHET_LO | 64.71 |
| RS_PRD_COMGAS_UP | 31.57 |
| RS_FLO_RSDHET00_HETHTH_UP | 29.04 |
| RS_ACT_SSCDCOKE00_FX | 19.31 |

| binding only in reference | sum |shadow| |
|---|---|
| TUC_Istruc_RIR-CYC | 10,699.4 |
| TUC_Istruc_PUP-RYC | 3,025.1 |
| TUC_Istruc_CST-SSTEEL | 364.6 |
| UC_DecrCCUS7 | 181.2 |
| AU_ELC_GEOMIN | 122.4 |
| UC_DecrCCUS3 | 34.77 |
| AU_ELC_HYRCAP | 12.41 |
| UC_VARU_CAP_EUFBCOL01 | 7.551 |
| UC_VARU_CAP_EUSTCOHcon01 | 7.551 |
| UC_VARU_CAP_EUSTCOHsup01 | 7.551 |
| UC_VARU_CAP_EUSTCOLsup01 | 7.551 |
| UC_NonDecrWinONCAP | 5.666 |
| UC_VARU_CAP_EUIGCOLCCSpre20 | 4.828 |
| UC_VARU_CAP_EUGEOORC01 | 3.776 |
| UC_VARU_CAP_EUFBCOH15 | 3.776 |

Shadow prices differing by more than 5 %: 275; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_ACT_EEPP_natgas_OCGT | 185,583.0 | 8,790.4 | 176,792.6 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 117,468.7 | 6,902.7 | 110,566.0 |
| UC_VARU_ACT_EEPP_naturalgas_th | 102,869.3 | 8,719.1 | 94,150.2 |
| UC_VARU_ACT_EEPP_HFO_th | 55,928.5 | 10,729.6 | 45,198.9 |
| UC_VARU_CAP_EEPP_naturalgas_th | 26,261.2 | 2,436.8 | 23,824.3 |
| UC_VARU_ACT_EEPP_lignite_th | 29,058.8 | 8,299.1 | 20,759.7 |
| UC_VARU_CAP_EEPP_natgas_CCGT | 19,738.5 | 1,318.7 | 18,419.9 |
| UC_VARU_ACT_EEPP_coal_th | 25,020.4 | 8,298.6 | 16,721.8 |
| UC_ACAES-STG_DischLimit | 16,403.1 | 1,094.8 | 15,308.3 |
| UC_DCAES-STG_DischLimit | 13,125.8 | 922.5 | 12,203.3 |
| TUC_TRA_Lcv-Lpg | 21,087.8 | 32,707.9 | -11,620.1 |
| TUC_Istruc_RIR-CYC | 0 | 10,699.4 | -10,699.4 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 11,512.1 | 1,269.5 | 10,242.7 |
| TUC_Istruc_COP_PRD | 23,840.1 | 33,064.1 | -9,224.0 |
| UC_VARU_CAP_EUCCGASCCSpos20 | 47,965.4 | 56,904.4 | -8,939.0 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 0 entries differ
- CST_FLOX: 0 entries differ
### investment: 247 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Hdt_Dis_10 | 0 | 29,643.7 | -29,643.7 |
| TRA_Hdt_Dis_01 | 45,440.8 | 19,113.7 | 26,327.1 |
| COMBATS01 | 0 | 10,588.6 | -10,588.6 |
| RSDBATS01 | 19,806.2 | 9,902.3 | 9,904.0 |
| TRA_Hdt_ELC_01 | 49,253.7 | 56,662.1 | -7,408.4 |
| BRF2_BTLFTDSL | 1,064.8 | 6,723.4 | -5,658.5 |
| TRA_Car_Dis_Sma_91 | 0 | 5,092.1 | -5,092.1 |
| TRA_Car_Gas_LoM_91 | 0 | 4,869.1 | -4,869.1 |
| TRA_Hdt_GH2_01 | 4,412.8 | 0 | 4,412.8 |
| TRA_Car_Dis_Sma_71 | 3,854.9 | 0 | 3,854.9 |
| TRA_Car_Elc_LoM_10 | 9,638.6 | 5,867.2 | 3,771.4 |
| HHTHGEO001 | 0 | 2,772.3 | -2,772.3 |

### fixed O&M: 231 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Hdt_Dis_10 | 0 | 4,700.7 | -4,700.7 |
| TRA_Hdt_Dis_01 | 7,205.8 | 3,031.0 | 4,174.8 |
| BRF2_BTLFTDSL | 430.9 | 2,720.7 | -2,289.8 |
| HHTHGEO001 | 0 | 2,197.7 | -2,197.7 |
| TRA_Car_Dis_Sma_91 | 0 | 1,157.3 | -1,157.3 |
| TRA_Car_Gas_LoM_91 | 0 | 1,106.7 | -1,106.7 |
| TRA_Hdt_ELC_01 | 7,100.4 | 8,168.3 | -1,068.0 |
| TRA_Car_Dis_Sma_71 | 876.1 | 0 | 876.1 |
| TRA_Car_Elc_LoM_10 | 1,802.3 | 971.2 | 831.1 |
| TRA_Hdt_GH2_01 | 780.3 | 0 | 780.3 |
| R_ES-SH-DH_BIO01 | 842.0 | 1,500.0 | -658.1 |
| SELCH2PEM01 | 309.8 | 885.4 | -575.6 |

### activity: 832 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| HHTHGEO001 | 0 | 693.1 | -693.1 |
| IMPBIOEMHV | 193.4 | 308.2 | -114.9 |
| IGHRECYCL10 | 433.1 | 543.2 | -110.1 |
| IPPPUPCHE01 | 2,833.8 | 2,934.4 | -100.6 |
| ICLADVPRO05 | 76.76 | 129.2 | -52.45 |
| ICLADVPRO01 | 106.8 | 55.7 | 51.13 |
| EUCCGASCCSpos20 | 149.8 | 199.6 | -49.78 |
| BRF2_BTLFTDSL | 10.38 | 58.46 | -48.07 |
| HHTHELC001 | 511.0 | 553.4 | -42.37 |
| SELCH2PEM01_LowAF | 19.56 | 60.75 | -41.19 |
| IGHRECYCL05 | 159.0 | 118.8 | 40.24 |
| ECHP_naturalgas_CCGT | 44.66 | 74.4 | -29.74 |

### flow/import: 68 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IMPOILCRD | 103,968.8 | 57,840.3 | 46,128.5 |
| EXPOILDST | -39,541.9 | -9,767.3 | -29,774.6 |
| EXPOILGSL | -37,160.6 | -16,267.1 | -20,893.5 |
| IMPOILHFO | 2,309.6 | 5,397.2 | -3,087.6 |
| EXPELC-fromFI | -4,087.9 | -1,343.3 | -2,744.6 |
| IMPOILGSL | 1,948.8 | 4,570.2 | -2,621.4 |
| MINMPPWOO1 | 113,030.4 | 115,521.8 | -2,491.5 |
| IMPOILDST | 13,423.6 | 15,101.9 | -1,678.3 |
| SSCDRFLX00 | 3,243.2 | 1,805.0 | 1,438.2 |
| IMPOILKER | 2,200.5 | 3,597.7 | -1,397.2 |
| IMPGAS_RU_PIP | 20,746.5 | 21,987.4 | -1,241.0 |
| EXPOILKER | -2,337.2 | -1,176.6 | -1,160.6 |

### capacity (sum over years): 74 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| R_ES-SH-DH_ELC07 | 2,321.0 | 786.7 | 1,534.3 |
| R_ES-SH-DH_BIO01 | 1,789.2 | 3,187.6 | -1,398.4 |
| TRA_Car_Elc_LoM_10 | 2,918.0 | 1,552.4 | 1,365.6 |
| R_ES-SH-FL_ELC01 | 13,621.2 | 12,484.1 | 1,137.1 |
| TRA_Car_PIH_LoM_20pct | 10,698.4 | 11,590.1 | -891.7 |
| TRA_Car_Elc_Sma_10 | 7,243.1 | 8,012.9 | -769.8 |
| R_ES-SH-FL_GAS01 | 0 | 749.8 | -749.8 |
| TRA_Car_Elc_Exe_10 | 15,105.7 | 14,414.0 | 691.6 |
| TRA_Car_PIH_Sma_20pct | 4,187.6 | 3,545.9 | 641.7 |
| R_ES-SH-SD_ELC05 | 2,958.7 | 3,320.2 | -361.4 |
| COMBATS01 | 0 | 356.8 | -356.8 |
| R_ES-SH-DH-70_ELC05 | 4,549.0 | 4,193.1 | 355.9 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## L. Output without inputs
- Processes running with less than 20 % of their reference inputs per unit of activity: 1
| process | activity (all years) | inputs/activity run | inputs/activity reference |
|---|---|---|---|
| AGR_Agr_For_Fis-Tech | 985.1 | 0 | 1 |


## Verdict
FAIL: NCAP_PASTI, PRC_RESID, output without inputs
