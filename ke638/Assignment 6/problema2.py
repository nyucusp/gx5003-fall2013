#Katherine Elliott
#ke638
#ProblemA Assignment 6

import pandas as pd
import matplotlib.pyplot as plt

incidents = pd.read_csv('labeled_data.csv', index_col = 'num_incidents')
incidents.sort()
    
fig = plt.figure()
ax = incidents.plot(y='population', style = 'o', label='incidents')

#set labels
ax.set_title('Incidence by Zip Code Population')
ax.set_xlabel('Number of Incidents')
ax.set_ylabel('Population')

#set axis limits
ax.set_xlim([1000,120000])# x-value changed to eliminate outliers and illustrate correlation
#ax.set_ylim([9950,14750])

#adjust spine
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')

ax.legend(loc='best')

plt.savefig('problema_3.png', dpi=300)
plt.show()