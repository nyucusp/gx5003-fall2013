from datetime import datetime, date, time
import sys

dateinput = sys.argv[1] #receive input of "09/19/2013 09:12:15" in the command line
dt = datetime.strptime(dateinput, "%m/%d/%Y %H:%M:%S") #define format of the input value
dt2=datetime.ctime(dt)#convert the input format to the date format that is being used in the Assignment 1 log file.
                      #It is to figure out which lines in the log file are after the date of input

myFile = open('Assignment1Log.txt','r')

state = 0 #to look for commit line
commitDateTimes = []

for line in myFile:
    if(state == 0):#look for commit line
        indexOfCommit = line.find("commit")
        if(indexOfCommit != -1):#found commit
            state = 1 #now find the Date of this commit, which is represented as stage 1
    else:#look for Date line
        indexOfDate = line.find("Date:")
        if(indexOfDate != -1):#found Date from the previous commit
            commitDateTimes.append(line)
            state = 0
myFile.close()

print 'The date/times of the commits after ' + dt2 + ' are '
for commitDateTime in commitDateTimes:
    commitDateTime2 = commitDateTime[8:] # to get the only date part of the Date line,
                                         #I removed the first 8 strings from the line.
                                         #For example, if you look at the Assignment Log file,
                                         #you can see the Date line like 'Date:   Thu Sep 19 11:32:52 2013 -0400' so that I wanted to remove "Date:   "
    commitDateTime3 = commitDateTime2[:-7] # to get the only date part of the Date line, I removed the last 7 strings from the line. For example,
                                           #if you look at the Assignment Log file, you can see the Date line like 'Date:   Thu Sep 19 11:32:52 2013 -0400'
                                           #so that I wanted to remove " -0400 "
    if (commitDateTime3 > dt2): #to get the date of commit when after the commit happened
        print commitDateTime3

