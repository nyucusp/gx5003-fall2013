import pylab
import scipy
import csv
import sys
import scipy
import array
from matplotlib import *
from pylab import *
from scipy import *
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.ticker as mticker 
from matplotlib import dates 
import datetime 
from scipy import stats
import dateutil.parser as dparser
from matplotlib import pyplot as PLT 
import collections 
import itertools
from matplotlib.dates import date2num



actions_file = open('actions-fall-2007.dat', 'rU')
actions_lines = csv.reader(actions_file)





list_actions = [] 
for x in actions_lines:
	list_actions.append(x)

#print list_actions[0]
list_actions = list_actions[1:]




list_dates = [] 

for x in list_actions:
	for i in x: 
		print i 
		list_dates.append(dparser.parse(i, fuzzy=True))

#print list_dates


bin_24_hours =  date2num(dparser.parse('2007-12-09 11:30:25', fuzzy=True)) - date2num(dparser.parse('2007-12-08 11:30:25', fuzzy=True)) 


list_deadlines_string = ['2007-09-18 12:00:00', '2007-09-18 12:00:00', '2007-10-04 12:00:00', '2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-15 12:00:00', '2007-12-11 12:00:00'] 

list_deadlines = [] 
for x in list_deadlines_string:
	list_deadlines.append(dparser.parse(x, fuzzy=True))


hfmt = dates.DateFormatter('%m/%d %H:%M')

fig, ax = plot.subplots()

#print min(date2num(list_dates)) 
#print max(date2num(list_dates))
#print bin_two_hours

list_bin = np.arange (min(date2num(list_dates)), max(date2num(list_dates)), bin_24_hours) 
 

ax.hist(date2num(list_dates), bins = list_bin)
ax.set_xticks(date2num(list_deadlines))
ax.xaxis.set_major_formatter(hfmt)
plot.xticks(rotation='vertical')

#ax.axis(num2date(date2num(list_dates)))

#deadlines 
plot.axvline(x=date2num(list_deadlines[0]), linestyle='-', color='orange', label='Deadlines')
plot.axvline(x=date2num(list_deadlines[1]), linestyle='-', color='orange')
plot.axvline(x=date2num(list_deadlines[2]), linestyle='-', color='orange')
plot.axvline(x=date2num(list_deadlines[3]), linestyle='-', color='orange')
plot.axvline(x=date2num(list_deadlines[4]), linestyle='-', color='orange')
plot.axvline(x=date2num(list_deadlines[5]), linestyle='-', color='orange')
plot.legend(loc='upper left', prop={'size':12}) 


fig.suptitle('Problem 2', fontsize = 14)
plot.xlabel('Actions', fontsize = 14)
plot.ylabel('Submissions', fontsize=14)
#plot.legend(loc='upper left', prop={'size':14})

plot.tight_layout()



#ax.xaxis.set_major_locator(years)
#ax.xaxis.set_major_formatter(autoFmt)
#ax.xaxis.set_minor_locator(months)



plot.show()

fig.savefig('Problem_2.png')
actions_file.close


'''
a) I chose 24 hours period to see how in advance students do their works (like a day ahead). Also smaller interval would have made the graph clustered. 

b) Assingment 5 required more works than other assingments yet the measuring of action could've been skewed by the nature of assignment. For instance, group project would have taken more actions - or a late notice on assignment and short deadline could've been the case. 

c) It appears to be the pattern where students work close to deadlines right before and after (like this one).




'''