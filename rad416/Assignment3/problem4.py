from collections import deque

inputFile = open('input4.txt','r')

inputQue = deque()

for lines in inputFile:
  inputQue.append(lines.rstrip())

instances = int(inputQue.popleft())

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

def gridCheck():
#    print "Rows\n"
    for i in range(int(rows)):
        stringCat = ""
        for j in range(int(columns)):
            stringCat += grid[i][j]
        wordCheck(stringCat,i,j,"row")
        
#    print "\nColumns\n"
    for j in range(int(columns)):
        stringCat = ""
        for i in range(int(rows)):
            stringCat += grid[i][j]
        wordCheck(stringCat,i,j,"column")

#    print "\nLR Diagonals\n"
    for k in range(0,max(int(rows),int(columns))):
        stringCat = ""
        j = (min(k,int(columns)))
        for i in range(0,min(k+1,int(rows))):
            stringCat += grid[i][j]
            j += -1
        wordCheck(stringCat,i,j,"lrDiag")

#        print stringCat

#    print "\nLR Residual\n"

    for k in range(1,int(rows)):
        stringCat = ""
        j = int(columns) - 1
        for i in range(k,int(rows)):
            stringCat += grid[i][j]
            j += -1
        wordCheck(stringCat,i,j,"lrDiag")

#        print stringCat

#    print "\nRL Diagonals\n"
    l = int(columns) - 1
    for k in range(1,int(columns)):
        stringCat = ""
        j = l
        for i in range(0,min(k,int(rows))):
            stringCat += grid[i][j]
            j += 1
        wordCheck(stringCat,i,j-1,"rlDiag")
#        print stringCat
        l += -1

 #   print"\nRL Residuals\n"
    l = int(rows)
    for k in range(0,int(rows)):
        stringCat = ""
        j = 0
        while (j < l):
            for i in range(k,int(rows)):
                stringCat += grid[i][j]
                j += 1
            wordCheck(stringCat,i,j-1,"rlDiag")
 #           print stringCat
            l +=-1
#end method gridCheck

def wordCheck(stringCat,row,col,stringType):
  for i in range(len(wordsList)):
    stringCatRev = stringCat[::-1]
    if (wordsList[i][1] == -1 and stringCat.find(wordsList[i][0]) >= 0):
      print "Word " + wordsList[i][0] + " in the string " + stringCat + " of type " + stringType + " that ends at " + str(row) + "," + str(col) + " at index " + str(stringCat.find(wordsList[i][0]))
    elif (wordsList[i][1] == -1 and stringCatRev.find(wordsList[i][0]) >= 0): 
      print "Word " + wordsList[i][0] + " in the string " + stringCatRev + " of type " + stringType + " that ends at " + str(row) + "," + str(col) + " at index " + str(stringCatRev.find(wordsList[i][0]))
#        else: 
#            print "Didn't find " + wordsList[i] + " in " + stringCat

#end while loop for instances