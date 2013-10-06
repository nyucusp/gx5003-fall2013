#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 3, Problem 4
"""
Given an m by n grid of letters and a list of words, this script finds the location in the grid at which the word can be found.

A word matches a straight, uninterrupted line of letters in the grid. A word can match the letters in the grid regardless 
of case (i.e., upper- and lowercase letters are to be treated as the same). The matching can be done in any of the eight horizontal, vertical, or diagonal directions through the grid.

"""


def checkNorth(gridlist, string, row, col):
    i = 0
    while(row >= 0 and i < len(string) and gridlist[row][col] == string[i]):
        row -= 1 #check north within the boundaries of the grid
        i += 1
    return (i == len(string)) #if the full length of string matches, return true

def checkSouth(gridlist, string, row, col):
    i = 0
    while(row < len(gridlist) and i < len(string) and gridlist[row][col] == string[i]):
        row += 1 #check south within the boundaries of the grid
        i += 1
    return (i == len(string)) #if the full length of string matches, return true

def checkWest(gridlist, string, row, col):
    i = 0
    while(col >= 0 and i < len(string) and gridlist[row][col] == string[i]):
        col -= 1 #check west within the boundaries of the grid
        i += 1
    return (i == len(string)) #if the full length of string matches, return true

def checkEast(gridlist, string, row, col):
    i = 0
    while(col < len(gridlist[row]) and i < len(string) and gridlist[row][col] == string[i]):
        col += 1 #check East within the boundaries of the grid
        i += 1
    return (i == len(string)) #if the full length of string matches, return true

def checkNorthEast(gridlist, string, row, col):
    i = 0
    while(row >= 0 and col < len(gridlist[row]) and i < len(string) and gridlist[row][col] == string[i]):
        row -= 1 #check North within the boundaries of the grid
        col += 1 #check East within the boundaries of the grid
        i += 1
    return (i == len(string)) #if the full length of string matches, return true

def checkNorthWest(gridlist, string, row, col):
    i = 0
    while(row >= 0 and col >= 0 and i < len(string) and gridlist[row][col] == string[i]):
        row -= 1 #check North within the boundaries of the grid
        col -= 1 #check West within the boundaries of the grid
        i += 1
    return (i == len(string)) #if the full length of string matches, return true

def checkSouthEast(gridlist, string, row, col):
    i = 0
    while(row < len(gridlist) and col < len(gridlist[row]) and i < len(string) and gridlist[row][col] == string[i]):
        row += 1 #check South within the boundaries of the grid
        col += 1 #check East within the boundaries of the grid
        i += 1
    return (i == len(string)) #if the full length of string matches, return true

def checkSouthWest(gridlist, string, row, col):
    i = 0
    while(row < len(gridlist) and col >= 0 and i < len(string) and gridlist[row][col] == string[i]):
        row += 1 #check South within the boundaries of the grid
        col -= 1 #check West within the boundaries of the grid
        i += 1
    return (i == len(string)) #if the full length of string matches, return true

"""
The method gridCheck will check all 8 directions from each cell in the grid 
and return the cell location of where the first letter of the given word and be found
and the second integer is where the columnn of the first letter of the given word
can be found
"""
def gridCheck(string, gridlist, numRows, numColumns):
    for row in range (0, numRows):
        for col in range (0,numColumns):
            if(gridlist[row][col] == string[0]):
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

def main():
	myFile = open('input4.txt', 'r')
	numScenarios = int(myFile.readline())

	currentScenario = 0

	myFile.readline() #read blank line

	#loop will iterate through all scenarios/ test cases
	while (currentScenario < numScenarios):
	    gridDimensions = myFile.readline().split()
	    [numRows, numColumns] = [int(num) for num in gridDimensions]

	    grid = []
	    for i in range(0,numRows):
	        line = list(myFile.readline().strip().lower())
	        grid.append(line)
	    numWords = int(myFile.readline())
	    words = []
	    for i in range(0,numWords):
	        words.append(myFile.readline().strip().lower()) #sets all letters in grid to lowercase
	    for word in words:
	        print gridCheck(word, grid, numRows, numColumns)

	    currentScenario += 1
	    if numScenarios > 1:
	    	print ""  #adding a blank line to satify problem specifications
	    	myFile.readline() #read blank line

	myFile.close()


if __name__=='__main__':
    main()