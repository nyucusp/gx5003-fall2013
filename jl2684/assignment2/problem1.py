
import sys
dateInput = str(sys.argv[1]) 

logFile = open('/home/jeongki/gx5003-fall2013/jl2684/assignment2/logsofar.txt','r') 

import time 
from datetime import datetime
from dateutil.parser import parse

dateConverted = parse(dateInput)
dateConverted = dateConverted.replace(tzinfo=None)

latelist = []
for line in logFile:

	indexOfdate = line.find("Date:")
	indexOfend = line.find(' -0400')
	if indexOfdate != -1:

		dateline = line[indexOfdate:indexOfend]
		dateline = dateline.replace('Date:   ', '')
		dateline = dateline.replace('  -0700 ','')

		dateSubmitted = parse(dateline)
		dateSubmitted = dateSubmitted.replace(tzinfo=None)


		if dateSubmitted > dateConverted:
			latelist.append(name)
			latelist.append(dateline)
	pass
print latelist

logFile.close()