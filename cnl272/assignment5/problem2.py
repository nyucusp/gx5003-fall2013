import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.dates as dt
from matplotlib import ticker
from datetime import datetime

myfile = open('actions-fall-2007.dat','r')
actions = []
times = []

deadline = ['2007-09-18 12:00:00','2007-09-18 12:00:00','2007-10-04 12:00:00',
'2007-10-25 12:00:00','2007-11-27 12:00:00','2007-12-11 12:00:00', '2007-12-15 12:00:00']
deadline_list= []
for date in deadline:
	temp_data = datetime.strptime(date.strip(), '%Y-%m-%d %H:%M:%S')
	temp_data2 = dt.date2num(temp_data)
	deadline_list.append(temp_data2)

for line in myfile:
	actions.append(line)
del actions[0]
for event in actions:
	event_data = datetime.strptime(event.strip(), '%Y-%m-%d %H:%M:%S')
	event_date_data = dt.date2num(event_data)
	times.append(event_date_data)

time1 = dt.date2num(datetime.strptime('2007-09-18 12:00:00','%Y-%m-%d %H:%M:%S'))
time2 = dt.date2num(datetime.strptime('2007-09-19 12:00:00','%Y-%m-%d %H:%M:%S'))

time_interval = time2 - time1
time_range = max(times)-min(times)
bins_number = time_range/time_interval

plot_bin_range_min = dt.date2num(datetime.strptime('2007-09-11 12:00:00','%Y-%m-%d %H:%M:%S'))
plot_bin_range_max = dt.date2num(datetime.strptime('2007-12-25 12:00:00','%Y-%m-%d %H:%M:%S'))

plt.hist(times, bins_number, range=(plot_bin_range_min, plot_bin_range_max), color='pink')
for deadline in deadline_list:
    plt.vlines(deadline, 0, 16000, colors = 'y', linestyles = 'solid')
plt.vlines(deadline_list[0], 0, 16000, colors = 'y', linestyles = 'solid', label = 'Due Time')

plt.xlabel("Dates", fontsize = 14)
plt.title("Actions in Science VIsualization Course, 2007", fontsize = 15)
plt.ylabel("Number of Actions", fontsize=14)
plt.xticks(np.arange(plot_bin_range_min, plot_bin_range_max, 10))
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda numdate, _: dt.num2date(numdate).strftime('%m/%d/%H:%M:%S')))
plt.gcf().autofmt_xdate()
plt.legend(loc = 'upper left')

duedays=['2007-09-18 12:00:00', '2007-10-04 12:00:00', '2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-11 12:00:00','2007-12-15 12:00:00']
due=[]
for k in duedays:
    due.append(datetime.strptime(k,'%Y-%m-%d %H:%M:%S'))
label=['Assignment 0&1','Assignment 2','Assignment 3','Assignment 4','Assignment 5','Assignment 6']   
for x in range(0,6):
    plt.text(due[x],10000+1000*x,label[x],size='small')
plt.vlines(dt.date2num(due),1000,16000, color="green")
plt.savefig('Problem2.png')

plt.show()
'''
(a)The bins I chose represent 24-hour periods based on the deadline on 12:00:00.
(b)From the histogram, it is obvious that the number of actions reaches the peak around deadlines while the semester approaching to final.
Therefore, there seems to be a trend that students tend to work earlier in the beginning of the semester, 
but forced to work on the last moment in the end of the semester.
(c)The number of actions increases significantly around the deadlines, especially for the last three assignments.
There is a large number of students handing their Assignment 3 after the deadline, and some handing late the Assignment 4.
Most of them still hand their assignments on time, especially for the first and second assignment.
