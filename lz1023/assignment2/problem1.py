import sys
from datetime import datetime

inputDateTime = sys.argv[1]
inputdt = datetime.strptime(inputDateTime, "%m/%d/%Y %H:%M:%S")#format the input time

myFile = open('logfile.txt','r')

commitDateTime = []#create an array of commit datetime
for line in myFile:
	if line.find("Author") != -1:#find author
		author = line

	if line.find("Date") != -1:#find date
		commitdt = datetime.strptime(line[8:-8], "%a %b %d %H:%M:%S %Y")#format the commit time


		if commitdt > inputdt:#compare the commit time and input time
	
			print commitdt
			print author