
#Month=[ Filler, January, February, March, April, May, June, July, August, September, October, November, December ]
#Value = days in month || Index = month
#Index off by 1 with filler to start at 1
Month=[ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

#WeekDay=[ Filler, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday ]
#Index = WeekDay || Value = Count it 
#Index off by 1 with filler to start at 1
WeekDay=[ 0, 1, 0, 0, 0, 0, 0, 0 ]

#Starting info
#Set to Tuesday January 1st 1901
Year=1901
#Weekday[3] == Tuesday
Today=3
#Set to January
#Month[1]
ThisMonth=1

SundayCounter=0
while Year <= 2000:
	if Year % 4 == 0:
		Month[2]=29
	else:
		Month[2]=28
	#Loop through months to determine if first day is Sunday
	ThisMonth=1
	while ThisMonth <= 12:
		if Today == 1:
			SundayCounter+=1
		#Calculate next month weekday
		Today = Today + Month[ThisMonth] % 7
		if Today > 7:
			Today = Today - 7
		ThisMonth+=1
	Year+=1

print "Number of Sundays on the first of the month:"
print SundayCounter
