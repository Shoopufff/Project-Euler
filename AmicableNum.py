import math

#Start point
Start = 1
#Evaluate numbers beneath stop
Stop = 10000

#Dictionary for Results to compare
FactSums = {}

#Get factors of N and add them together.
#Because factors are in pairs we get them
#both at the same time. 
#Original number not included.
def Sum_Factors(n):
	limit=int(math.sqrt(n))
	i=2
	sum = 1
	while i <= limit:
		if n % i == 0:
			#Get other part of pair and only add them both if they aren't the same number.
			temp = n / i
			if temp != i:
				sum += i + temp
			else:
				sum += i
		i+=1
	return sum

result = 0
while Start < Stop:
	Temp = Sum_Factors(Start)
	#Only add to dictionary if it isn't 1 (Not prime)
	if Temp != 1:
		FactSums[Start] = Sum_Factors(Start)
		#If factor sum is less than the number
		#Check dictionary for pair and add both to results
		if Temp < Start:
			if Temp in FactSums:
				if FactSums[Temp] == Start:
					result += Start + Temp
	Start += 1
	
print result
