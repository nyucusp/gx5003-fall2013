#Alex Chohlas-Wood (acw438). Assignment 3, Problem 1.

from decimal import *

rawFile = open('input1.txt', 'r')
input1 = []
for line in rawFile:
    input1.append(line.strip())

#Initialize variables
inputIndex = 0
peopleCount = 0
expensesList = []
expensesMean = 0
expense = 0.0

#While our general index is less than the length of the list:
while inputIndex < len(input1):

    #Get number of people on this trip:
    peopleCount = int(input1[inputIndex])

    #Discard empty trips:
    if peopleCount != 0:

        #Reset moneyTotal
        moneyTotal = Decimal(0)

        #Put personal expenses into a temporary list:
        expensesList = input1[inputIndex+1:inputIndex+peopleCount+1]

        #Make expenses into Decimal instances:
        expensesList = [Decimal(i) for i in expensesList]

        #Find mean of expensesList:
        expensesMean = (sum(expensesList)/len(expensesList)).quantize(Decimal('.01'), rounding=ROUND_UP)
        #Loop through list and accumulate distances above mean:
        for item in expensesList:
            expense = Decimal(item)
            if expense > expensesMean:
                moneyTotal += (expense - expensesMean)

        #Print total distances from mean (total money exchanged):
        print '$' + str(moneyTotal)

    #Move to next trip
    inputIndex += peopleCount + 1

rawFile.close()
