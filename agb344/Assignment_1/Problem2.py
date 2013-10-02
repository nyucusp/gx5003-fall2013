#!/usr/bin/python
import sys

n = int(sys.argv[1])
list = sys.argv[2:]
intList = map(int, list)
possibleList = range(1, n)
diffList = []

if(n == len(list)):
    for i in xrange(1, n):
       #print intList[i]
       #print intList[i-1]
       diffList.append(abs(intList[i]-intList[i-1]))

    if sorted(diffList) == sorted(possibleList):
        print "Jolly"
    else:
        print "Not Jolly"

else:
    print "Please enter a valid input"
#print diffList
#print possibleList
