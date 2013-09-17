import sys

def displayfield(field):
  for i in range(len(field)):
    for j in range(len(field[0])):
      print field[i][j],
    print "\n"

def countMines(field):
  mineCountList = [[0] * len(field[0]) for i in range(len(field))]
  for i in range(len(field)):
    for j in range(len(field[0])):
      print "running calcMineSum(",i,j,")"
      mineCountList[i][j] = calcMineSum(field,i,j)
  return mineCountList

  #for each position in field
def calcMineSum(field, row, col):
  mineSum = 0
  rowMax = len(field)
  colMax = len(field[0])
  print "rowMax is",rowMax
  print "colMax is",colMax
  
  print "for cell ", row, col
  
  for i in range(row-1,row+2):
    for j in range(col-1, col+2):
      print "testing cell", i, j 
      if (i < 0 or j < 0 or i >= rowMax or j >= colMax or (i == row and j == col)):
        print "breaking..."
        continue
      elif (field[i][j] == "*"):
        print "counting..."
        mineSum += 1
  print "mineSum is",mineSum
  return mineSum

def fieldSumCombine(field,mineCount):
  for i in range(len(field)):
    for j in range(len(field[0])):
      if (field[i][j] == "."):
        field[i][j] = mineCount[i][j]
  return field

lines = sys.argv[1]
lines_split = lines.split('\\n')

field = []

for i in range(1,len(lines_split)):
  field.append(list(lines_split[i]))

displayfield(field)

mineCount = countMines(field)
displayfield(fieldSumCombine(field, mineCount))


