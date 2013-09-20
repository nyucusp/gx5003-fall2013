#!/usr/bin/python
import sys


fieldList = []
countedFieldList = []

def getField (rows, columns): #creates a field from user input - assumes correct input
    field = []
    for i in xrange(0, rows):
        row = list(raw_input(""))
        field.append(row)
    return field


def getPair():
    pairText = raw_input("")
    n = int(pairText[0])
    m = int(pairText[2])
    return n, m


def printFields(fieldList): #prints the list of fields
    for idx, i in enumerate(fieldList):
        print "\nField "+str(idx+1)+":"
        for j in i:
            for k in j:
                print k,
            print ""


def countMines(field): #counte the total mines in the field - used for testing
    mines = 0
    clear = 0
    for row in field:
        for location in row:
            if location == '*':
                mines += 1
            else:
                clear +=1
    print "Mines: "+str(mines)+", Clear: "+str(clear)


def countSurrounding(field, row, col): #given a field and location of a cell, counts surrounding mines
    cell = field[row][col]
    if cell == '*':
        #print cell,
        return cell
    last_row = len(field)-1
    last_col = len(field[0])-1
    
    surroundingMines = 0
    
    if (row != 0 and row != last_row and col != 0 and col !=last_col):
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                    if field[i][j] == '*':
                        surroundingMines += 1
    elif row == 0:
        if col == 0:
            #print "top right corner"
            for i in range(row, row+2):
                for j in range(col, col+2):
                    if field[i][j] == '*':
                        surroundingMines +=1
        elif col != last_col:
            #print "top middle"
            for i in range(row, row+2):
                for j in range(col-1, col+2):
                    if field[i][j] == '*':
                        surroundingMines +=1
        else:
            #print "top left corner"
            for i in range(row, row+2):
                for j in range(col-1, col+1):
                    if field[i][j] == '*':
                        surroundingMines +=1
    
    elif row == last_row:
        if col == 0:
            #print "bottom right corner"
            for i in range(row-1, row+1):
                for j in range(col, col+2):
                    if field[i][j] == '*':
                        surroundingMines += 1
        elif col!= last_col:
            for i in range(row-1, row+1):
                for j in range(col-1, col+2):
                    if field[i][j] == '*':
                        surroundingMines += 1
        else:
            for i in range(row-1, row+1):
                for j in range(col-1, col+1):
                    if field[i][j] == '*':
                        surroundingMines += 1
    elif col == 0:
        for i in range(row-1, row+2):
            for j in range(col, col+2):
                if field[i][j] == '*':
                    surroundingMines += 1
    else:
        for i in range(row-1, row+2):
            for j in range(col-1, col+1):
                if field[i][j] == '*':
                    surroundingMines += 1
    

    #print surroundingMines,
    return surroundingMines

def checkField(field): #checks all cells in 'field' using 'countSurrounding()'
    countedField = field
    rows = len(field)
    cols = len(field[0])

    for i in range(0, rows):
        for j in range(0, cols):
            countedField[i][j] = countSurrounding(field, i, j)
    return countedField

def makeFields(): #loops until user inputs 0 0 to create fields - assumes correct input
    n, m = getPair()

    while (n!= 0 and m!=0):
        field = getField(n, m)
        fieldList.append(field)
        countedFieldList.append(checkField(field))
        n, m = getPair()
    
    print ""
    printFields(countedFieldList)

makeFields()
