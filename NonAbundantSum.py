#!/usr/bin/python

import math
import time

start = time.time()

Limit=28123
AbundantNums = []
AbundantSums = {}

#Return array of factors of given number
#Proper Divisors of 28 = 1, 2, 4, 7, 14
def GetFactors( num ):
    temp = []
    for i in range(1,int(math.sqrt(num)) + 1):
        if ( (num % i) == 0 ):
			Pair=(num / i)
			if (Pair == i) or (Pair == num):
				temp.append(i)
			else: 
				temp.append(i)
				temp.append(Pair)
	temp.sort()
    return temp

def Abundant(test):
	Factors=GetFactors(test)
	Total=0
	for x in Factors:
		Total+=x
	if Total > test:
		return True
	else:
		return False

#Get all abundant numbers <= 28123 (All can be created after this)		
for num in range(1, Limit):
	if Abundant(num):
		AbundantNums.append(num)

#Build Abundunt Sums Dictionary (Add each abundant num to one another)
for i in AbundantNums:
	j = i
	for j in AbundantNums:
		value=i+j
		if value > 28123:
			break 
		AbundantSums[value] = 1

#Return non-abundant sums by checking AbundantSums dictionary
Sum=0
for num in range(1,Limit):
	if num not in AbundantSums:
		#print num
		Sum += num

end = time.time()
print Sum
print (end - start)
