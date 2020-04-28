# adapted from https://github.com/gokcehan/lf/blob/master/etc/lfcd.ps1

$tmp = [System.IO.Path]::GetTempFileName()
cdir_cli "$tmp" "$pwd"
if (test-path -pathtype leaf "$tmp") {
    $dir = type "$tmp"
    remove-item -force "$tmp"
    if (test-path -pathtype container "$dir") {
        if ("$dir" -ne "$pwd") {
            cd "$dir"
        }
    }
}