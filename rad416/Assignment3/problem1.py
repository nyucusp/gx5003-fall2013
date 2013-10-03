import sys
from collections import deque
from decimal import Decimal
from operator import sub

def findPayAvg(inputList): # find the amount each owes 
  def calcPayDiff(inputList, payAvg): # subtract the average from each student
    # subtract the average from each  element
    payDiff = [sub(x,payAvg) for x in inputList] 

    # function to filter only those values greater than 0
    def filterGreaterZero(x): return x>0 

    #filter result list for only those positive values
    posPayList = filter(filterGreaterZero,payDiff)

    #return sum of positive numbers
    return sum(posPayList)

  paymentAvg = round(sum(inputList)/len(inputList),2)
  return calcPayDiff(inputList, paymentAvg)

#open file
inputFile = open('input1.txt','r')

#empty deque for file elements
inputQue = deque()

#read in file elements
for line in inputFile:
  inputQue.append( line.rstrip() )

#empty list to hold student payment elements
inputList = []

#convert elements in deque to list of lists
while (len(inputQue) > 1):
    tempList = []
    studentNum = int(inputQue.popleft())
    for i in range (0,studentNum):
        tempList.append(Decimal(inputQue.popleft()))
    inputList.append(tempList)

output = []

#calc paymax for each list of students
for i in inputList:
  output += findPayAvg(i)

for i in output:
  print "$" + i


