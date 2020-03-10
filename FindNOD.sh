#!/usr/bin/env bash

gcd ()
{
a=$1
b=$2

while [[ True ]]
do
    if [[ $a -lt 0 || $b -lt 0 ]]; then
        echo "GCD is 1"
    fi

    if [[ $a -gt $b ]]; then
        let "a = a - b"
    elif [[ $a -lt $b ]]; then
        let "b = b - a"
    else
        echo "GCD is $b"; break
    fi
done

}

while [[ True ]]
do
    read var1 var2
    if [[ $var1 == "" ]]
    then
        echo "bye"
        break
    elif [[ $var1 = $var2 ]]
    then
        echo "GCD is $var1"
    else
    gcd $var1 $var2
    fi
done