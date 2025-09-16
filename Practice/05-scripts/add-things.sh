#!/bin/bash

read -p "Give me one number: " FIRNUM
read -p "Now give me another number: " SECNUM

SUMTHEM=$(($FIRNUM + $SECNUM))

echo "The sum of your two entries is $SUMTHEM"
