import sys
from datetime import datetime

# myFile = open('logsofar.txt','r')
dateTimeOfInterestString = sys.argv[1] + ' -0400'

dateTimeOfInterest = datetime.strptime(dateTimeOfInterestString, '%m/%d/%Y %H:%M:%S %z')



print dateOfInterest

# # python problem1.py "09/19/2013 09:12:15"
# state = 0
# commitDateTimes = []
# for line in myFile:
#   if(state == 0):#look for author line
#     indexOfCollab = line.find(collabName)
#     if(indexOfCollab != -1): #found a commit from Collab
#       state = 1 #now find the date time of this commit
#   else:
#     indexOfDate = line.find("Date:")
#     if(indexOfDate != -1):#found date from the previous commit
#       commitDateTimes.append(line)
#       state = 0
# myFile.close()
