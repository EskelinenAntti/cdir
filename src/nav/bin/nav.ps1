$nav_root_dir = (Get-Item $PSScriptRoot).parent.FullName

py -m nav $pwd.tostring()

# If script runned successfully
if ($LASTEXITCODE -eq 0) {
    . "$nav_root_dir\tmp\navigate_to.ps1"
    erase "$nav_root_dir\tmp\navigate_to.ps1"
}