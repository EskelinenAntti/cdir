@echo off

%NAV_HOME%\env\python.exe %NAV_HOME%\src\main.py %CD%
IF NOT ERRORLEVEL 1 (
    CALL %NAV_HOME%\tmp\navigate_to.bat 
    erase %NAV_HOME%\tmp\navigate_to.bat
)

