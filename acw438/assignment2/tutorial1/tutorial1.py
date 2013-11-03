import sys
collabName = sys.argv[1]

myFile = open('logsofar.txt','r')

state = 0
commitDateTimes = []
for line in myFile:
    if(state==0):#look for author line
        indexOfCollab = line.find(collabName)
        if(indexOfCollab != -1): #found a commit from Collab
            state = 1 #now find the date time of this commit
            #commitDateTimes.append(line)
    else:
        indexOfDate = line.find("Date:")
        if(indexOfDate != -1): #found date from previous commit
            commitDateTimes.append(line)
            state = 0

myFile.close()

outputFile = open('output.txt', 'w')

#print 'The date/times of the commits of', collabName, 'were:'
for commitDateTime in commitDateTimes:
    outputFile.write(commitDateTime)
outputFile.close()
