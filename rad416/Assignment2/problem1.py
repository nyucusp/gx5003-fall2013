# A script to take in a time from the command line and display all commits 
# that occured at or after the time passed.  Output to STDOUT

import sys
from datetime import datetime, timedelta
from dateutil.parser import parse

dateTimeOfInterestString = sys.argv[1] + '-0400' #append EST timezone to datetime string
dateTimeOfInterest = parse(dateTimeOfInterestString) #parse string to datetime obj

#open and read from file
myFile = open('logsofar.txt','r')
file_list = [] #list to hold file elements
for line in myFile: #iterator through the file to create list of file elements
  file_list.append(line)
myFile.close() #close file since no longer used

#iterate through and test file
for i in range(0,len(file_list)):
  line_test = file_list[i] #temporary variable to hold line from list
  if "Date:" in line_test: #find a line with a date
    line_split = line_test.split(" ") #split the line
    line_combine = "" #blank line to accept date
    for j in range(4,9): #iterate through the germane parts of line
      line_combine += " " + line_split[j] #create line string
    date_line = parse(line_combine) #create date time object for comparison
    if (date_line - dateTimeOfInterest >= timedelta(0)): #test for date being equal or greater to date of interest
      if "Merge" in file_list[i-2]: #check that the line to be printed doesn't start with Merge
        print file_list[i-3], #print line above "Merge"
      else:
        print file_list[i-2], #pring line of commit