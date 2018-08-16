#!/usr/bin/python

import math

#Formula n^2 + an + b
#a < 1000
#b <= 1000
#Find the consecutive prime numbers starting from 0

#function for testing if number is prime.
def Checkprime( num ):
    i = 2
    limit=round(math.sqrt(num))
    while i <= limit:
        if ( (num % i) == 0 ):
            return False
        i += 1
    return True

Max=0
for a in range(-999,1000):
	for b in range(-1000,1001):
		n = 0
		#First Test
		count=0
		Test=(n ** 2) + (a * n) + b 
		while Checkprime(abs(Test)):
			count+=1
			if count > Max:
				Max = count
				MaxA = a
				MaxB = b
			n += 1
			Test=(n ** 2) + (a * n) + b

print "Max num of primes: " + str(Max)
print "Coefficients: " + str(MaxA) + " " + str(MaxB)
print "Product: " + str(MaxA * MaxB)
