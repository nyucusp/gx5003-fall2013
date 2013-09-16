import sys

#generate field
fieldRows = 3
fieldCols = 3

field = [[".",".","*"],["*",".","."],["*",".","."]]

#write matrix
#def writeMatrix(rows, cols):

def displayMatrix(matrix):
  for i in range(len(matrix[0])):
    for j in range(len(matrix)):
      print matrix[i][j],
    print "\n"

displayMatrix(field)


#generate counts of mines
