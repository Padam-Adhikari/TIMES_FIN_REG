@echo off
SET "$case_name=baseline-sami"
SET "$vd_file_name=baseline-sami_1711"
Title baseline-sami [GAMS_WRKTIMES] 
CALL ..\GAMS_SrcTIMES.v4.8.3\VT_GAMS %$case_name% GAMS_SrcTIMES.v4.8.3 GAMSSAVE\%$case_name% '' ..\ lo=1 2>&1 | tee "%$case_name%_run_log.txt"
GDX2VEDA GAMSSAVE\%$case_name% ..\GAMS_SrcTIMES.v4.8.3\times2veda.vdd %$vd_file_name%
@echo Closed >RunTerminated
