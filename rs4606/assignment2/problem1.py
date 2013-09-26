import sys
import datetime
date_input = sys.argv[1]

"""
First we turn the input date into a nice datetime object called date_compare
"""
date = date_input.split()[0]
time = date_input.split()[1]

month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:10])

hour = int(time[0:2])
minute = int(time[3:5])
second = int(time[6:8])

date_compare = datetime.datetime(year, month, day, hour, minute, second)

"""
We now open the file and save the lines in a list called "lines"
"""
myFile = open('logAfterAssignment1.txt', 'r')

lines = []
for line in myFile:
    lines.append(line)
myFile.close()

"""
Finally, we go through the list "lines" and when we find a line that begins with a date,
we compare date_compare from above, with the date in the line (converted to a 
datetime object also).
"""
num_lines = len(lines)
for i in range(0, num_lines):
    if lines[i].find("Date:") != -1 and i < (num_lines):
        if date_compare < datetime.datetime.strptime(lines[i][8:-7], "%a %b %d %H:%M:%S %Y"):
            for j in range(-3,3):
                print lines[i+j]
