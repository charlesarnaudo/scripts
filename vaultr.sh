#!/bin/bash
# Read from hashicorp vault
echo "" 
KEY=`vault read -field=ansible_key secret/$1/ansible-vault` 
echo $KEY
echo $KEY | pbcopy
