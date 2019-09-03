#!/bin/bash
if [[ -z "$1" ]]; then
    echo "Program to kill not specified"
    return
fi

kill -9 $(ps aux | grep '[/Applications/]$1' | awk '{print $2}')
