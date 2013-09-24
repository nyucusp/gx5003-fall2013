#Aliya Merali
#Assignment 1 - Problem 3

import sys

lines = sys.argv[1]
inputval = lines.split('\\n')

val = inputval[0].split(' ')
m = int(val[0])
n = int(val[1])

x=0
y=1
if (inputval[x][0]=='.' or inputval[x][0]=='*'):
    x=x+1
else:
    print 'Field# ' + str(y)        
    y = y+1
    x=x+1

def cellvalue(i, j):
    if i<0 or j<1 or i>=n or j>m:
        return 0
    if inputval[j][i] == '*':
        return 1
    else:
        return 0

y=1
while y<=m:
    x=0
    while x<n :
        count = 0
        count = count + cellvalue(x-1,y-1)
        count = count + cellvalue(x,y-1)
        count = count + cellvalue(x+1,y-1)
        count = count + cellvalue(x-1,y)
        count = count + cellvalue(x+1,y)
        count = count + cellvalue(x-1,y+1)
        count = count + cellvalue(x,y+1)
        count = count + cellvalue(x+1,y+1)
        if inputval[y][x]=='*':
            print '*',
        else:
            print count,
        x=x+1
    print
    y=y+1
