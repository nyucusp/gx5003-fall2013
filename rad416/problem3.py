import sys

#generate field
fieldRows = 3
fieldCols = 3

field = [[".",".","*"],["*",".","."],["*",".","."]]




def displayfield(field):
  for i in range(len(field[0])):
    for j in range(len(field)):
      print field[i][j],
    print "\n"

def countMines(field):
  mineCountArray = []
  for i in range(len(field[0])):
    print "row iteration"
    for j in range(len(field)):
      # mineCountArray[i][j] = 
      calcMineSum(field,i,j)
  # return mineCountArray

  #for each position in field
def calcMineSum(field, row, col):
  mineSum = 0
  rowMax = len(field[0])
  colMax = len(field)
  print "rowMax is ", rowMax
  print "colMax is ", colMax
  print "row is ", row
  print "col is ", col

  for i in range(row-1,row+2):
    for j in range(col-1, col+2):
      print "this is ",i,j
      if (i < 0 or j < 0 or i >= rowMax or j >= rowMax or (i == row and j == col)):
        print "breaking..."
        continue
      elif (field[i][j] == "*"):
        mineSum += 1
  print "The mineSum of cell", row, col, " is ", mineSum

displayfield(field)

# mineCount = 
countMines(field)
# displayfield(mineCount)


