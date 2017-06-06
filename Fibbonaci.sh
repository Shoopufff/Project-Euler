#!/bin/bash

prev=1
curr=2
total=0

while [ $curr -le 4000000 ]
do
    test=$((curr%2))
    if [ $test == 0 ]; then
        total=$((total + curr))
    fi
    temp=$((curr + prev))
    prev=$curr
    curr=$temp
done

echo $total
