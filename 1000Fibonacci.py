#!/usr/bin/python

#Go through the Fibonacci sequence
#Return first to contain num digits
def Fibonacci(num):
	count=1
	Previous=0
	Fib=1
	Temp=0
	while num > len(str(Fib)):
		Temp=Fib
		Fib+=Previous
		Previous=Temp
		count+=1
	return count, Fib

print Fibonacci(1000)
