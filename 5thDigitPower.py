#!/usr/bin/python

import math

#9^power * power+1
#power + 1 = maximum number of digits

Power=5
Maximum=((9 ** Power) * (Power + 1))
Total=0

print "Power Used: ", Power
for x in range(2,Maximum):
	Sum = 0
	for y in str(x):
		Sum += int(y)**Power
	if Sum == x:
		print x
		Total += x

print "Total: ", Total
