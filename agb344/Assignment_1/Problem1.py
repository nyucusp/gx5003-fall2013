#!/usr/bin/python
import sys

tempList = []
occurenceList = []

def prob1(n):
    tempList.append(n)
    if n==1:
        return 1
    elif n%2==0:
        return prob1(n/2)
    else:
        return prob1((3*n)+1)

Arg1 = int(sys.argv[1])
Arg2 = int(sys.argv[2])

for i in xrange(Arg1,Arg2+1):
    prob1(i)
    occurenceList.append(len(tempList))
    tempList=[]

print Arg1, Arg2, max(occurenceList)
