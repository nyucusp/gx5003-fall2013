import sys
from datetime import datetime, date, time
import time
#Using datetime.strptime()
datetemp = sys.argv[1]
datetemp1 = datetime.strptime(datetemp,"%m/%d/%Y %H:%M:%S")
##datetemp2 = datetemp1.ctime()

print datetemp1

myFile = open("logAfterAssignment1.txt","r")

lateAuthor = []
submissionDate = []
count = 0
for date in myFile:
    if(count==0):
        indexofDate = date.find("Date:")        
        if indexofDate != -1:
            ds = date.split()
            x = (str(ds[2])+' '+str(ds[3])+' '+str(ds[5])+' '+str(ds[4]))
            subDate = datetime.strptime(x,"%b %d %Y %H:%M:%S",)
            if subDate>datetemp1:
                submissionDate.append(date)
                count = 1
    else:
        indexofAuthor = date.find("Author:")
        if indexofAuthor !=-1:
            lateAuthor.append(date)
            count = 0
myFile.close()

mydic = dict(zip(lateAuthor, submissionDate))

for key, value in mydic.iteritems() :
    print 'Late Submission','\n',key, value
    
