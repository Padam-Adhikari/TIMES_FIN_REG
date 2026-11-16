# Regionalisation scan of GAMS_WrkTIMES/baseline-sami.run

Regions with processes: 19

## 1. Non-zero bounds with the same value on FI and in >= 2 regions (national quantity per region?)
| attribute | file | item | entries | example value | regions |
|---|---|---|---|---|---|

## 2. User constraints per region (R_E) with a non-zero RHS
| UC | regions (R_E) | RHS example |
|---|---|---|

## 3. Hub-only attributes on commodities in the regions
- COM_TAXNET: HETHTH (bau-general.dd, 19), IISHTH (bau-general.dd, 19), MISOXY (bau-general.dd, 19), MISPLT (bau-general.dd, 19), MISRIR (bau-general.dd, 19), MISSNT (bau-general.dd, 19)

## 4. Attributes on internal links TB_* (expected: definitions, ACT_COST, UC_IRE corrections)
- CAP_BND (kill_coalphaseout2030.dd): 72
- CAP_BND (syssettings.dd): 36
- NCAP_START (zietassumptions.dd): 2

## 5. Constraints with terms only on FI whose processes also exist in regions

## Summary
- 1 national bound per region: 0
- 2 per-region UC with RHS: 0
- 3 COM_TAXNET: 6
- 4 CAP_BND: 108
- 4 NCAP_START: 2
- 5 FI-only UC over moved processes: 0
