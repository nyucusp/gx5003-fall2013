#!usr/bin/python

######################################################################
#
# 	Assignment 3 - Problem 4
# 	October 7th, 2013
#
# 	Michael Musick
#
######################################################################

import sys

# def searchForLetter( word, word_index, grid, row, col ):
# 	gridSize[0] = len(grid)
# 	gridSize[1] = len(grid[0])

# 	for 







# open the db file containing zipcodes for each borough
dbFile = open('input4.txt','r')

numOfCases = int(dbFile.readline())
line = dbFile.readline()

gridSize = dbFile.readline()
gridSize = gridSize.strip().split(' ')
gridSize = [int(gridSize[0]), int(gridSize[1])]
print gridSize

grid = []
for row in xrange(gridSize[0]):
	line = dbFile.readline()
	line = line.strip('\n')
	line = line.lower()
	tempLine = []

	for col in xrange(gridSize[1]):
		tempLine.append(line[col])

	grid.append(tempLine)

print len(grid)

# get the number of words to find
wordNum = int(dbFile.readline())	

wordList = {}
for _ in xrange(wordNum):
	word = dbFile.readline()
	word = word.strip('\n')
	word = word.lower()	
	wordList[word] = [0, 0]

print wordList


for word in wordList:
	print word	
	# look through this sucker
	for row in xrange(gridSize[0]):
		for col in xrange(gridSize[1]):

			found = False
			wordLen = len(word)

			if grid[row][col] == word[0]:
				print "found " + str(row) + " " + str(col)
				
				# check east
				letterPos = 1
				check = 1
				while check == 1:								
					check = 0
					if col+letterPos < gridSize[1]:
						if grid[row][col+letterPos] == word[letterPos]:
							print "at " + str(row) + " " + str(col+letterPos)
							print grid[row][col+letterPos]
							check = 1
							letterPos += 1
				print
				

				# check south east
				letterPos = 1
				check = 1
				while check == 1:								
					check = 0
					if col+letterPos < gridSize[1] and row+letterPos < gridSize[0]:
						if grid[row+letterPos][col+letterPos] == word[letterPos]:
							print "at " + str(row+letterPos) + " " + str(col+letterPos)
							print grid[row+letterPos][col+letterPos]
							check = 1
							letterPos += 1
							if letterPos == wordLen:
								found = True
								wordList[word] = [row+1, col+1]
				print

				# check south
				letterPos = 1
				check = 1
				while check == 1:								
					check = 0
					if row+letterPos < gridSize[0]:
						if grid[row+letterPos][col] == word[letterPos]:
							print "at " + str(row+letterPos) + " " + str(col)
							print grid[row+letterPos][col]
							check = 1
							letterPos += 1
							if letterPos == wordLen:
								found = True
								wordList[word] = [row+1, col+1]
				print

				# check south west
				letterPos = 1
				check = 1
				while check == 1:								
					check = 0
					if col-letterPos > 0 and row+letterPos < gridSize[0]:
						if grid[row+letterPos][col-letterPos] == word[letterPos]:
							print "at " + str(row+letterPos) + " " + str(col-letterPos)
							print grid[row+letterPos][col-letterPos]
							check = 1
							letterPos += 1
							if letterPos == wordLen:
								found = True
								wordList[word] = [row+1, col+1]
				print




print wordList




