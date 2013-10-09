 
import sys
import numbers 
import os 
import ast 
from operator import itemgetter

inputFile = open('input4.txt','r') 
inputLine = inputFile.readlines()

## Clean the Data ## 

inputClean = []
for x in inputLine:
	x =	x.rstrip(os.linesep)
	inputClean.append(x) 

## Changed the Input into all lower cases ## 
inputClean_lower = [item.lower() for item in inputClean]

## Organized the Indexes and Input Information ## 
indexofspace = inputClean_lower.index('')
casenumber = inputClean_lower[inputClean_lower.index('') - 1] 
rownumber = (inputClean_lower[inputClean_lower.index('') + 1])[:(inputClean_lower[inputClean_lower.index('') + 1]).index(' ')]
columnnumber = (inputClean_lower[inputClean_lower.index('') + 1])[((inputClean_lower[inputClean_lower.index('') + 1]).index(' ')+1):]


word_lines = inputClean_lower[(int(indexofspace) + 2):(int(indexofspace) + int(rownumber) + 2)] 
word_key_number = inputClean_lower[(int(indexofspace) + int(rownumber) + 2)]
word_key = inputClean_lower[(int(indexofspace) + int(rownumber) + 3):(int(indexofspace) + int(rownumber) + 3 + int(word_key_number))] 


'''
From this point, my goal has been for each point in the word_lines, I will create eight strings that goes all direction.
Then, I will search for word key in those strings. If there is the word string, then I'll print the position of the point. 

'''
#:(int(indexofspace) + int(rownumber) + 2)] 
#print word_key

#letter_key = []
#for x in word_key:
#	letter_key.append(x[0])

#all_letters = []
#for x in word_lines:
#	for y in x:
#		all_letters.append(y)
#print all_letters

class Searchlist:
   def __init__(self, location, horizontalright, horizontalreverse, verticalright, verticalreverse, diagonalsoutheast, diagonalnortheast, diagonalsouthwest, diagonalnorthwest):
		self.name = self
		self.location = location 
		self.horizontalright = horizontalright
		self.horizontalreverse = horizontalreverse
		self.verticalright = verticalright
		self.verticalreverse = verticalreverse
		self.diagonalsoutheast = southeast
		self.diagonalnortheast = northeast
		self.diagonalsouthwest = southwest
		self.diagonalnorthwest = northwest 

#		self.diagonalreverse = diagonalreverse

rowlist = list(xrange(1, int(rownumber) + 1))
columnlist = list(xrange(1, int(columnnumber) + 1))
locationlist = [(x,y) for x in rowlist for y in columnlist]

print rowlist 
print columnlist
print locationlist 

#Horizontal Line for Position 0,0 # 
print word_lines[0][0:int(columnnumber)]
#Horizontal Line for Position 0,1 # 
print word_lines[0][1:int(columnnumber)]

#Reverse Horizontal Line for Position 0,0 ## 
print (word_lines[0])[::-1][int(columnnumber) - 1 - 0:]
#Reverse Horizontal Line for Position 0,1 ## 
print (word_lines[0])[::-1][int(columnnumber) - 1 - 1:]


#Vertical Line for Position 0,0 ## 
flip_word_lines = [] 

n = 0 
while n < int(columnnumber):
	y = [] 
	for x in word_lines:  
		y.append(x[n])
		''.join(y) 
	n += 1
	flip_word_lines.append(''.join(y))

print word_lines
print flip_word_lines


#Vertical Line for Position 0,0 # 
print flip_word_lines[0][0:int(rownumber)]
#Vertical Line for Position 0,1 # 
print flip_word_lines[0][1:int(rownumber)]

#Reverse Vertical Line for Position 0,0 ## 
print (flip_word_lines[0])[::-1][int(rownumber) - 1 - 0:]
#Reverse Vertical Line for Position 0,1 ## 
print (flip_word_lines[0])[::-1][int(rownumber) - 1 - 1:]



#Diagonal South East of Position 0,0 ## 
n = 0 
southeast = [] 
while n < min((int(rownumber)- 0), (int(columnnumber) - 0)): 
	southeast.append(word_lines[int(0) + n][int(0) + n])
	n += 1 
southeast = ''.join(southeast) 

print southeast

#Diagonal South West of Position 0,0 ## 
n = 0
northeast = [] 
while n < min((int(rownumber)- 0), (int(columnnumber) - 0)): 
	if int(0) - n >= 0:
		northeast.append(word_lines[int(0) + n][int(0) - n])
		n += 1 
	else:
		n += 1  
northeast = ''.join(northeast)

print northeast

#Diagonal North West of Position 0,0 ## 
n = 0
northwest = [] 
while n < min((int(rownumber)- 0), (int(columnnumber) - 0)): 
	if int(0) - n >= 0:
		northwest.append(word_lines[int(0) - n][int(0) + n])
		n += 1 
	else:
		n += 1  
northwest = ''.join(northwest)

print northwest

## Diagonal South West of Position 0,0 ## 
n = 0
southwest = [] 
while n < min((int(rownumber)- 3), (int(columnnumber) - 3)): 
	if int(3) - n >= 0:
		southwest.append(word_lines[int(3) - n][int(3) - n])
		n += 1 
	else:
		n += 1  
southwest = ''.join(southwest)

print southwest

#remember this is different from position number # 
#print word_lines[0][0] + word_lines[1][1]


#	while n <= int(rownumber): 
#		y.append(x[n])
#		y = ''.join(y)
#		n += 1 
#	flip_word_lines.append(y)

#print flip_word_lines

#	flip_word_lines.append(y)

# a = ['a', 'b', 'c', 'd']
#''.join(a)
#'abcd'


# Diagonal Line for Position 0,0 ##
#print min(int(rownumber), int(columnnumber))

#print rownumber
#print columnnumber

#import itertools
#for item in itertools.chain(rowlist, columnlist)
#print rowlist

#print zip(rowlist, columnlist)



#def location(list):
#	rowcount = 0 
#	columcount = 0
#	rowlist = []  
#	while columncount <= columnnumber:


#print letter_key

#dictofword_key = []
 
#for x in word_key: 
#	dictofword_key.append(dict(zip(x, counter)))
#	counter += 1 


#print dictofword_key

#dictofword_lines = dict(zip(xrange(1, int(rownumber) + 1), word_lines))

#print dictofword_lines
#print letter_key
#zipPopdic = dict(zip(ziplist, poplist))



#for searchname in letter_key:
#	counter = 0 
#	for key, value in dictofword_lines.iteritems(): 
#		if searchname in value and counter == 0:  
#			print str(key) + ' ' + str(int(value.index(searchname)) + 1) 
#			counter += 1





#r = xrange(2000, 2005)
#h = zip(xrange(1, len(r) + 1), r)
#print h

#dictofvoters = []
#for x in listofvotessplit:
#	dictofvoters.append(dict(zip(x, listofcandidates)))
#print dictofvoters


inputFile.close 
