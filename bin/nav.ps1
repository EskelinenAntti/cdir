py $env:NAV_HOME\src\main.py $pwd.tostring() # or Success
if ($LASTEXITCODE -eq 0) {
    . $env:NAV_HOME\tmp\navigate_to.ps1
    erase $env:NAV_HOME\tmp\navigate_to.ps1
}