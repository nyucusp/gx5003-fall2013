import sys
collabName = sys.argv[1]

myFile = open('logsofar.txt','r')
outputFile = open('output.txt','w')

state = 0
commitDateTimes= []
for line in myFile:
    if(state==0):   
        indexOfCollab = line.find(collabName)
        if (indexOfCollab != -1):
            state = 1
    else: 
        indexOfDate = line.find("Date:")
        if (indexOfDate != -1):
            commitDateTimes.append(line)
            state = 0
myFile.close()

outputFile.write( 'The date/times of the commits of ' + collabName + ' were ' + '\n')
for commitDateTime in commitDateTimes:
    outputFile.write("\n" + commitDateTime)
outputFile.close()

