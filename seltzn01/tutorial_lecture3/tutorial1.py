# Nathan Seltzer
# Tutorial 1

import sys
collabName = sys.argv[1]

myFile = open('logsofar.txt', 'r')

state = 0
commitDateTimes = []
for line in myFile:
	if(state == 0): # look for author line
		indexOfCollab = line.find(collabName)
		if (indexOfCollab != -1): # found a commit from Collab 
			state = 1 # now find the date time fo this commit
	else:
		indexOfDate = line.find("Date:")
		if(indexOfDate != -1): # found date from the previous commit
			commitDateTimes.append(line)
			state = 0
myFile.close()

print 'The date/times of the commits of ' + collabName + ' were ' 
for  commitDateTimes in commitDateTimes:
	print commitDateTimes

outputFile = open('output.txt', 'w')

for commitDateTimes in  commitDateTimes:
	outputFile.write(commitDateTimes)
outputFile.close()
