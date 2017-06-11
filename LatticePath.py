Gridsize=20

#Create factorial function
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

#Result is Gridsize times 2 (because it's a square)
#So it becomes Gridsize * 2 Choose Gridsize for paths
#Can only make 20 moves 
print factorial(Gridsize * 2) / factorial(Gridsize)**2

