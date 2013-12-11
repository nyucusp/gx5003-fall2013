import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cross_validation import KFold


data = pd.read_csv('labeled_data.csv')
plot_data = data[['# zipcode','population','num_incidents']]
plot_data.plot(x='population', y='num_incidents',style='o')
plt.ylabel('Number of Incidents')
plt.ylim(0,125000)
plt.title('311 Data: Number of Incidents vs. Population')
plt.savefig('Parta.png',dpi = 300)
#plt.show()

min_mag, max_mag = np.min(data['num_incidents']), np.max(data['num_incidents'])
#binsize = 500
#num_bins = np.floor((max_mag - min_mag) / binsize)
fig, ax = plt.subplots(figsize = (5, 5))
ax.set_xlabel('Number of Incidents')
ax.set_ylabel('Frequency')
ax.set_xlim(-100,120000)
ax.set_ylim(0,200)
ax.hist(data['num_incidents'], 80, color='red', lw=2.)
#fig.show()
fig.savefig('histogram.png')


plot_data.plot('# zipcode','num_incidents',kind='bar', legend=False)
plt.ylabel('Number of Incidents')
plt.xlabel('zipcodes')
plt.xticks(np.arange(1,300, 5))
plt.ylim(0,125000)
plt.title('311 Data: Number of Incidents by Zip Code')
#plt.savefig('Partb.png',dpi = 300)
#plt.show()


#plot_data2 = data['num_incidents']

#plot_data2.plot(kind='bar', legend=False)


#plot2=plot_data.plot(x=data[data.columns[0]], y='num_incidents',style='o')
#plot2.set_ylabel('Number of Incidents')
#plot2.set_ylim(0,125000)
#plot2.set_yticks(data[data.columns[0]])
#plot2.set_title('311 Data: Number of Incidents vs. Population')
