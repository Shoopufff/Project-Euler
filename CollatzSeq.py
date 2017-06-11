maxnum=0
max=0
for current in range(1000000):
    count=0
    i=current
    while i > 1:
        if i % 2 == 0:
            i=(i/2)
        else:
            i=((3*i)+1)
        count+=1
    if count > max:
        max=count
        maxnum=current
print maxnum

