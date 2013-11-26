import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.dates as dt
from matplotlib import ticker
from datetime import datetime

data = open('actions-fall-2007.dat','r') #open file

ddl_date = ['2007-09-18 12:00:00','2007-09-18 12:00:00','2007-10-04 12:00:00',
'2007-10-25 12:00:00','2007-11-27 12:00:00','2007-12-11 12:00:00', '2007-12-15 12:00:00'] #deadlines's dates
ddl_lst = []
for element in ddl_date:
    temp = datetime.strptime(element.strip(), '%Y-%m-%d %H:%M:%S')
    temp2 = dt.date2num(temp)
    ddl_lst.append(temp2)
#assignemnts
assignments = []
for line in data: 
    assignments.append(line)
del assignments[0]
#number & times of assignments
num_time = []
for event in assignments: 
    event_date = datetime.strptime(event.strip(),'%Y-%m-%d %H:%M:%S')
    event_date_num = dt.date2num(event_date)
    num_time.append(event_date_num)

#10 hour period for date1
date1 = dt.date2num(datetime.strptime('2007-09-18 12:00:00','%Y-%m-%d %H:%M:%S'))
date2 = dt.date2num(datetime.strptime('2007-09-19 12:00:00','%Y-%m-%d %H:%M:%S'))
date_interval = date2 - date1#
#bins size divided by 10= number of bins
date_range = max(num_time) - min(num_time)
num_bins = date_range/date_interval

#plot 
plot_bin_range_min = dt.date2num(datetime.strptime('2007-09-11 12:00:00','%Y-%m-%d %H:%M:%S'))#Limits of minimum date
plot_bin_range_max = dt.date2num(datetime.strptime('2007-12-25 12:00:00','%Y-%m-%d %H:%M:%S'))#Limits of maximum date

plt.hist(num_time, bins = num_bins, range = (plot_bin_range_min, plot_bin_range_max))
for deadline in ddl_lst:
    plt.vlines(deadline, 0, 14000, colors = 'y', linestyles = 'solid')
plt.vlines(ddl_lst[0], 0, 14000, colors = 'y', linestyles = 'solid', label = 'Due Dates')

plt.title('Histogram for Assignments')
plt.xlabel('TimeStamp')
plt.ylabel('Number of Assignments')
plt.xticks(np.arange(plot_bin_range_min, plot_bin_range_max, 10))

plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda numdate, _: dt.num2date(numdate).strftime('%m/%d/%H:%M:%S')))
plt.gcf().autofmt_xdate()
plt.legend(loc='center left')

plt.tight_layout()
plt.show()