#Alex Chohlas-Wood (acw438). Assignment 1, Problem 2.

import sys
intList = map(int, sys.argv[1:]) #store intList as sequence of integers
diffLen = intList[0] #number of "divisions" between integers
intList.pop(0) #remove list length integer at beginning of input

checkList = list() #ordered list of successes for each difference
for x in range(diffLen-1):
    checkList.append(0)

if checkList == []:#to handle exception of single integer sequence
    print "Jolly"
else:
    for x in range(diffLen-1):
        indexCk = abs(intList[x]-intList[x+1]) - 1
        if checkList[indexCk] == 0: #true if this difference hasn't been found yet
            if x == diffLen-2: #if we've gone through the whole sequence
                print "Jolly"
            checkList[indexCk] = 1 #otherwise mark the difference as found
        else:
            print "Not jolly"
            break #as soon as repeat is found, print "not jolly" and quit
