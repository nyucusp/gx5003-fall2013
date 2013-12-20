#Katherine Elliott
#ke638
#Problem2 Assignment 5

import matplotlib.pyplot as plt
import pandas as pd
import pylab
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter, date2num, num2date
from matplotlib.ticker import MultipleLocator

 
actions = pd.read_table('actions-fall-2007.dat', sep=',')
actions['timestamp'] = pd.to_datetime(actions['timestamp'])
actions['timestamp'] = date2num(actions['timestamp'])

fig, ax = plt.subplots()
                
#set labels
ax.set_title('Actions Fall 2007')
ax.set_xlabel('Due Dates')
ax.set_ylabel('Number of Commits')
ax.set_xticklabels('')

actions_data = [(datetime(2007, 9, 18), 'Assignment 1), (datetime(2007, 9, 18), 'Assignment 2'),(datetime(2007, 10, 04), 'Assignment 3'),
    

#adjust spine
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')

plt.hist(actions['timestamp'], histtype='stepfilled', color='green', zorder=2, ec='none')

ax.legend(loc='best')

plt.savefig('problem2.png', dpi=300)
plt.show()
