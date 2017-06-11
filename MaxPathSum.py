
#Triangle Structure
#Each Value is connected to the value at the same indice below and same indice + 1
#E.G TR01[0] is connected to TR02[0] and TR02[1] n = 0 then connected to n and n + 1
#index 0 is leftmost edge and last index in each row is rightmost edge

NumRows=15

TR = [0 for i in range(16)]

TR[1] =  [ 75 ]
TR[2] =  [ 95, 64 ]
TR[3] =  [ 17, 47, 82 ]
TR[4] =  [ 18, 35, 87, 10 ]
TR[5] =  [ 20, 4,  82, 47, 65 ]
TR[6] =  [ 19, 1,  23, 75, 3,  34 ]
TR[7] =  [ 88, 2,  77, 73, 7,  63, 67 ]
TR[8] =  [ 99, 65, 4,  28, 6,  16, 70, 92 ]
TR[9] =  [ 41, 41, 26, 56, 83, 40, 80, 70, 33 ]
TR[10] = [ 41, 48, 72, 33, 47, 32, 37, 16, 94, 29 ]
TR[11] = [ 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14 ]
TR[12] = [ 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57 ]
TR[13] = [ 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48 ]
TR[14] = [ 63, 66, 4,  68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31 ]
TR[15] = [ 4,  62, 98, 27, 23, 9,  70, 98, 73, 93, 38, 53, 60, 4,  23 ]

#Go from bottom up to determine the most efficient path
#Take largest sum of each line to determine final value of next line

#Step 1 :
#3 0 0 0
#7 4 0 0
#2 4 6 0
#8 5 9 3

#Step 2 :
#3  0  0  0
#7  4  0  0
#10 13 15 0

#Step 3 :
#3  0  0  0
#20 19 0  0

#Step 4:
#23 0 0 0

#Function to read in last line and compare to previous line for combination of values
def SumPath ( LowerRow, UpperRow ):
	index = 0
	while index < len(UpperRow):
		if LowerRow[index] > LowerRow[index + 1]:
			UpperRow[index] += LowerRow[index]
		else:
			UpperRow[index] += LowerRow[index + 1]
		index += 1
	return UpperRow

while NumRows > 1:
	print SumPath( TR[NumRows], TR[NumRows - 1])
	NumRows -= 1 



			













