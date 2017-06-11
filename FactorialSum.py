
print "Enter the number to Factorial Sum:"
FacNum = int(raw_input())
fact = 1
result = 0
Orig = FacNum

while FacNum >= 1:
	fact *= FacNum
	FacNum -= 1

for char in str(fact):
	result += int(char)

print "Factorial Sum of %d is %d" % (Orig, result)



