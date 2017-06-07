#!/bin/bash

Factor=$1
Limit=$(echo "sqrt ( $Factor )" | bc )
echo "====Factor $Factor===="
count=0

Helper() {
	TEMP=$1
	TempLimit=$(echo "sqrt ( $TEMP )" | bc )
	for ((a=2; a<=TempLimit; a++))
	do
		prelim=$((a % 2))
		if [ $prelim == 0 ]; then
			continue
		fi 
		test=$((TEMP % a))
		if [ $test == 0 ]; then
			return 1
		fi
	done
	return 0

}

for ((i=2; i<=Limit; i++))
do
	prelim=$((i % 2))
	if [ $prelim == 0 ]; then
		continue
	fi 
	test=$((Factor % i))
	if [ $test == 0 ]; then
		if Helper $i; then
			array[$count]=$i
			count=$((count + 1))
		fi
	fi 
done

echo "Prime Factors: " ${array[@]}
