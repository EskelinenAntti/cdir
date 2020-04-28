


$tmp = [System.IO.Path]::GetTempFileName()
nav_cli "$tmp" "$pwd"
if (test-path -pathtype leaf "$tmp") {
    $dir = type "$tmp"
    remove-item -force "$tmp"
    if (test-path -pathtype container "$dir") {
        if ("$dir" -ne "$pwd") {
            cd "$dir"
        }
    }
}