import math

limit=2000000
i=2
count=2

def Checkprime( num ):
    j=2
    limit=round(math.sqrt(num))
    while j <= limit:
        if ( (num % j) == 0 ):
            return False
        j+=1
    return True


while i < limit:
    if i % 2 == 0:
        i+=1
        continue
    if Checkprime(i):
        count+=i
    i+=1
        
print(count)
