import sys
import time
DateTimes = sys.argv[1]
#We turn the input of directive of date and time into an object called DeadLine.
DeadLine = time.strptime(DateTimes, "%m/%d/%Y %H:%M:%S")
#open and read the file of logsofar.txt
myFile = open('logAfterAssignment1.txt','r')
state = 0
commitDateTimes = []
for line in myFile:
	#read and save the lines of Author so we can prints the one who passes the dead line.
	if line.find("Author") != -1:
		authorline = line
	#Now we go through the lines of Date and compare them with the DeadLine and find out those which pass it.	
	if line.find("Date") != -1:
		Datefound = time.strptime(line[8:-7], "%a %b %d %H:%M:%S %Y")

		if Datefound > DeadLine:
			print line
			print authorline


myFile.close()
