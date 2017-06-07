squaresum = 0
sumsquare = 0
total = 0

for a in range(1, 101, 1):
    squaresum+=a**2
    sumsquare+=a
    
sumsquare=sumsquare**2
total=sumsquare-squaresum
print(total)
