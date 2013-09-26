import sys
import time
DateTimes = sys.argv[1]
#turn the input of directive of date and time into an object called DeadLine.
DeadLine = time.strptime(DateTimes, "%m/%d/%Y %H:%M:%S")
#open and read the file of logAfterAssignment.txt
myFile = open('logAfterAssignment1.txt','r')

commitDateTimes = []
for line in myFile:
	#read and save the lines of Author so we can prints the one who passes the dead line.
	if line.find("Author") != -1:
		authorline = line
	#go through the lines of Date and compare them with the DeadLine and find out those which pass it.	
	if line.find("Date") != -1:
		Datefound = time.strptime(line[8:-7], "%a %b %d %H:%M:%S %Y")

		if Datefound > DeadLine:
			print line[8:-7]
			print authorline


myFile.close()
