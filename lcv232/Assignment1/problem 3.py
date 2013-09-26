import sys

lines = sys.argv[1]

field = []

def outputField(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
        print field[i][j]
    print "\n"

    def totalofField(field, listMines):
    for i in range(len(field)):
    for j in range(len(field[0])):
        if (field[i][j] == "."):
            field[i][j] == mineList[i][j]
    return field


    def totalofMines(field, x, y):
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


def numberofMines(field):
    putMines = [[0] * len(field[0]) for i in range(len(field))]
    for i in range(len(field)):
    for j in range(len(field[0])):
        putMines[i][j] = totalofMines(field,i,j)
    return putMines


for i in range(1, len(tokens)):
    field.append(list(tokens[i]))

putMines = numberofMines(field)