#!/usr/bin/python

import sys
import itertools
import string
import csv

#Create alphabet dictionary for scoring
alpha = {}
count = 1
for char in string.ascii_uppercase:
	alpha[char] = count
	count += 1

Names = []
Nscore = []

#Score names by alphebetical position of letters
def Score(namestr):
	score=0
	for char in namestr:
		score+=alpha[char]
	return score
		
#Compare names alphabetically return true if name1 is equal or less than name2	 
def Compare(name1, name2):
	for n1char, n2char in zip(name1, name2):
		if n1char < n2char:
			return True
		elif n1char > n2char:
			return False
	if len(name1) < len(name2):
		return True
	elif len(name1) > len(name2):
		return False
	else:
		 return True
					

#Open file comma delimited file
ctr=0
with open('names.txt') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		#Read all columns (unknown number passed)
		while True:
			try:
				current=0
				Limit=len(Names)
				while current < Limit:
					if Compare(row[ctr], Names[current]):
						Names.insert(current, row[ctr])
						Nscore.insert(current, Score(row[ctr]))
						break
					elif current == (Limit - 1):
						Names.append(row[ctr])
						Nscore.append(Score(row[ctr]))
					current+=1
				#If first name to be added
				if Limit == 0:
					Names.append(row[ctr])
					Nscore.append(Score(row[ctr]))
				ctr+=1
			except IndexError:
				break

#Get Total of Name Scores
#Names Score = Position * Nscore
Total=0
val=0
for val in range(len(Names)):
	Total += (Nscore[val] * (val+1))

print Total

