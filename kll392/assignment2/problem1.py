#Kara Leary
#Urban Informatics
#Assignment 2, Problem 1

import sys
import datetime

myFile = open('gitlog.txt', 'r') #open file titled 'gitlog.txt' in my repository

#this puts the file into an array so it can be accessed later onto be printed:
lines = tuple(open('gitlog.txt', 'r'))

temptime = sys.argv[1]
searchdate = datetime.datetime(int(temptime[6:10]),int(temptime[0:2]), int(temptime[3:5]), int(temptime[11:13]), int(temptime[14:16]), int(temptime[17:19]))

month = 0
day = 0
year = 0
hour = 0
minute = 0
second = 0

#The function defined here, 'isafterdate' takes a reference date (the date after 
#which we want to find all commits, and a current date (the date of the commit being 
#checked).  It returns 'true' if the current date is after the reference date, 
# and returns 'false' if it is prior to the reference date

def isafterdate(refdate, currentdate):
    if (currentdate.year > refdate.year):
        return 'true'
    elif (currentdate.year == refdate.year):
        if (currentdate.month > refdate.month):
            return 'true'
        elif (currentdate.month == refdate.month):
            if (currentdate.day > refdate.day):
                return 'true'
            elif (currentdate.day == refdate.day):
                if (currentdate.hour > refdate.hour):
                    return 'true'
                elif (currentdate.hour == refdate.hour):
                    if (currentdate.minute > refdate.minute):
                        return 'true'
                    elif (currentdate.minute == refdate.minute):
                        if (currentdate.second >= refdate.second):
                            return 'true'
    else:
        return 'false'

i = 0 #i is a counter that increments after each line is read. I use it to print
      #lines from the 'lines' tuple created earlier

for line in myFile:
    isDate = line.find("Date:")              #find if a line contains a date
    if (isDate == 0):
        indexdate = line[12:15]              #switch the name of the month for number
        if (indexdate == "Jan"):
            month = 1
        elif (indexdate == "Feb"):
            month = 2
        elif (indexdate == "Mar"):
            month = 3
        elif (indexdate == "Apr"):
            month = 4
        elif (indexdate == "May"):
            month = 5
        elif (indexdate == "Jun"):
            month = 6
        elif (indexdate == "Jul"):
            month = 7
        elif (indexdate == "Aug"):
            month = 8
        elif (indexdate == "Sep"):
            month = 9
        elif (indexdate == "Oct"):
            month = 10
        elif (indexdate == "Nov"):
            month = 11
        else:
            month = 12
        k = 0                                #k is used to correct for a missing '0' in front of a day (i.e. Sep 06 vs Sep 6)
        if (int(line[16]) == 1 or int(line[16]) == 2 or int(line[16]) == 3):
            if (int(line[17]) == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0):
                k = 1
        thisLineDate = datetime.datetime(int(line[(27+k):(31+k)]), int(month), int(line[16:(17+k)]), int(line[(18+k):(20+k)]), int(line[(21+k):(23+k)]), int(line[(24+k):(26+k)]))
        isdate = isafterdate(searchdate, thisLineDate)   #use function defined previously to determine chronology
        if (isdate == 'true'):
            print lines[i-1]      #if the date of commit is after reference date, print the date and author from 'lines' tuple
            print lines[i]
            print ' '
    i += 1





        
