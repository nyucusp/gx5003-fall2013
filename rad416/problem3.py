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
  mineCountList = [[0] * len(field[0]) for i in range(len(field))]
  for i in range(len(field[0])):
    for j in range(len(field)):
      mineCountList[i][j] = calcMineSum(field,i,j)
  return mineCountList

  #for each position in field
def calcMineSum(field, row, col):
  mineSum = 0
  rowMax = len(field[0])
  colMax = len(field)
  
  for i in range(row-1,row+2):
    for j in range(col-1, col+2):
      if (i < 0 or j < 0 or i >= rowMax or j >= rowMax or (i == row and j == col)):
        continue
      elif (field[i][j] == "*"):
        mineSum += 1
  return mineSum

def fieldSumCombine(field,mineCount):
  for i in range(len(field[0])):
    for j in range(len(field)):
      if (field[i][j] == "."):
        field[i][j] = mineCount[i][j]
  return field

displayfield(field)

mineCount = countMines(field)
displayfield(fieldSumCombine(field, mineCount))


