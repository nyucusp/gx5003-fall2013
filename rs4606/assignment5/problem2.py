"""
Note: annotations that answer the questions in the assignment are at the *bottom* of this
code.
"""

import sys
import numpy
import matplotlib.pyplot as plt
import datetime as DT
from matplotlib.dates import date2num, MonthLocator, DateFormatter


"""
First we open the text file and save the lines to the list input_lines
"""


inputfile = open('actions-fall-2007.dat', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()



"""
Next we create a list called timestamp_days, which contains just the days associated
with all the timestamps.  We define a day as going from noon (including noon)
to noon on the *next* day, so, for example, a timestamp of the form 2007-09-15 21:24:56 
would correspond to the day 2007-09-15, whereas a timestamp of the form 
2007-09-15 09:24:56 would correspond to the day 2007-09-14
"""
timestamp_days = []

for i in range(1, len(input_lines)):
    time_object = DT.datetime.strptime(input_lines[i][:-1], "%Y-%m-%d %H:%M:%S")
    if time_object.time() >= DT.time(12,0,0):
        timestamp_days.append(time_object.date())
    else:
        corrected_date = time_object.date() - DT.timedelta(days=1)
        timestamp_days.append(corrected_date)

"""
Now we create the histogram.
"""

#setting background color
chart = plt.figure()
chart.patch.set_facecolor('white')

ax = chart.add_subplot(1,1,1,)

counts, bins, patches = ax.hist(date2num(timestamp_days), bins=68, facecolor='grey')
ax.set_xticks(bins)
plt.subplots_adjust(bottom=.15)

#labeling the x axis with month names
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter('%B'))


#set x axis limit here
ax.set_xlim(DT.date(2007,9,2))



#labeling the vertical lines that show when assignments are due
assignment_dates = ['2007-09-18', '2007-10-04', '2007-10-25', '2007-11-27', '2007-12-15', '2007-12-11']
assignment_dates2 = []
for elt in assignment_dates:
    assignment_dates2.append(DT.datetime.strptime(elt, "%Y-%m-%d"))

vlines_labels = ['Assignment 0 and 1 due', 'Assignment 2 due', 'Assignment 3 due', 'Assignment 4 due', 'Assignment 5 due', 'Assignment 6 due']

for i in range(0, 6):
    plt.text(assignment_dates2[i],9000 + 1000*i,vlines_labels[i],rotation=0, size='small')

#plotting vertical lines that show when assignments are due
plt.vlines(date2num(assignment_dates2), 0, 16000, linestyle = 'dashed')

#creating the title and y-axis label
plt.title("Daily count of student actions, Sept-Dec 2007")
plt.ylabel("Number of actions")


chart.set_size_inches(14,5)
plt.show()



"""
Answers to questions:
a) I selected 68 bins for the histogram corresponding to the 68 distinct dates that
had student activity timestamps.  This is enough bins to get a feel for trends in the data
but not too much that the plot becomes unmanageable.  I labeled the bins by month, however
as this makes it easier for the viewer understand.  (I got this idea from Alex C.W.)

b) We can see that the total amount of work for the first three assignments was considerably
less than for the last four assignments. Assignments 3, 4, and 6 in particular had a lot
of activity (so they probably required a lot of work).

c) We can see that the amount of work for an assignment spikes dramatically right before
the assignment is due (and in the case of assignments 3 and 4, the day after also.  Maybe
students are turning in their assignments slightly late).

"""
