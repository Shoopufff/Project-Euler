#!/usr/bin/python

import math

#Range for a & b
Rval=100
#Store results of a^b
Pval = []
for x in range(2,Rval+1):
	for y in range(2,Rval+1):
		Pval.append(x ** y)

#return number of sorted list (no duplicates)
print len(sorted(set(Pval)))
