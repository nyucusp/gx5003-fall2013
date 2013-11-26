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

micro_file = open('microprocessors.dat', 'rU')
micro_lines = csv.reader(micro_file)

list_processor = [] 
list_year = [] 
list_transistor = [] 

for x in micro_lines:
	list_processor.append(x[0])
	list_year.append(x[1])
	list_transistor.append((x[2]))


#poplog=log10(pop)  # log stransform the variables
#gdplog=log10(gdp)

list_processor = list_processor[1:]
list_year = list_year[1:]
list_transistor = list_transistor[1:]

list_year_dates = [] 
for x in list_year:
	list_year_dates.append(dparser.parse(x, fuzzy=True))


list_transistor_float = [] 
for x in list_transistor:
	list_transistor_float.append(float(x))

log_transistor = log10(list_transistor_float)

#print list_processor
#print list_year
#print list_transistor
#print log_transistor
#print list_year_dates

list_num_processor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

years = dates.YearLocator()
yearsFmt = dates.DateFormatter('%Y' )

labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

fig = PLT.figure() 
#fig, axes = plot.subplots(nrows = 1, ncols = 2)
ax1 = fig.add_subplot(1,2,1)
ax1.scatter(list_year_dates, list_num_processor, 50, color='blue')
#ax1.set_aspect('equal')

#fig.subplots_adjust(left)
for i, txt in enumerate(list_processor):
	ax1.annotate(txt, (list_year_dates[i],list_num_processor[i]))


# format the ticks 
#ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(yearsFmt)
fig.autofmt_xdate()

#plot.gcf().subplots_adjust(bottom = .15, left =0.13, right = 0.95, top = 0.96)

#Need to Widen 

plot.xlabel('Year', fontsize = 14)
plot.ylabel('Processor', fontsize=14)

ax2 = fig.add_subplot(122)
ax2.scatter(log_transistor, list_num_processor, 50, color = 'orange')

for i, txt in enumerate(list_processor):
	ax2.annotate(txt, (log_transistor[i],list_num_processor[i]))



fig.suptitle('Problem 3', fontsize = 14)
plot.xlabel('Number of Transistor (log)', fontsize = 14)
plot.ylabel('Processor', fontsize=14)



fig.savefig('Problem_3.png')
plt.show()
micro_file.close 



