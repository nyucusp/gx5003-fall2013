# Awais Malik
# Assignment 2
# Problem 1

import sys
from datetime import datetime
from dateutil.parser import parse

# Extracting the due date and due time from input
due_date = datetime.strptime(sys.argv[1], '%m/%d/%Y %H:%M:%S')

logs = open('logAfterAssignment1.txt','r')

LateCommits = []

# Function to convert date in commit to datetime object
def convertdate(rawdate):
    rawdate = rawdate[8:-6]
    return parse(rawdate)

# Find the Date line in logs and check if it is after the due_date
for line in logs:
    indexofDate = line.find("Date:")
    if(indexofDate != -1):
        dateline = convertdate(line)
        if(dateline > due_date):
            LateCommits.append(dateline)

print LateCommits