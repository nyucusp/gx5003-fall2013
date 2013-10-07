"""
A script to take in a crossword, find the words of interest and output the location of the 
first character in the word of interest on a 1-start indexed grid.
"""


from collections import deque

def gridCheck():
#   Rows
    for i in range(int(rows)):
        stringCat = ""
        for j in range(int(columns)):
            stringCat += grid[i][j]
        wordCheck(stringCat,i,j,"row")
        
#   Columns
    for j in range(int(columns)):
        stringCat = ""
        for i in range(int(rows)):
            stringCat += grid[i][j]
        wordCheck(stringCat,i,j,"column")

#   LR Diagonals
    for k in range(0,max(int(rows),int(columns))):
        stringCat = ""
        j = (min(k,int(columns)))
        for i in range(0,min(k+1,int(rows))):
            stringCat += grid[i][j]
            j += -1
        wordCheck(stringCat,i,j,"lrDiag")

#   LR Residual
    for k in range(1,int(rows)):
        stringCat = ""
        j = int(columns) - 1
        for i in range(k,int(rows)):
            stringCat += grid[i][j]
            j += -1
        wordCheck(stringCat,i,j,"lrDiag")

#   RL Diagonals
    l = int(columns) - 1
    for k in range(1,int(columns)):
        stringCat = ""
        j = l
        for i in range(0,min(k,int(rows))):
            stringCat += grid[i][j]
            j += 1
        wordCheck(stringCat,i,j-1,"rlDiag")
        l += -1

#   RL Residuals
    l = int(rows)
    for k in range(0,int(rows)):
        stringCat = ""
        j = 0
        while (j < l):
            for i in range(k,int(rows)):
                stringCat += grid[i][j]
                j += 1
            wordCheck(stringCat,i,j-1,"rlDiag")
            l +=-1
#end method gridCheck

def wordCheck(stringCat,row,col,stringType):
    for i in range(len(wordsList)):
        stringCatRev = stringCat[::-1]
        if (wordsList[i][1] == -1 and stringCat.find(wordsList[i][0]) >= 0):
            if (stringType == "row"):
                col = col - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                wordsList[i][1] = [row,col]
            elif (stringType == "column"):
                row = row - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                wordsList[i][1] = [row,col]
            elif (stringType == "rlDiag"):
                row = row - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                col = col - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                wordsList[i][1] = [row,col]
            elif (stringType == "lrDiag"):
                row = row - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                col = col + len(stringCat) - 1 - stringCat.find(wordsList[i][0])
                wordsList[i][1] = [row,col]
        elif (wordsList[i][1] == -1 and stringCatRev.find(wordsList[i][0]) >= 0): 
            if (stringType == "row"):
                col = col - stringCatRev.find(wordsList[i][0])
                wordsList[i][1] = [row,col]
            elif (stringType == "column"):
                row = row - stringCatRev.find(wordsList[i][0])
                wordsList[i][1] = [row,col]
            elif (stringType == "rlDiag"):
                row = row - stringCatRev.find(wordsList[i][0])
                col = col - stringCatRev.find(wordsList[i][0])
                wordsList[i][1] = [row,col]
            elif (stringType == "lrDiag"):
                row = row - stringCatRev.find(wordsList[i][0])
                col = col + stringCatRev.find(wordsList[i][0])
                wordsList[i][1] = [row,col]


#begin script operation
inputFile = open('input4.txt','r') #read in input file

inputQue = deque() #deque for holding file contents

for lines in inputFile: #read input into deque
  inputQue.append(lines.rstrip())

instances = int(inputQue.popleft()) #instances of the crossword search

#start while loop for instances
instanceCounter = 1
while (instanceCounter <= instances):
    inputQue.popleft() #kill blank line

    rows, columns = inputQue.popleft().split(" ") #split line with rows and columns into variables

    grid = [] # grid list
    for i in range(0,int(rows)): # populate grid with input from file
        grid.append(list(inputQue.popleft().lower()))

    words = int(inputQue.popleft()) # count of words of interest

    wordsList = [] # list for words of interest

    for i in range(0,words): # populate words of interest
      wordsList.append([inputQue.popleft().lower(),-1])

    gridCheck() #run the check for the word location and append result to list

    #output result
    for element in wordsList:
        for i in element[1]:
            print i+1,
        print ""

    instanceCounter += 1 #increment counter for while loop
#end while loop for instances