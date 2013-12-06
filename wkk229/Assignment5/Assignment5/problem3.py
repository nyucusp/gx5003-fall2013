import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter
from matplotlib.dates import date2num, YearLocator, DateFormatter
from matplotlib.patches import ConnectionPatch
import pandas as pd
import numpy as np
import datetime
import math
import pylab
pd.set_option('display.mpl_style', 'default')
#plt.figsize(15,7)



# Input data into pandas dataframe, convert, and sort
df = pd.read_table('microprocessors.dat', sep=',')
df['Year of Introduction'] = df['Year of Introduction'].astype(str) + "-01-01"
df['Year of Introduction'] = pd.to_datetime(df['Year of Introduction'])
df.sort(['Year of Introduction'], ascending=True, inplace=True)
df = df.reset_index(drop=False)
df['Processor'] = df['Processor'].map(lambda x: x.rstrip(' processor'))
v = [datetime.datetime.strptime('1970-01-01 00:00:00', '%Y-%m-%d %X'),datetime.datetime.strptime('2010-01-01 00:00:00', '%Y-%m-%d %X'), 0, 14]
plt.axis(v)


ax = plt.gca()
plt.yticks(np.arange(14))


procList = []
procList.append("")
proc = ""

for row in df['Processor']:
    procList.append(row)

listDates = []

for row in df['Year of Introduction']:
    listDates.append(row)

transistors = []
transistors.append(0)
for row in df['Transistors']:
    transistors.append(row)

plt.Axes.set_yticklabels(ax,procList)
plt.plot_date(listDates, [1,2,3,4,5,6,7,8,9,10,11,12,13])
# plt.legend(loc = 1, title = 'Year Released')
plt.xlabel("Year of Introduction", color = 'blue')
plt.ylabel("Processor")
ax2 = plt.twiny()


ax2.set_xscale('log')
#ax2.set_xticks(transistors)
ax2.plot(transistors, [0,1,2,3,4,5,6,7,8,9,10,11,12,13],'go--' )
v2 = [0,50000000,0,15]
ax2.axis(v2)
ax2.legend('best', title = 'Transistors')
ax2.set_xlabel("Number of Transistors", color = 'green')

plt.savefig('Problem3.png', dpi=300)
