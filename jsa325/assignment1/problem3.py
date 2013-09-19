input sys

lines = sys.argv[1]
tokens = lines.split('\\n')

field = []

def printField(field):
    for i in range(len(field)):
    for j in range(len(field[0])):
        print field[i][j]
    print "\n"

def countMines(field):
    listMines = [[0] * len(field[0]) for i in range(len(field))]
    for i in range(len(field)):
    for j in range(len(field[0])):
        listMines[i][j] = sumMines(field,i,j)
    return listMines

def sumMines(field, x, y):
    count = 0
    xMax = len(field)
    yMax = len(field[0])
    for i in range(max(0, x - 1), min(xMax, x + 2)):
    for j in range(max(o, y - 1), min(yMax, y + 2)):
        if (i == x and j == y):
            continue
        elif (field[i][j] == "*"):
            count += 1
    return count

def sumField(field, listMines):
    for i in range(len(field)):
    for j in range(len(field[0])):
        if (field[i][j] == "."):
            field[i][j] == mineList[i][j]
    return field

for i in range(1, len(tokens)):
    field.append(list(tokens[i]))

listMines = countMines(field)
printField(sumMines(field,listMines))
