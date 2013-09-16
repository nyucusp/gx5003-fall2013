#Alex Chohlas-Wood (acw438). Assignment 1, Problem 2.

import sys
intList = map(int, sys.argv[1:])
diffLen = len(intList)-1

checkList = list()
for x in range(diffLen):
    checkList.append(0)

if checkList == []:
    print "Jolly"
else:
    for x in range(diffLen):
        indexCk = abs(intList[x]-intList[x+1]) - 1
        if checkList[indexCk] == 0:
            if x == diffLen-1:
                print "Jolly"
            checkList[indexCk] = 1
        else:
            print "Not jolly"
            break
