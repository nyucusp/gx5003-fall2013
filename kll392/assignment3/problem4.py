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

myFile.close()

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

lastinvert = reverseGrid[::-1]
NNE = reverse(lastinvert)

print 'normal grid'
for line in grid:
    print line

print ''
print 'reverse grid'
for line in reverseGrid:
    print line
 
print ''
print 'last invert'
for line in lastinvert:
    print line 

print ''
print 'reverse vertical grid'
for line in reverseVerticalGrid:
    print line

for word in words:
    if (word.isFound == False):
        linenumber = 1
        for line in grid:
            place = searchHorizontal(word, line)
            if (place != -1):
                word.isFound = True
                print word.word, linenumber, place
                break
            linenumber += 1
    if (word.isFound == False):
        linenumber = 1
        for line in reverseGrid:
            place = searchHorizontal(word, line)
            if (place != -1):
                word.isFound = True
                print word.word, linenumber, n - place + 1
                break
            linenumber += 1
    if (word.isFound == False):
        linenumber = 1
        for line in verticalGrid:
            place = searchHorizontal(word, line)
            if (place != -1):
                word.isFound = True
                print word.word, place, linenumber
            linenumber += 1
    if (word.isFound == False):
        linenumber = 1
        for line in reverseVerticalGrid:
            place = searchHorizontal(word, line)
            if (place != -1):
                word.isFound = True
                print word.word, m - place + 1, linenumber
            linenumber += 1
    if (word.isFound == False):
        if (searchDiagonal(word, grid) != -1):
            word.isFound = True
            xx, yy = searchDiagonal(word, grid)
            print word.word, xx, yy
    if (word.isFound == False):
        if (searchDiagonal(word, reverseGrid) != -1):
            word.isFound = True
            xx, yy = searchDiagonal(word, reverseGrid)
            print word.word, xx, n - yy + 1
    if (word.isFound == False):
        if (searchDiagonal(word, lastinvert) != -1):
            word.isFound = True
            xx, yy = searchDiagonal(word, lastinvert)
            print word.word, m - xx + 1, n - yy + 1
    if (word.isFound == False):
        if (searchDiagonal(word, NNE) != -1):
            word.isFound = True
            xx, yy = searchDiagonal(word, NNE)
            print word.word, m - xx + 1, yy
