# Audit of 5cfix2b.gdx vs 5bfix7.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,527,170.27 M EUR, reference 1,529,070.30, difference -1,900.02 (-0.1243%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 144,551.5 | 144,791.6 | -240.1 |
| INV | 918,318.9 | 919,524.3 | -1,205.4 |
| VAR | 464,299.8 | 464,754.4 | -454.6 |
| VARX | 0.04334 | 0.02769 | 0.01565 |

| region | objective share |
|---|---|
| FI | 996,393.1 |
| FI1B1 | 115,716.4 |
| FI196 | 53,428.3 |
| FI19B | 43,161.9 |
| FI1D9 | 42,775.3 |
| FI1C1 | 39,861.6 |
| FI198 | 26,078.3 |
| FI1C7 | 25,264.5 |
| FI1DB | 23,433.2 |
| FI1C5 | 22,930.9 |
| FI1D7 | 21,696.1 |
| FI19A | 20,908.3 |
| FI199 | 19,666.9 |
| FI1C6 | 17,335.9 |
| FI1C2 | 16,489.0 |
| FI1DC | 14,368.4 |
| FI1DA | 12,022.2 |
| FI1D5 | 6,289.2 |
| FI1D8 | 6,237.4 |
| FI200 | 3,113.5 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: conserved
- PRC_RESID national totals: conserved

## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| ECHP_biomass_thermal | 324.9 | 313.5 | 11.33 |
| ECHP_naturalgas_CCGT | 81.02 | 84.17 | -3.15 |
| EEPP_coal_thermal | 42.51 | 40.86 | 1.644 |
| ECHP_coal_thermal | 100.6 | 99.14 | 1.499 |
| EUHYDDAM00 | 1,371.8 | 1,372.7 | -0.8601 |
| ECHP_LFO_thermal | 0.4061 | 0 | 0.4061 |
| ECHP_lignite_thermal | 30.19 | 29.84 | 0.3512 |
| ECHP_HFO_thermal | 8.401 | 8.107 | 0.2944 |
| EEPP_biomass_thermal | 86.02 | 86.03 | -0.007911 |
| ECHP_naturalgas_thermal | 2.219 | 2.221 | -0.001319 |
| EEPP_naturalgas_thermal | 0.0636 | 0.06313 | 0.0004689 |
| EEPP_PV | 42.5 | 42.5 | -0.0001191 |
| EEPP_windON | 1,066.4 | 1,066.4 | -9.212e-05 |
| ENFI_OLKILUOTO-3 | 928.4 | 928.4 | 3.925e-05 |
| EEPP_LFO_thermal | 0.08295 | 0.08295 | -6.853e-06 |
| EEPP_windOFF | 23.59 | 23.59 | -1.895e-06 |
| ENFI_OLKILUOTO-2_00 | 102.9 | 102.9 | -9.05e-08 |
| ENFI_OLKILUOTO-1_00 | 86.09 | 86.09 | -8.63e-08 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | -7.932e-08 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | -5.563e-08 |
| EEPP_HFO_thermal | 2.141 | 2.141 | 8.428e-09 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 8.691e-10 |

By class and year: 31 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_biomass_thermal / 2033 | 3.783 | 0 | 3.783 |
| ECHP_biomass_thermal / 2038 | 3.782 | 0 | 3.782 |
| ECHP_biomass_thermal / 2035 | 3.773 | 0 | 3.773 |
| ECHP_naturalgas_CCGT / 2018 | 1.768 | 3.947 | -2.179 |
| ECHP_naturalgas_CCGT / 2020 | 1.767 | 3.944 | -2.177 |
| EEPP_coal_thermal / 2013 | 4.735 | 3.091 | 1.644 |
| ECHP_coal_thermal / 2020 | 15.43 | 14.25 | 1.174 |
| EUHYDDAM00 / 2033 | 55.03 | 54.22 | 0.8054 |
| EUHYDDAM00 / 2060 | 53.74 | 54.26 | -0.517 |
| EUHYDDAM00 / 2058 | 54.28 | 54.71 | -0.4376 |
| EUHYDDAM00 / 2030 | 53.86 | 54.28 | -0.4174 |
| ECHP_naturalgas_CCGT / 2015 | 28.61 | 28.2 | 0.4039 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,285.1 |
| FI198 | 76.88 |
| FI199 | 157.5 |
| FI19A | 262.6 |
| FI19B | 94.53 |
| FI1B1 | 253.9 |
| FI1C1 | 122.8 |
| FI1C2 | 51.4 |
| FI1C5 | 238.4 |
| FI1C6 | 30.41 |
| FI1C7 | 56.1 |
| FI1D5 | 165.3 |
| FI1D7 | 590.8 |
| FI1D8 | 92.7 |
| FI1D9 | 733.5 |
| FI1DA | 74.4 |
| FI1DB | 23.54 |
| FI1DC | 97.46 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 337.9 | 337.5 | 0.401 |
| 2013 | 294.7 | 292.7 | 2.082 |
| 2015 | 320.4 | 319.9 | 0.4846 |
| 2018 | 371.5 | 373.0 | -1.502 |
| 2020 | 314.8 | 315.7 | -0.8343 |
| 2023 | 379.5 | 381.7 | -2.183 |
| 2025 | 421.2 | 423.2 | -2.051 |
| 2028 | 475.0 | 478.7 | -3.745 |
| 2030 | 503.6 | 507.7 | -4.112 |
| 2033 | 443.8 | 442.6 | 1.23 |
| 2035 | 463.6 | 464.9 | -1.292 |
| 2038 | 520.1 | 522.2 | -2.117 |
| 2040 | 571.3 | 573.9 | -2.606 |
| 2043 | 623.4 | 623.7 | -0.2399 |
| 2045 | 644.9 | 643.8 | 1.064 |
| 2048 | 668.7 | 670.8 | -2.05 |
| 2050 | 707.1 | 707.3 | -0.148 |
| 2053 | 718.3 | 718.4 | -0.1168 |
| 2055 | 728.5 | 729.1 | -0.6225 |
| 2058 | 749.8 | 750.0 | -0.1672 |
| 2060 | 764.9 | 765.2 | -0.3309 |
| 2063 | 778.9 | 780.1 | -1.162 |
| 2065 | 789.0 | 789.7 | -0.6595 |
| 2068 | 805.7 | 805.9 | -0.2186 |
| 2070 | 817.2 | 817.3 | -0.1116 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 197.5 | 198.8 | -1.283 |
| 2013 | 180.9 | 179.9 | 1.014 |
| 2015 | 132.8 | 131.7 | 1.089 |
| 2018 | 132.8 | 133.5 | -0.6891 |
| 2020 | 148.6 | 148.3 | 0.2845 |
| 2023 | 134.1 | 134.8 | -0.6744 |
| 2025 | 120.4 | 122.5 | -2.088 |
| 2028 | 209.5 | 212.3 | -2.819 |
| 2030 | 229.3 | 232.2 | -2.884 |
| 2033 | 172.6 | 168.5 | 4.099 |
| 2035 | 180.4 | 177.4 | 3.088 |
| 2038 | 189.5 | 189.2 | 0.2861 |
| 2040 | 204.2 | 203.6 | 0.6433 |
| 2043 | 224.4 | 223.6 | 0.8181 |
| 2045 | 232.4 | 231.0 | 1.394 |
| 2048 | 237.3 | 234.7 | 2.601 |
| 2050 | 239.6 | 239.2 | 0.474 |
| 2053 | 239.1 | 238.1 | 1.011 |
| 2055 | 244.0 | 243.4 | 0.6363 |
| 2058 | 249.9 | 249.7 | 0.2342 |
| 2060 | 257.9 | 257.1 | 0.8105 |
| 2063 | 262.4 | 262.4 | 0.006511 |
| 2065 | 264.3 | 264.6 | -0.2811 |
| 2068 | 268.9 | 269.1 | -0.2764 |
| 2070 | 271.5 | 271.8 | -0.3035 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 4.689 | 4.69 |
| 2018 | 12.25 | 0.4136 |
| 2025 | 6.77 | 0.2293 |
| 2033 | 35.89 | 1.215 |
| 2040 | 50.01 | 1.693 |
| 2048 | 28.75 | 0.9732 |
| 2055 | 28.01 | 0.9252 |
| 2063 | 29.81 | 0.984 |
| 2070 | 29.21 | 0.9626 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 9.081 | 0.7159 |
| 2018 | 21.19 | 1.67 |
| 2025 | 195.7 | 15.42 |
| 2033 | 24.41 | 0.0002 |
| 2040 | 32.52 | 0.0002001 |
| 2048 | 15.76 | 0.0002 |
| 2055 | 16.48 | 0.0002001 |
| 2063 | 17.3 | 0.0002001 |
| 2070 | 17.07 | 0.0002003 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,103.3 | 0.09716 |
| ICMFISCO2 | 10,393.6 | 0 |
| ELCHIG | 4,415.7 | 0.0124 |
| INDELC | 30.52 | 4,091.4 |
| IPPHTH | 6.741 | 4,004.3 |
| OILCRD | 0.1073 | 3,898.1 |
| GreenCert-ELC | 3,368.7 | 2.123 |
| BIOOILFS | 0.3804 | 3,314.7 |
| BIOHVO | 2,860.7 | 0.3806 |
| ELCLOW | 30.11 | 2,774.0 |
| INDBLQ | 2,552.9 | 1.471 |
| OILDST | 1,570.3 | 523.0 |
| TRADST | 2.103 | 1,690.9 |
| HETHTH | 405.0 | 1,099.4 |
| OILGSL | 1,415.0 | 3.859 |
| ELCHYD | 1.951 | 1,374.0 |
| ELCWOO | 1.885 | 1,305.1 |
| ELCWIN | 3.07 | 1,094.8 |
| INDBIO | 259.7 | 611.1 |
| MPPWOO | 0.01266 | 772.5 |
| ELCNUC | 0.003976 | 751.8 |
| TRAGSLSP95 | 2.362 | 667.8 |
| ELCMED | 34.33 | 464.7 |
| ELCCOH | 0.09226 | 455.4 |
| INDHTH | 0.8005 | 446.8 |
| OILHFO | 255.0 | 165.2 |
| OILNEU | 0.5001 | 411.7 |
| INDCOK | 2.887 | 346.9 |
| INDLFO | 2.418 | 304.9 |
| INDCOA | 2.2 | 298.0 |
| INDGAS | 9.72 | 282.8 |
| OILNAP | 0.5003 | 290.3 |
| INDRFG | 0.5062 | 290.2 |
| INDHFO | 2.538 | 268.6 |
| IOIHTH | 15.96 | 234.4 |
| ELCGAS | 10.7 | 212.2 |
| SUPRPG | 0.1146 | 221.8 |
| OILKER | 203.1 | 3.865 |
| COALIG | 3.857 | 193.4 |
| OILLPG | 7.895 | 179.1 |
| BIOWOO | 2.477 | 165.4 |
| OILOTH | 36.8 | 121.7 |
| ELCCOL | 0.2621 | 150.7 |
| COACOK | 131.5 | 3.93 |
| ICHHTH | 3.789 | 126.2 |
| BIOGAS | 88.88 | 31.87 |
| MPPRYC | 0.014 | 118.2 |
| TRAGSLE85 | 2.403 | 110.1 |
| OILRFG | 62.66 | 37.42 |
| INDHH2 | 48.14 | 47.9 |
| ELCHIGG | 47.49 | 47.49 |
| TRALH2 | 47.49 | 47.49 |
| SYNH2CT | 49.89 | 42.44 |
| GASNAT | 12.9 | 76.81 |
| INFHTH | 24.53 | 45.09 |
| MISSNT | 0.02523 | 65.57 |
| MPPGYP | 0 | 63.92 |
| ELCSOL | 3.367 | 48.96 |
| SUPRPP | 0.1229 | 51.44 |
| INDLPG | 3.732 | 44.54 |
| GASCOG | 44.57 | 0.1253 |
| MISRIR | 38.28 | 0 |
| ICMPARA | 37.78 | 0.1183 |
| ELCHFO | 3.447 | 32.67 |
| GASP2GB | 14.47 | 19.53 |
| INMHTH | 16.24 | 17.13 |
| AGRGAS | 16.26 | 16.26 |
| GASP2G | 15.83 | 15.83 |
| MISOXY | 0 | 27.68 |
| TRAHFO | 27.01 | 0 |
| INDCOG | 0.1964 | 26.77 |
| COAHAR | 0.004764 | 22.72 |
| MISORE | 0 | 20.57 |
| MLMSTN | 0 | 20.19 |
| INDSLU | 3.825 | 16.22 |
| BIOMUN | 2.874 | 17.08 |
| BIOSLU | 2.878 | 16.93 |
| IIS | 18.48 | 0.05994 |
| SUPGAS | 0.5791 | 16.74 |
| MISBFS | 7.873 | 7.77 |
| BRFH2 | 0.3869 | 14.87 |
| MPPKAO | 0 | 14.53 |
| INDMUN | 2.754 | 10.21 |
| MISCST | 7.705 | 3.279 |
| GASBFG | 9.974 | 0.4163 |
| INDCOL | 3.006 | 6.847 |
| MISSCR | 0 | 9.287 |
| ELCDST | 3.487 | 5.711 |
| COABRO | 3.949 | 3.985 |
| OILDST-e | 3.944 | 3.976 |
| OILKER-e | 3.945 | 3.975 |
| COOFRE | 3.916 | 4 |
| OILGSL-e | 3.958 | 3.958 |
| GASGWG | 3.958 | 3.958 |
| TRAGSLSP95E10 | 3.848 | 3.848 |
| REFHTH | 0 | 7.503 |
| ETSCO2 | 3.618 | 3.621 |
| ELCCO2N | 0.001989 | 6.602 |
| MPPNOH | 0 | 5.747 |
| SUPBIO | 0.142 | 5.163 |
| IALHTH | 1.051 | 3.053 |
| MPPOXY | 0 | 3.284 |
| IGH | 1.722 | 0.02943 |
| IISHTH | 0.4581 | 1.165 |
| MALBAU | 0.1733 | 1.059 |
| MISPLT | 0.04417 | 1.151 |
| MGHRYC | 0 | 1.174 |
| BIOPROP | 0.4756 | 0.4 |
| ICMLC3 | 0.4166 | 0.4166 |
| INDBFG | 0.03513 | 0.6675 |
| RENGEO | 0 | 0.6914 |
| BRFCA3 | 0 | 0.6865 |
| INDCOB | 0.2709 | 0.4096 |
| SUPELC | 0 | 0.6405 |
| ICLHTH | 0.1773 | 0.4031 |
| ICUHTH | 0 | 0.4682 |
| MALSCR | 0 | 0.4547 |
| GASIIS | 0.2026 | 0.227 |
| GreenCert-FIN | 0.1972 | 0.2321 |
| OILFDS | 0.2042 | 0.2126 |
| GASCOP | 0.1873 | 0.1873 |
| MCUORE | 0 | 0.3679 |
| MISQLI | 0 | 0.2985 |
| ICU | 0.2011 | 0.03235 |
| SUPHTH | 0 | 0.1442 |
| RENSOL | 0 | 0.1223 |
| MCUSCR | 0.04813 | 0.04138 |
| MCUSCU | 0.04377 | 0.04483 |
| MISRFC | 0.04417 | 0.04417 |
| RENAHT | 0 | 0.008304 |
| RENGHT | 0 | 3.887e-05 |

- Back-and-forth on the same link, year and timeslice: 76966 cases, volume 542.4
| link / year / ts | min(imp, exp) |
|---|---|
| TB_MISCST_FI_FI1C5 / 2020 / ANNUAL | 0.2767 |
| TB_MISCST_FI_FI1D9 / 2020 / ANNUAL | 0.2304 |
| TB_MISCST_FI_FI1D7 / 2020 / ANNUAL | 0.2144 |
| TB_MISCST_FI_FI1C2 / 2020 / ANNUAL | 0.1423 |
| TB_INDBIO_FI_FI1C5 / 2070 / ANNUAL | 0.04199 |
| TB_ETSCO2_FI_FI1B1 / 2070 / ANNUAL | 0.04175 |
| TB_ETSCO2_FI_FI1D9 / 2070 / ANNUAL | 0.04175 |
| TB_ETSCO2_FI_FI1D7 / 2070 / ANNUAL | 0.04175 |
| TB_ETSCO2_FI_FI1C5 / 2070 / ANNUAL | 0.04175 |
| TB_ETSCO2_FI_FI1DA / 2070 / ANNUAL | 0.04175 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 131,950.7, reference 131,578.9 (+0.28%); 24 years differ >0.1 %
- ETSCO2: produced, all years: run 343,718.5, reference 343,312.2 (+0.12%); 18 years differ >0.1 %
- INDCO2N: produced, all years: run 123,462.7, reference 124,830.0 (-1.10%); 24 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,197.6, reference 11,166.3 (+0.28%); 19 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 6,047.9, reference 6,085.1 (-0.61%); 22 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'GreenCert-ELC': -4.6, 'ETSCO2': 182051.2, 'ELCCO2N': 73721.1} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 73 | 790.9 |
| FI / ELCHIGG | 300 | 80 | 33.59 |
| FI / ELCLOW | 300 | 45 | 112.7 |
| FI / ELCMED | 300 | 71 | 14.38 |
| FI / HETHTH | 300 | 0 | 0 |
| FI196 / ELCHIGG | 300 | 135 | 4,395.7 |
| FI196 / ELCLOW | 300 | 96 | 4,083.5 |
| FI196 / ELCMED | 300 | 165 | 6,958.9 |
| FI198 / ELCHIGG | 300 | 147 | 4,600.0 |
| FI198 / ELCLOW | 300 | 165 | 7,035.8 |
| FI198 / ELCMED | 300 | 179 | 5,427.7 |
| FI199 / ELCHIGG | 300 | 271 | 10,032.3 |
| FI199 / ELCLOW | 300 | 139 | 6,379.0 |
| FI199 / ELCMED | 300 | 175 | 7,733.2 |
| FI19A / ELCHIGG | 300 | 231 | 6,659.2 |
| FI19A / ELCLOW | 300 | 134 | 5,405.1 |
| FI19A / ELCMED | 300 | 127 | 6,682.7 |
| FI19B / ELCHIGG | 300 | 300 | 10,985.9 |
| FI19B / ELCLOW | 300 | 154 | 7,024.1 |
| FI19B / ELCMED | 300 | 69 | 3,138.0 |
| FI1B1 / ELCHIGG | 300 | 223 | 9,273.4 |
| FI1B1 / ELCLOW | 300 | 153 | 6,516.6 |
| FI1B1 / ELCMED | 300 | 203 | 9,053.8 |
| FI1C1 / ELCHIGG | 300 | 189 | 7,085.5 |
| FI1C1 / ELCLOW | 300 | 195 | 7,691.0 |
| FI1C1 / ELCMED | 300 | 193 | 7,395.9 |
| FI1C2 / ELCHIGG | 300 | 47 | 2,023.9 |
| FI1C2 / ELCLOW | 300 | 153 | 6,029.3 |
| FI1C2 / ELCMED | 300 | 155 | 5,568.5 |
| FI1C5 / ELCHIGG | 300 | 0 | 0 |
| FI1C5 / ELCLOW | 300 | 147 | 6,129.8 |
| FI1C5 / ELCMED | 300 | 135 | 2,661.2 |
| FI1C6 / ELCHIGG | 300 | 300 | 10,985.9 |
| FI1C6 / ELCLOW | 300 | 111 | 4,318.6 |
| FI1C6 / ELCMED | 300 | 163 | 6,118.8 |
| FI1C7 / ELCHIGG | 300 | 299 | 10,973.8 |
| FI1C7 / ELCLOW | 300 | 154 | 6,342.2 |
| FI1C7 / ELCMED | 300 | 278 | 10,405.2 |
| FI1D5 / ELCHIGG | 300 | 176 | 6,523.9 |
| FI1D5 / ELCLOW | 300 | 157 | 6,488.7 |
| FI1D5 / ELCMED | 300 | 156 | 5,521.1 |
| FI1D7 / ELCHIGG | 300 | 92 | 3,682.8 |
| FI1D7 / ELCLOW | 300 | 173 | 7,331.2 |
| FI1D7 / ELCMED | 300 | 116 | 3,307.7 |
| FI1D8 / ELCHIGG | 300 | 189 | 6,235.8 |
| FI1D8 / ELCLOW | 300 | 186 | 6,816.8 |
| FI1D8 / ELCMED | 300 | 64 | 2,538.7 |
| FI1D9 / ELCHIGG | 300 | 61 | 2,238.4 |
| FI1D9 / ELCLOW | 300 | 88 | 2,545.0 |
| FI1D9 / ELCMED | 300 | 237 | 9,220.8 |
| FI1DA / ELCHIGG | 300 | 17 | 398.9 |
| FI1DA / ELCLOW | 300 | 143 | 5,232.8 |
| FI1DA / ELCMED | 300 | 209 | 9,168.8 |
| FI1DB / ELCHIGG | 300 | 1 | 19.72 |
| FI1DB / ELCLOW | 300 | 152 | 5,925.6 |
| FI1DB / ELCMED | 300 | 88 | 3,083.7 |
| FI1DC / ELCHIGG | 300 | 85 | 1,538.9 |
| FI1DC / ELCLOW | 300 | 152 | 5,871.1 |
| FI1DC / ELCMED | 300 | 205 | 7,375.6 |
| FI200 / ELCHIGG | 300 | 214 | 7,829.0 |
| FI200 / ELCLOW | 300 | 176 | 7,128.8 |
| FI200 / ELCMED | 300 | 246 | 9,139.1 |

- Peak equations outside the hub: 57 region/commodity pairs (expected none in the hub design)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 316; only in run: 1; only in reference: 3
| binding only in run | sum |shadow| |
|---|---|
| RS_PRD_COMBIO_UP | 4.659e-06 |

| binding only in reference | sum |shadow| |
|---|---|
| RS_FLO_RSDHET00_HETHTH_UP | 30.03 |
| U_MAXTotalCUMCO2_2026_2028 | 2.793e-06 |
| UC_DecrCCSSUP | 1.235e-06 |

Shadow prices differing by more than 5 %: 116; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_CAP_EEPP_natgas_CCGT | 380,247.8 | 504,031.0 | -123,783.2 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 356,839.6 | 474,794.9 | -117,955.2 |
| UC_VARU_CAP_EEPP_naturalgas_th | 357,209.3 | 472,524.7 | -115,315.4 |
| UC_VARU_CAP_EEPP_HFO_th | 151,574.5 | 196,227.0 | -44,652.5 |
| UCI_UP_CHPShare-IAL | 93,354.0 | 129,910.3 | -36,556.3 |
| UC_COMBatt1_DischLimit | 32,980.2 | 127.2 | 32,853.1 |
| UCI_UP_CHPShare-ICL | 72,390.1 | 94,029.0 | -21,638.9 |
| UCI_UP_CHPShare-ICU | 42,328.8 | 54,667.4 | -12,338.6 |
| UC_COMBatt2_DischLimit | 7,869.2 | 127.2 | 7,742.0 |
| UC_VARU_CAP_EEPP_lignite_th | 12,258.7 | 15,885.4 | -3,626.6 |
| UC_VARU_CAP_EEPP_coal_th | 12,269.9 | 15,883.1 | -3,613.2 |
| UC_VARU_ACT_EEPP_lignite_th | 25,509.9 | 27,533.9 | -2,024.0 |
| UC_VARU_ACT_EUICBGS01 | 13,879.9 | 15,733.5 | -1,853.6 |
| UC_VARU_ACT_EEPP_coal_th | 17,602.2 | 18,903.3 | -1,301.1 |
| UC_R_SPLBoiler_DH_GAS | 3,827.4 | 4,955.6 | -1,128.2 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 396 entries differ
| key | run | reference | diff |
|---|---|---|---|
| FI / 2070 / IGFHTH | 0.001048 | 6.83e-05 | 0.0009801 |
| FI / 2070 / IAMHTH | 0.001048 | 7.545e-05 | 0.0009729 |
| FI / 2070 / ICMHTH | 0.001048 | 0.0001153 | 0.0009331 |
| FI / 2070 / IGHHTH | 0.001048 | 0.0002315 | 0.0008169 |
| FI1C5 / 2070 / MCMCLKBYF | 0.002076 | 0.001319 | 0.0007571 |
| FI1C1 / 2070 / MCMCLKBYF | 0.002075 | 0.001318 | 0.0007565 |
| FI1C5 / 2070 / MCMCLKCCSC | 0.002048 | 0.001302 | 0.0007457 |
| FI1C1 / 2070 / MCMCLKCCSC | 0.002045 | 0.0013 | 0.0007444 |
| FI1C5 / 2070 / MCMCLKLAPP | 0.001896 | 0.001202 | 0.0006937 |
| FI / 2070 / ILMHTH | 0.001048 | 0.0006505 | 0.0003979 |

- CST_FLOX: 0 entries differ
### investment: 882 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| EUWINOFH01 | 2,014.7 | 3,136.8 | -1,122.1 |
| TRA_Car_PIH_LoM_20pct | 28,270.6 | 29,379.9 | -1,109.3 |
| TRA_Car_Elc_LoM_10 | 6,854.3 | 5,857.1 | 997.2 |
| EUWINONM01 | 43,624.7 | 43,294.4 | 330.3 |
| EUIGCCWOO01 | 13,077.1 | 13,330.3 | -253.1 |
| EUCCGASCCSpos20 | 6,639.6 | 6,466.4 | 173.2 |
| CHPINDSPWOO101 | 208.2 | 43.77 | 164.4 |
| TRA_Car_PIH_UpM_20pct | 18,330.1 | 18,190.1 | 140.0 |
| TRA_Car_Gas_LoM_71 | 4,509.0 | 4,413.7 | 95.34 |
| EUPVSOLL101 | 4,289.9 | 4,200.4 | 89.43 |
| R_ES-SH-DH-70_ELC05 | 6,530.2 | 6,618.7 | -88.5 |
| TRA_Car_Dis_LoM_41 | 3,081.2 | 3,167.2 | -86.03 |

### fixed O&M: 728 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Car_PIH_LoM_20pct | 6,546.6 | 6,799.4 | -252.8 |
| TRA_Car_Elc_LoM_10 | 1,188.1 | 968.7 | 219.4 |
| EUWINOFH01 | 286.8 | 447.9 | -161.1 |
| CHPINDSPWOO101 | 74.86 | 15.74 | 59.12 |
| R_ES-SH-FL_GAS01 | 78.76 | 130.3 | -51.54 |
| EUWINONM01 | 6,105.5 | 6,059.4 | 46.13 |
| IOISTMBIO01 | 432.9 | 476.7 | -43.8 |
| EUCCGASCCSpos20 | 1,226.8 | 1,194.8 | 31.98 |
| TRA_Car_PIH_UpM_20pct | 4,232.5 | 4,201.0 | 31.47 |
| ICLADVPRO05 | 130.2 | 159.1 | -28.83 |
| ICLADVPRO01 | 53.71 | 25.11 | 28.6 |
| SBIOH2GCC01 | 2,181.9 | 2,209.3 | -27.44 |

### activity: 1379 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| ICLADVPRO05 | 129.3 | 159.2 | -29.86 |
| ICLADVPRO01 | 55.17 | 25.5 | 29.68 |
| ECHP_biomass_thermal | 481.8 | 465.2 | 16.63 |
| EUWINOFH01 | 20.99 | 32.52 | -11.53 |
| IPPPUPCHE01 | 2,938.5 | 2,929.2 | 9.393 |
| EUCCGASCCSpos20 | 195.3 | 189.4 | 5.905 |
| EUIGCCWOO01 | 287.6 | 292.9 | -5.215 |
| EUWINONM01 | 458.0 | 454.5 | 3.535 |
| EUCCGTGAS15 | 110.0 | 113.3 | -3.32 |
| ECHP_naturalgas_CCGT | 71.37 | 74.03 | -2.662 |
| EEPP_coal_thermal | 65.35 | 62.86 | 2.494 |
| IISSINTERBIO | 357.9 | 360.3 | -2.441 |

### flow/import: 125 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IMPOILCRD | 58,687.9 | 57,974.6 | 713.3 |
| EXPOILGSL | -17,405.8 | -16,733.0 | -672.8 |
| EXPOILDST | -10,110.2 | -9,920.4 | -189.8 |
| MINMPPWOO1 | 115,574.0 | 115,386.7 | 187.3 |
| IMPGAS_RU_PIP | 21,853.5 | 21,979.3 | -125.9 |
| EXPOILHFO | -1,909.1 | -1,848.9 | -60.14 |
| MINMPPRYC1 | 17,730.1 | 17,787.9 | -57.87 |
| IMPELC-SEtoFI | 6,073.6 | 6,015.9 | 57.71 |
| IMPOILDST | 15,323.6 | 15,269.4 | 54.21 |
| IMPOILKER | 3,535.5 | 3,586.0 | -50.47 |
| IMPOILGSL | 4,828.0 | 4,780.6 | 47.45 |
| IMPOILHFO | 5,351.9 | 5,398.0 | -46.05 |

### capacity (sum over years): 299 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| TRA_Car_PIH_LoM_20pct | 11,064.9 | 11,485.6 | -420.7 |
| TRA_Car_Elc_LoM_10 | 1,906.2 | 1,548.3 | 357.9 |
| R_ES-SH-FL_GAS01 | 358.0 | 592.3 | -234.3 |
| R_ES-SH-FL_ELC01 | 12,911.1 | 12,678.8 | 232.3 |
| R_ES-SH-SD_ELC01 | 2,076.1 | 2,131.2 | -55.06 |
| R_ES-SH-DH-70_ELC05 | 3,976.6 | 4,030.3 | -53.7 |
| TRA_Car_PIH_UpM_20pct | 7,132.6 | 7,081.0 | 51.63 |
| R_ES-SH-SD_GAS01 | 590.4 | 550.4 | 40.04 |
| R_ES-SH-SD_HET01 | 7,790.6 | 7,753.9 | 36.65 |
| R_ES-SH-SD_ELC05 | 3,380.5 | 3,347.0 | 33.51 |
| R_ES-SH-DH-70_GAS01 | 825.7 | 796.0 | 29.62 |
| R_ES-SH-DH-70_ELC04 | 129.5 | 102.3 | 27.18 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: none

## L. Output without inputs
- Processes running with less than 20 % of their reference inputs per unit of activity: none

## Verdict
Hard checks pass (dummy imports, inputs conserved, regional emissions sent to the hub, coal phase-out).
