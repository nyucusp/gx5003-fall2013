import sys

inputFile = open('input1.txt', 'r')
inputFile.seek(0)
thisLine = inputFile.readline()
tripList = []
averageList = []
finalList = []

while thisLine != '0\n':
    thisTrip = []
    numStudents = int(thisLine[:-1])
    thisLine = inputFile.readline()
    for student in range(0, numStudents):
        thisTrip.append(round(float(thisLine[:-1]),2))
        thisLine = inputFile.readline()
    tripList.append(thisTrip)
    averageList.append(round(round(sum(thisTrip)/len(thisTrip),3),2))

#print tripList
#print averageList

tripAverages = zip(tripList, averageList)

for trip in tripAverages:
    thisPayment = 0
    tripPayments = trip[0]
    tripAverage = trip[1]

    for payment in tripPayments:
        if payment > tripAverage:
            thisPayment += payment - tripAverage
    finalList.append(thisPayment)
    thisPayment = 0

for finalPayment in finalList:
    print '$'+("%.2f"%finalPayment)
