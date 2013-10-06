import sys
import re
from datetime import *
import dateutil.parser as parser
from dateutil.tz import *

#The three variables below were created just so I could try other modules and functions in this problem
date = sys.argv[1]
time = sys.argv[2]
dT = date + " " + time

start = datetime.strptime(sys.argv[1] + " " + sys.argv[2], "%m/%d/%Y %H:%M:%S")
#In the line below, I was going to use "parser", but decided to go the route I used above
#testEntry = parser.parser().parse(dT + " -0400", None )
#print testEntry

# read the file
lines = open('logfile.txt', 'r').readlines()


entries = []
current_entry = []
for line in lines:
    # clean the line
    line = line.strip()

    # read until end of entry
    if line[:7] == 'commit ':
        # this is the start of a new entry, so put the old one in the list
        if len(current_entry) > 3 and 'Date: ' in current_entry[3]:
            entries.append(current_entry)

        # and start a new one
        current_entry = []

    current_entry.append(line)



for entry in entries:

    #grab the date line and split
    date_string, offset = entry[3].rsplit(' ', 1)
    #print date_string

    #make this info into a datetime object
    entry_time = datetime.strptime(date_string, "Date:     %a %b %d %H:%M:%S %Y")


    #adjust the entry time for the timezone difference. 4 hours = 14400 seconds
    entry_time = entry_time + timedelta(0, 14400)
    #The line below, I tried to use tzoffset, but I could not get it to function correctly
    #entry_time = entry_time(tzoffset(None, -14400)).astimezone(tzutc())


    #Print entries which are equal to or later than the time which was entered
    if entry_time >= start:
        for line in entry:
            print line


###################################################
#Below this: Original code attempts as I worked through the problem
######################################################

#change into usable format to compare to file...
#split into parts
# startDateSplit = startDate.split("/", 2)
# startTimeSplit = startTime.split(":", 2)

# #change items from str to ints
# startTimeSplit = map(int, startTimeSplit)
# startDateSplit = map(int, startDateSplit)

#account for time zone
# zoneCount = 4
# while (zoneCount != 0):
#     if startTimeSplit[0] != 0:
#         startTimeSplit[0] = startTimeSplit[0] - 1
#         zoneCount = zoneCount - 1

#     else:
#         startTimeSplit[0] = 23
#         zoneCount = zoneCount - 1
#         startDateSplit[1] = startDateSplit[1] - 1

# #open log file
# logFile = open('logfile.txt', 'r')
# #save lines to list
# logFileList = logFile.readlines()
# #get length of list
# numOfLines = len(logFileList)
# #read through file checking for "dates", differences in date/times
# lineNum = 0


# lineNumKeeper = []
# print numOfLines
# while lineNum != numOfLines:
#     #if its a date line
#     if logFileList[lineNum].find("Date") !=-1:
#         dateTimeLine = []
#         lineNumKeeper.append(lineNum)
#         finalLine = 0
#         i = 0

#         #split up line into parts
#         dateTimeLine = logFileList[lineNum].split()
#         #trim uneeded pieces
#         dateTimeLine.pop(0)
#         dateTimeLine.pop(0)
#         dateTimeLine.pop(0)
#         timePart = dateTimeLine[1]
#         #split time by :
#         timePart = timePart.split(":", 2)
#         #trim of old time stamp
#         dateTimeLine.pop(1)
#         #make sure elements are ints
#         dateTimeLine = map(int, dateTimeLine)

#         timePart = map(int, timePart)


#         if dateTimeLine[0] >= startDateSplit[1]:

#             print logFileList[i]
#             i = i + 1
#             return i
#             #compare hours
#             if timePart[0] >= startTimeSplit[0]:
#                 print logFileList[i]
#                 i = i + 1
#                 #compare minutes
#                 if timePart[1] >= startTimeSplit[1]:
#                     print logFileList[i]
#                     i = i + 1
#                     if timePart[2] >= startTimeSplit[2]:
#                         print logFileList[i]
#                         i = i + 1
#                         #finalLine = len(lineNumKeeper)
#                         #print finalLine
#                     else:
#                         print "Top"


#                 else:
#                     print "prior minute"
#             else:
#                 print "prior hour"

#         else:
#             print "prior date"

#         lineNum = lineNum + 1
#         #compare date/time



#     #if it's not a date line
#     else:
#         lineNum = lineNum + 1

# #if >/= date/time, then add to list
# #collect all following commits into a list


# #Test Area
# print startTimeSplit
# print startDateSplit

