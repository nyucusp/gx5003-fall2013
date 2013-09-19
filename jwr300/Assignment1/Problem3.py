#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 1, Problem 3
#MineSweeper game that takes input from the command line of a minefield and returns the count
# of adjacent mines for each cell

import sys

def main(argv):

	lines = sys.argv[1]
	global M
	M = int(lines[0][0])
	
	global N
	N = int(lines[2][0])

	inputList2 = lines.split('\\n')
	inputList = []

	for i in range(1,len(inputList2)):
		inputList.append(list(inputList2[i]))

	mineDict = createDict(inputList) #create mine dictionary

	trackerDict =  createTrackerDict(mineDict) #create tracker dictionary

	field = mineDisplay(mineDict, trackerDict)

	mineOutput(mineDict)


#iterate through each cell and return mineCount

def createTrackerDict(mineDict):
	trackerDict = {}
	for k,v in mineDict.items(): # iterates through dictionary
		trackerDict[k[0],k[1]] = mineCount(mineDict,k[0],k[1]) #assigns minecount value for each cell in field
	return trackerDict

#pass the multi-input single array into a dictionary with key value pair as index


def createDict(inputList):
	i = 0
	values = []
	keys = []
	while i < M:
		j = 0
		while j < N:
			values.append(inputList[i][j])
			keys.append((i,j))
			j = j + 1
		i = i + 1


	dictionary = dict(zip(keys, values)) #build dictionary using dict function

	return dictionary

def mineCount(mineDict, row, col):
    rowLength = M
    columnLength = N
    mineCount = 0
    for i in range(max(0,row-1),min(rowLength,row+2)):
        for j in range(max(0,col-1), min(columnLength,col+2)):
            if (i == row and j == col): #dont count the refence cell
                continue
            elif (mineDict[i,j] == "*"):
                mineCount += 1
    
    return mineCount

def mineDisplay(mineDict, trackerDict): 
	for k,v in mineDict.items():
		if mineDict[k[0],k[1]] != "*":
			mineDict[k[0],k[1]] = trackerDict[k[0],k[1]]

def mineOutput(mineDict):
	print "Field:", "\n"
	i = 0
	while i < M:
	    j = 0
	    while j < N:
	        print mineDict[i,j],
	        j = j + 1
	    print "\n"
	    i = i + 1


if __name__ == "__main__":
	main(sys.argv)
