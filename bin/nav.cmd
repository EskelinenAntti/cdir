@echo off
rem adapted from https://github.com/gokcehan/lf/blob/master/etc/lfcd.cmd

:tmploop
set tmpfile="%tmp%\nav.%random%.tmp"
if exist %tmpfile% goto:tmploop

CALL nav_cli %tmpfile% "%CD%"
if not exist %tmpfile% exit
set /p dir=<%tmpfile%
del /f %tmpfile%

echo %dir%

if not exist "%dir%" exit
if "%dir%" == "%cd%" exit
cd /d "%dir%"