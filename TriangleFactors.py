import math

n=1
trinum=0
while 1:
	trinum=(n*(n+1))/2
	if trinum % 2 != 0:
		n+=1
		continue
	limit=int(math.sqrt(trinum))
	i=1
	count=0
	while i <= limit:
		if trinum % i == 0:
			count+=2
		i+=1
	if count > 500:
		print trinum
		break
	n+=1
	
