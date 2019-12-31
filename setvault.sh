#!/bin/bash
echo ""

vaults=("https://vault.dkinternal.com" "https://vault.preprod.dkinternal.com")

echo "Select from the following the accounts"

index=1
for i in ${vaults[@]}
do
  echo  "  $index" $i
  index=`expr $index + 1`
done

read input
if [[ $input -gt ${#vaults[@]} || $input -lt 1 ]]; then
  echo "Not a valid account number"
  exit

elif [[ $input -eq 1 ]]; then
  export VAULT_ADDR=${vaults[0]} && vault login -method=ldap username=carnaudo
elif [[ $input -eq 2 ]]; then
  export VAULT_ADDR=${vaults[1]} && vault login -method=ldap username=carnaudo
fi
