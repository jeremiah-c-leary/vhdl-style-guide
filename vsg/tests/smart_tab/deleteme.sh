#!/usr/bin/bash
echo $1
cp ../styles/code_examples/$1 $1;vsg --style jcl -c config.yaml --fix -f $1
