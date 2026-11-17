# Audit of reg_baseline-sami_2026-11-17_task4b.gdx vs single_baseline-sami_2026-11-16.gdx

Regions in run: 20 (FI, FI196, FI198, FI199, FI19A, FI19B, FI1B1, FI1C1, FI1C2, FI1C5, FI1C6, FI1C7, FI1D5, FI1D7, FI1D8, FI1D9, FI1DA, FI1DB, FI1DC, FI200)

## A. Objective
Run 1,349,705.25 M EUR, reference 1,529,919.88, difference -180,214.63 (-11.7794%)

| component | run | reference | difference |
|---|---|---|---|
| ELS | 0 | 0 | 0 |
| FIX | 136,446.9 | 144,742.3 | -8,295.4 |
| INV | 892,570.4 | 919,897.7 | -27,327.3 |
| VAR | 320,687.9 | 465,279.9 | -144,592.0 |

| region | objective share |
|---|---|
| FI | 1,255,947.6 |
| FI196 | 29,320.6 |
| FI1B1 | 15,356.2 |
| FI1D9 | 11,351.5 |
| FI1C5 | 8,203.2 |
| FI1C7 | 6,636.0 |
| FI19B | 4,030.5 |
| FI1D7 | 3,975.9 |
| FI19A | 3,951.9 |
| FI198 | 3,655.7 |
| FI1DB | 2,339.0 |
| FI1C2 | 1,126.0 |
| FI1C6 | 961.2 |
| FI1C1 | 960.9 |
| FI1DC | 825.6 |
| FI1DA | 455.9 |
| FI199 | 283.4 |
| FI1D5 | 263.7 |
| FI1D8 | 53.31 |
| FI200 | 7.081 |

## B. Hard checks
- Dummy import activity: none
- COM_PROJ national totals: conserved
- NCAP_PASTI national totals: 7 keys differ
| key | run | reference | diff |
|---|---|---|---|
| IPPPRCBIO00 | 0 | 6.281 | -6.281 |
| IPPPUPCHE00 | 0 | 4.965 | -4.965 |
| IPPPRCHFO00 | 0 | 2.692 | -2.692 |
| INDIPPHTH00 | 0 | 2.532 | -2.532 |
| IPPPUPMEC00 | 0 | 0.4965 | -0.4965 |
| CHPAUTOGENBLQ00 | 0 | 0.0978 | -0.0978 |
| IPPPUPRYC00 | 0 | 0.05517 | -0.05517 |

- PRC_RESID national totals: 84 keys differ
| key | run | reference | diff |
|---|---|---|---|
| IPPPRCBIO00 / 2010 | 0 | 12 | -12 |
| IPPPRCBIO00 / 2013 | 0 | 10.8 | -10.8 |
| IPPPRCBIO00 / 2015 | 0 | 10 | -10 |
| IPPPUPCHE00 / 2010 | 0 | 9.488 | -9.488 |
| IPPPRCBIO00 / 2018 | 0 | 8.801 | -8.801 |
| IPPPUPCHE00 / 2013 | 0 | 8.539 | -8.539 |
| IPPPRCBIO00 / 2020 | 0 | 8.001 | -8.001 |
| IPPPUPCHE00 / 2015 | 0 | 7.907 | -7.907 |
| IPPPUPCHE00 / 2018 | 0 | 6.958 | -6.958 |
| IPPPRCBIO00 / 2023 | 0 | 6.801 | -6.801 |
| IPPPUPCHE00 / 2020 | 0 | 6.325 | -6.325 |
| IPPPRCBIO00 / 2025 | 0 | 6.001 | -6.001 |
| IPPPUPCHE00 / 2023 | 0 | 5.377 | -5.377 |
| IPPPRCHFO00 / 2010 | 0 | 5.144 | -5.144 |
| IPPPRCBIO00 / 2028 | 0 | 4.801 | -4.801 |


## C. Existing power/CHP plants moved to the regions (activity, PJ)
- Activity of these classes left on the FI hub: none
| class | run (all years) | reference | difference |
|---|---|---|---|
| ECHP_naturalgas_CCGT | 4.175 | 84.67 | -80.5 |
| ECHP_biomass_thermal | 373.3 | 313.6 | 59.71 |
| ECHP_coal_thermal | 106.4 | 97.15 | 9.235 |
| ENFI_OLKILUOTO-3 | 920.0 | 928.4 | -8.4 |
| EUHYDDAM00 | 1,373.3 | 1,380.6 | -7.351 |
| ENFI_OLKILUOTO-2_00 | 95.83 | 102.9 | -7.119 |
| EEPP_HFO_thermal | 6.343 | 2.141 | 4.203 |
| EEPP_PV | 42.52 | 45.46 | -2.942 |
| EEPP_coal_thermal | 37.77 | 40.22 | -2.445 |
| EEPP_windON | 1,066.4 | 1,068.0 | -1.636 |
| ECHP_HFO_thermal | 7.173 | 8.341 | -1.168 |
| ENFI_OLKILUOTO-1_00 | 85.6 | 86.09 | -0.4897 |
| EEPP_biomass_thermal | 86.04 | 86.31 | -0.2709 |
| EEPP_naturalgas_thermal | 0.06909 | 0.09998 | -0.03089 |
| ECHP_LFO_thermal | 0.01304 | 0.02023 | -0.007191 |
| EEPP_windOFF | 23.58 | 23.59 | -0.003647 |
| ECHP_naturalgas_thermal | 2.227 | 2.229 | -0.002229 |
| ECHP_naturalgas_OCGT | 0 | 0.001022 | -0.001022 |
| ECHP_lignite_thermal | 29.84 | 29.84 | -0.0008848 |
| EEPP_LFO_thermal | 0.08297 | 0.08335 | -0.0003801 |
| EEPP_lignite_thermal | 8.505 | 8.505 | 8.882e-15 |
| ENFI_LOVIISA-2_00 | 58.02 | 58.02 | 0 |
| ENFI_LOVIISA-1_00 | 43.52 | 43.52 | 0 |

By class and year: 81 differ by more than 0.1 %; largest:

| class / year | run | reference | diff |
|---|---|---|---|
| ECHP_naturalgas_CCGT / 2015 | 4.175 | 28.22 | -24.05 |
| ECHP_naturalgas_CCGT / 2013 | 0 | 24.04 | -24.04 |
| ECHP_naturalgas_CCGT / 2010 | 0 | 24.04 | -24.04 |
| ECHP_biomass_thermal / 2035 | 21.81 | 0 | 21.81 |
| ECHP_biomass_thermal / 2033 | 21.81 | 0 | 21.81 |
| ECHP_coal_thermal / 2020 | 25.41 | 12.65 | 12.76 |
| ECHP_biomass_thermal / 2038 | 12.12 | 0 | 12.12 |
| ENFI_OLKILUOTO-3 / 2025 | 38.02 | 46.42 | -8.4 |
| ENFI_OLKILUOTO-2_00 / 2010 | 18.62 | 25.74 | -7.119 |
| ECHP_naturalgas_CCGT / 2020 | 0 | 4.179 | -4.179 |
| ECHP_naturalgas_CCGT / 2018 | 0 | 4.179 | -4.179 |
| ECHP_biomass_thermal / 2040 | 4.033 | 0 | 4.033 |

| region | activity of moved classes (all years) |
|---|---|
| FI196 | 1,265.5 |
| FI198 | 77.14 |
| FI199 | 157.3 |
| FI19A | 269.9 |
| FI19B | 77.99 |
| FI1B1 | 217.2 |
| FI1C1 | 127.0 |
| FI1C2 | 53.08 |
| FI1C5 | 246.6 |
| FI1C6 | 26.93 |
| FI1C7 | 55.69 |
| FI1D5 | 167.9 |
| FI1D7 | 592.1 |
| FI1D8 | 92.31 |
| FI1D9 | 736.5 |
| FI1DA | 83.03 |
| FI1DB | 23.55 |
| FI1DC | 97.96 |
| FI200 | 2.93 |

## D. Electricity and heat production (excluding internal links)
### ELCHIG production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 305.9 | 337.6 | -31.69 |
| 2013 | 266.7 | 292.1 | -25.34 |
| 2015 | 292.7 | 320.1 | -27.41 |
| 2018 | 326.0 | 373.1 | -47.1 |
| 2020 | 319.1 | 314.9 | 4.291 |
| 2023 | 361.1 | 380.3 | -19.19 |
| 2025 | 409.6 | 423.2 | -13.68 |
| 2028 | 466.6 | 478.3 | -11.63 |
| 2030 | 495.0 | 507.3 | -12.25 |
| 2033 | 469.7 | 442.2 | 27.51 |
| 2035 | 496.8 | 464.2 | 32.6 |
| 2038 | 545.4 | 521.6 | 23.85 |
| 2040 | 596.7 | 573.8 | 22.96 |
| 2043 | 634.3 | 623.9 | 10.39 |
| 2045 | 657.7 | 644.7 | 13 |
| 2048 | 673.5 | 670.5 | 3.025 |
| 2050 | 724.2 | 708.1 | 16.11 |
| 2053 | 735.3 | 719.1 | 16.24 |
| 2055 | 740.9 | 727.8 | 13.11 |
| 2058 | 758.0 | 749.1 | 8.858 |
| 2060 | 778.3 | 763.8 | 14.5 |
| 2063 | 795.0 | 779.1 | 15.99 |
| 2065 | 804.0 | 788.8 | 15.24 |
| 2068 | 821.6 | 805.1 | 16.46 |
| 2070 | 835.6 | 816.6 | 19 |

### HETHTH production by year (PJ)
| year | run | reference | diff |
|---|---|---|---|
| 2010 | 167.4 | 200.0 | -32.57 |
| 2013 | 149.2 | 179.3 | -30.1 |
| 2015 | 118.3 | 131.1 | -12.83 |
| 2018 | 123.7 | 132.5 | -8.796 |
| 2020 | 130.7 | 145.3 | -14.69 |
| 2023 | 134.2 | 134.0 | 0.2134 |
| 2025 | 118.1 | 124.4 | -6.254 |
| 2028 | 216.1 | 212.8 | 3.281 |
| 2030 | 224.9 | 230.4 | -5.521 |
| 2033 | 224.8 | 168.8 | 55.95 |
| 2035 | 233.1 | 177.8 | 55.29 |
| 2038 | 248.8 | 190.0 | 58.8 |
| 2040 | 263.0 | 204.3 | 58.76 |
| 2043 | 270.0 | 224.7 | 45.35 |
| 2045 | 274.3 | 229.2 | 45.13 |
| 2048 | 278.1 | 235.1 | 42.99 |
| 2050 | 278.9 | 239.0 | 39.95 |
| 2053 | 277.6 | 238.4 | 39.15 |
| 2055 | 279.7 | 242.9 | 36.9 |
| 2058 | 280.6 | 249.0 | 31.6 |
| 2060 | 257.0 | 257.1 | -0.101 |
| 2063 | 262.3 | 262.1 | 0.1707 |
| 2065 | 262.5 | 263.8 | -1.372 |
| 2068 | 265.5 | 268.4 | -2.915 |
| 2070 | 268.4 | 271.1 | -2.631 |

### ELCHIG price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 1.813 | 0.05831 |
| 2018 | 8.266 | 0.2799 |
| 2025 | 2.274 | 0.07714 |
| 2033 | 35.05 | 1.186 |
| 2040 | 56.87 | 1.925 |
| 2048 | 27.45 | 0.929 |
| 2055 | 28.05 | 0.9494 |
| 2063 | 30.66 | 1.038 |
| 2070 | 31.37 | 1.062 |

### HETHTH price (PAR_COMBALEM, mean over timeslices): hub vs largest regional deviation
| year | FI hub | max |region - hub| |
|---|---|---|
| 2010 | 0.139 | 0.01116 |
| 2018 | 13.22 | 1.042 |
| 2025 | 206.8 | 16.3 |
| 2033 | 26.97 | 2.126 |
| 2040 | 40.45 | 3.188 |
| 2048 | 14.31 | 1.068 |
| 2055 | 16.17 | 1.071 |
| 2063 | 14.98 | 0.9953 |
| 2070 | 15.31 | 0.406 |

## E. Internal links (TB_*)
| commodity | into hub (IMP at FI) | out of hub (EXP at FI) |
|---|---|---|
| INDSCO2N | 29,170.5 | 0 |
| ELCHIG | 4,375.8 | 0 |
| OILCRD | 0 | 4,172.3 |
| GreenCert-ELC | 3,479.6 | 0 |
| BIOOILFS | 0 | 2,410.4 |
| IPPHTH | 0 | 2,254.7 |
| BIOHVO | 2,080.2 | 0 |
| OILDST | 1,692.7 | 0 |
| OILGSL | 1,521.9 | 0 |
| ELCWOO | 0 | 1,459.2 |
| INDELC | 0 | 1,420.8 |
| ELCHYD | 0 | 1,373.4 |
| ELCWIN | 0 | 1,091.6 |
| HETHTH | 812.5 | 53.06 |
| ELCNUC | 0 | 740.6 |
| ELCCOH | 0 | 463.9 |
| INDBIO | 65.28 | 292.0 |
| OILHFO | 343.5 | 4.3 |
| INDCOK | 0 | 344.6 |
| INDRFG | 0 | 289.6 |
| INDCOA | 0 | 277.3 |
| OILKER | 244.3 | 0 |
| SUPRPG | 0 | 237.3 |
| MPPRYC | 0 | 233.3 |
| COALIG | 0 | 205.5 |
| ELCCOL | 0 | 149.0 |
| COACOK | 140.0 | 0 |
| OILRFG | 115.3 | 0 |
| INDBLQ | 102.4 | 0 |
| OILOTH | 96.82 | 0 |
| INDHFO | 0 | 87.94 |
| BIOGAS | 86.16 | 0 |
| INDHTH | 0 | 80.33 |
| GASBFG | 79.11 | 0 |
| MPPWOO | 0 | 68.5 |
| MPPGYP | 0 | 63.92 |
| MISSNT | 0 | 62.39 |
| OILNAP | 60.24 | 0 |
| OILLPG | 57.87 | 0 |
| SUPRPP | 0 | 54.88 |
| GASCOG | 48.19 | 0 |
| ELCSOL | 0 | 45.51 |
| ELCHFO | 0 | 37.89 |
| MISRIR | 37.77 | 0 |
| MISOXY | 0 | 27.27 |
| INDGAS | 0 | 26.64 |
| ICHHTH | 0 | 25.06 |
| MISORE | 0 | 22.86 |
| MISCST | 15.41 | 5.795 |
| MLMSTN | 0 | 20.16 |
| INDCOG | 0 | 17.67 |
| SUPGAS | 0 | 17.52 |
| ICLHTH | 7.808 | 7.808 |
| OILNEU | 14.83 | 0 |
| ELCGAS | 0 | 14.78 |
| MPPKAO | 0 | 14.53 |
| INDLPG | 0 | 12.61 |
| IIS | 11.73 | 0 |
| BRFH2 | 0 | 10.53 |
| REFHTH | 0 | 8.032 |
| MISSCR | 0 | 7.732 |
| MISBFS | 6.921 | 0 |
| SUPBIO | 0 | 5.375 |
| MISPLT | 1.037 | 1.625 |
| INDLFO | 0 | 1.634 |
| IGH | 1.61 | 0 |
| MGHRYC | 0 | 1.088 |
| INDHH2 | 0 | 0.9281 |
| INDBFG | 0 | 0.6906 |
| IISHTH | 0 | 0.5496 |
| MPPNOH | 0 | 0.5207 |
| BRFCA3 | 0 | 0.4992 |
| ICUHTH | 0 | 0.4682 |
| SUPELC | 0 | 0.4658 |
| ELCDST | 0 | 0.3796 |
| MCUORE | 0 | 0.3679 |
| MPPOXY | 0 | 0.2976 |
| MISQLI | 0 | 0.2901 |
| ICU | 0.1455 | 0 |
| SUPHTH | 0 | 0.1048 |
| MCUSCU | 0.01932 | 0.001058 |
| MCUSCR | 0.005822 | 0 |

- Back-and-forth on the same link, year and timeslice: 11 cases, volume 64.7
| link / year / ts | min(imp, exp) |
|---|---|
| TB_HETHTH_FI_FI1DC / 2010 / SP | 22.15 |
| TB_HETHTH_FI_FI1DC / 2010 / FP | 10.3 |
| TB_HETHTH_FI_FI1DC / 2013 / FP | 10.15 |
| TB_HETHTH_FI_FI1DC / 2013 / SP | 7.319 |
| TB_ICLHTH_FI_FI1B1 / 2030 / R | 4.011 |
| TB_ICLHTH_FI_FI1B1 / 2028 / R | 3.263 |
| TB_HETHTH_FI_FI1DC / 2010 / RP | 3.135 |
| TB_MISCST_FI_FI1D7 / 2015 / ANNUAL | 2.51 |
| TB_MISCST_FI_FI1D7 / 2018 / ANNUAL | 1.021 |
| TB_ICLHTH_FI_FI1B1 / 2033 / R | 0.5342 |

## F. Emissions and certificates
- ELCCO2N: produced, all years: run 120,509.2, reference 130,244.3 (-7.47%); 25 years differ >0.1 %
- ETSCO2: produced, all years: run 338,185.9, reference 343,808.2 (-1.64%); 23 years differ >0.1 %
- INDCO2N: produced, all years: run 133,275.0, reference 126,331.9 (+5.50%); 25 years differ >0.1 %
- GreenCert-ELC: produced, all years: run 11,022.3, reference 11,202.8 (-1.61%); 25 years differ >0.1 %
- GreenCert-FIN: produced, all years: run 3,003.3, reference 6,065.4 (-50.48%); 25 years differ >0.1 %
- Counted in the region where emitted (production - net export to the hub), all years: {'GreenCert-ELC': -4.5, 'ETSCO2': 154531.7, 'ELCCO2N': 64468.8} (regional COM_BNDNET makes the net free; correct as long as the national targets sum the regions, checked next)
- CO2TargetAllSectors2030FI: terms in 20 regions
- CO2TargetESR2030: terms in 20 regions
- cementCO2: terms in 20 regions

## G. Peak equations (EQ_PEAK)
| region / commodity | equations | binding | sum |shadow price| |
|---|---|---|---|
| FI / ELCForPeak | 300 | 0 | 0 |
| FI / ELCHIG | 300 | 0 | 0 |
| FI / ELCHIGG | 300 | 6 | 8.929 |
| FI / ELCLOW | 300 | 1 | 102.0 |
| FI / ELCMED | 300 | 5 | 19.1 |
| FI / HETHTH | 300 | 0 | 0 |

- Peak equations outside the hub: 0 region/commodity pairs (none, as intended)

## H. 2030 coal phase-out
- Capacity of coal/peat classes from 2030: none

## I. User constraints: shadow prices
- Binding in both: 259; only in run: 22; only in reference: 27
| binding only in run | sum |shadow| |
|---|---|
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 7,755.2 |
| RS_PRD_RSDFINOIL_LO | 2,277.5 |
| RS_PRD_COMFINOIL_LO | 2,270.9 |
| RS_PRD_RSDBIO_LO | 1,607.6 |
| RS_PRD_COMBIO_LO | 1,561.4 |
| TUC_MinShareofCenELCinINDELC | 1,475.2 |
| UC_VARU_CAP_S_CCUS_P2GU | 957.1 |
| RS_PRD_RSDHET_LO | 560.7 |
| RS_PRD_COMGAS_LO | 347.2 |
| RS_PRD_RSDGAS_LO | 328.8 |
| RS_ACT_EEHP_DistHeating_LO | 206.3 |
| RS_PRD_INDFINGAS_LO | 99.85 |
| RS_PRD_COMHET_LO | 78.03 |
| RS_FLO_RSDHET00_HETHTH_UP | 42.24 |
| RS_ACT_SSCDCOKE00_LO | 27.44 |

| binding only in reference | sum |shadow| |
|---|---|
| TUC_Istruc_PUP-MEC | 17,406.1 |
| TUC_Istruc_RIR-CYC | 10,699.4 |
| TUC_Istruc_PUP-CHE | 6,882.4 |
| TUC_Istruc_PUP-RYC | 3,025.1 |
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

Shadow prices differing by more than 5 %: 257; largest:

| UC | run | reference | diff |
|---|---|---|---|
| UC_VARU_ACT_EEPP_natgas_OCGT | 247,715.9 | 8,790.4 | 238,925.5 |
| UC_VARU_ACT_EEPP_natgas_CCGT | 167,011.1 | 6,902.7 | 160,108.4 |
| UC_VARU_ACT_EEPP_naturalgas_th | 138,311.7 | 8,719.1 | 129,592.6 |
| UC_HydroLakeSupply_CE | 113,429.1 | 35,734.3 | 77,694.8 |
| UC_VARU_ACT_EEPP_HFO_th | 70,907.2 | 10,729.6 | 60,177.6 |
| UC_VARU_CAP_EEPP_naturalgas_th | 37,003.3 | 2,436.8 | 34,566.5 |
| UC_VARU_ACT_EEPP_coal_th | 32,636.8 | 8,298.6 | 24,338.2 |
| UC_VARU_CAP_EEPP_natgas_CCGT | 21,350.0 | 1,318.7 | 20,031.3 |
| TUC_Istruc_PUP-MEC | 0 | 17,406.1 | -17,406.1 |
| UC_ACAES-STG_DischLimit | 16,550.5 | 1,094.8 | 15,455.7 |
| UC_DCAES-STG_DischLimit | 12,782.6 | 922.5 | 11,860.2 |
| UC_VARU_ACT_EEPP_lignite_th | 19,908.7 | 8,299.1 | 11,609.6 |
| TUC_Istruc_RIR-CYC | 0 | 10,699.4 | -10,699.4 |
| UC_VARU_CAP_EEPP_natgas_OCGT | 10,868.8 | 1,269.5 | 9,599.4 |
| RS_NCAP_ENFI_OLKILUOTO-3_FX | 7,755.2 | 0 | 7,755.2 |

## J. Taxes/penalties and largest differences by process
- CST_COMX: 0 entries differ
- CST_FLOX: 0 entries differ
### investment: 262 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IPPPUPCHE01 | 0 | 18,566.1 | -18,566.1 |
| COMBATS01 | 3,531.1 | 10,588.6 | -7,057.5 |
| IPPPUPRYC01 | 0 | 6,927.5 | -6,927.5 |
| RSDBATS01 | 16,798.3 | 9,902.3 | 6,896.0 |
| EUCCGASCCSpos20 | 12,199.5 | 6,799.3 | 5,400.2 |
| EUIGCCWOO01 | 9,145.3 | 12,884.8 | -3,739.5 |
| EUWINOFH01 | 267.7 | 2,948.8 | -2,681.2 |
| R_ES-SH-DH_ELC05 | 1,151.8 | 2,896.3 | -1,744.5 |
| EUWINONM01 | 44,891.8 | 43,385.6 | 1,506.2 |
| INDIPPBLQHTH06 | 444.7 | 1,665.9 | -1,221.2 |
| CHPIPCSREBLQ015 | 0 | 1,054.2 | -1,054.2 |
| IPPLOWQUA01 | 31,749.4 | 30,771.8 | 977.5 |

### fixed O&M: 239 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IPPPUPCHE01 | 0 | 4,394.8 | -4,394.8 |
| IPPPUPRYC01 | 0 | 2,606.2 | -2,606.2 |
| EUCCGASCCSpos20 | 2,250.1 | 1,256.3 | 993.8 |
| HHTHGEO001 | 1,573.9 | 2,197.7 | -623.8 |
| INDIPPBLQHTH06 | 157.9 | 591.7 | -433.8 |
| IPPLOWQUA01 | 12,322.1 | 11,897.1 | 425.0 |
| EUWINOFH01 | 36.03 | 420.9 | -384.9 |
| IPPPUPMEC15 | 0 | 380.3 | -380.3 |
| IOISTMBIO01 | 93.75 | 474.0 | -380.2 |
| IISELAFUR01 | 3,852.8 | 3,496.4 | 356.3 |
| IPPPRCBIO01 | 0 | 346.7 | -346.7 |
| EUCCGTGAS15 | 943.8 | 1,281.9 | -338.2 |

### activity: 560 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| IPPPUPCHE01 | 0 | 2,934.4 | -2,934.4 |
| IGHRECYCL10 | 0 | 543.2 | -543.2 |
| IGHRECYCL05 | 460.5 | 118.8 | 341.7 |
| INDIPPBLQHTH06 | 13.03 | 312.8 | -299.7 |
| IMPBIOEMHV | 105.7 | 308.2 | -202.6 |
| HHTHGEO001 | 496.3 | 693.1 | -196.7 |
| EUCCGASCCSpos20 | 340.9 | 199.6 | 141.3 |
| ICLADVPRO05 | 0 | 129.2 | -129.2 |
| ICLADVPRO01 | 183.1 | 55.7 | 127.4 |
| IISELAFUR01 | 1,519.9 | 1,428.5 | 91.47 |
| EUIGCCWOO01 | 194.8 | 283.3 | -88.5 |
| ECHP_biomass_thermal | 552.8 | 465.2 | 87.6 |

### flow/import: 74 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| MINMPPWOO1 | 10,758.1 | 115,521.8 | -104,763.8 |
| MINMPPRYC1 | 34,994.0 | 17,755.0 | 17,239.1 |
| IMPOILCRD | 62,085.0 | 57,840.3 | 4,244.6 |
| EXPOILGSL | -20,204.8 | -16,267.1 | -3,937.6 |
| IMPGAS_RU_PIP | 18,884.6 | 21,987.4 | -3,102.8 |
| EXPELC-fromFI | -3,374.5 | -1,343.3 | -2,031.2 |
| EXPOILDST | -11,176.8 | -9,767.3 | -1,409.5 |
| EXPOILKER | -2,256.7 | -1,176.6 | -1,080.1 |
| IMPELC-SEtoFI | 7,325.3 | 6,367.7 | 957.6 |
| IMPOILGSL | 5,401.8 | 4,570.2 | 831.7 |
| IMPBIOOIL | 6,849.2 | 7,380.1 | -531.0 |
| IMPOILHFO | 4,978.8 | 5,397.2 | -418.4 |

### capacity (sum over years): 79 processes differ; largest
| process | run | reference | diff |
|---|---|---|---|
| R_ES-SH-DH_ELC01 | 1,933.6 | 889.1 | 1,044.4 |
| R_ES-SH-DH_ELC05 | 641.1 | 1,601.4 | -960.4 |
| R_ES-SH-FL_GAS01 | 0 | 749.8 | -749.8 |
| R_ES-SH-FL_ELC01 | 13,193.2 | 12,484.1 | 709.2 |
| R_ES-SH-SD_ELC05 | 2,727.4 | 3,320.2 | -592.8 |
| R_ES-SH-FL_ELC04 | 559.0 | 0 | 559.0 |
| R_ES-SH-DH-70_ELC01 | 1,296.3 | 786.5 | 509.9 |
| R_ES-SH-DH-70_BIO01 | 91.35 | 380.6 | -289.2 |
| R_ES-SH-DH_BIO01 | 3,466.7 | 3,187.6 | 279.1 |
| R_ES-SH-DH-70_ELC07 | 2,215.4 | 1,939.9 | 275.5 |
| R_ES-SH-SD_ELC04 | 260.7 | 0 | 260.7 |
| R_ES-SH-SD_ELC07 | 666.0 | 427.2 | 238.8 |

## K. Activity without a capacity variable
- Processes with capacity in the reference that run without capacity: 42
| region / process | activity (all years) |
|---|---|
| FI1C5 / IPPPUPRYC00 | 28.68 |
| FI1C7 / IPPPUPRYC00 | 28.64 |
| FI196 / IPPPUPRYC00 | 18.46 |
| FI1D7 / IPPPUPRYC00 | 15.95 |
| FI1D9 / IPPPUPRYC00 | 15.18 |
| FI19B / IPPPUPRYC00 | 15.09 |
| FI198 / IPPPUPRYC00 | 14.87 |
| FI19A / IPPPUPRYC00 | 13.3 |
| FI1B1 / IPPPUPRYC00 | 10.34 |
| FI1DB / IPPPUPRYC00 | 9.178 |
| FI1C6 / IPPPUPRYC00 | 3.745 |
| FI1DC / IPPPUPRYC00 | 3.419 |
| FI1C2 / IPPPUPRYC00 | 3.28 |
| FI1C5 / IPPPUPCHE00 | 2.494 |
| FI1C7 / IPPPUPCHE00 | 2.108 |
| FI1D9 / IPPPUPCHE00 | 1.498 |
| FI19B / IPPPUPCHE00 | 1.329 |
| FI196 / IPPPUPCHE00 | 1.322 |
| FI19A / IPPPUPCHE00 | 1.205 |
| FI198 / IPPPUPCHE00 | 1.189 |
| FI1D7 / IPPPUPCHE00 | 1.186 |
| FI1C5 / IPPPRCHFO00 | 1.081 |
| FI1C7 / IPPPRCHFO00 | 0.993 |
| FI1DB / IPPPUPCHE00 | 0.8319 |
| FI1B1 / IPPPUPCHE00 | 0.8239 |
| FI1D9 / IPPPRCHFO00 | 0.8054 |
| FI1D7 / IPPPRCHFO00 | 0.6864 |
| FI196 / IPPPRCHFO00 | 0.5865 |
| FI198 / IPPPRCHFO00 | 0.4887 |
| FI19B / IPPPRCHFO00 | 0.4652 |
| FI19A / IPPPRCHFO00 | 0.43 |
| FI1C6 / IPPPUPCHE00 | 0.3395 |
| FI1B1 / IPPPRCHFO00 | 0.3309 |
| FI1C2 / IPPPUPCHE00 | 0.2973 |
| FI1DB / IPPPRCHFO00 | 0.2968 |
| FI1DC / IPPPUPCHE00 | 0.2542 |
| FI1C7 / INDIPPHTH00 | 0.2404 |
| FI1C2 / IPPPRCHFO00 | 0.2039 |
| FI1C6 / IPPPRCHFO00 | 0.1211 |
| FI1DC / IPPPRCHFO00 | 0.07781 |
| FI1D9 / IPPPUPMEC00 | 0.05024 |
| FI1C7 / IPPPUPMEC00 | 0.007939 |


## Verdict
FAIL: NCAP_PASTI, PRC_RESID, activity without capacity
