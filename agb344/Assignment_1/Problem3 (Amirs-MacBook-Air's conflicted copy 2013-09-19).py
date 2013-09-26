#!/usr/bin/python
import sys

#pairText = raw_input("enter field\n")
#n = int(pairText[0])
#m = int(pairText[2])

#fieldSizeList = []
#fieldList = []

#while(n!=0 and m!=0):
    #n_m = (n, m)
    #print n_m
    #fieldSizeList.append(n_m)
    #pairText = raw_input("")
    #field = []
    #for i in xrange(0, n-1):
        #row = raw_input("")
        #while len(row)!=m:
            #print "Please enter a valid row"
        #field.append(list(row))
        #print field
    #pairText = raw_input("")
    #n = int(pairText[0])
    #m = int(pairText[2])
    #fieldList.append(field)




#print fieldList

fieldList = []



def getField (rows, columns):
    #print "new", rows, " by ", columns, " field"
    field = []
    for i in xrange(0, rows):
        row = list(raw_input(""))
        field.append(row)
    return field


#for i in range (0,5):
    #field = getField(4, 4)
    #fieldList.append(field)

#print fieldList

def getPair():
    pairText = raw_input("")
    n = int(pairText[0])
    m = int(pairText[2])
    return n, m

def printFields(fieldList):
    for idx, i in enumerate(fieldList):
        print "field "+str(idx+1)+":"
        for j in i:
            for k in j:
                print k,
            print ""
        countMines(i)

def countMines(field):
    mines = 0
    clear = 0
    for row in field:
        for location in row:
            if location == '*':
                mines += 1
            else:
                clear +=1
    print "Mines: "+str(mines)+", Clear: "+str(clear)


def countSurrounding(field, row, col):
    cell = field[row][col]
    if cell == '*':
        return cell
    #print cell
    last_row = len(field)-1
    last_col = len(field[0])-1
    surroundingMines = 0
    
    if (row != 0 and row != last_row and col != 0 and col !=last_col):
        #print "not edge"
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                    #print field[i][j]
                    if field[i][j] == '*':
                        surroundingMines += 1
    #else:
        #print "edge"
    #for i in range(row-1, row+2):
        #for j in range(col-1, col+2):
                    #print field[i][j]
                    #if field[i][j] == '*':
                        #surroundingMines += 1
    print surroundingMines
    return surroundingMines

def makeFields():    
    n, m = getPair()

    while (n!= 0 and m!=0):
        field = getField(n, m)
        fieldList.append(field)
        n, m = getPair()

        printFields(fieldList)
