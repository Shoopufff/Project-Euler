import math

i=1
count=0

def Checkprime( num ):
    j=2
    limit=round(math.sqrt(num))
    while j <= limit:
        if ( (num % j) == 0 ):
            return False
        j+=1
    return True

while count < 10001:
    i+=1
    if Checkprime(i):
        count+=1

print(i)
