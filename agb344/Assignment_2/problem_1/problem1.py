import datetime
import sys

def getDateTime (dateTimeString, fromLog):
    if fromLog == False:
        return datetime.datetime.strptime(dateTimeString, '%m/%d/%Y %H:%M:%S')
    else:
        return datetime.datetime.strptime(dateTimeString, 'Date: %c')


cutoffText = sys.argv[1]
lastTime = getDateTime(cutoffText, False)

logFile = open('logAfterAssignment1.txt', 'r')

commitLog = []
merge = False


for line in logFile:

    if line.find('commit') == 0:
        commitLog.append(line[:-1])
        nextLine = logFile.next()

        if nextLine.find('Merge') == 0:
            merge = True
            logFile.next()

        commitLog.append(nextLine[:-1])
        line = logFile.next()

    if line.find('Date') == 0 and merge == False:
        commitLog.append(line)
        thisDate = getDateTime(line[:-7], True)

        if thisDate > lastTime:
            for i in commitLog:
                print i

    commitLog = []
    merge = False
