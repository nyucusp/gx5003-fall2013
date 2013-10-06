import sys
from datetime import datetime
date = sys.argv[1]

date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S')
file = open('commitdata.txt')
print file
print date

count = 0
for line in file:
	if line.find('Date:') != -1:
		string = line[8:-7]
		linedate = datetime.strptime(string, '%a %b %d %H:%M:%S %Y')
		if linedate > date:
			count = count + 1

			print linedate
print count