import sys 

myFile = open('input1.txt','r')
numStudents = 0
expenses = []
TotalExpenses = 0.0
for line in myFile:
    if line != '0':
        numStudents += 1
        expenses.append(float(line.strip()))
        TotalExpenses += float(line.strip())
avgExpense = round(TotalExpenses / numStudents,2)
print "NumStudents: " + str(numStudents)
print "expenses: " + str(expenses)
print "TotalExpenses: " + str(TotalExpenses)
print "AvgExpense: " + str(avgExpense)

diffExpenses = []
for i in range (0,numStudents-1):
    diffExpenses.append(round(expenses[i] - avgExpense,2))

print "diffExpenses: " + str(diffExpenses)

expGiven = []
expReceived = []
expGivenAmount = 0.0
expReceivedAmount = 0.0

for i in range (0, numStudents-1):
    if diffExpenses[i] > 0:
        expReceived.append(diffExpenses[i])
        expReceivedAmount += diffExpenses[i]
    else:
        expGiven.append(diffExpenses[i])
        expGivenAmount -= diffExpenses[i]

print "expGiven: " + str(expGiven)
print "expReceived: " + str(expReceived)

print "expGivenAmount: " + str(expGivenAmount)
print "expReceivedAmount: " + str(expReceivedAmount)


if expGivenAmount < expReceivedAmount:
    print "$%.2f" % (expGivenAmount)
else:
    print "$%.2f" % (expReceivedAmount)