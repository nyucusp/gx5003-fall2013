import sys

inputFile = open("input4.txt", "r")                 # open .txt file

numCases = int(inputFile.readline())
inputFile.readline()

NM = inputFile.readline().split()
m = int(NM[0])
n = int(NM[1])

"""
Define a class Word with memebers self. Define a function addLoc that takes 
members and their locations in the grid as input.
"""

class Word():
  def __init__(self, word):
    self.word = word
    self.isFound = False
    self.mLoc = 0
    self.nLoc = 0
  def addLoc(self, mLoc, nLoc):
    self.mLoc = mLoc
    self.nLoc = nLoc

"""
Create grid.
"""

grid = []                                                 
for i in range (0, m):
  newline = inputFile.readline().strip('\n')
  grid.append(newline.lower())

numWords = int(inputFile.readline())

"""
Create list of words.
"""

words = []
for i in range (0, numWords):
  newline = inputFile.readline().strip('\n')
  newword = Word(newline.lower())
  words.append(newword)

"""
Define a function searchLR (search left-right) that takes words and lines 
as input.
"""

def searchLR(word, line):
  for i in range (0, len(line)):
    if (line[i] == word.word[0]):
      search = True
      j = 0
      while search is True:
        if (line[i] == word.word[j]):
          i += 1
          j += 1
        else:
          search = False
        if (j == len(word.word)):
          return (i = len(word.word) + 1)
        if (i == len(line)):
          break
  return -1

def reverse(grid):
    newGrid = []
    for line in grid:
        line = line[::-1]
        newgrid.append(line)
    return newGrid
    
"""
Define a function searchDiagonal that takes words and lines and grid as
input.
"""

def searchDiagonal(word, grid):
  j = 0
  for line in grid:
    k = 0
    for letter in line:
      if (letter == word.word[0]):
        search = True
        i = 0
        count = 0
        jj = j
        kk = k
        while search is True:
          if (grid[jj][kk] == word.word[i]):
            jj += 1
            kk += 1
            count += 1
          else:
            break
          if (count == len(word.word)):
            return j + 1, k + 1
          i += 1
          if (i == len(word.word)):
            break
          if ((jj = m) or (kk = n)):
            break
      k += 1
    j += 1
  return -1

UDGrid = []                               # up-down grid
for j in range (0, n):
  newline = ''
  for i in range (0, m):
    newline += str(grid[i][j])
  UDGrid.append(newline)
  
"""
I create mirror images of the grids and iterate the two search functions searchLR
and searchDiagonal over the original grids and the reversed grids to search in all 
directions.
"""

reverseGrid = reverse(grid)
reverseUDGrid = reverse(UDGrid)

ULdiagonal = reverseGrid[::-1]            # BR to UL diagonal
URdiagonal = reverse(ULdiagonal)          # BL to UR diagonal

for word in words:
  linenumber = 1
  for line in grid:
    place = searchLR(word, line)          # search for horizontal word (left to right)
    if (place != -1):
      word.isFound = True
      word.addLoc(linenumber, place)
      break
    linenumber += 1

  linenumber = 1
  for line in reverseGrid:                # reverse the grid
    place = searchLR(word, line)          # search for horizontal word in reverseGrid
    if (place != -1):
      if (word.isFound == False):
        word.isFound = True
        word.addLoc(linenumber, n - place + 1)
      elif (word.isFound == True):
        if (word.mLoc >= linenumber):
          if (word.nLoc > n - place + 1):
            word.addLoc(linenumber, n - place + 1)
    linenumber += 1

  linenumber = 1
  for line in UDGrid:
    place = searchLR(word, line)          # search for vertical word (left to right in UDGrid)
    if (place != -1):
      if (word.isFound == False):
        word.isFound = True
        word.addLoc(place, linenumber)
      elif (word.isFound == True):
        if (place < word.mLoc):
          word.addLoc(place, linenumber)
        elif (place == word.mLoc):
          if (linenumber < word.nLoc):
            word.addLoc(place, linenumber)
    linenumber += 1

  linenumber = 1
  for line in reverseUDGrid:              # reverse the grid
    place = searchLR(word, line)          # search for vertical word in reverseUDGrid
    if (place != -1):
      if (word.isFound == False):
        word.isFound = True
        word.addLoc(m - place + 1, linenumber)
      elif (word.isFound == True):
        if ((m - place + 1) < word.mLoc):
          word.addLoc(m - place + 1, linenumber)
        elif ((m - place + 1) == word.mLoc):
          if (linenumber < word.nLoc):
            word.addLoc(m - place + 1, linenumber)
    linenumber += 1

  if (searchDiagonal(word, grid) != -1):  # search for diagonal word from UL to BR
    if (word.isFound == False):
      word.isFound = True
      xx, yy = searchDiagonal(word, grid)
      word.addLoc(xx, yy)
    elif (word.isFound == True):
      if (xx < word.mLoc):
        word.addLoc(xx, yy)
      elif (xx == word.mLoc):
        if (yy < word.nLoc):
          word.addLoc(xx, yy)
                
  if (searchDiagonal(word, reverseGrid) != -1):     # search for diagonal word UR to BL
    if (word.isFound == False):
      word.isFound = True
      xx, yy = searchDiagonal(word, reverseGrid)
    elif (word.isFound == True):
      if (xx < word.mLoc):
        word.addLoc(xx, n - yy + 1)
      elif (xx == word.mLoc):
        if ((n - yy + 1) < word.nLoc):
          word.addLoc(xx, n - yy + 1)

  if (searchDiagonal(word, ULdiagonal) != -1):      # search for diagonal word BR to UL
    if (word.isFound == False):
      word.isFound = True
      xx, yy = searchDiagonal(word, ULdiagonal)
      word.addLoc(m - xx + 1, n - yy + 1)
    elif (word.isFound == True):
      if ((m - xx + 1) < word.mLoc):
        word.addLoc(m - xx + 1, n - yy + 1)
      elif ((m - xx + 1) == word.mLoc):
        if ((n - yy + 1) < word.nLoc):
          word.addLoc(m - xx + 1, n - yy + 1)

  if (searchDiagonal(word, URdiagonal) != -1):      # search for diagonal word BL to UR
    if (word.isFound == False):
      word.isFound = True
      xx, yy = searchDiagonal(word, URdiagonal)
    elif (word.isFound == True):
      if ((m - xx + 1) < word.mLoc):
        word.addLoc(m - xx + 1, yy)
      elif ((m - xx + 1) == word.mLoc):
        if (yy < word.nLoc):
          word.addLoc(m - xx + 1, yy)


for word in words:
  print word.mLoc, word.nLoc
print ''

inputFile.close()
