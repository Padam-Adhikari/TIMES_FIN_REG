# Audit of reg_baseline-sami_2026-11-19_task5b_run4.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,527,592.91 M EUR, reference 1,529,919.88, difference -2,326.98 (-0.1521%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,674.1 | 144,742.3 | -68.2 |
| INV | 918,768.8 | 919,897.7 | -1,128.9 |
| VAR | 464,150.0 | 465,279.9 | -1,129.9 |
| VARX | 0.04537 | 0 | 0.04537 |

| region | objective share |
|---|---|
| FI | 1,018,480.4 |
| FI1B1 | 109,623.8 |
| FI196 | 52,503.0 |
| FI19B | 41,360.5 |
| FI1D9 | 41,188.9 |
| FI1C1 | 37,925.4 |
| FI198 | 25,077.9 |
| FI1C7 | 24,600.7 |
| FI1DB | 22,419.5 |
| FI1C5 | 22,385.4 |
| FI1D7 | 20,890.0 |
| FI19A | 20,178.7 |
| FI199 | 18,950.8 |
| FI1C6 | 16,570.3 |
| FI1C2 | 15,713.3 |
| FI1DC | 13,649.5 |
| FI1DA | 11,290.0 |
| FI1D5 | 5,947.6 |
| FI1D8 | 5,868.8 |
| FI200 | 2,968.6 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved
- PRC_RESID national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| EEPP_PV | 42.5 | 45.46 | -2.962 |
| ECHP_coal_thermal | 99.14 | 97.15 | 1.991 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| EEPP_coal_thermal | 41.14 | 40.22 | 0.9251 |
| EUHYDDAM00 | 1,379.7 | 1,380.6 | -0.8778 |
| ECHP_naturalgas_CCGT | 84.25 | 84.67 | -0.4165 |
| EEPP_biomass_thermal | 86.03 | 86.31 | -0.2746 |
| ECHP_HFO_thermal | 8.106 | 8.341 | -0.2351 |
| ECHP_biomass_thermal | 313.5 | 313.6 | -0.05821 |
| EEPP_naturalgas_thermal | 0.06191 | 0.09998 | -0.03807 |
| ECHP_LFO_thermal | 0 | 0.02023 | -0.02023 |
| ECHP_naturalgas_thermal | 2.219 | 2.229 | -0.00962 |
| ECHP_lignite_thermal | 29.84 | 29.84 | -0.003012 |
| EEPP_windOFF | 23.59 | 23.59 | -0.001947 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| EEPP_LFO_thermal | 0.08295 | 0.08335 | -0.0003985 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | -9.319e-06 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | -2.036e-07 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | -1.976e-07 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | -1.874e-07 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | -1.374e-07 |
| EEPP_HFO_thermal | 2.141 | 2.141 | 1.22e-08 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 1.264e-09 |

By class and year: 60 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_coal_thermal / 2020 | 14.1 | 12.65 | 1.451 |
| EEPP_coal_thermal / 2013 | 3.37 | 2.445 | 0.9251 |
| EUHYDDAM00 / 2030 | 54.28 | 55.04 | -0.7532 |
| ECHP_coal_thermal / 2018 | 38.65 | 38.11 | 0.5405 |
| EEPP_PV / 2023 | 2.688 | 2.932 | -0.2439 |
| EEPP_PV / 2040 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2038 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2035 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2033 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2030 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2028 | 3.564 | 3.796 | -0.2319 |
| EEPP_PV / 2025 | 3.564 | 3.796 | -0.2319 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,284.6 |
| FI198 | 76.95 |
| FI199 | 157.7 |
| FI19A | 265.8 |
| FI19B | 93.38 |
| FI1B1 | 249.3 |
| FI1C1 | 122.2 |
| FI1C2 | 49.98 |
| FI1C5 | 237.7 |
| FI1C6 | 30.86 |
| FI1C7 | 56.62 |
| FI1D5 | 165.5 |
| FI1D7 | 591.6 |
| FI1D8 | 93.38 |
| FI1D9 | 732.9 |
| FI1DA | 73.04 |
| FI1DB | 23.58 |
| FI1DC | 98.11 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.5 | 337.6 | -0.07724 |
| 2013 | 292.9 | 292.1 | 0.8689 |
| 2015 | 319.9 | 320.1 | -0.2253 |
| 2018 | 373.2 | 373.1 | 0.1176 |
| 2020 | 315.6 | 314.9 | 0.7161 |
| 2023 | 381.6 | 380.3 | 1.313 |
| 2025 | 423.2 | 423.2 | -0.006932 |
| 2028 | 478.8 | 478.3 | 0.5059 |
| 2030 | 507.8 | 507.3 | 0.5163 |
| 2033 | 442.3 | 442.2 | 0.09072 |
| 2035 | 464.5 | 464.2 | 0.3747 |
| 2038 | 522.8 | 521.6 | 1.247 |
| 2040 | 576.2 | 573.8 | 2.443 |
| 2043 | 624.4 | 623.9 | 0.4994 |
| 2045 | 643.4 | 644.7 | -1.241 |
| 2048 | 670.4 | 670.5 | -0.09066 |
| 2050 | 700.5 | 708.1 | -7.56 |
| 2053 | 712.3 | 719.1 | -6.819 |
| 2055 | 724.7 | 727.8 | -3.13 |
| 2058 | 748.3 | 749.1 | -0.8617 |
| 2060 | 763.3 | 763.8 | -0.4286 |
| 2063 | 779.1 | 779.1 | 0.0721 |
| 2065 | 788.5 | 788.8 | -0.2475 |
| 2068 | 805.3 | 805.1 | 0.1764 |
| 2070 | 817.6 | 816.6 | 1.006 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 198.7 | 200.0 | -1.243 |
| 2013 | 179.2 | 179.3 | -0.1198 |
| 2015 | 131.0 | 131.1 | -0.1526 |
| 2018 | 133.2 | 132.5 | 0.6794 |
| 2020 | 147.4 | 145.3 | 2.066 |
| 2023 | 134.2 | 134.0 | 0.2291 |
| 2025 | 122.5 | 124.4 | -1.88 |
| 2028 | 212.2 | 212.8 | -0.6924 |
| 2030 | 231.5 | 230.4 | 1.137 |
| 2033 | 168.2 | 168.8 | -0.6531 |
| 2035 | 177.0 | 177.8 | -0.8105 |
| 2038 | 189.0 | 190.0 | -1.009 |
| 2040 | 202.5 | 204.3 | -1.753 |
| 2043 | 222.4 | 224.7 | -2.236 |
| 2045 | 229.0 | 229.2 | -0.2275 |
| 2048 | 233.0 | 235.1 | -2.102 |
| 2050 | 233.7 | 239.0 | -5.277 |
| 2053 | 234.9 | 238.4 | -3.494 |
| 2055 | 241.2 | 242.9 | -1.637 |
| 2058 | 248.4 | 249.0 | -0.5788 |
| 2060 | 256.2 | 257.1 | -0.9427 |
| 2063 | 260.6 | 262.1 | -1.517 |
| 2065 | 263.7 | 263.8 | -0.1037 |
| 2068 | 268.3 | 268.4 | -0.1649 |
| 2070 | 271.6 | 271.1 | 0.5011 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 4.711 | 4.719 |
| 2018 | 12.9 | 0.4352 |
| 2025 | 8.696 | 0.2945 |
| 2033 | 35.22 | 1.192 |
| 2040 | 47.43 | 1.605 |
| 2048 | 27.02 | 0.9147 |
| 2055 | 29.93 | 0.9893 |
| 2063 | 30.5 | 1.006 |
| 2070 | 29.27 | 0.9643 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.107 | 0.7179 |
| 2018 | 21.61 | 1.703 |
| 2025 | 235.5 | 18.56 |
| 2033 | 23.35 | 1.554 |
| 2040 | 30.05 | 1.739 |
| 2048 | 14.81 | 0.7664 |
| 2055 | 16.42 | 0.7847 |
| 2063 | 16.58 | 0.797 |
| 2070 | 16.37 | 0.68 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,103.3 | 0.09706 |
| ICMFISCO2 | 10,399.4 | 0 |
| ELCHIG | 4,411.6 | 0.01205 |
| OILCRD | 0.1071 | 4,106.4 |
| INDELC | 3.301 | 4,070.9 |
| IPPHTH | 6.786 | 4,002.5 |
| BIOOILFS | 0.349 | 3,602.9 |
| GreenCert-ELC | 3,350.0 | 2.105 |
| BIOHVO | 3,109.4 | 0.3493 |
| INDBLQ | 2,549.7 | 1.472 |
| OILDST | 1,627.2 | 515.6 |
| TRADST | 2.033 | 1,633.2 |
| OILGSL | 1,492.1 | 0.1087 |
| ELCHYD | 1.942 | 1,381.9 |
| ELCWOO | 1.929 | 1,271.4 |
| ELCLOW | 31.79 | 1,152.6 |
| ELCWIN | 3.045 | 1,094.7 |
| INDBIO | 257.9 | 651.2 |
| MPPWOO | 0.0127 | 771.1 |
| HETHTH | 758.8 | 0.01148 |
| ELCNUC | 0.003972 | 751.8 |
| TRAGSLSP95 | 2.269 | 663.8 |
| ELCCOH | 0.09162 | 446.8 |
| INDHTH | 0.7981 | 443.4 |
| OILHFO | 274.0 | 165.4 |
| OILNEU | 0.1099 | 410.6 |
| INDCOK | 2.978 | 347.0 |
| INDLFO | 2.405 | 304.8 |
| INDCOA | 2.295 | 297.6 |
| INDGAS | 9.552 | 283.9 |
| INDRFG | 0.1105 | 289.8 |
| OILNAP | 0.1531 | 286.0 |
| INDHFO | 2.522 | 268.3 |
| SUPRPG | 0.114 | 233.7 |
| OILKER | 232.7 | 0.1134 |
| ELCGAS | 10.58 | 218.4 |
| IOIHTH | 16.64 | 204.3 |
| COALIG | 0.1032 | 189.7 |
| BIOWOO | 0 | 151.3 |
| ELCCOL | 0.2662 | 149.2 |
| OILOTH | 33.59 | 113.4 |
| OILLPG | 12.94 | 117.6 |
| COACOK | 127.7 | 0.117 |
| ICHHTH | 3.536 | 121.5 |
| MPPRYC | 0.01391 | 118.6 |
| TRAGSLE85 | 2.298 | 110.2 |
| BIOGAS | 96.98 | 10.27 |
| ELCMED | 42.87 | 57.28 |
| INDHH2 | 47.65 | 47.41 |
| OILRFG | 63.01 | 32.01 |
| ELCHIGG | 46.99 | 46.99 |
| TRALH2 | 46.99 | 46.99 |
| SYNH2CT | 49.49 | 42.02 |
| GASNAT | 12.95 | 67.19 |
| INFHTH | 24.95 | 42.01 |
| MISSNT | 0.02521 | 65.57 |
| MPPGYP | 0 | 63.92 |
| SUPRPP | 0.1213 | 54.18 |
| ELCSOL | 3.336 | 48.93 |
| INDLPG | 3.697 | 44.7 |
| GASCOG | 43.24 | 0.1245 |
| MISRIR | 38.28 | 0 |
| ICMPARA | 37.78 | 0.1182 |
| ELCHFO | 3.43 | 31.82 |
| GASP2GB | 14.38 | 19.33 |
| INMHTH | 16.16 | 16.9 |
| AGRGAS | 16.09 | 16.09 |
| GASP2G | 15.66 | 15.66 |
| TRAHFO | 29.73 | 0 |
| MISOXY | 0 | 27.68 |
| INDCOG | 0.204 | 26.78 |
| COAHAR | 0.1398 | 22.56 |
| MISORE | 0 | 20.57 |
| MLMSTN | 0 | 20.19 |
| INDSLU | 3.787 | 15.86 |
| IIS | 18.48 | 0.05977 |
| SUPGAS | 0.5803 | 16.74 |
| BRFH2 | 0.3627 | 16.11 |
| MISBFS | 7.881 | 7.771 |
| MPPKAO | 0 | 14.53 |
| INDMUN | 2.727 | 9.933 |
| MISCST | 7.705 | 3.279 |
| INDCOL | 3.101 | 6.944 |
| MISSCR | 0 | 9.287 |
| REFHTH | 0 | 7.904 |
| GASBFG | 7.189 | 0.4125 |
| TRAGSLSP95E10 | 3.71 | 3.71 |
| ELCDST | 3.495 | 3.881 |
| ETSCO2 | 3.604 | 3.605 |
| ELCCO2N | 0.001954 | 6.57 |
| MPPNOH | 0 | 5.737 |
| SUPBIO | 0.1403 | 5.43 |
| IALHTH | 1.047 | 3.049 |
| MPPOXY | 0 | 3.278 |
| IGH | 1.722 | 0.02924 |
| IISHTH | 0.4545 | 1.161 |
| SUPELC | 0.4449 | 1.141 |
| MALBAU | 0.173 | 1.058 |
| MISPLT | 0.04372 | 1.15 |
| MGHRYC | 0 | 1.174 |
| BIOPROP | 0.5069 | 0.3812 |
| ICMLC3 | 0.4122 | 0.4122 |
| BRFCA3 | 0 | 0.7462 |
| INDCOB | 0.2791 | 0.4178 |
| RENGEO | 0 | 0.6901 |
| INDBFG | 0.02517 | 0.6575 |
| ICLHTH | 0.1587 | 0.3841 |
| ICUHTH | 0 | 0.4682 |
| MALSCR | 0 | 0.4547 |
| GreenCert-FIN | 0.1948 | 0.2314 |
| GASIIS | 0.2005 | 0.2245 |
| OILFDS | 0.202 | 0.2104 |
| GASCOP | 0.1853 | 0.1853 |
| MCUORE | 0 | 0.3679 |
| MISQLI | 0 | 0.2985 |
| ICU | 0.2012 | 0.03238 |
| SUPHTH | 0 | 0.1567 |
| RENSOL | 0 | 0.1125 |
| MCUSCR | 0.04774 | 0.04099 |
| MCUSCU | 0.04334 | 0.0444 |
| MISRFC | 0.04372 | 0.04372 |

- Back-and-forth on the same link, year and timeslice: 66083 cases, volume 469.2
| link / year / ts | min(imp, exp) |
|---|---|
| TB_MISCST_FI_FI1C5 / 2020 / ANNUAL | 0.2763 |
| TB_MISCST_FI_FI1D9 / 2020 / ANNUAL | 0.2306 |
| TB_MISCST_FI_FI1D7 / 2020 / ANNUAL | 0.2149 |
| TB_MISCST_FI_FI1C2 / 2020 / ANNUAL | 0.1422 |
| TB_SUPELC_FI_FI1C5 / 2058 / SN | 0.04221 |
| TB_SUPELC_FI_FI1B1 / 2058 / SN | 0.0419 |
| TB_ETSCO2_FI_FI1C5 / 2070 / ANNUAL | 0.0415 |
| TB_ETSCO2_FI_FI1D7 / 2070 / ANNUAL | 0.0415 |
| TB_ETSCO2_FI_FI1D9 / 2070 / ANNUAL | 0.0415 |
| TB_ETSCO2_FI_FI1DA / 2070 / ANNUAL | 0.0415 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 131,223.6, reference 130,244.3 (+0.75%); 24 years differ >0.1 %
- ETSCO2: produced, all years: run 344,075.7, reference 343,808.2 (+0.08%); 23 years differ >0.1 %
- INDCO2N: produced, all years: run 126,426.8, reference 126,331.9 (+0.08%); 24 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,124.3, reference 11,202.8 (-0.70%); 21 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,120.2, reference 6,065.4 (+0.90%); 19 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'ELCCO2N': 72875.7, 'ETSCO2': 182162.7, 'GreenCert-ELC': -4.5} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 78 | 792.5 |
| FI / ELCHIGG | 300 | 91 | 33.32 |
| FI / ELCLOW | 300 | 52 | 120.6 |
| FI / ELCMED | 300 | 85 | 11.91 |
| FI / HETHTH | 300 | 0 | 0 |
| FI196 / ELCHIGG | 300 | 65 | 2,878.6 |
| FI196 / ELCLOW | 300 | 115 | 5,607.4 |
| FI196 / ELCMED | 300 | 217 | 8,685.4 |
| FI198 / ELCHIGG | 300 | 0 | 0 |
| FI198 / ELCLOW | 300 | 106 | 5,101.9 |
| FI198 / ELCMED | 300 | 148 | 6,695.1 |
| FI199 / ELCHIGG | 300 | 86 | 2,287.1 |
| FI199 / ELCLOW | 300 | 128 | 5,292.7 |
| FI199 / ELCMED | 300 | 89 | 2,328.8 |
| FI19A / ELCHIGG | 300 | 74 | 3,223.2 |
| FI19A / ELCLOW | 300 | 125 | 6,235.8 |
| FI19A / ELCMED | 300 | 121 | 2,040.7 |
| FI19B / ELCHIGG | 300 | 35 | 1,879.2 |
| FI19B / ELCLOW | 300 | 91 | 4,918.5 |
| FI19B / ELCMED | 300 | 278 | 10,245.5 |
| FI1B1 / ELCHIGG | 300 | 5 | 212.4 |
| FI1B1 / ELCLOW | 300 | 187 | 7,251.9 |
| FI1B1 / ELCMED | 300 | 241 | 9,730.2 |
| FI1C1 / ELCHIGG | 300 | 57 | 855.2 |
| FI1C1 / ELCLOW | 300 | 177 | 7,517.8 |
| FI1C1 / ELCMED | 300 | 52 | 2,297.0 |
| FI1C2 / ELCHIGG | 300 | 198 | 7,456.1 |
| FI1C2 / ELCLOW | 300 | 41 | 2,436.2 |
| FI1C2 / ELCMED | 300 | 178 | 5,384.8 |
| FI1C5 / ELCHIGG | 300 | 170 | 7,716.0 |
| FI1C5 / ELCLOW | 300 | 90 | 4,807.6 |
| FI1C5 / ELCMED | 300 | 116 | 2,622.0 |
| FI1C6 / ELCHIGG | 300 | 0 | 0 |
| FI1C6 / ELCLOW | 300 | 206 | 7,907.9 |
| FI1C6 / ELCMED | 300 | 265 | 10,506.6 |
| FI1C7 / ELCHIGG | 300 | 11 | 99.23 |
| FI1C7 / ELCLOW | 300 | 178 | 7,192.6 |
| FI1C7 / ELCMED | 300 | 103 | 5,253.4 |
| FI1D5 / ELCHIGG | 300 | 154 | 5,739.0 |
| FI1D5 / ELCLOW | 300 | 120 | 4,245.7 |
| FI1D5 / ELCMED | 300 | 43 | 2,416.3 |
| FI1D7 / ELCHIGG | 300 | 237 | 8,429.1 |
| FI1D7 / ELCLOW | 300 | 160 | 6,405.1 |
| FI1D7 / ELCMED | 300 | 63 | 3,216.1 |
| FI1D8 / ELCHIGG | 300 | 289 | 10,455.0 |
| FI1D8 / ELCLOW | 300 | 80 | 3,563.1 |
| FI1D8 / ELCMED | 300 | 169 | 7,664.7 |
| FI1D9 / ELCHIGG | 300 | 173 | 8,731.1 |
| FI1D9 / ELCLOW | 300 | 141 | 5,750.6 |
| FI1D9 / ELCMED | 300 | 159 | 6,245.1 |
| FI1DA / ELCHIGG | 300 | 67 | 1,166.9 |
| FI1DA / ELCLOW | 300 | 81 | 2,277.6 |
| FI1DA / ELCMED | 300 | 44 | 586.4 |
| FI1DB / ELCHIGG | 300 | 151 | 5,479.3 |
| FI1DB / ELCLOW | 300 | 96 | 3,128.7 |
| FI1DB / ELCMED | 300 | 129 | 4,550.0 |
| FI1DC / ELCHIGG | 300 | 110 | 3,755.2 |
| FI1DC / ELCLOW | 300 | 178 | 5,914.6 |
| FI1DC / ELCMED | 300 | 172 | 6,931.9 |
| FI200 / ELCHIGG | 300 | 52 | 1,493.8 |
| FI200 / ELCLOW | 300 | 252 | 9,338.0 |
| FI200 / ELCMED | 300 | 74 | 3,730.3 |

- Peak equations outside the hub: 57 region/commodity pairs (expected none in the hub design)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 265; only in run: 57; only in reference: 21
| binding only in run | sum |shadow| |
|---|---|
| UCI_UP_CHPShare-IAL | 138,653.3 |
| UCI_UP_CHPShare-ICL | 99,436.4 |
| UCI_UP_CHPShare-ICU | 53,303.5 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 10,726.8 |
| RS_PRD_RSDFINOIL_LO | 2,357.6 |
| RS_PRD_COMFINOIL_LO | 2,340.1 |
| RS_PRD_RSDBIO_LO | 1,185.0 |
| RS_PRD_COMBIO_LO | 1,135.8 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 633.6 |
| RS_PRD_COMGAS_LO | 407.7 |
| RS_PRD_RSDGAS_LO | 371.8 |
| UCI_UP_CHPShare-IIS | 90.92 |
| RS_PRD_COMHET_LO | 78.67 |
| RS_PRD_INDFINGAS_LO | 62.75 |

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

Shadow prices differing by more than 5 %: 208; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_CAP_EEPP_natgas_CCGT | 489,545.9 | 1,318.7 | 488,227.2 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 460,115.5 | 1,269.5 | 458,846.0 |
| UC_VARU_CAP_EEPP_naturalgas_th | 459,056.0 | 2,436.8 | 456,619.1 |
| UC_VARU_CAP_EEPP_HFO_th | 190,750.7 | 702.2 | 190,048.5 |
| UCI_UP_CHPShare-IAL | 138,653.3 | 0 | 138,653.3 |
| UC_VARU_ACT_EEPP_natgas_OCGT | 131,052.9 | 8,790.4 | 122,262.6 |
| UCI_UP_CHPShare-ICL | 99,436.4 | 0 | 99,436.4 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 103,432.6 | 6,902.7 | 96,529.8 |
| UC_VARU_ACT_EEPP_naturalgas_th | 100,901.9 | 8,719.1 | 92,182.7 |
| UC_VARU_ACT_EEPP_HFO_th | 79,924.4 | 10,729.6 | 69,194.8 |
| UCI_UP_CHPShare-ICU | 53,303.5 | 0 | 53,303.5 |
| UC_HydroLakeSupply_CE | 65,229.6 | 35,734.3 | 29,495.3 |
| UC_VARU_ACT_EEPP_lignite_th | 27,108.1 | 8,299.1 | 18,809.0 |
| UC_VARU_CAP_EEPP_lignite_th | 15,432.1 | 630.4 | 14,801.7 |
| UC_VARU_CAP_EEPP_coal_th | 15,439.1 | 1,060.7 | 14,378.4 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 416 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI1C5 / 2070 / MCMCLKBYF | 0.002078 | 0 | 0.002078 |
| FI1C1 / 2070 / MCMCLKBYF | 0.002077 | 0 | 0.002077 |
| FI1C5 / 2070 / MCMCLKCCSC | 0.002052 | 0 | 0.002052 |
| FI1C1 / 2070 / MCMCLKCCSC | 0.002048 | 0 | 0.002048 |
| FI1C5 / 2070 / MCMCLKLAPP | 0.001894 | 0 | 0.001894 |
| FI / 2070 / ILMHTH | 0.0009923 | 0 | 0.0009923 |
| FI1B1 / 2070 / INFOTH | 0.0008409 | 0 | 0.0008409 |
| FI200 / 2070 / INFOTH | 0.0008409 | 0 | 0.0008409 |
| FI1D5 / 2070 / INFOTH | 0.0008409 | 0 | 0.0008409 |
| FI199 / 2070 / INFOTH | 0.0008409 | 0 | 0.0008409 |

- CST_FLOX: 0 entries differ
### investment: 888 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| COMBATS01 | 0 | 10,588.6 | -10,588.6 |
| RSDBATS01 | 18,396.7 | 9,902.3 | 8,494.4 |
| TRA_Hdt_ELC_01 | 61,242.3 | 56,662.1 | 4,580.2 |
| TRA_Hdt_Dis_01 | 15,517.4 | 19,113.7 | -3,596.3 |
| SELCH2PEM01 | 983.7 | 2,349.5 | -1,365.7 |
| SELCH2EC01 | 983.8 | 135.6 | 848.1 |
| EUWINONM01 | 42,841.6 | 43,385.6 | -544.0 |
| TRA_Car_Dis_LoM_41 | 3,642.1 | 3,153.3 | 488.8 |
| TRA_Lcv_Dis_01 | 16,670.4 | 16,226.2 | 444.3 |
| TRA_Car_Gas_LoM_91 | 5,293.1 | 4,869.1 | 423.9 |
| TRA_Car_Gas_LoM_71 | 3,813.1 | 4,233.6 | -420.4 |
| TRA_Lcv_Elc_01 | 2,673.6 | 3,093.8 | -420.2 |

### fixed O&M: 733 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Hdt_ELC_01 | 8,828.6 | 8,168.3 | 660.3 |
| TRA_Hdt_Dis_01 | 2,460.7 | 3,031.0 | -570.3 |
| SELCH2PEM01 | 371.7 | 885.4 | -513.7 |
| P_COMBATS01 | 0 | 372.8 | -372.8 |
| SELCH2EC01 | 371.7 | 51.24 | 320.5 |
| P_RSDBATS01 | 694.5 | 397.7 | 296.8 |
| TRA_Car_Dis_LoM_41 | 827.8 | 716.7 | 111.1 |
| TRA_Lcv_Elc_01 | 566.4 | 666.0 | -99.62 |
| TRA_Car_Gas_LoM_91 | 1,203.0 | 1,106.7 | 96.35 |
| TRA_Lcv_Dis_01 | 3,604.8 | 3,508.7 | 96.06 |
| TRA_Car_Gas_LoM_71 | 866.7 | 962.2 | -95.56 |
| TRA_Car_Gas_Sma_91 | 384.9 | 476.4 | -91.51 |

### activity: 1376 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| SELCH2PEM01_LowAF | 25.23 | 60.75 | -35.52 |
| ICLADVPRO01 | 24.71 | 55.7 | -31 |
| ICLADVPRO05 | 160.0 | 129.2 | 30.76 |
| IISELAFUR01 | 1,458.8 | 1,428.5 | 30.33 |
| S_CCUS_EMIS_H2T | 380.7 | 408.7 | -27.93 |
| SELCH2EC01_LowAF | 25.23 | 3.418 | 21.81 |
| MINBIOCRP41 | 1,598.6 | 1,607.3 | -8.752 |
| EUIGCCWOO01 | 291.8 | 283.3 | 8.475 |
| S_CCUS_EMIS_H2T_LowAF | 109.9 | 117.6 | -7.787 |
| SBIOH2GCC01 | 171.7 | 178.2 | -6.535 |
| EUHYDLAKELC01 | 45.61 | 39.42 | 6.19 |
| EUWINONM01 | 449.5 | 455.5 | -5.96 |

### flow/import: 120 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IMPOILCRD | 61,778.7 | 57,840.3 | 3,938.4 |
| EXPOILGSL | -18,470.7 | -16,267.1 | -2,203.6 |
| IMPOILDST | 13,321.6 | 15,101.9 | -1,780.3 |
| EXPOILKER | -1,889.2 | -1,176.6 | -712.6 |
| IMPOILGSL | 4,055.1 | 4,570.2 | -515.0 |
| TRABAT_ChgStn | 10,940.2 | 10,525.0 | 415.2 |
| IMPELC-SEtoFI | 5,994.3 | 6,367.7 | -373.4 |
| IMPELC-EetoFI | 1,859.6 | 1,528.3 | 331.3 |
| EXPOILDST | -9,563.3 | -9,767.3 | 204.0 |
| IMPOILHFO | 5,238.1 | 5,397.2 | -159.0 |
| TRAELC00 | 4,252.9 | 4,101.9 | 151.0 |
| EXPCO2-fromFI-coastal | 5,005.5 | 5,133.4 | -127.9 |

### capacity (sum over years): 313 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| COMBATS01 | 0 | 356.8 | -356.8 |
| RSDBATS01 | 656.8 | 371.0 | 285.9 |
| R_ES-SH-FL_ELC01 | 12,637.0 | 12,484.1 | 152.9 |
| R_ES-SH-DH-70_ELC05 | 4,072.6 | 4,193.1 | -120.5 |
| R_ES-SH-FL_GAS01 | 635.0 | 749.8 | -114.8 |
| TRA_Car_Elc_Sma_10 | 7,898.1 | 8,012.9 | -114.7 |
| P_COMBATS01 | 0 | 89.2 | -89.2 |
| R_ES-SH-SD_GAS01 | 546.3 | 632.6 | -86.26 |
| P_RSDBATS01 | 164.2 | 92.74 | 71.47 |
| R_ES-SH-DH-70_ELC04 | 103.1 | 35.78 | 67.29 |
| R_ES-SH-FL_ELC05 | 205.5 | 261.9 | -56.39 |
| TRA_Car_Elc_Exe_10 | 14,466.1 | 14,414.0 | 52.08 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## L. Output without inputs
- Processes running with less than 20 % of their reference inputs per unit of activity: none

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
