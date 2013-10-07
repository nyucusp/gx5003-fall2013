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
  wordsList.append(inputQue.popleft().lower())

def gridCheck():
  print "Rows\n"
  for i in range(int(rows)):
    stringCat = ""
    for j in range(int(columns)):
      stringCat += grid[i][j]
    wordCheck(stringCat)
      
  print "\nColumns\n"
  for j in range(int(columns)):
    stringCat = ""
    for i in range(int(rows)):
      stringCat += grid[i][j]
    wordCheck(stringCat)

  print "\nLR Diagonals\n"
  for k in range(0,max(int(rows),int(columns))):
    stringCat = ""
    j = (min(k,int(columns)))
    for i in range(0,min(k+1,int(rows))):
      stringCat += grid[i][j]
      j += -1
    wordCheck(stringCat)
    # print stringCat

  print "\nLR Residual\n"

  for k in range(1,int(rows)):
    stringCat = ""
    j = int(columns) - 1
    for i in range(k,int(rows)):
      stringCat += grid[i][j]
      j += -1
    wordCheck(stringCat)
    # print stringCat

  print "\nRL Diagonals\n"
  l = int(columns) - 1
  for k in range(1,int(columns)):
    stringCat = ""
    j = l
    for i in range(0,min(k,int(rows))):
      stringCat += grid[i][j]
      j += 1
    wordCheck(stringCat)
    # print stringCat
    l += -1

  print"\nRL Residuals\n"
  l = int(rows)
  for k in range(0,int(rows)):
    stringCat = ""
    j = 0
    while (j < l):
      for i in range(k,int(rows)):
        stringCat += grid[i][j]
        j += 1
      wordCheck(stringCat)
      # print stringCat
      l +=-1
#end method gridCheck

def wordCheck(stringCat):
  for i in range(len(wordsList)):
    if stringCat.find(wordsList[i]) >= 0:
      print "Found " + wordsList[i] + " in " + stringCat
    elif stringCat[::-1].find(wordsList[i]) >= 0: 
      print "Found " + wordsList[i] + " in " + stringCat
#        else: 
#            print "Didn't find " + wordsList[i] + " in " + stringCat

#end while loop for instances