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
            # print "Word " + wordsList[i][0] + " in the string " + stringCat + " of type " + stringType + " that ends at " + str(row) + "," + str(col) + " at index " + str(stringCat.find(wordsList[i][0]))
            if (stringType == "row"):
                col = col - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                #print "The start of the word is " + str(row) + "," + str(col)
                wordsList[i][1] = [row,col]
            elif (stringType == "column"):
                row = row - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                #print "The start of the word is " + str(row) + "," + str(col)
                wordsList[i][1] = [row,col]
            elif (stringType == "rlDiag"):
                row = row - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                col = col - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                #print "The start of the word is " + str(row) + "," + str(col)
                wordsList[i][1] = [row,col]
            elif (stringType == "lrDiag"):
                row = row - len(stringCat) + 1 + stringCat.find(wordsList[i][0])
                col = col + len(stringCat) - 1 - stringCat.find(wordsList[i][0])
                #print "The start of the word is " + str(row) + "," + str(col)
                wordsList[i][1] = [row,col]
        elif (wordsList[i][1] == -1 and stringCatRev.find(wordsList[i][0]) >= 0): 
            # print "Word " + wordsList[i][0] + " in the string " + stringCatRev + " of type " + stringType + " that ends at " + str(row) + "," + str(col) + " at index " + str(stringCatRev.find(wordsList[i][0]))
            if (stringType == "row"):
                col = col - stringCatRev.find(wordsList[i][0])
                #print "The start of the word is " + str(row) + "," + str(col)
                wordsList[i][1] = [row,col]
            elif (stringType == "column"):
                row = row - stringCatRev.find(wordsList[i][0])
                #print "The start of the word is " + str(row) + "," + str(col)
                wordsList[i][1] = [row,col]
            elif (stringType == "rlDiag"):
                row = row - stringCatRev.find(wordsList[i][0])
                col = col - stringCatRev.find(wordsList[i][0])
                #print "The start of the word is " + str(row) + "," + str(col)
                wordsList[i][1] = [row,col]
            elif (stringType == "lrDiag"):
                row = row - stringCatRev.find(wordsList[i][0])
                col = col + stringCatRev.find(wordsList[i][0])
                #print "The start of the word is " + str(row) + "," + str(col)
                wordsList[i][1] = [row,col]


#begin script operation
inputFile = open('input4.txt','r') #read in input file

inputQue = deque() #deque for holding file contents

for lines in inputFile: #read input into deque
  inputQue.append(lines.rstrip())

instances = int(inputQue.popleft()) #instances of the crossword search

#start while loop for instances

inputQue.popleft() #kill blank line

rows, columns = inputQue.popleft().split(" ")

grid = [] # grid list
for i in range(0,int(rows)):
    grid.append(list(inputQue.popleft().lower()))

words = int(inputQue.popleft())

wordsList = []

for i in range(0,words):
  wordsList.append([inputQue.popleft().lower(),-1])

gridCheck()

#output result
for element in wordsList:
    for i in element[1]:
        print i+1,
    print ""
#end while loop for instances