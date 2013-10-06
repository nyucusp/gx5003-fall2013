#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 3, Problem 4

myFile = open('input4.txt', 'r')
numScenarios = int(myFile.readline())

currentScenario = 0

myFile.readline() #read blank line

def checkNorth(gridlist, string, row, col):
    i = 0
    while(row >= 0 and i < len(string) and gridlist[row][col] == string[i]):
        row -= 1 #check north
        i += 1
    return (i == len(string))

def checkSouth(gridlist, string, row, col):
    i = 0
    while(row < len(gridlist) and i < len(string) and gridlist[row][col] == string[i]):
        row += 1 #check south
        i += 1
    return (i == len(string))

def checkWest(gridlist, string, row, col):
    i = 0
    while(col >= 0 and i < len(string) and gridlist[row][col] == string[i]):
        col -= 1 #check West
        i += 1
    return (i == len(string))

def checkEast(gridlist, string, row, col):
    i = 0
    while(col < len(gridlist[row]) and i < len(string) and gridlist[row][col] == string[i]):
        col += 1 #check West
        i += 1
    return (i == len(string))

def checkNorthEast(gridlist, string, row, col):
    i = 0
    while(row >= 0 and col < len(gridlist[row]) and i < len(string) and gridlist[row][col] == string[i]):
        row -= 1 #check North
        col += 1 #check East
        i += 1
    return (i == len(string))

def checkNorthWest(gridlist, string, row, col):
    i = 0
    while(row >= 0 and col >= 0 and i < len(string) and gridlist[row][col] == string[i]):
        row -= 1 #check North
        col -= 1 #check West
        i += 1
    return (i == len(string))

def checkSouthEast(gridlist, string, row, col):
    i = 0
    while(row < len(gridlist) and col < len(gridlist[row]) and i < len(string) and gridlist[row][col] == string[i]):
        row += 1 #check South
        col += 1 #check East
        i += 1
    return (i == len(string))

def checkSouthWest(gridlist, string, row, col):
    i = 0
    while(row < len(gridlist) and col >= 0 and i < len(string) and gridlist[row][col] == string[i]):
        row += 1 #check South
        col -= 1 #check West
        i += 1
    return (i == len(string))


def gridCheck(string, gridlist):
    for row in range (0, numRows):
        for col in range (0,numColumns):
            if(grid[row][col] == string[0]):
               if(checkNorth(gridlist, string, row, col) or 
                  checkSouth(gridlist, string, row, col) or 
                  checkEast(gridlist, string, row, col) or 
                  checkWest(gridlist, string, row, col) or 
                  checkNorthEast(gridlist, string, row, col) or  
                  checkNorthWest(gridlist, string, row, col) or 
                  checkSouthEast(gridlist, string, row, col) or 
                  checkSouthWest(gridlist, string, row, col)):
                    return str(row+1) + " " + str(col+1)
    return "0 0"


while (currentScenario < numScenarios):
    gridDimensions = myFile.readline().split()

    numColumns = int(gridDimensions[0])
    numRows = int(gridDimensions[1])

    grid = []
    for i in range(0,numColumns):
        line = list(myFile.readline().strip().lower())
        grid.append(line)
    numWords = int(myFile.readline())
    words = []
    for i in range(0,numWords):
        words.append(myFile.readline().strip().lower())
    for word in words:
        print gridCheck(word, grid)
    if numScenarios > 1:
    	print "" #adding a blank line to satify problem specifications
    currentScenario += 1