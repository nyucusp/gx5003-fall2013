myFile = open("input4.txt","r")
temp = myFile.readlines()
data = temp[1:]

lines = []
for line in data:
    lines.extend(line.split())

numOfCases = int(temp[0][0])

#Finds the rows of different cases
data = data[2:]
numOfCase = []
numOfCase.append(0)
i = 0
for line in data:
    if line == "\n":
        numOfCase.append(i+2)
    i = i + 1
numOfCase.append(len(data))
numOfCase[numOfCases] = numOfCase[numOfCases]+1


#Extends the grid by two
def wrap(grid, ROWS, COLS):
    return (['.' * (COLS+2)] +
           ['.'+r+'.' for r in grid] +
           ['.' * (COLS+2)])

#Looks through the neighbors
def neighbor():
    for i in range(len(neighbors)):
        dr,dc = neighbors[i]
    return dr,dc

#Gives the matching locations of the first letter
def location(self):
    loc=[]
    for c in xrange(cols):
        for r in xrange(rows):
            if wrap_letters[r][c] == self[0].lower():                
                loc.append([r,c])
    return loc

#Checks the rest of the letters (if they match or not)
def check(self, r, c, dr, dc):
    i = 1
    text=[]
    a,b = r,c
    while(i<len(self)):
        if (wrap_letters[r+dr][c+dc] == self[i]):
            text.append(wrap_letters[r+dr][c+dc])
            r = r + dr
            c = c + dc
            if len(text)== len(self)-1:
                print a,b
                break
        else:
            break
        i=i+1

#Runs main program, gives the result
def main(self):
    for location in locations:
        r,c = location
        i=0
        while(i<len(neighbors)):
            dr, dc = neighbors[i]
            check(self, r, c, dr, dc)
            i=i+1

#neighbors instead of using a lot of different if loops
neighbors = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]


#loop for each case
i=0
while(i<numOfCases):
    a = numOfCase[i]
    rows = int(lines[a])
    b = a+1
    cols = int(lines[b])
    c = b+rows+1
    temp = lines[b+1:c]
    numOfWords = int(lines[c])
    d = c+1
    e = d+numOfWords
    words = lines[d:e]
    letters=[]
    elements=[]
    for elements in temp:    
        letters.append(elements.lower())
    wrap_letters = wrap(letters, rows, cols)
    for word in words:
        locations = location(word)
        main(word)
    print ''
    i=i+1

