#Katherine Elliott
#ke638
#ProblemA Assignment 6

import pandas as pd
import matplotlib.pyplot as plt

incidents = pd.read_csv('labeled_data.csv', index_col = 'num_incidents')
incidents.sort()
    
fig = plt.figure()
ax = incidents.plot(y='# zipcode', style = 'o', label='incidents')
#ax = incidents.plot(y='population', style = 'o', label='incidents by population')

#set labels
ax.set_title('Incidence by Zip Code')
ax.set_xlabel('Incidents')
ax.set_ylabel('Zip Code')

#set axis limits
#ax.set_xlim([])
ax.set_ylim([9950,14750])

#adjust spine
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')

ax.legend(loc='best')

plt.savefig('problema_1.png', dpi=300)
plt.show()