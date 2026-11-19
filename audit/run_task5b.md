# Audit of reg_baseline-sami_2026-11-19_task5b_run2.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,980,800.21 M EUR, reference 1,529,919.88, difference +450,880.33 (+29.4708%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 207,196.7 | 144,742.3 | 62,454.4 |
| INV | 1,345,081.2 | 919,897.7 | 425,183.5 |
| VAR | 428,522.3 | 465,279.9 | -36,757.6 |
| VARX | 0.06615 | 0 | 0.06615 |

| region | objective share |
|---|---|
| FI | 959,610.7 |
| FI1B1 | 226,994.4 |
| FI1C1 | 87,907.9 |
| FI19B | 87,859.4 |
| FI196 | 83,041.1 |
| FI1D9 | 75,728.9 |
| FI199 | 48,961.2 |
| FI1DB | 48,377.1 |
| FI198 | 48,219.1 |
| FI1C7 | 41,144.8 |
| FI1D7 | 40,925.3 |
| FI19A | 38,099.1 |
| FI1C6 | 36,826.0 |
| FI1C2 | 35,814.7 |
| FI1C5 | 33,743.1 |
| FI1DC | 28,273.0 |
| FI1DA | 25,740.9 |
| FI1D5 | 14,075.8 |
| FI1D8 | 13,154.8 |
| FI200 | 6,302.8 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved
- PRC_RESID national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| ECHP_naturalgas_CCGT | 58.3 | 84.67 | -26.37 |
| ECHP_coal_thermal | 114.7 | 97.15 | 17.54 |
| ECHP_biomass_thermal | 329.3 | 313.6 | 15.68 |
| EUHYDDAM00 | 1,375.1 | 1,380.6 | -5.509 |
| EEPP_coal_thermal | 43.25 | 40.22 | 3.03 |
| EEPP_PV | 42.59 | 45.46 | -2.877 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| EEPP_HFO_thermal | 3.413 | 2.141 | 1.272 |
| ECHP_lignite_thermal | 30.43 | 29.84 | 0.5902 |
| ECHP_HFO_thermal | 7.88 | 8.341 | -0.4616 |
| EEPP_biomass_thermal | 86.03 | 86.31 | -0.2821 |
| EEPP_naturalgas_thermal | 0.06016 | 0.09998 | -0.03982 |
| ECHP_LFO_thermal | 0.01155 | 0.02023 | -0.008682 |
| ECHP_naturalgas_thermal | 2.224 | 2.229 | -0.004877 |
| EEPP_windOFF | 23.59 | 23.59 | -0.001948 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08294 | 0.08335 | -0.0004068 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | -3.038e-06 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | -3.144e-07 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | -3.041e-07 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | -2.869e-07 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | -1.996e-07 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 2.136e-09 |

By class and year: 79 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_coal_thermal / 2020 | 24.41 | 12.65 | 11.76 |
| ECHP_naturalgas_CCGT / 2015 | 22.22 | 28.22 | -6.008 |
| ECHP_naturalgas_CCGT / 2013 | 18.04 | 24.04 | -6.004 |
| ECHP_naturalgas_CCGT / 2010 | 18.04 | 24.04 | -6.004 |
| ECHP_biomass_thermal / 2033 | 5.629 | 0 | 5.629 |
| ECHP_coal_thermal / 2023 | 5.077 | 0 | 5.077 |
| ECHP_biomass_thermal / 2035 | 5.058 | 0 | 5.058 |
| ECHP_biomass_thermal / 2038 | 5.058 | 0 | 5.058 |
| ECHP_naturalgas_CCGT / 2018 | 0 | 4.179 | -4.179 |
| ECHP_naturalgas_CCGT / 2020 | 0 | 4.179 | -4.179 |
| EEPP_coal_thermal / 2013 | 5.475 | 2.445 | 3.03 |
| EUHYDDAM00 / 2063 | 53.85 | 55.04 | -1.187 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,286.5 |
| FI198 | 76.98 |
| FI199 | 157.7 |
| FI19A | 270.2 |
| FI19B | 87.36 |
| FI1B1 | 240.4 |
| FI1C1 | 130.8 |
| FI1C2 | 49.93 |
| FI1C5 | 240.0 |
| FI1C6 | 31.64 |
| FI1C7 | 56.36 |
| FI1D5 | 165.7 |
| FI1D7 | 591.1 |
| FI1D8 | 92.99 |
| FI1D9 | 734.3 |
| FI1DA | 74.79 |
| FI1DB | 23.57 |
| FI1DC | 97.72 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 332.0 | 337.6 | -5.594 |
| 2013 | 289.5 | 292.1 | -2.507 |
| 2015 | 314.1 | 320.1 | -5.978 |
| 2018 | 370.0 | 373.1 | -3.128 |
| 2020 | 322.0 | 314.9 | 7.149 |
| 2023 | 378.9 | 380.3 | -1.434 |
| 2025 | 406.8 | 423.2 | -16.5 |
| 2028 | 452.3 | 478.3 | -25.99 |
| 2030 | 456.0 | 507.3 | -51.3 |
| 2033 | 424.7 | 442.2 | -17.47 |
| 2035 | 445.3 | 464.2 | -18.85 |
| 2038 | 488.7 | 521.6 | -32.85 |
| 2040 | 532.9 | 573.8 | -40.92 |
| 2043 | 551.0 | 623.9 | -72.91 |
| 2045 | 577.4 | 644.7 | -67.23 |
| 2048 | 624.1 | 670.5 | -46.37 |
| 2050 | 665.2 | 708.1 | -42.9 |
| 2053 | 683.5 | 719.1 | -35.62 |
| 2055 | 695.4 | 727.8 | -32.46 |
| 2058 | 710.9 | 749.1 | -38.27 |
| 2060 | 722.7 | 763.8 | -41.06 |
| 2063 | 737.1 | 779.1 | -41.96 |
| 2065 | 747.7 | 788.8 | -41.06 |
| 2068 | 763.6 | 805.1 | -41.52 |
| 2070 | 774.5 | 816.6 | -42.06 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 193.2 | 200.0 | -6.729 |
| 2013 | 191.0 | 179.3 | 11.69 |
| 2015 | 150.9 | 131.1 | 19.81 |
| 2018 | 156.9 | 132.5 | 24.44 |
| 2020 | 193.3 | 145.3 | 47.96 |
| 2023 | 158.6 | 134.0 | 24.62 |
| 2025 | 138.9 | 124.4 | 14.57 |
| 2028 | 176.7 | 212.8 | -36.12 |
| 2030 | 209.1 | 230.4 | -21.25 |
| 2033 | 158.2 | 168.8 | -10.6 |
| 2035 | 166.9 | 177.8 | -10.86 |
| 2038 | 190.4 | 190.0 | 0.3997 |
| 2040 | 203.6 | 204.3 | -0.7202 |
| 2043 | 224.7 | 224.7 | 0.01812 |
| 2045 | 226.5 | 229.2 | -2.714 |
| 2048 | 233.0 | 235.1 | -2.095 |
| 2050 | 241.2 | 239.0 | 2.205 |
| 2053 | 248.4 | 238.4 | 10.04 |
| 2055 | 253.4 | 242.9 | 10.59 |
| 2058 | 258.4 | 249.0 | 9.433 |
| 2060 | 266.5 | 257.1 | 9.415 |
| 2063 | 271.9 | 262.1 | 9.833 |
| 2065 | 273.1 | 263.8 | 9.27 |
| 2068 | 274.4 | 268.4 | 5.944 |
| 2070 | 274.0 | 271.1 | 2.957 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 4.764 | 4.764 |
| 2018 | 11.22 | 0.3782 |
| 2025 | 11.53 | 0.3878 |
| 2033 | 31.71 | 1.073 |
| 2040 | 39.85 | 1.349 |
| 2048 | 31 | 1.049 |
| 2055 | 30.99 | 1.049 |
| 2063 | 30.55 | 1.034 |
| 2070 | 29.95 | 1.014 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 11.55 | 0.9102 |
| 2018 | 18.16 | 1.432 |
| 2025 | 86.77 | 6.839 |
| 2033 | 20.88 | 1.646 |
| 2040 | 24.95 | 1.491 |
| 2048 | 17.63 | 0.9709 |
| 2055 | 16.3 | 0.7996 |
| 2063 | 16.62 | 0.8205 |
| 2070 | 16.58 | 0.6982 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 28,492.5 | 0.1444 |
| ICMFISCO2 | 10,452.4 | 0 |
| OILCRD | 0.1571 | 6,024.5 |
| ELCHIG | 4,416.2 | 0.017 |
| INDELC | 3.753 | 4,072.2 |
| IPPHTH | 10.21 | 3,971.2 |
| GreenCert-ELC | 3,379.3 | 3.133 |
| OILDST | 2,404.1 | 515.6 |
| INDBLQ | 2,473.0 | 2.186 |
| OILGSL | 2,193.3 | 0.1597 |
| BIOOILFS | 0.5623 | 2,138.2 |
| BIOHVO | 1,845.4 | 0.5631 |
| TRADST | 2.815 | 1,677.2 |
| ELCHYD | 2.896 | 1,378.2 |
| ELCWOO | 2.744 | 1,319.3 |
| ELCWIN | 4.485 | 1,096.2 |
| INDBIO | 209.7 | 617.0 |
| HETHTH | 779.3 | 0.01705 |
| ELCNUC | 0.005875 | 751.8 |
| MPPWOO | 0.01897 | 741.6 |
| OILHFO | 419.4 | 163.5 |
| TRAGSLSP95 | 3.596 | 508.9 |
| ELCCOH | 0.1275 | 503.8 |
| INDHTH | 1.193 | 457.6 |
| OILNEU | 0.1627 | 403.8 |
| OILKER | 372.9 | 0.1664 |
| INDCOK | 4.09 | 349.2 |
| SUPRPG | 0.1681 | 342.8 |
| INDGAS | 13.87 | 305.1 |
| INDLFO | 3.598 | 303.9 |
| INDCOA | 3.213 | 293.9 |
| INDRFG | 0.1636 | 289.9 |
| ELCLOW | 0.001435 | 268.2 |
| OILNAP | 0.2282 | 260.2 |
| IOIHTH | 17.46 | 242.3 |
| INDHFO | 3.778 | 229.0 |
| COALIG | 0.1536 | 195.8 |
| ELCGAS | 15.56 | 161.1 |
| ELCCOL | 0.3742 | 152.0 |
| BIOWOO | 0 | 151.4 |
| OILOTH | 56.4 | 89.22 |
| INDHH2 | 69.49 | 69.18 |
| ELCHIGG | 68.82 | 68.82 |
| TRALH2 | 68.82 | 68.82 |
| OILRFG | 110.5 | 26.5 |
| ICHHTH | 3.804 | 132.5 |
| COACOK | 132.5 | 0.1742 |
| SYNH2CT | 69.53 | 62.14 |
| MPPRYC | 0.02098 | 126.0 |
| TRAGSLE85 | 3.333 | 109.8 |
| OILLPG | 12.54 | 92.96 |
| BIOGAS | 84.32 | 15.39 |
| GASNAT | 18.69 | 74.58 |
| SUPRPP | 0.1797 | 79.43 |
| INFHTH | 25.39 | 41 |
| MPPGYP | 0 | 63.92 |
| MISSNT | 0.03761 | 62.03 |
| ELCSOL | 4.92 | 50.63 |
| INDLPG | 5.417 | 42.61 |
| INMHTH | 23.43 | 24.15 |
| AGRGAS | 23.49 | 23.49 |
| GASP2GB | 21.7 | 25 |
| GASCOG | 46.06 | 0.1861 |
| GASP2G | 22.94 | 22.94 |
| ELCHFO | 4.973 | 36.41 |
| MISRIR | 38.05 | 0 |
| ICMPARA | 37.84 | 0.1762 |
| TRAHFO | 32.17 | 0 |
| INDCOG | 0.3036 | 29.62 |
| MISOXY | 0 | 27.87 |
| INDSLU | 5.557 | 19.47 |
| MISORE | 0 | 24.24 |
| COAHAR | 0.2088 | 22.64 |
| MLMSTN | 0 | 20.2 |
| IIS | 18.51 | 0.08939 |
| SUPGAS | 0.8583 | 17.54 |
| INDMUN | 3.998 | 12.71 |
| MISBFS | 8.236 | 8.176 |
| MPPKAO | 0 | 14.53 |
| ELCMED | 0.00148 | 14.38 |
| INDCOL | 4.28 | 8.087 |
| REFHTH | 0 | 11.6 |
| ETSCO2 | 5.318 | 5.322 |
| ELCDST | 5.127 | 5.508 |
| TRAGSLSP95E10 | 5.308 | 5.308 |
| MISSCR | 0 | 10.55 |
| BRFH2 | 0.5757 | 9.918 |
| MISCST | 7.654 | 2.069 |
| ELCCO2N | 0.003059 | 9.367 |
| SUPBIO | 0.2051 | 7.966 |
| GASBFG | 5.35 | 0.6001 |
| MPPNOH | 0 | 5.512 |
| IALHTH | 1.554 | 3.556 |
| MPPOXY | 0 | 3.15 |
| IISHTH | 0.6147 | 1.551 |
| IGH | 1.947 | 0.04126 |
| MALBAU | 0.2609 | 1.146 |
| SUPELC | 0.4457 | 0.8588 |
| MISPLT | 0.06417 | 1.218 |
| MGHRYC | 0 | 1.277 |
| BIOPROP | 0.6636 | 0.5892 |
| ICMLC3 | 0.6037 | 0.6037 |
| INDCOB | 0.3715 | 0.5102 |
| INDBFG | 0.02825 | 0.8315 |
| RENGEO | 0 | 0.7577 |
| ICLHTH | 0.228 | 0.4796 |
| GreenCert-FIN | 0.2837 | 0.3437 |
| GASIIS | 0.2937 | 0.3276 |
| OILFDS | 0.2958 | 0.3081 |
| GASCOP | 0.2714 | 0.2714 |
| ICUHTH | 0 | 0.4682 |
| MALSCR | 0 | 0.4547 |
| BRFCA3 | 0 | 0.4428 |
| MCUORE | 0 | 0.3679 |
| MISQLI | 0 | 0.3043 |
| ICU | 0.2172 | 0.04844 |
| MCUSCR | 0.06799 | 0.06124 |
| MCUSCU | 0.06374 | 0.0648 |
| MISRFC | 0.06417 | 0.06417 |
| RENSOL | 0 | 0.1076 |
| SUPHTH | 0 | 0.09298 |
| IGF | 0 | 1.293e-08 |

- Back-and-forth on the same link, year and timeslice: 54674 cases, volume 578.5
| link / year / ts | min(imp, exp) |
|---|---|
| TB_ETSCO2_FI_FI1B1 / 2070 / ANNUAL | 0.06125 |
| TB_ETSCO2_FI_FI1D9 / 2070 / ANNUAL | 0.06124 |
| TB_ETSCO2_FI_FI1DA / 2070 / ANNUAL | 0.06124 |
| TB_ETSCO2_FI_FI1D7 / 2070 / ANNUAL | 0.06124 |
| TB_ETSCO2_FI_FI1C1 / 2070 / ANNUAL | 0.06124 |
| TB_ETSCO2_FI_FI1C5 / 2070 / ANNUAL | 0.06124 |
| TB_ETSCO2_FI_FI199 / 2070 / ANNUAL | 0.06124 |
| TB_ETSCO2_FI_FI1D5 / 2070 / ANNUAL | 0.06124 |
| TB_ETSCO2_FI_FI19A / 2070 / ANNUAL | 0.06124 |
| TB_ETSCO2_FI_FI198 / 2070 / ANNUAL | 0.06124 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 147,728.4, reference 130,244.3 (+13.42%); 25 years differ >0.1 %
- ETSCO2: produced, all years: run 362,410.7, reference 343,808.2 (+5.41%); 25 years differ >0.1 %
- INDCO2N: produced, all years: run 116,090.4, reference 126,331.9 (-8.11%); 25 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 10,803.6, reference 11,202.8 (-3.56%); 24 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 5,713.6, reference 6,065.4 (-5.80%); 25 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'GreenCert-ELC': -4.6, 'ETSCO2': 191916.2, 'ELCCO2N': 75480.2} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 85 | 808.1 |
| FI / ELCHIGG | 300 | 88 | 24.01 |
| FI / ELCLOW | 300 | 52 | 122.5 |
| FI / ELCMED | 300 | 75 | 8.021 |
| FI / HETHTH | 300 | 0 | 0 |
| FI196 / ELCHIGG | 300 | 84 | 3,406.2 |
| FI196 / ELCLOW | 300 | 116 | 5,591.3 |
| FI196 / ELCMED | 300 | 224 | 8,421.8 |
| FI198 / ELCHIGG | 300 | 0 | 0 |
| FI198 / ELCLOW | 300 | 105 | 4,214.0 |
| FI198 / ELCMED | 300 | 138 | 6,195.1 |
| FI199 / ELCHIGG | 300 | 85 | 2,219.6 |
| FI199 / ELCLOW | 300 | 119 | 5,191.2 |
| FI199 / ELCMED | 300 | 98 | 2,546.6 |
| FI19A / ELCHIGG | 300 | 81 | 3,034.7 |
| FI19A / ELCLOW | 300 | 135 | 6,352.3 |
| FI19A / ELCMED | 300 | 282 | 10,025.2 |
| FI19B / ELCHIGG | 300 | 24 | 969.1 |
| FI19B / ELCLOW | 300 | 91 | 4,688.6 |
| FI19B / ELCMED | 300 | 277 | 10,028.4 |
| FI1B1 / ELCHIGG | 300 | 1 | 83.16 |
| FI1B1 / ELCLOW | 300 | 185 | 7,106.5 |
| FI1B1 / ELCMED | 300 | 194 | 8,999.7 |
| FI1C1 / ELCHIGG | 300 | 56 | 884.2 |
| FI1C1 / ELCLOW | 300 | 201 | 8,213.1 |
| FI1C1 / ELCMED | 300 | 3 | 167.0 |
| FI1C2 / ELCHIGG | 300 | 200 | 5,705.9 |
| FI1C2 / ELCLOW | 300 | 39 | 2,260.4 |
| FI1C2 / ELCMED | 300 | 204 | 6,987.4 |
| FI1C5 / ELCHIGG | 300 | 71 | 2,758.3 |
| FI1C5 / ELCLOW | 300 | 72 | 3,601.0 |
| FI1C5 / ELCMED | 300 | 132 | 3,743.2 |
| FI1C6 / ELCHIGG | 300 | 0 | 0 |
| FI1C6 / ELCLOW | 300 | 213 | 8,005.3 |
| FI1C6 / ELCMED | 300 | 222 | 9,094.2 |
| FI1C7 / ELCHIGG | 300 | 11 | 101.2 |
| FI1C7 / ELCLOW | 300 | 171 | 7,428.8 |
| FI1C7 / ELCMED | 300 | 99 | 4,908.0 |
| FI1D5 / ELCHIGG | 300 | 154 | 4,770.3 |
| FI1D5 / ELCLOW | 300 | 94 | 3,232.1 |
| FI1D5 / ELCMED | 300 | 68 | 1,600.4 |
| FI1D7 / ELCHIGG | 300 | 237 | 6,978.3 |
| FI1D7 / ELCLOW | 300 | 171 | 7,152.6 |
| FI1D7 / ELCMED | 300 | 54 | 2,449.9 |
| FI1D8 / ELCHIGG | 300 | 289 | 8,782.2 |
| FI1D8 / ELCLOW | 300 | 85 | 4,346.2 |
| FI1D8 / ELCMED | 300 | 156 | 5,976.4 |
| FI1D9 / ELCHIGG | 300 | 173 | 6,957.8 |
| FI1D9 / ELCLOW | 300 | 150 | 5,762.2 |
| FI1D9 / ELCMED | 300 | 127 | 5,400.4 |
| FI1DA / ELCHIGG | 300 | 74 | 1,294.6 |
| FI1DA / ELCLOW | 300 | 76 | 2,280.6 |
| FI1DA / ELCMED | 300 | 48 | 790.6 |
| FI1DB / ELCHIGG | 300 | 154 | 4,823.6 |
| FI1DB / ELCLOW | 300 | 83 | 3,218.0 |
| FI1DB / ELCMED | 300 | 122 | 4,989.6 |
| FI1DC / ELCHIGG | 300 | 125 | 4,228.4 |
| FI1DC / ELCLOW | 300 | 170 | 5,956.9 |
| FI1DC / ELCMED | 300 | 120 | 4,215.7 |
| FI200 / ELCHIGG | 300 | 49 | 1,376.2 |
| FI200 / ELCLOW | 300 | 276 | 10,855.9 |
| FI200 / ELCMED | 300 | 109 | 4,700.5 |

- Peak equations outside the hub: 57 region/commodity pairs (expected none in the hub design)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 259; only in run: 52; only in reference: 27
| binding only in run | sum |shadow| |
|---|---|
| UCI_UP_CHPShare-IAL | 149,287.0 |
| UCI_UP_CHPShare-ICL | 97,533.8 |
| UCI_UP_CHPShare-ICU | 47,483.8 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 6,472.2 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDBIO_LO | 691.0 |
| RS_PRD_COMBIO_LO | 659.1 |
| RS_PRD_RSDHET_LO | 329.0 |
| RS_PRD_COMGAS_LO | 177.5 |
| RS_PRD_RSDFINOIL_LO | 139.3 |
| RS_PRD_RSDGAS_LO | 133.4 |
| RS_PRD_COMFINOIL_LO | 131.9 |
| RS_PRD_COMHET_LO | 65.76 |
| UCI_UP_CHPShare-IIS | 54.64 |
| RS_FLO_RSDHET00_HETHTH_UP | 31.6 |

| binding only in reference | sum |shadow| |
|---|---|
| TUC_Istruc_RIR-CYC | 10,699.4 |
| UC_transport_H2_pre2028 | 3,118.0 |
| UC_Trucks_EV_pre2028 | 714.8 |
| UC_Trucks_EV_InSales | 387.2 |
| UC_DecrCCUS7 | 181.2 |
| AU_ELC_GEOMIN | 122.4 |
| UC_DecrCCUS3 | 34.77 |
| UC_VARU_CAP_EUFBCOL01 | 7.551 |
| UC_VARU_CAP_EUSTCOHcon01 | 7.551 |
| UC_VARU_CAP_EUSTCOHsup01 | 7.551 |
| UC_VARU_CAP_EUSTCOLsup01 | 7.551 |
| UC_VARU_CAP_EUIGCOLCCSpre20 | 4.828 |
| UC_VARU_CAP_EUGEOORC01 | 3.776 |
| UC_VARU_CAP_EUFBCOH15 | 3.776 |
| UC_VARU_CAP_EUGEOEGS01 | 3.776 |

Shadow prices differing by more than 5 %: 302; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_CAP_EEPP_natgas_CCGT | 472,337.0 | 1,318.7 | 471,018.3 |
| UC_VARU_CAP_EEPP_naturalgas_th | 466,691.8 | 2,436.8 | 464,255.0 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 464,532.1 | 1,269.5 | 463,262.6 |
| UC_VARU_CAP_EEPP_HFO_th | 169,964.2 | 702.2 | 169,262.0 |
| UCI_UP_CHPShare-IAL | 149,287.0 | 0 | 149,287.0 |
| UC_HydroLakeSupply_CE | 156,465.3 | 35,734.3 | 120,731.0 |
| UCI_UP_CHPShare-ICL | 97,533.8 | 0 | 97,533.8 |
| UC_VARU_ACT_EEPP_natgas_OCGT | 102,309.7 | 8,790.4 | 93,519.3 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 85,589.9 | 6,902.7 | 78,687.2 |
| UC_VARU_ACT_EEPP_naturalgas_th | 81,937.7 | 8,719.1 | 73,218.6 |
| UC_VARU_ACT_EEPP_HFO_th | 58,496.0 | 10,729.6 | 47,766.4 |
| UCI_UP_CHPShare-ICU | 47,483.8 | 0 | 47,483.8 |
| TUC_TRA_Lcv-Lpg | 6,593.4 | 32,707.9 | -26,114.6 |
| UC_VARU_CAP_EEPP_lignite_th | 13,745.1 | 630.4 | 13,114.7 |
| UC_VARU_CAP_EEPP_coal_th | 13,754.0 | 1,060.7 | 12,693.3 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 476 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI1C5 / 2070 / MCMCLKBYF | 0.003036 | 0 | 0.003036 |
| FI1C1 / 2070 / MCMCLKBYF | 0.003034 | 0 | 0.003034 |
| FI1C5 / 2070 / MCMCLKCCSC | 0.002997 | 0 | 0.002997 |
| FI1C1 / 2070 / MCMCLKCCSC | 0.002992 | 0 | 0.002992 |
| FI1C5 / 2070 / MCMCLKLAPP | 0.002771 | 0 | 0.002771 |
| FI / 2070 / ILMHTH | 0.00152 | 0 | 0.00152 |
| FI1B1 / 2070 / INFOTH | 0.001212 | 0 | 0.001212 |
| FI200 / 2070 / INFOTH | 0.001212 | 0 | 0.001212 |
| FI1D5 / 2070 / INFOTH | 0.001212 | 0 | 0.001212 |
| FI199 / 2070 / INFOTH | 0.001212 | 0 | 0.001212 |

- CST_FLOX: 0 entries differ
### investment: 958 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Hdt_Dis_01 | 552,246.2 | 19,113.7 | 533,132.4 |
| TRA_Hdt_ELC_01 | 0.06825 | 56,662.1 | -56,662.1 |
| TRA_Hdt_Dis_10 | 0.07689 | 29,643.7 | -29,643.6 |
| TRA_Bus_Dis_Urb_01 | 18,942.3 | 0 | 18,942.3 |
| TRA_Car_PIH_UpM_20pct | 6,920.0 | 18,154.7 | -11,234.6 |
| COMBATS01 | 0 | 10,588.6 | -10,588.6 |
| TRA_Lcv_Dis_01 | 7,590.1 | 16,226.2 | -8,636.0 |
| RSDBATS01 | 18,457.8 | 9,902.3 | 8,555.6 |
| TRA_Car_Gas_UpM_11 | 7,254.1 | 0 | 7,254.1 |
| TRA_Car_PIH_LoM_20pct | 36,587.9 | 29,648.3 | 6,939.5 |
| TRA_Bus_Eth_Urb_01 | 6,874.7 | 0 | 6,874.7 |
| BRF2_BTLFTDSL | 0.0001718 | 6,723.4 | -6,723.4 |

### fixed O&M: 798 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Hdt_Dis_01 | 87,572.3 | 3,031.0 | 84,541.3 |
| TRA_Hdt_ELC_01 | 0.009839 | 8,168.3 | -8,168.3 |
| TRA_Hdt_Dis_10 | 0.01219 | 4,700.7 | -4,700.7 |
| TRA_Bus_Dis_Urb_01 | 3,369.9 | 0 | 3,369.9 |
| BRF2_BTLFTDSL | 6.953e-05 | 2,720.7 | -2,720.7 |
| TRA_Car_PIH_UpM_20pct | 1,600.7 | 4,193.0 | -2,592.3 |
| HHTHGEO001 | 0.001058 | 2,197.7 | -2,197.7 |
| TRA_Lcv_Dis_01 | 1,641.3 | 3,508.7 | -1,867.4 |
| TRA_Car_Gas_UpM_11 | 1,648.7 | 0 | 1,648.7 |
| TRA_Car_PIH_LoM_20pct | 8,459.5 | 6,861.4 | 1,598.1 |
| TRA_Car_PIH_Sma_20pct | 3,613.4 | 2,089.1 | 1,524.3 |
| TRA_Car_Dis_UpM_21 | 1,240.9 | 0 | 1,240.9 |

### activity: 1398 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| HHTHGEO001 | 0.0003316 | 693.1 | -693.1 |
| S_CCUS_EMIS_H2T | 600.9 | 408.7 | 192.3 |
| IPPPUPCHE01 | 2,750.3 | 2,934.4 | -184.1 |
| EUCCGASCCSpos20 | 73.78 | 199.6 | -125.8 |
| IGHRECYCL10 | 433.6 | 543.2 | -109.6 |
| BRF2_BTLFTDSL | 1.453e-06 | 58.46 | -58.46 |
| ICLADVPRO05 | 75.54 | 129.2 | -53.67 |
| SBIOH2GCC01 | 230.3 | 178.2 | 52.02 |
| ICLADVPRO01 | 105.5 | 55.7 | 49.79 |
| S_CCUS_EMIS_H2T_LowAF | 167.2 | 117.6 | 49.51 |
| MINBIOCRP41 | 1,566.4 | 1,607.3 | -40.91 |
| SELCH2EC01_LowAF | 42.36 | 3.418 | 38.94 |

### flow/import: 170 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IMPOILCRD | 88,514.8 | 57,840.3 | 30,674.4 |
| EXPOILGSL | -32,027.2 | -16,267.1 | -15,760.1 |
| EXPOILDST | -21,262.8 | -9,767.3 | -11,495.6 |
| TRABAT_ChgStn | 1,562.5 | 10,525.0 | -8,962.5 |
| IMPOILDST | 7,889.3 | 15,101.9 | -7,212.5 |
| MINMPPWOO1 | 111,017.3 | 115,521.8 | -4,504.5 |
| TRAELC00 | 842.8 | 4,101.9 | -3,259.1 |
| IMPOILGSL | 1,948.8 | 4,570.2 | -2,621.4 |
| EXPELC-fromFI | -3,945.4 | -1,343.3 | -2,602.1 |
| EXPOILHFO | -3,982.1 | -1,871.8 | -2,110.3 |
| IMPOILKER | 1,643.3 | 3,597.7 | -1,954.3 |
| IMPELC-SEtoFI | 5,165.8 | 6,367.7 | -1,201.9 |

### capacity (sum over years): 328 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Car_PIH_UpM_20pct | 2,701.9 | 7,067.6 | -4,365.7 |
| TRA_Car_PIH_LoM_20pct | 14,276.8 | 11,590.1 | 2,686.7 |
| TRA_Car_PIH_Sma_20pct | 6,108.9 | 3,545.9 | 2,563.0 |
| TRA_Car_Elc_Sma_10 | 6,110.4 | 8,012.9 | -1,902.5 |
| R_ES-SH-FL_ELC01 | 13,685.7 | 12,484.1 | 1,201.7 |
| R_ES-SH-FL_GAS01 | 0.003236 | 749.8 | -749.8 |
| TRA_Car_Elc_Exe_10 | 14,930.8 | 14,414.0 | 516.8 |
| R_ES-SH-DH-70_BIO01 | 0.001651 | 380.6 | -380.6 |
| TRA_Car_PIH_Exe_20pct | 360.1 | 0 | 360.1 |
| COMBATS01 | 0 | 356.8 | -356.8 |
| R_ES-SH-SD_GAS01 | 937.5 | 632.6 | 304.9 |
| RSDBATS01 | 658.7 | 371.0 | 287.7 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## L. Output without inputs
- Processes running with less than 20 % of their reference inputs per unit of activity: none

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
