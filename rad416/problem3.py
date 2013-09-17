import sys

# A script to take in the definition of a minefield using "." for a clear spot and "*" for a mine.
# Counts are provided for the mines in any of the touching cells and outputed to the terminal.
# The lines shoud be demarcated with a "\n".
# For example, to generate a minefield that looks like this:

# . . *
# * . . 
# * . . 

# Enter the following on the command line: python problem3.py "3 3\n..*\n*..\n*.."
# A matrix of the mine locations and the counts of mines touching non-mine cells will be
# outputed to the console. 

def displayfield(field):
  for i in range(len(field)):
    for j in range(len(field[0])):
      print field[i][j],
    print "\n"

def countMines(field):
  mineCountList = [[0] * len(field[0]) for i in range(len(field))]
  for i in range(len(field)):
    for j in range(len(field[0])):
      mineCountList[i][j] = calcMineSum(field,i,j)
  return mineCountList

  #for each position in field
def calcMineSum(field, row, col):
  mineSum = 0
  rowMax = len(field)
  colMax = len(field[0])
  for i in range(row-1,row+2):
    for j in range(col-1, col+2):
      if (i < 0 or j < 0 or i >= rowMax or j >= colMax or (i == row and j == col)):
        continue
      elif (field[i][j] == "*"):
        mineSum += 1
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

mineCount = countMines(field)
displayfield(fieldSumCombine(field, mineCount))


