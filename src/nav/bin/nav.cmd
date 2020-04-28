@echo off
rem adapted from https://github.com/gokcehan/lf/blob/master/etc/lfcd.cmd

:tmploop
set tmpfile="%tmp%\lf.%random%.tmp"
if exist %tmpfile% goto:tmploop
nav_cli %tmpfile% "%CD%"
if not exist %tmpfile% exit
set /p dir=<%tmpfile%
del /f %tmpfile%
if not exist "%dir%" exit
if "%dir%" == "%cd%" exit
cd /d "%dir%"