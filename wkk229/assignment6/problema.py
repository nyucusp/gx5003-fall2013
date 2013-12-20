import panda as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import kFold

data=pd.read_cvs('labeled_data.cvs')
plot_data = data[['#zipcode','population','num_incidents']]
plot_data.plot(x='population',y='num_incidents',style='o')
plt.ylabel('num_incidents')
plt.ylim(0,125000)
plt.title('311 Data:Number of Incidents vs population')
plt.savefig('parta.png',dpi = 300)
#plt.show()

min_mag,max_mag=np.min(data['num_incidents']),np.max(data['num_incidents'])
fig,ax=plt.subplots( figsize= (5,5))
ax.set_xlabel('num_incidents')
ax.set_ylabel('frequency')
ax.set_xlim(-100,120000)
ax.set_ylim(0,200)
ax.hist(data['num_incidents'],80,color='red'lw=2.)
#figshow()
fig.savefig('histogram.png')

plot_data.plot('#zipcode','num_incidents',kind='bar',legend=False)
plt.ylabel('num_incidents')
plt.xlabel('zipcode')
plt.xticks(np.arange(1,300,5))
plt.ylim(0,125000)
plt.title('311 Data:Number of Incidents by zipcode')
#plt.savefig('partb.png',dpi=300)
#plt.show()
