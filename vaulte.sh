#!/bin/bash
if [[ -z "$1" ]]; then
    echo "File to encrypt not specified"
    return
fi
ansible-vault encrypt $1