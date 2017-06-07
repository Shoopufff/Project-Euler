#!/bin/bash

check=0
num=2520

while [ $check == 0 ]
do
	for a in {11..20}
	do
		Test=$((num % a))
		if [ $Test == 0 ]; then
			if [ $a == 20 ]; then
				echo "ANSWER: "$num
				check=1
				exit 0
			else
				continue
			fi
		else
			break
		fi
	done
	num=$((num + 20))
	echo -en "$num\r"
done
