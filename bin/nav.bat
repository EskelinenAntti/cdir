@echo off

py %NAV_HOME%\src\main.py %CD%
IF NOT ERRORLEVEL 1 (
    CALL %NAV_HOME%\tmp\navigate_to.bat 
    erase %NAV_HOME%\tmp\navigate_to.bat
)

