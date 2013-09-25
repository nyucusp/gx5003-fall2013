from datetime import datetime, date, time
import sys

#first parse input
dt = datetime.strptime(sys.argv[1], "%m/%d/%Y %H:%M:%S") 
print dt

#now go through log file and print post-date commits
commit = ''
lfile = open('logAfterAssignment1.txt','r')
for line in lfile:
	if 'commit' in line and not line[0] == '\t':
		commit = line.split()[1]
	elif 'Date:' in line and not line[0] == '\t':
		lspl = line.split()
		#example line: "Date:   Fri Sep 20 10:27:36 2013 -0400"
		dt_temp = datetime.strptime(lspl[2]+" "+lspl[3]+" "+lspl[5]+" "+lspl[4], "%b %d %Y %H:%M:%S")
		if dt_temp>dt:
			print commit
		
