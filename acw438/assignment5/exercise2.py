# I selected bins for every 24-hr period, from noon to noon. I did
# this so that the bins would automatically separate at the deadlines,
# which all took place at noon. This way we also have some pretty
# granular detail about what is happening day-to-day.

# It appears that assignments 3, 4, 5, and 6 were the assignments that
# required the most actions, which may be a proxy for how difficult
# the assignments were. Some of the assignments (like #3) had most of
# the work piled up into a couple 24-hour periods around the deadline,
# while others (like assignment 5) were a little more spread out.

# Similarly, assignments 0, 1, and 2 required fairly few actions in
# comparison.

# Almost all the assignments had the highest count of actions grouped
# into the two 24-hour periods surrounding the deadline. Most
# assignments had more actions before the deadline (assignments 0, 1,
# 4, 5, and 6), while a couple had more actions after the deadline
# (assignments 2 and 3). On another note, there seems to be a buildup
# of actions in the 24-hour periods approaching a deadline, but
# typically on a much smaller level than appears immediately before or
# after the deadline. (The exceptions are assignments 0 and 1, in
# which there were no dramatic spikes in the 24-hour periods
# surrounding the deadline).

# --------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter, date2num, num2date
from matplotlib.ticker import MultipleLocator
import pandas as pd

#Set pylab formatting parameters
import pylab
params = {'axes.labelsize': 13,
          'text.fontsize': 10,
          'legend.fontsize': 13,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12,
          'text.usetex': True, 
          'font.family': 'serif',
          'font.serif': ['Palatino'],
          'xtick.direction': 'out'}
pylab.rcParams.update(params)



#Input data into pandas dataframe
actions_df = pd.read_table('actions-fall-2007.dat', sep=',')
actions_df['timestamp'] = pd.to_datetime(actions_df['timestamp'])
actions_df['timestamp'] = date2num(actions_df['timestamp'])
#print actions_df.head(10)

fig, ax = plt.subplots()

# Format x-ticks
month = MonthLocator()
month_format = DateFormatter('%B')
ax.xaxis.set_major_locator(month)
ax.xaxis.set_major_formatter(month_format)
# Format y-ticks
fourties = MultipleLocator(2500)
ax.yaxis.set_major_locator(fourties)

# Set x-axis limit
xmin = pd.to_datetime('2007-09-02')
xmax = pd.to_datetime('2007-12-20')
ax.set_xlim(xmin, xmax)
# Set y-axis limit
ax.set_ylim(1, 16000)

# Remove top & right spines
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')

#Plot duedates vertical lines
duedates = ['2007-09-18 12:00:00', '2007-09-18 12:00:00', '2007-10-04 12:00:00', '2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-15 12:00:00', '2007-12-11 12:00:00']
duedates = pd.to_datetime(duedates)
duedates = date2num(duedates)
ax.vlines(duedates, 0, 16000, color='0.35', zorder=10, linestyle='--', linewidth=1)

#Add minor horizontal lines
h_lines = [5000, 10000, 15000]
ax.hlines(h_lines, xmin, xmax, color='0.85', zorder=1, linestyle=':')

#Label duedates
asslabels = ["Assn." + str(x) + " " for x in range (0, 7)]
asslabels[0] = asslabels[0] + ",\nAssn. 1"
counter = 0
for date in duedates:
    if counter != 1 and counter != 5:
        ax.text(date-1, 15500, asslabels[counter] + "\ndue", ha='right', va='top', multialignment='right', color='0.35', fontsize=10)
    counter += 1
ax.text(duedates[5]+1, 15500, asslabels[5] + "\ndue", ha='left', va='top', color='0.35', fontsize=10)

#Set daily bins for histogram
base = str(num2date(actions_df['timestamp'].min()))
noon = ' 12:00:00+00:00'
base = base.split(' ')[0] + noon
base = date2num(pd.to_datetime(base))
binList = [ base + i for i in range(0,99) ]

#Plot histogram
plt.hist(actions_df['timestamp'], binList, histtype='stepfilled', color='gray', zorder=2, ec='none')

# Add labels
t = ax.set_title('Actions in Scientific Visualization Course, 2007.')
t.set_y(1.03)
ax.set_ylabel('NUMBER OF ACTIONS')
ax.set_xlabel('24-HR PERIODS (NOON TO NOON)')
plt.subplots_adjust(left=.11, top=.9, right=.95, bottom=.13)

plt.savefig('Problem 2.png', dpi=300)
