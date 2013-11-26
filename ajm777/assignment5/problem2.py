#Aliya Merali
#Urban Informatics
#Assignment 5
#Problem 2

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.dates as dt
from matplotlib import ticker
from datetime import datetime

data = open('actions-fall-2007.dat','r')

deadlines_dates = ['2007-09-18 12:00:00','2007-09-18 12:00:00','2007-10-04 12:00:00', '2007-10-25 12:00:00','2007-11-27 12:00:00','2007-12-11 12:00:00', '2007-12-15 12:00:00']
deadlines_list = []
for element in deadlines_dates:
    temp = datetime.strptime(element.strip(), '%Y-%m-%d %H:%M:%S')
    temp2 = dt.date2num(temp)
    deadlines_list.append(temp2)

actions = []
for line in data: 
    actions.append(line)
del actions[0]

times = []
for event in actions: 
    event_date = datetime.strptime(event.strip(),'%Y-%m-%d %H:%M:%S')
    event_date_num = dt.date2num(event_date)
    times.append(event_date_num)

#Figure out the date2num number for 10 hour period 
date_1 = dt.date2num(datetime.strptime('2007-09-18 12:00:00','%Y-%m-%d %H:%M:%S'))
date_2 = dt.date2num(datetime.strptime('2007-09-19 12:00:00','%Y-%m-%d %H:%M:%S'))
date_interval = date_2 - date_1
#Now use this to get bin size of 10 hours by dividing range by this to get number of bins
date_range = max(times) - min(times)
num_bins = date_range/date_interval

plot_bin_range_min = dt.date2num(datetime.strptime('2007-09-11 12:00:00','%Y-%m-%d %H:%M:%S'))
plot_bin_range_max = dt.date2num(datetime.strptime('2007-12-25 12:00:00','%Y-%m-%d %H:%M:%S'))

plt.hist(times, bins = num_bins, range = (plot_bin_range_min, plot_bin_range_max))
for deadline in deadlines_list:
    plt.vlines(deadline, 0, 14000, colors = 'r', linestyles = 'solid')
plt.vlines(deadlines_list[0], 0, 14000, colors = 'r', linestyles = 'solid', label = 'Assignment Due Date')

plt.title('Scientific Visualization Assignment Actions in 2007')
plt.xlabel('Timestamp')
plt.ylabel('Number of Actions')
plt.xticks(np.arange(plot_bin_range_min, plot_bin_range_max, 10))

plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda numdate, _: dt.num2date(numdate).strftime('%m-%d,%H:%M:%S')))
plt.gcf().autofmt_xdate()
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

#___________Problem 2 Annotations
"""
(2a) For this histogram, I selected bins that would represent 24 hour periods.
I did this by first calculating the date2num number of 24 hour period, then 
dividing the total range plotted by this period. This gave me the appropriate
number of bins to make each approximately 24 hours. I chose this number 
because I felt that it would represent the amount of work on a timescale 
small enough to show when the most work is being done, but large enough not 
to overcrowd the plot. I found with smaller bins, it was very difficult to 
see the amound of work being done around the deadlines because of the volume 
of bins.

(2b) By looking at this histogram, you can see that the amount of work 
(number of actions) increases significantly around the deadlines. This 
indicates that people generally tend to complete the work closer to the 
deadline, and then some are forced to work even after the deadline. You 
can also see that this trend started at the second assignment and got more
extreme for the later assignments, indicating that people becan the semester 
by starting work early but ended the semester by working more closer to the 
deadline. 

(2c) It appears that the amount of work approaching the deadline increases 
exponentially  for the later deadlines. It may be that early on in the 
semester, students started assignments earlier, and later in teh semester, 
they left the assignments until much closer to the deadline and were forced 
to work on them much more just before and just after the deadlines. 
"""
