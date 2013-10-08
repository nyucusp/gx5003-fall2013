import sys
from datetime import datetime
deadline = datetime.strptime(sys.argv[1],"%m/%d/%Y %H:%M:%S")
Func1 = open('logAfterAssignment1.txt','r')
date1 = []
commit = []
count = 0

# For loop condition to set commits on date

for line in Func1:
    if count == 0: 
        commit = line.find("Mark as Commit.")
        if commit != -1:
            commit.append(line)
            count = count + 1
    else: 
            mark = line.find("The Date is:")
            if mark != -1:
                data = date1.strptime(line[8:-7],"%a %b %d %H:%M:%S %Y")
                if data > deadline:
                    for x in commit:
                        print x
                    count = 0
Func1.close()              
            
