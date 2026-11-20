@echo off
SET "$case_name=5c"
SET "$vd_file_name=5c_2011"
Title 5c [GAMS_WRKTIMES] 
CALL ..\GAMS_SrcTIMES.v4.8.3\VT_GAMS %$case_name% GAMS_SrcTIMES.v4.8.3 GAMSSAVE\%$case_name% '' ..\ lo=1 2>&1 | tee "%$case_name%_run_log.txt"
GDX2VEDA GAMSSAVE\%$case_name% ..\GAMS_SrcTIMES.v4.8.3\times2veda.vdd %$vd_file_name%
@echo Closed >RunTerminated
