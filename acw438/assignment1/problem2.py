#Alex Chohlas-Wood (acw438). Assignment 1, Problem 2.

import sys
intList = map(int, sys.argv[1:]) #store intList as sequence of integers
diffLen = len(intList)-1 #number of "divisions" between integers

checkList = list() #list of successes for each jolly #
for x in range(diffLen):
    checkList.append(0)

if checkList == []:#to handle exception of single integer sequence
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
            break #as soon as repeat is found, print "not jolly" and quit
