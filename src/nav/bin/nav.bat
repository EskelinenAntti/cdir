@echo off

set nav_home=%~dp0..\

py -m nav "%CD%"
IF NOT ERRORLEVEL 1 (
    CALL "%nav_home%\tmp\navigate_to.bat"
    erase "%nav_home%\tmp\navigate_to.bat"
)

