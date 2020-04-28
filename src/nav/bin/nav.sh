#!/bin/bash

# adapted from https://github.com/gokcehan/lf/blob/master/etc/lfcd.sh

tmp="$(mktemp)"
nav_cli "$tmp" $PWD;
if [ -f "$tmp" ]; then
    dir="$(cat "$tmp")"
    rm -f "$tmp"
    if [ -d "$dir" ]; then
        if [ "$dir" != "$(pwd)" ]; then
            cd "$dir"s
        fi
    fi
fi