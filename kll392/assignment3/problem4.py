import sys

myFile = open("input4.txt", "r")

nCases = int(myFile.readline())
myFile.readline()

NM = myFile.readline().split()
m = int(NM[0])
n = int(NM[1])

class Word():
    def __init__(self, word):
        self.word = word
        self.isFound = False
        self.mCoord = 0
        self.nCoord = 0
    def addLocation(self, m_coord, n_coord):
        self.mCoord = m_coord
        self.nCoord = n_coord

"""Create grid"""
grid = []
for i in range (0, m):
    newline = myFile.readline().strip('\n')
    grid.append(newline.lower())

nWords = int(myFile.readline())

"""Create words"""
words = []
for i in range (0, nWords):
    newline = myFile.readline().strip('\n')
    newword = Word(newline.lower())
    words.append(newword)


def searchHorizontal(word, line):
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
                    return (i - len(word.word) + 1)
                if (i == len(line)):
                    break
    return -1

def reverse(grid):
    newgrid = []
    for line in grid:
        line = line[::-1]
        newgrid.append(line)
    return newgrid


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
                    if ((jj == m) or (kk == n)):
                        break
            k += 1
        j += 1
    return -1

verticalGrid = []
for j in range (0, n):
    newline = ''
    for i in range (0, m):
        newline += str(grid[i][j])
    verticalGrid.append(newline)

reverseGrid = reverse(grid)
reverseVerticalGrid = reverse(verticalGrid)

NWdiagonal = reverseGrid[::-1]
NEdiagonal = reverse(NWdiagonal)


#For this problem, I wrote a function to search for each word horizontally (left to right) and one to search for words diagonally from Northwest to Southeast.  I then search for each word in all eight directions by using these two functions and rotating the grid to fit them.  For example, to search for the word backwards horizontally, I run my searchHorizontal function on a grid that has been flipped left to right.  To find a word diagonally from SW to NE, I run my searchDiagonal function on a grid that has been rotated clockwise 90 degrees.  If the word.isFound == True, then that means the word has already been found in the grid, and I compare its existing coordinates to the new ones to see if its place needs to be updated to be either uppermost or leftmost in the grid as requested.
for word in words:

    # Search for horizontal word (West to East):
    linenumber = 1
    for line in grid:
        place = searchHorizontal(word, line)
        if (place != -1):
            word.isFound = True
            word.addLocation(linenumber, place)
            break
        linenumber += 1

    # Seach for horizontal backwards word (East to West):
    linenumber = 1
    for line in reverseGrid:
        place = searchHorizontal(word, line)
        if (place != -1):
            if (word.isFound == False):
                word.isFound = True
                word.addLocation(linenumber, n - place + 1)
            elif (word.isFound == True):
                if (word.mCoord >= linenumber):
                    if (word.nCoord > n - place + 1):
                        word.addLocation(linenumber, n - place + 1)
        linenumber += 1

    # Search for vertical word (North to South):
    linenumber = 1
    for line in verticalGrid:
        place = searchHorizontal(word, line)
        if (place != -1):
            if (word.isFound == False):
                word.isFound = True
                word.addLocation(place, linenumber)
            elif (word.isFound == True):
                if (place < word.mCoord):
                    word.addLocation(place, linenumber)
                elif (place == word.mCoord):
                    if (linenumber < word.nCoord):
                        word.addLocation(place, linenumber)
        linenumber += 1

    # Search for vertical word (South to North):
    linenumber = 1
    for line in reverseVerticalGrid:
        place = searchHorizontal(word, line)
        if (place != -1):
            if (word.isFound == False):
                word.isFound = True
                word.addLocation(m - place + 1, linenumber)
            elif (word.isFound == True):
                if ((m - place + 1) < word.mCoord):
                    word.addLocation(m - place + 1, linenumber)
                elif ((m - place + 1) == word.mCoord):
                    if (linenumber < word.nCoord):
                        word.addLocation(m - place + 1, linenumber)
        linenumber += 1

    # Search for diagonal word (direction: Southeast):
    if (searchDiagonal(word, grid) != -1):
        if (word.isFound == False):
            word.isFound = True
            xx, yy = searchDiagonal(word, grid)
            word.addLocation(xx, yy)
        elif (word.isFound == True):
            if (xx < word.mCoord):
                word.addLocation(xx, yy)
            elif (xx == word.mCoord):
                if (yy < word.nCoord):
                    word.addLocation(xx, yy)
                
    # Search for diagonal word (direction: Southwest):
    if (searchDiagonal(word, reverseGrid) != -1):
        if (word.isFound == False):
            word.isFound = True
            xx, yy = searchDiagonal(word, reverseGrid)
        elif (word.isFound == True):
            if (xx < word.mCoord):
                word.addLocation(xx, n - yy + 1)
            elif (xx == word.mCoord):
                if ((n - yy + 1) < word.nCoord):
                    word.addLocation(xx, n - yy + 1)

    #Search for diagonal word (direction: Northwest):
    if (searchDiagonal(word, NWdiagonal) != -1):
        if (word.isFound == False):
            word.isFound = True
            xx, yy = searchDiagonal(word, NWdiagonal)
            word.addLocation(m - xx + 1, n - yy + 1)
        elif (word.isFound == True):
            if ((m - xx + 1) < word.mCoord):
                word.addLocation(m - xx + 1, n - yy + 1)
            elif ((m - xx + 1) == word.mCoord):
                if ((n - yy + 1) < word.nCoord):
                    word.addLocation(m - xx + 1, n - yy + 1)

    # Search for diagonal word (direction: Northeast)
    if (searchDiagonal(word, NEdiagonal) != -1):
        if (word.isFound == False):
            word.isFound = True
            xx, yy = searchDiagonal(word, NEdiagonal)
        elif (word.isFound == True):
            if ((m - xx + 1) < word.mCoord):
                word.addLocation(m - xx + 1, yy)
            elif ((m - xx + 1) == word.mCoord):
                if (yy < word.nCoord):
                    word.addLocation(m - xx + 1, yy)


for word in words:
    print word.mCoord, word.nCoord
print ''

myFile.close()
