# Audit of reg_baseline-sami_2026-11-19_task5b.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 2,262,896.08 M EUR, reference 1,529,919.88, difference +732,976.20 (+47.9094%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 240,261.1 | 144,742.3 | 95,518.8 |
| INV | 1,552,214.3 | 919,897.7 | 632,316.6 |
| VAR | 428,043.0 | 465,279.9 | -37,236.9 |
| VARX | 42,377.8 | 0 | 42,377.8 |

| region | objective share |
|---|---|
| FI | 958,506.6 |
| FI1B1 | 290,663.3 |
| FI1C1 | 115,383.5 |
| FI19B | 113,454.4 |
| FI196 | 99,716.5 |
| FI1D9 | 95,039.4 |
| FI199 | 65,387.4 |
| FI1DB | 62,592.2 |
| FI198 | 61,494.6 |
| FI1D7 | 52,088.4 |
| FI1C7 | 50,925.3 |
| FI19A | 48,270.8 |
| FI1C6 | 47,499.4 |
| FI1C2 | 46,892.9 |
| FI1C5 | 40,674.6 |
| FI1DC | 36,509.4 |
| FI1DA | 33,548.7 |
| FI1D5 | 18,618.1 |
| FI1D8 | 17,333.9 |
| FI200 | 8,296.9 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: 6 keys differ
| key | run | reference | diff |
|---|---|---|---|
| TRA_Lcv_Dis | 0 | 175.8 | -175.8 |
| TRA_Mop_Gas | 0 | 146.2 | -146.2 |
| TRA_Mot_Gas | 0 | 127.6 | -127.6 |
| TRA_Hdt_Dis | 0 | 62.23 | -62.23 |
| TRA_Lcv_Gas | 0 | 11.85 | -11.85 |
| TRA_Hdt_Gas | 0 | 1.445 | -1.445 |

- PRC_RESID national totals: 34 keys differ
| key | run | reference | diff |
|---|---|---|---|
| TRA_Lcv_Dis / 2010 | 0 | 321.7 | -321.7 |
| TRA_Mop_Gas / 2010 | 0 | 259.9 | -259.9 |
| TRA_Lcv_Dis / 2013 | 0 | 257.3 | -257.3 |
| TRA_Mot_Gas / 2010 | 0 | 226.9 | -226.9 |
| TRA_Lcv_Dis / 2015 | 0 | 214.4 | -214.4 |
| TRA_Mop_Gas / 2013 | 0 | 194.9 | -194.9 |
| TRA_Mot_Gas / 2013 | 0 | 170.2 | -170.2 |
| TRA_Mop_Gas / 2015 | 0 | 151.6 | -151.6 |
| TRA_Lcv_Dis / 2018 | 0 | 150.1 | -150.1 |
| TRA_Mot_Gas / 2015 | 0 | 132.3 | -132.3 |
| TRA_Hdt_Dis / 2010 | 0 | 113.8 | -113.8 |
| TRA_Lcv_Dis / 2020 | 0 | 107.2 | -107.2 |
| TRA_Hdt_Dis / 2013 | 0 | 91.07 | -91.07 |
| TRA_Mop_Gas / 2018 | 0 | 86.63 | -86.63 |
| TRA_Hdt_Dis / 2015 | 0 | 75.89 | -75.89 |


## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| ECHP_naturalgas_CCGT | 56.7 | 84.67 | -27.97 |
| ECHP_coal_thermal | 116.6 | 97.15 | 19.46 |
| ECHP_biomass_thermal | 329.2 | 313.6 | 15.63 |
| EUHYDDAM00 | 1,375.0 | 1,380.6 | -5.621 |
| EEPP_coal_thermal | 43.78 | 40.22 | 3.56 |
| EEPP_PV | 42.59 | 45.46 | -2.877 |
| ECHP_lignite_thermal | 32.32 | 29.84 | 2.476 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_HFO_thermal | 7.837 | 8.341 | -0.5049 |
| EEPP_HFO_thermal | 2.442 | 2.141 | 0.301 |
| EEPP_biomass_thermal | 86.03 | 86.31 | -0.282 |
| EEPP_naturalgas_thermal | 0.06024 | 0.09998 | -0.03974 |
| ECHP_LFO_thermal | 0.01155 | 0.02023 | -0.008682 |
| ECHP_naturalgas_thermal | 2.224 | 2.229 | -0.004875 |
| EEPP_windOFF | 23.59 | 23.59 | -0.001948 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08294 | 0.08335 | -0.0004075 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | -3.187e-06 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | -3.405e-07 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | -3.279e-07 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | -3.069e-07 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | -2.149e-07 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 2.613e-09 |

By class and year: 78 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_coal_thermal / 2020 | 25.43 | 12.65 | 12.78 |
| ECHP_naturalgas_CCGT / 2015 | 21.68 | 28.22 | -6.54 |
| ECHP_naturalgas_CCGT / 2013 | 17.51 | 24.04 | -6.536 |
| ECHP_naturalgas_CCGT / 2010 | 17.51 | 24.04 | -6.536 |
| ECHP_coal_thermal / 2023 | 5.978 | 0 | 5.978 |
| ECHP_biomass_thermal / 2033 | 5.548 | 0 | 5.548 |
| ECHP_biomass_thermal / 2035 | 5.073 | 0 | 5.073 |
| ECHP_biomass_thermal / 2038 | 5.073 | 0 | 5.073 |
| ECHP_naturalgas_CCGT / 2018 | 0 | 4.179 | -4.179 |
| ECHP_naturalgas_CCGT / 2020 | 0 | 4.179 | -4.179 |
| EEPP_coal_thermal / 2013 | 6.005 | 2.445 | 3.56 |
| ECHP_lignite_thermal / 2018 | 2.485 | 0 | 2.485 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,287.0 |
| FI198 | 77.15 |
| FI199 | 157.7 |
| FI19A | 270.2 |
| FI19B | 87.39 |
| FI1B1 | 239.4 |
| FI1C1 | 131.6 |
| FI1C2 | 49.91 |
| FI1C5 | 239.9 |
| FI1C6 | 31.64 |
| FI1C7 | 56.54 |
| FI1D5 | 165.8 |
| FI1D7 | 591.2 |
| FI1D8 | 92.98 |
| FI1D9 | 734.4 |
| FI1DA | 74.91 |
| FI1DB | 23.76 |
| FI1DC | 97.88 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 331.0 | 337.6 | -6.579 |
| 2013 | 289.2 | 292.1 | -2.883 |
| 2015 | 313.4 | 320.1 | -6.684 |
| 2018 | 371.8 | 373.1 | -1.242 |
| 2020 | 322.9 | 314.9 | 8.031 |
| 2023 | 379.5 | 380.3 | -0.791 |
| 2025 | 407.5 | 423.2 | -15.76 |
| 2028 | 452.4 | 478.3 | -25.84 |
| 2030 | 456.1 | 507.3 | -51.15 |
| 2033 | 424.7 | 442.2 | -17.51 |
| 2035 | 446.2 | 464.2 | -17.94 |
| 2038 | 486.6 | 521.6 | -34.96 |
| 2040 | 530.9 | 573.8 | -42.91 |
| 2043 | 549.5 | 623.9 | -74.42 |
| 2045 | 577.1 | 644.7 | -67.53 |
| 2048 | 624.1 | 670.5 | -46.39 |
| 2050 | 665.6 | 708.1 | -42.46 |
| 2053 | 683.3 | 719.1 | -35.83 |
| 2055 | 696.0 | 727.8 | -31.86 |
| 2058 | 711.2 | 749.1 | -37.92 |
| 2060 | 722.7 | 763.8 | -41.05 |
| 2063 | 737.2 | 779.1 | -41.84 |
| 2065 | 747.4 | 788.8 | -41.39 |
| 2068 | 764.3 | 805.1 | -40.81 |
| 2070 | 774.9 | 816.6 | -41.63 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 196.8 | 200.0 | -3.112 |
| 2013 | 191.0 | 179.3 | 11.69 |
| 2015 | 147.6 | 131.1 | 16.52 |
| 2018 | 158.1 | 132.5 | 25.64 |
| 2020 | 192.3 | 145.3 | 46.94 |
| 2023 | 157.6 | 134.0 | 23.54 |
| 2025 | 139.4 | 124.4 | 14.97 |
| 2028 | 177.1 | 212.8 | -35.75 |
| 2030 | 209.4 | 230.4 | -20.93 |
| 2033 | 158.1 | 168.8 | -10.74 |
| 2035 | 167.4 | 177.8 | -10.33 |
| 2038 | 190.5 | 190.0 | 0.5514 |
| 2040 | 203.7 | 204.3 | -0.5764 |
| 2043 | 224.5 | 224.7 | -0.1998 |
| 2045 | 226.3 | 229.2 | -2.953 |
| 2048 | 232.7 | 235.1 | -2.397 |
| 2050 | 241.7 | 239.0 | 2.686 |
| 2053 | 249.4 | 238.4 | 10.94 |
| 2055 | 253.2 | 242.9 | 10.31 |
| 2058 | 258.0 | 249.0 | 8.986 |
| 2060 | 265.8 | 257.1 | 8.675 |
| 2063 | 271.6 | 262.1 | 9.499 |
| 2065 | 272.7 | 263.8 | 8.899 |
| 2068 | 274.0 | 268.4 | 5.534 |
| 2070 | 273.9 | 271.1 | 2.822 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 4.506 | 4.504 |
| 2018 | 11.08 | 0.3735 |
| 2025 | 11.53 | 0.3882 |
| 2033 | 31.95 | 1.082 |
| 2040 | 38.11 | 1.29 |
| 2048 | 31.43 | 1.064 |
| 2055 | 31.31 | 1.06 |
| 2063 | 30.71 | 1.039 |
| 2070 | 30.12 | 1.019 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 10.86 | 0.8562 |
| 2018 | 17.25 | 1.359 |
| 2025 | 86.77 | 6.839 |
| 2033 | 21.24 | 1.674 |
| 2040 | 23.22 | 1.385 |
| 2048 | 18.17 | 0.9961 |
| 2055 | 16.48 | 0.8055 |
| 2063 | 16.67 | 0.822 |
| 2070 | 16.66 | 0.7003 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 28,446.3 | 0.149 |
| ICMFISCO2 | 10,455.8 | 0 |
| OILCRD | 0.162 | 6,038.9 |
| ELCHIG | 4,417.8 | 0.01741 |
| INDELC | 3.87 | 4,073.2 |
| IPPHTH | 10.53 | 3,972.1 |
| GreenCert-ELC | 3,379.3 | 3.232 |
| OILDST | 2,412.7 | 515.6 |
| INDBLQ | 2,474.3 | 2.25 |
| OILGSL | 2,194.9 | 0.1646 |
| BIOOILFS | 0.5798 | 2,109.7 |
| BIOHVO | 1,820.8 | 0.5806 |
| TRADST | 2.926 | 1,651.7 |
| ELCHYD | 2.99 | 1,378.2 |
| ELCWOO | 2.823 | 1,319.3 |
| ELCWIN | 4.618 | 1,096.3 |
| INDBIO | 209.7 | 619.5 |
| HETHTH | 784.7 | 0.01737 |
| ELCNUC | 0.006046 | 751.8 |
| MPPWOO | 0.01951 | 742.1 |
| OILHFO | 420.7 | 163.6 |
| ELCCOH | 0.1312 | 511.3 |
| TRAGSLSP95 | 3.77 | 505.5 |
| INDHTH | 1.226 | 456.6 |
| OILNEU | 0.1677 | 403.7 |
| OILKER | 373.1 | 0.1714 |
| INDCOK | 4.303 | 348.9 |
| SUPRPG | 0.1731 | 343.6 |
| INDGAS | 14.76 | 303.5 |
| INDLFO | 3.71 | 305.2 |
| INDCOA | 3.418 | 293.7 |
| INDRFG | 0.1687 | 289.9 |
| ELCLOW | 0.001486 | 268.8 |
| OILNAP | 0.2352 | 259.2 |
| IOIHTH | 18.31 | 240.6 |
| INDHFO | 3.909 | 234.9 |
| COALIG | 0.1582 | 195.3 |
| ELCGAS | 16.03 | 157.6 |
| ELCCOL | 0.3837 | 160.0 |
| BIOWOO | 0 | 151.4 |
| OILOTH | 56.5 | 88.96 |
| INDHH2 | 71.55 | 71.23 |
| ELCHIGG | 70.88 | 70.88 |
| TRALH2 | 70.88 | 70.88 |
| OILRFG | 110.9 | 26.51 |
| ICHHTH | 3.965 | 132.5 |
| SYNH2CT | 71.49 | 64.1 |
| COACOK | 132.0 | 0.1793 |
| MPPRYC | 0.02153 | 125.8 |
| TRAGSLE85 | 3.465 | 110.1 |
| OILLPG | 13.33 | 92.81 |
| BIOGAS | 85.11 | 15.84 |
| GASNAT | 19.54 | 75.42 |
| SUPRPP | 0.1849 | 79.62 |
| INFHTH | 25.48 | 41.17 |
| MPPGYP | 0 | 63.92 |
| MISSNT | 0.03867 | 62.14 |
| ELCSOL | 5.077 | 50.79 |
| INMHTH | 24.15 | 24.88 |
| GASP2GB | 22.41 | 25.72 |
| AGRGAS | 24.05 | 24.05 |
| GASP2G | 23.63 | 23.63 |
| GASCOG | 45.95 | 0.1914 |
| INDLPG | 5.581 | 39.13 |
| ELCHFO | 5.157 | 33.7 |
| ICMPARA | 37.84 | 0.1814 |
| MISRIR | 37.95 | 0 |
| TRAHFO | 32.33 | 0 |
| INDCOG | 0.3093 | 29.4 |
| MISOXY | 0 | 27.86 |
| INDSLU | 5.728 | 19.53 |
| MISORE | 0 | 24.01 |
| COAHAR | 0.2175 | 22.64 |
| MLMSTN | 0 | 20.2 |
| IIS | 18.51 | 0.09251 |
| SUPGAS | 0.9032 | 17.54 |
| INDMUN | 4.124 | 12.7 |
| MISBFS | 8.226 | 8.205 |
| MPPKAO | 0 | 14.53 |
| ELCMED | 0.00153 | 14.38 |
| INDCOL | 4.502 | 8.312 |
| REFHTH | 0 | 11.62 |
| TRAGSLSP95E10 | 5.498 | 5.498 |
| ETSCO2 | 5.482 | 5.486 |
| ELCDST | 5.279 | 5.66 |
| MISSCR | 0 | 10.6 |
| BRFH2 | 0.5932 | 9.815 |
| MISCST | 7.703 | 2.074 |
| ELCCO2N | 0.003191 | 9.705 |
| SUPBIO | 0.214 | 7.993 |
| GASBFG | 6.277 | 0.6155 |
| MPPNOH | 0 | 5.516 |
| IALHTH | 1.617 | 3.619 |
| MPPOXY | 0 | 3.152 |
| IISHTH | 0.6303 | 1.575 |
| IGH | 1.948 | 0.04255 |
| MALBAU | 0.2714 | 1.157 |
| SUPELC | 0.4627 | 0.8703 |
| BIOPROP | 0.6817 | 0.6071 |
| MISPLT | 0.06603 | 1.213 |
| MGHRYC | 0 | 1.277 |
| ICMLC3 | 0.6217 | 0.6217 |
| INDCOB | 0.3913 | 0.5301 |
| INDBFG | 0.0431 | 0.8522 |
| RENGEO | 0 | 0.7638 |
| ICLHTH | 0.2382 | 0.4897 |
| GreenCert-FIN | 0.2927 | 0.354 |
| GASIIS | 0.3024 | 0.3376 |
| OILFDS | 0.3047 | 0.3173 |
| GASCOP | 0.2795 | 0.2795 |
| ICUHTH | 0 | 0.4682 |
| MALSCR | 0 | 0.4547 |
| BRFCA3 | 0 | 0.4368 |
| MCUORE | 0 | 0.3679 |
| MISQLI | 0 | 0.3045 |
| ICU | 0.2195 | 0.05078 |
| MCUSCR | 0.06987 | 0.06312 |
| MCUSCU | 0.06561 | 0.06667 |
| MISRFC | 0.06603 | 0.06603 |
| RENSOL | 0 | 0.1083 |
| SUPHTH | 0 | 0.09174 |
| IGF | 0 | 1.324e-08 |

- Back-and-forth on the same link, year and timeslice: 54674 cases, volume 598.2
| link / year / ts | min(imp, exp) |
|---|---|
| TB_ETSCO2_FI_FI1DA / 2070 / ANNUAL | 0.06307 |
| TB_ETSCO2_FI_FI1D7 / 2070 / ANNUAL | 0.06307 |
| TB_ETSCO2_FI_FI1C5 / 2070 / ANNUAL | 0.06307 |
| TB_ETSCO2_FI_FI1D9 / 2070 / ANNUAL | 0.06307 |
| TB_ETSCO2_FI_FI1C1 / 2070 / ANNUAL | 0.06307 |
| TB_ETSCO2_FI_FI1B1 / 2070 / ANNUAL | 0.06306 |
| TB_ETSCO2_FI_FI1D5 / 2070 / ANNUAL | 0.06306 |
| TB_ETSCO2_FI_FI199 / 2070 / ANNUAL | 0.06306 |
| TB_ETSCO2_FI_FI1C6 / 2070 / ANNUAL | 0.06306 |
| TB_ETSCO2_FI_FI1C2 / 2070 / ANNUAL | 0.06306 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 148,780.2, reference 130,244.3 (+14.23%); 25 years differ >0.1 %
- ETSCO2: produced, all years: run 363,244.0, reference 343,808.2 (+5.65%); 24 years differ >0.1 %
- INDCO2N: produced, all years: run 116,523.0, reference 126,331.9 (-7.76%); 25 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 10,793.9, reference 11,202.8 (-3.65%); 25 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 5,706.2, reference 6,065.4 (-5.92%); 25 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'GreenCert-ELC': -4.5, 'ETSCO2': 192974.4, 'ELCCO2N': 76585.1} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 80 | 807.1 |
| FI / ELCHIGG | 300 | 84 | 24.96 |
| FI / ELCLOW | 300 | 49 | 125.4 |
| FI / ELCMED | 300 | 70 | 8.113 |
| FI / HETHTH | 300 | 0 | 0 |
| FI196 / ELCHIGG | 300 | 84 | 3,000.9 |
| FI196 / ELCLOW | 300 | 121 | 5,606.0 |
| FI196 / ELCMED | 300 | 164 | 5,364.6 |
| FI198 / ELCHIGG | 300 | 0 | 0 |
| FI198 / ELCLOW | 300 | 114 | 4,641.1 |
| FI198 / ELCMED | 300 | 172 | 6,832.1 |
| FI199 / ELCHIGG | 300 | 82 | 1,965.4 |
| FI199 / ELCLOW | 300 | 94 | 3,553.6 |
| FI199 / ELCMED | 300 | 97 | 2,576.9 |
| FI19A / ELCHIGG | 300 | 76 | 2,872.6 |
| FI19A / ELCLOW | 300 | 122 | 5,925.4 |
| FI19A / ELCMED | 300 | 294 | 10,938.8 |
| FI19B / ELCHIGG | 300 | 21 | 760.6 |
| FI19B / ELCLOW | 300 | 92 | 4,777.4 |
| FI19B / ELCMED | 300 | 245 | 8,422.9 |
| FI1B1 / ELCHIGG | 300 | 1 | 80.69 |
| FI1B1 / ELCLOW | 300 | 179 | 6,795.8 |
| FI1B1 / ELCMED | 300 | 248 | 9,735.1 |
| FI1C1 / ELCHIGG | 300 | 48 | 750.2 |
| FI1C1 / ELCLOW | 300 | 198 | 7,944.3 |
| FI1C1 / ELCMED | 300 | 74 | 3,887.7 |
| FI1C2 / ELCHIGG | 300 | 183 | 5,261.2 |
| FI1C2 / ELCLOW | 300 | 46 | 2,533.1 |
| FI1C2 / ELCMED | 300 | 208 | 6,617.7 |
| FI1C5 / ELCHIGG | 300 | 160 | 6,514.3 |
| FI1C5 / ELCLOW | 300 | 97 | 3,881.0 |
| FI1C5 / ELCMED | 300 | 194 | 8,018.1 |
| FI1C6 / ELCHIGG | 300 | 0 | 0 |
| FI1C6 / ELCLOW | 300 | 173 | 6,435.4 |
| FI1C6 / ELCMED | 300 | 267 | 10,604.9 |
| FI1C7 / ELCHIGG | 300 | 6 | 27.82 |
| FI1C7 / ELCLOW | 300 | 136 | 6,743.0 |
| FI1C7 / ELCMED | 300 | 85 | 3,584.7 |
| FI1D5 / ELCHIGG | 300 | 146 | 4,331.4 |
| FI1D5 / ELCLOW | 300 | 157 | 6,672.0 |
| FI1D5 / ELCMED | 300 | 71 | 1,665.4 |
| FI1D7 / ELCHIGG | 300 | 224 | 6,475.6 |
| FI1D7 / ELCLOW | 300 | 186 | 8,173.9 |
| FI1D7 / ELCMED | 300 | 61 | 3,022.9 |
| FI1D8 / ELCHIGG | 300 | 292 | 8,917.5 |
| FI1D8 / ELCLOW | 300 | 76 | 3,980.6 |
| FI1D8 / ELCMED | 300 | 91 | 2,771.5 |
| FI1D9 / ELCHIGG | 300 | 185 | 7,183.5 |
| FI1D9 / ELCLOW | 300 | 145 | 5,633.8 |
| FI1D9 / ELCMED | 300 | 192 | 6,370.6 |
| FI1DA / ELCHIGG | 300 | 49 | 805.0 |
| FI1DA / ELCLOW | 300 | 74 | 2,741.3 |
| FI1DA / ELCMED | 300 | 45 | 770.2 |
| FI1DB / ELCHIGG | 300 | 136 | 4,265.7 |
| FI1DB / ELCLOW | 300 | 95 | 3,875.6 |
| FI1DB / ELCMED | 300 | 116 | 4,461.8 |
| FI1DC / ELCHIGG | 300 | 122 | 3,757.4 |
| FI1DC / ELCLOW | 300 | 151 | 4,679.0 |
| FI1DC / ELCMED | 300 | 184 | 6,619.4 |
| FI200 / ELCHIGG | 300 | 27 | 1,037.8 |
| FI200 / ELCLOW | 300 | 266 | 10,498.6 |
| FI200 / ELCMED | 300 | 112 | 4,671.8 |

- Peak equations outside the hub: 57 region/commodity pairs (expected none in the hub design)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 260; only in run: 53; only in reference: 26
| binding only in run | sum |shadow| |
|---|---|
| UCI_UP_CHPShare-IAL | 130,255.8 |
| UCI_UP_CHPShare-ICL | 84,005.9 |
| UCI_UP_CHPShare-ICU | 39,860.1 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 6,469.6 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDBIO_LO | 684.1 |
| RS_PRD_COMBIO_LO | 653.9 |
| RS_PRD_RSDHET_LO | 323.8 |
| RS_PRD_COMGAS_LO | 174.2 |
| RS_PRD_RSDFINOIL_LO | 131.3 |
| RS_PRD_RSDGAS_LO | 130.5 |
| RS_PRD_COMFINOIL_LO | 127.8 |
| RS_PRD_COMHET_LO | 62.98 |
| UCI_UP_CHPShare-IIS | 54.72 |
| RS_FLO_RSDHET00_HETHTH_UP | 31.12 |

| binding only in reference | sum |shadow| |
|---|---|
| TUC_Istruc_RIR-CYC | 10,699.4 |
| UC_transport_H2_pre2028 | 3,118.0 |
| UC_Trucks_EV_pre2028 | 714.8 |
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
| UC_VARU_CAP_EUGEOF01 | 3.776 |

Shadow prices differing by more than 5 %: 304; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_CAP_EEPP_natgas_CCGT | 390,887.0 | 1,318.7 | 389,568.3 |
| UC_VARU_CAP_EEPP_naturalgas_th | 387,513.1 | 2,436.8 | 385,076.3 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 382,934.6 | 1,269.5 | 381,665.2 |
| UC_VARU_CAP_EEPP_HFO_th | 142,549.6 | 702.2 | 141,847.4 |
| UCI_UP_CHPShare-IAL | 130,255.8 | 0 | 130,255.8 |
| UC_HydroLakeSupply_CE | 153,730.4 | 35,734.3 | 117,996.1 |
| UC_VARU_ACT_EEPP_natgas_OCGT | 103,063.7 | 8,790.4 | 94,273.3 |
| UCI_UP_CHPShare-ICL | 84,005.9 | 0 | 84,005.9 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 85,059.0 | 6,902.7 | 78,156.2 |
| UC_VARU_ACT_EEPP_naturalgas_th | 81,381.1 | 8,719.1 | 72,662.0 |
| UC_VARU_ACT_EEPP_HFO_th | 58,369.5 | 10,729.6 | 47,639.8 |
| UCI_UP_CHPShare-ICU | 39,860.1 | 0 | 39,860.1 |
| TUC_TRA_Lcv-Lpg | 3,881.5 | 32,707.9 | -28,826.4 |
| UC_VARU_ACT_EEPP_lignite_th | 19,642.4 | 8,299.1 | 11,343.3 |
| TUC_Istruc_COP_PRD | 21,834.6 | 33,064.1 | -11,229.6 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 718 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI1B1 / 2015 / THDT | 2,251.6 | 0 | 2,251.6 |
| FI1C1 / 2015 / THDT | 974.7 | 0 | 974.7 |
| FI1B1 / 2013 / THDT | 917.9 | 0 | 917.9 |
| FI19B / 2015 / THDT | 905.9 | 0 | 905.9 |
| FI1D9 / 2015 / THDT | 679.6 | 0 | 679.6 |
| FI196 / 2015 / THDT | 596.8 | 0 | 596.8 |
| FI199 / 2015 / THDT | 582.7 | 0 | 582.7 |
| FI1DB / 2015 / THDT | 502.0 | 0 | 502.0 |
| FI198 / 2015 / THDT | 463.6 | 0 | 463.6 |
| FI1C1 / 2013 / THDT | 397.4 | 0 | 397.4 |

- CST_FLOX: 0 entries differ
### investment: 966 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Hdt_Dis_01 | 633,453.1 | 19,113.7 | 614,339.4 |
| TRA_Hdt_ELC_01 | 0.06241 | 56,662.1 | -56,662.1 |
| TRA_Hdt_Dis_10 | 0.06955 | 29,643.7 | -29,643.6 |
| TRA_Bus_Dis_Urb_01 | 18,920.5 | 0 | 18,920.5 |
| TRA_Car_PIH_UpM_20pct | 6,943.8 | 18,154.7 | -11,210.9 |
| COMBATS01 | 0 | 10,588.6 | -10,588.6 |
| RSDBATS01 | 18,457.5 | 9,902.3 | 8,555.2 |
| TRA_Lcv_Dis_01 | 8,590.7 | 16,226.2 | -7,635.5 |
| TRA_Car_Gas_UpM_11 | 7,237.1 | 0 | 7,237.1 |
| TRA_Car_PIH_LoM_20pct | 36,558.5 | 29,648.3 | 6,910.2 |
| TRA_Bus_Eth_Urb_01 | 6,896.7 | 0 | 6,896.7 |
| BRF2_BTLFTDSL | 0.0001776 | 6,723.4 | -6,723.4 |

### fixed O&M: 804 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Hdt_Dis_01 | 100,449.6 | 3,031.0 | 97,418.7 |
| TRA_Hdt_ELC_01 | 0.008997 | 8,168.3 | -8,168.3 |
| TRA_Hdt_Dis_10 | 0.01103 | 4,700.7 | -4,700.7 |
| TRA_Bus_Dis_Urb_01 | 3,366.1 | 0 | 3,366.1 |
| BRF2_BTLFTDSL | 7.185e-05 | 2,720.7 | -2,720.7 |
| TRA_Car_PIH_UpM_20pct | 1,606.1 | 4,193.0 | -2,586.9 |
| HHTHGEO001 | 0.00108 | 2,197.7 | -2,197.7 |
| TRA_Lcv_Dis_01 | 1,857.6 | 3,508.7 | -1,651.1 |
| TRA_Car_Gas_UpM_11 | 1,644.9 | 0 | 1,644.9 |
| TRA_Car_PIH_LoM_20pct | 8,452.8 | 6,861.4 | 1,591.4 |
| TRA_Car_PIH_Sma_20pct | 3,613.3 | 2,089.1 | 1,524.2 |
| TRA_Car_Dis_UpM_21 | 1,238.6 | 0 | 1,238.6 |

### activity: 1400 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| HHTHGEO001 | 0.0003363 | 693.1 | -693.1 |
| S_CCUS_EMIS_H2T | 600.4 | 408.7 | 191.8 |
| IPPPUPCHE01 | 2,753.5 | 2,934.4 | -180.9 |
| EUCCGASCCSpos20 | 76.72 | 199.6 | -122.8 |
| IGHRECYCL10 | 433.5 | 543.2 | -109.8 |
| IMPBIOEMHV | 205.7 | 308.2 | -102.5 |
| BRF2_BTLFTDSL | 1.498e-06 | 58.46 | -58.46 |
| ICLADVPRO05 | 75.5 | 129.2 | -53.71 |
| SBIOH2GCC01 | 231.7 | 178.2 | 53.46 |
| ICLADVPRO01 | 105.5 | 55.7 | 49.83 |
| S_CCUS_EMIS_H2T_LowAF | 167.0 | 117.6 | 49.38 |
| SELCH2EC01_LowAF | 42.71 | 3.418 | 39.29 |

### flow/import: 170 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IMPOILCRD | 88,788.0 | 57,840.3 | 30,947.7 |
| EXPOILGSL | -32,090.8 | -16,267.1 | -15,823.6 |
| EXPOILDST | -20,913.3 | -9,767.3 | -11,146.1 |
| TRABAT_ChgStn | 1,569.0 | 10,525.0 | -8,956.0 |
| IMPOILDST | 7,271.6 | 15,101.9 | -7,830.3 |
| MINMPPWOO1 | 111,096.2 | 115,521.8 | -4,425.6 |
| TRAELC00 | 845.2 | 4,101.9 | -3,256.7 |
| EXPELC-fromFI | -4,012.1 | -1,343.3 | -2,668.8 |
| IMPOILGSL | 1,948.8 | 4,570.2 | -2,621.4 |
| EXPOILHFO | -4,040.1 | -1,871.8 | -2,168.3 |
| IMPOILKER | 1,643.3 | 3,597.7 | -1,954.3 |
| EXPOILKER | -2,337.2 | -1,176.6 | -1,160.6 |

### capacity (sum over years): 330 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Car_PIH_UpM_20pct | 2,711.0 | 7,067.6 | -4,356.7 |
| TRA_Car_PIH_LoM_20pct | 14,265.7 | 11,590.1 | 2,675.6 |
| TRA_Car_PIH_Sma_20pct | 6,108.7 | 3,545.9 | 2,562.9 |
| TRA_Car_Elc_Sma_10 | 6,110.3 | 8,012.9 | -1,902.5 |
| R_ES-SH-FL_ELC01 | 13,722.5 | 12,484.1 | 1,238.4 |
| R_ES-SH-FL_GAS01 | 0.003283 | 749.8 | -749.8 |
| TRA_Car_Elc_Exe_10 | 15,137.3 | 14,414.0 | 723.2 |
| R_ES-SH-DH-70_ELC05 | 4,583.9 | 4,193.1 | 390.8 |
| R_ES-SH-SD_ELC05 | 2,936.0 | 3,320.2 | -384.1 |
| R_ES-SH-DH-70_BIO01 | 0.00194 | 380.6 | -380.6 |
| COMBATS01 | 0 | 356.8 | -356.8 |
| RSDBATS01 | 658.5 | 371.0 | 287.5 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## L. Output without inputs
- Processes running with less than 20 % of their reference inputs per unit of activity: none

## Verdict
FAIL: NCAP_PASTI, PRC_RESID
