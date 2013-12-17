# #Nathan Seltzer
# #Homework 5
# #Problem2.py


"""
I worked on this problem for a long amount of time taking many approaches.
However, I was unable to figure out how to complete it. I first tried using
the dateutil parser, but couldn't get the date entries inside. I then moved
onto the strptime function of datetime which did effectively get the date
entries successfully into datetime format. But I could not figure out how
to get those plotted onto a histogram. But to answer the questions:

A) I would choose 72 bins because thats aproximately the amount of days
between the first submitted and last submitted student action.

B and C) I can't really do this since I couldn't get the output, but I
bet that the distribution was skewed towards each due date -- a lot of
students did the majority of their assignment actions closer towards the
due date, while less did it ahead of time.  

"""


from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import numpy
from dateutil.parser import *



f = open('actions-fall-2007.dat', 'r') #opens file with intention of reading, but hasn't read yet
f.readline()

#created index
datelist =[]

# append the "datelist" with the entries in datetime format.
for line in f:
	numChars = line[0:19]
	datelist.append(datetime.strptime(numChars,'%Y-%m-%d %X'))
# %X was a helpful shortcut

timebinsDict = defaultdict(int)
for line in datelist:
    timebinsDict[line.strftime('%m-%d')] += 1


#Assignmnet due dates for later tick marks
Due0 = "2007-09-18 12:00:00"
Due1 = "2007-09-18 12:00:00"
Due2 = "2007-10-04 12:00:00"
Due3 = "2007-10-25 12:00:00"
Due4 = "2007-11-27 12:00:00"
Due5 = "2007-12-15 12:00:00"
Due6 = "2007-12-11 12:00:00"

#check to see whether it actually worked
print datelist[1]
print datelist[-1]

#based off the starting and end dates that I printed, I created
#beggining and ending points for the histogram
start = datetime.strptime('2007-09-09 21:24:56','%Y-%m-%d %X')
end = datetime.strptime('2007-12-08 17:30:27','%Y-%m-%d %X')

"""
The following was my attempt to get the histogram set up
"""

# plt.figure()
# plt.title('Distribution of Student Actions')
# plt.xlabel('Time')
# plt.ylabel('Action Count')


# totaltime = date.DayLocator(end - start)
# bins = numpy.arange(1, totaltime + 2) 
# plt.hist(datelist, bins=72)


# plt.legend()






plt.show()


# date_object = datetime.strptime(fl,'%y-%m-%d %H:%M:%S')

# p