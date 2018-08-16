#!/usr/bin/python

import math
import decimal

decimal.getcontext().prec = 998

quolist=[]
remlist=[]
def Divide(top,bot):
	#print str(top) + ' / ' + str(bot)
	rem = (top * (10 ** len(str(bot)))) % bot
	quo = (top * (10 ** len(str(bot)))) / bot
	if rem in remlist or rem == 0:
		return len(quolist)
	else:
		quolist.append(quo)	
		remlist.append(rem)
		return Divide(rem, bot)

Largest = 0
number = 0
#Set Range to check in (currently < 1000)
for x in range(2,1000):
	quolist=[]
	remlist=[]
	temp = Divide(1,x)
	#print temp
	if temp > Largest:
		Largest = temp
		number = x

print 'Divisor #: ' + str(number)
quolist=[]
remlist=[]
Divide(1,number)
print 'Numbers: ' + str(quolist)
	
