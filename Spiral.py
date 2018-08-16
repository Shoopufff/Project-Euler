#!/usr/bin/python

import math

#initial is total size you want
#Step = 0 for starting (shows steps away outermost corners)
def CreateSpiral(init, step, ssum):
	#arrays start at 0 
	num = init - step
	onespot = (init - 1) / 2
	if step == onespot:
		#Place one in middle of arrays
		spiral[onespot][onespot] = 1
		ssum += 1
		return ssum
	else:
		#Start creating current borders
		#VAL = COLUMN
		#STEP = ROW
		#current value working with
		val = init - (step * 2)
		#max array val
		maxarr = init - 1 - step
		#top right corner
		tright = val * val 
		spiral[step][maxarr] = tright
		#top left corner
		tleft = tright - val + 1
		spiral[step][step] = tleft
		#bottom left corner
		bleft = tleft - val + 1	
		spiral[maxarr][step] = bleft
		#bottom right corner (array size - 1)
		bright = bleft - val + 1	
		spiral[maxarr][maxarr] = bright
		#work towards top right corner from top left
		i = step 
		j = maxarr - 1
		temp = tright
		while j > step:
			temp -= 1 
			spiral[i][j] = temp
			j -= 1
		i = step + 1 
		j = step
		temp = tleft
		while i < maxarr:
			temp -= 1
			spiral[i][j] = temp
			i += 1
		i = maxarr
		j = step + 1
		temp = bleft
		while j < maxarr:
			temp -= 1
			spiral[i][j] = temp
			j += 1
		i = maxarr - 1
		j = maxarr
		temp = bright
		while i > step:
			temp -= 1
			spiral[i][j] = temp
			i -= 1
		#Print Spiral
		#for row in spiral:
		#	for val in row:
		#		print "{0:^{1}}".format(val, fsize),
		#	print
		#print
		ssum = ssum + tleft + tright + bleft + bright
		return CreateSpiral(init,step + 1,ssum)

#Set Size of Spiral to be made
Size = 1001
#Formatting size for printing
fsize = len(str(Size * Size))
spiral = [[0 for x in range(Size)] for y in range(Size)]
print CreateSpiral(Size,0,0)
#Print Spiral
#for row in spiral:
#	for val in row:
#		print "{0:^{1}}".format(val, fsize),
#	print



