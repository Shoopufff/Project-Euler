
#ones=[ zero, one, two, three, four, five, six, seven, eight, nine ]
ones=[ 0, 3, 3, 5, 4, 4, 3, 5, 5, 4 ]

#teens=[ ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen ]
teens=[ 3, 6, 6, 8, 8, 7, 7, 9, 8, 8 ]

#tens=[ zero, teens, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety ]
tens=[ 0, 0, 6, 6, 5, 5, 5, 7, 6, 6 ]

#hundred=[ zero, one hundred, two hundred, three hundred, four hundred, five hundred, six hundred, seven hundred, eight hundred, nine hundred ]
hundred=[ 0, 10, 10, 12, 11, 11, 10, 12, 12, 11 ]

#thousand=[ zero, one thousand ]
thousand=[ 0, 11 ]

#Get Number of letters for any number passed to split
def NumLetters (number):
	temp=str(number)[::-1]
	#Position relative to digit (start at ones)
	Pos=1
	Count=0
	for char in temp:
		if Pos == 1:	
			Count=ones[int(char)]
			#Keep current number in case this is in the teens
			Save=int(char)
		if Pos == 2:
			if int(char) == 1:
				Count=teens[Save]
			else:
				Count+=tens[int(char)]
		if Pos == 3:
			if Count != 0:
				#including And letters for not pure hundreds
				Count += 3
			Count+=hundred[int(char)]
		if Pos == 4:
			Count+=thousand[int(char)]
		Pos+=1
	return Count

current=1
LetterCount=0
while(current<=1000):
	Temp=NumLetters(current)
	LetterCount += Temp
	print str(current) + " " + str(Temp)
	current += 1

print LetterCount	
		
		

