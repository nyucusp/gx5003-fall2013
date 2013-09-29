import sys

#converting the given string time to datetime
from datetime import datetime, date, time
import dateutil.parser as timePR
#date_str = "09/19/2013 09:12:15"
givenDateTime = sys.argv[1] + " " + sys.argv[2]
parsedDT = timePR.parser().parse( givenDateTime, None )
#dt_obj= datetime.strptime(date_str,"%m/%d/%Y %H:%M:%S")
#print repr(dt_obj)
print parsedDT

#commits that happened after this date
myfile= open ('logAfterAssignment1.txt','r')
myfilelines=[]

for line in myfile:
  myfilelines.append(line)
i=0

while i < len(myfilelines):
  Getdate =myfilelines[i].find("Date:")

  if(Getdate !=-1):
    commitDate= timePR.parse(myfilelines[i][8:-6])


    if commitDate >= parsedDT:
        #myfilelines.append(myfile)
      print myfilelines[i-2], myfilelines[i-1], myfilelines[i], myfilelines[i+1], myfilelines[i+2]
  i=i+1


#     Getdate= datetime.strptime(line[8:-6])


myfile.close()

# for key,value in mydic.iteritems():
#   print 'GetDate' , '\n',key,value
