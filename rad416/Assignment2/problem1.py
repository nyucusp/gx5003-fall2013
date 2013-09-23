import sys
from datetime import datetime, timedelta
from dateutil.parser import parse

# python problem1.py "09/19/2013 09:12:15"
dateTimeOfInterestString = sys.argv[1] + '-0400'
dateTimeOfInterest = parse(dateTimeOfInterestString)
print dateTimeOfInterest

myFile = open('logsofar.txt','r')

for line in myFile:
  if "Date:" in line: #find a line with a date
    line_combine = "" #blank line to accept date
    line_split = line.split(" ") #split the line
    for i in range(4,9): #iterate through the germane parts of line
      line_combine += " " + line_split[i] #create line string
    date_line = parse(line_combine)
    if (date_line - dateTimeOfInterest >= timedelta(0)):
      print date_line, "After DOI"
    else:
      print date_line, "Before DOI"


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
myFile.close()
