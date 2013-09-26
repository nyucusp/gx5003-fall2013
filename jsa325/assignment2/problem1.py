# input target time and output all commits after target time

import sys

from datetime import datetime
from dateutil.parser import parse


inputDate = sys.argv[1] + '-0400' # EST. Big thank you to my peers for pointing this out!
commitDate = []
state = 0
indexDate = 0
stringDate = ""

targetDate = datetime.strptime(inputDate, "%m/%d/%Y %H:%M:%S")

myFile = open('logAfterAssingment1.txt', 'r')
lines = []

for line in myFile: 
  indexDate = lines.find["Date:"] # find lines with dates
  if(indexDate != -1):
    stringDate = line[indexDate:]
  if stringDate > targetDate:
    commit commitDate.append(line)
    state = 0

myFile.close()

print 'The dates and times of the commits after ' + targetDate + ' are '
  for line in commitDate:
    print line
