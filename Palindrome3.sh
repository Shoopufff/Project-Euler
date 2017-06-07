#!/bin/bash

CheckPalindrome() {
	palin=$1
	palinmax=${#palin}
	palinsize=$((palinmax / 2))
	palinmax=$((palinmax - 1))
	for ((j=0; j<=$palinsize; j++))
	do
		if [ ${palin:$j:1} == ${palin:$palinmax:1} ]; then
			palinmax=$((palinmax - 1))
			continue
		else
			return 1
		fi
	done
	return 0	
}


for a in {900..999}
do
	for i in {900..999}
	do
		TEST=$((a * i))
		if CheckPalindrome $TEST; then
			Answer=$TEST
		fi
	done
done

echo $Answer
	
