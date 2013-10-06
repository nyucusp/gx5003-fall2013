import sys

#converting the given string time to datetime
#from dateutil.rrule import*
from datetime import *
from dateutil.parser import *
givenDateTime = "09/19/2013 09:12:15"
#givenDateTime = sys.argv[1] + " " + sys.argv[2]
parsedDT =parse( givenDateTime, None )
#dt_obj= datetime.strptime(date_str,"%m/%d/%Y %H:%M:%S")
#print repr(dt_obj)
print parsedDT
import os
#commits that happened after this date
myfile= open ('logAfterAssignment1.txt','r')
myfilelines=[]

for line in myfile:
	myfilelines.append(line)
i=0
while i < len(myfilelines):
	Getdate=myfilelines[i].find("Date:")
	if Getdate!=-1:
		commitDate=parse(myfilelines[i][8:-6])
		if commitDate >= parsedDT:
		    #myfilelines.append(myfile)
		    print myfilelines[i-2], myfilelines[i-1], myfilelines[i], myfilelines[i+1], myfilelines[i+2]

	i=i+1


#     Getdate= datetime.strptime(line[8:-6])
