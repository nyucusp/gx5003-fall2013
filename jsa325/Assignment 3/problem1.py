import sys

inputFile = open('input1.txt', 'r')                       # open .txt file

inputLines = []                                           # save lines in a list
for line in inputFile:
  inputLines.append(line)
inputFile.close()

"""
Define a function that will take costs (as floats) as input and will print as output the 
minimum amount of money (again as floats) that needs to be exchanged to equalize the costs. 
The function will first compute the average cost avg, which will give the net cost for each 
person, then compute the distance between the average cost and the individual costs. The 
minimum amount minAMT of money that needs to change hands to equalize costs is then the sum 
over the differences.
"""

def minCostEqualize(costList):
    avg = sum(costList)/len(costList)                     # compute average cost
    minAmt = 0.00
    for elt in costList:
        if elt <= avg:                                    # if an element is less than or equal to the average
            minAmt += round((avg - elt), 2)               # round to the nearest cent when computing the difference
    return minAmt
    
"""
Parse through inputLines. Find positive integer that denotes number of students on the trip, 
and convert subsequent integers to floats and feed to printMinAmt, and print the result. 
Append a 0 to the result of printMinAmt if the result has only one decimal place.
"""
    
for i in range(0,len(inputLines)):
    if inputLines[i].find(".") == -1:                     # find integer that denotes the number of students on the trip
        expenses = []                                     # save subsequent integers in a list of expenses
        for j in range(i+1, i+int(inputLines[i])+1):
            expenses.append(float(inputLines[j]))         # convert integers to floats
        if len(expenses) > 0:
            if len(str(printMinAmt(expenses) - int(printMinAmt(expenses)))) > 3:
                print printMinAmt(expenses)
            else: 
                print str(printMinAmt(expenses)) + "0"    # append a 0 on the end of a float that has only 1 decimal place
