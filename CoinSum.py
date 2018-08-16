#!/usr/bin/python

import math

#British money
#1 2 5 10 20 50 100 200
#1a + 2b + 5c + 10d + 20e + 50f + 100g + 200h = 200

Money = [ 200, 100, 50, 20, 10, 5, 2, 1 ]
Values = [ 0, 0, 0, 0, 0, 0 ,0 ,0 ]
Max = [ 0, 0, 0, 0, 0, 0 ,0 ,0 ]
#Money = [ 10, 5, 2, 1 ]
#Values = [ 0, 0, 0, 0 ]
#Max = [ 0, 0, 0, 0 ]
#Money = [ 20, 10, 5, 2, 1 ]
#Values = [ 0, 0, 0, 0, 0 ]
#Max = [ 0, 0, 0, 0, 0 ]
#Money = [ 50, 20, 10, 5, 2, 1 ]
#Values = [ 0, 0, 0, 0, 0, 0 ]
#Max = [ 0, 0, 0, 0, 0, 0 ]
Target = 200
Amount = 0
Count=0

for x in range(len(Money)):
	Max[x]=Target / Money[x]	

Mlen = len(Money) - 1

print "Target Value: " + str(Target)
print "Coin Values Used: "
print Money
#current index working with
i = 0
#Farthest left index used
j = 0

while Values[Mlen] != Max[Mlen]:
	#if Count >= 20:
	#	break
	#Count current money in various denominations
	Amount = 0
	for temp in range(Mlen + 1):
		Amount += (Values[temp] * Money[temp])
	#Hit target - reset amount and increment counter
	if Amount == Target:
		Count += 1
		print Values
		#Max amount reached & no other coins used
		if Values[j] == Max[j] and i == j: 
			Values[j] -= 1
			#Last of that denomination (move on)
			if Values[j] == 0:
				j += 1
				i = j
			else:
				i += 1
		#If all is in smallest value and upper one decrement upper and reset
		elif Values[Mlen] != 0 and ((Values[Mlen] * Money[Mlen]) + (Values[j] * Money[j])) == Target:
			Values[j] -= 1
			Values[Mlen] = 0
			if Values[j] == 0:
				j += 1
				i = j
			else:
				i = j+1
		elif i != Mlen:
			Values[i] -= 1
			i += 1
		#Decrement previous values that aren't the largest current denomination
		elif (i - 1) != j:
			offset=1
			for x in range(j,Mlen):
				if Values[i-offset] == 0:
					offset += 1
				#If you reach 1 beyond J also remove Maxlen value.
				elif (i-offset) == j:
					Values[i] -= 1
					i += 1
					for y in range(i,Mlen+1):
						Values[y] = 0
					break
				else:
					Values[i-offset] -= 1
					i = i-offset+1
					for y in range(i,Mlen+1):
						Values[y] = 0
					break
		#No Other conditions met, decrement current largest value and move to next
		else:
			Values[i] -= 1
			i += 1
		#elif (i+1 <= Mlen) and (Values[i] > 0):
	#Current denomination too large, decrement and get next smallest.
	elif Amount > Target:
		Values[i] -= 1
		i += 1
	#Add more from current denomination
	else:
		Values[i] += 1
print Values
Count += 1
print "# of Combinations: " + str(Count)
