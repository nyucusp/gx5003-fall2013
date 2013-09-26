import sys
import time
import datetime

myFile = open('logAfterAssignment1.txt','r')
dateq = sys.argv[1]
t = time.strptime(dateq, "%m/%d/%Y %H:%M:%S")
deadline=datetime.datetime(t[0], t[1], t[2],t[3], t[4], t[5])


state= 0
commitDateTimes =[]
commitCommit=[]
for line in myFile:
	if(state == 0):
		indexOfCollab=line.find("Date:")
		if(indexOfCollab != -1):
			#r=commitDateTimes.append(line)
			str=line
			temp=str.split()			
			a= time.strptime(temp[1]+" "+temp[2]+" "+temp[3]+" "+temp[4]+" "+temp[5],"%a %b %d %H:%M:%S %Y")
			ctime=datetime.datetime(a[0], a[1], a[2],a[3], a[4], a[5])			
			if (ctime>deadline):
			        	state =1
	else: 
		indexOfDate = line.find("Author")
		if(indexOfDate != -1):
			commitCommit.append(line)
			state =0
myFile.close()	

print 'The date/times of the commits of'  
for commitCommit in commitCommit:
	print commitCommit
