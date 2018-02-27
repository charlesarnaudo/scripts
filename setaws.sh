#!/bin/bash

echo ""

accounts=("" "")

echo "Select from the following the accounts"

index=1
for i in ${accounts[@]}
do
  echo  "  $index" $i
  index=`expr $index + 1`
done

read input

if [[ $input -gt ${#accounts[@]} || $input -lt 1 ]]; then
  echo "Not a valid account number"
  return
  echo ""

elif [[ $input -eq 1 ]]; then
  export AWS_ACCESS_KEY_ID="";export AWS_SECRET_ACCESS_KEY="";export AWS_REGION="us-east-1" ;
elif [[ $input -eq 2 ]]; then
  export AWS_ACCESS_KEY_ID="";export AWS_SECRET_ACCESS_KEY="";export AWS_REGION="us-east-1" ;
fi

echo ""
