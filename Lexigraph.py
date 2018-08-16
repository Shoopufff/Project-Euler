#!/usr/bin/python

digits = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

small = [ 0, 1, 2]

Bigger = [ 0, 1, 2, 3 ]

#Starting Permutation
#Permutation=digits
#print Permutation

#print small

#Permute on iterable values
def Permute(values):
	#single value remaining, return
	if len(values) == 1:
		yield values
	#Loop through possible values setting farthest left
	#for each possible iteration
	for i in range(len(values)):
		#Set first value
		if i == 0:
			pool=values[i+1:]
		#Set end value
		elif i == len(values):
			pool=values[:i]
		#Set middle value
		else:
			pool=values[:i] + values[i+1:]
		#Permute on remaining values
		for perm in Permute(pool):
			yield [ values[i] ] + perm

count = 0
for next in Permute(digits):
	if count == 999999 :
		print next
		break
	count+=1
			
