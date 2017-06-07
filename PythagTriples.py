import math

answer=0
a=1
b=1
c=1

for a in range(1,333, 1):
    if a % 2 == 0:
        c=500-math.floor((a/2))+1
        b=499-math.floor((a/2))
    else:
        c=500-math.floor((a/2))
        b=499-math.floor((a/2))
    while b > a:
        test=(a**2)+(b**2)
        testsum=(c**2)
        if ( test == testsum ):
            answer=(a * b * c)
        b-=1
        c+=1
        
print(answer)
