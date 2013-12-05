import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as date
from matplotlib.dates import date2num, MonthLocator, DateFormatter

#read input file
action=[]
myfile=open('actions-fall-2007.dat','r')
for i in myfile:
    action.append(i)
del action[0]
action.sort()

# change time to numbers
time=[]
for j in action:
    a=dt.datetime.strptime(j.strip(),'%Y-%m-%d %H:%M:%S')
    b=date.date2num(a)
    time.append(b)


#define bins
a=max(time)-min(time)
bins=int(a)+1

#histogram
begin= date.date2num(dt.datetime.strptime('2007-09-10 12:00:00','%Y-%m-%d %H:%M:%S'))
final= date.date2num(dt.datetime.strptime('2007-12-18 12:00:00','%Y-%m-%d %H:%M:%S'))
plt.hist(time, bins, range=(begin, final))

plt.xlabel('Time')
plt.ylabel('Actions')
plt.title('Students actions of assignments')
plt.gca().xaxis.set_major_formatter(DateFormatter('%m-%d'))



deadline=['2007-09-18 12:00:00', '2007-10-04 12:00:00', '2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-11 12:00:00','2007-12-15 12:00:00']
due=[]
for k in deadline:
    due.append(dt.datetime.strptime(k,'%Y-%m-%d %H:%M:%S'))


label=['Assignment 0&1','Assignment 2','Assignment 3','Assignment 4','Assignment 5','Assignment 6']
    
for x in range(0,6):
    plt.text(due[x],10000+1000*x,label[x],size='small')
plt.vlines(date2num(due),0,16000)

plt.show()
# (a) The bin is 24 hours according to the due time 12:00:00.          
# (b) From the number of actions, assignment 3 and 5 have the most amount of work
# (c) Most students handing on assignments before deadline in assignment 0,1,4 and 6.