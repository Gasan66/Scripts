#!/usr/bin/env bash

var1=9
re='^[0-9]+$'

if [[ $var1 =~ $re ]]; then
    echo "True"
fi