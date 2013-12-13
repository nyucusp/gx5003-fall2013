from pylab import *
import matplotlib.pyplot as plt

from sklearn.cross_validation import KFold


'''
Seems like some of the data locations have less incidents than the others. The way  I filtered the data was to remove the number of incidents which is lower than 10.

The number of incidents lower than 100 is 176
The number of incidents lower than 50 is  175
The number of incidents lower than 10 is 143

Therefore, I didn't take the places that has less than 10 incidents into consideration for this study.

In addition, target dataset has no zipcodes which has a population more than 100 thousand. I also removed the populations that is more than that.
'''

zipcodes = []
population = []
incidents = []
with open('labeled_data.csv','r') as f:
    f.next()
    for row in f:
        a = row.strip('\n').split(',')
        if (float(a[2])>10):
            if(float(a[1])<100000):
                zipcodes.append(float(a[0]))
                population.append(float(a[1]))
                incidents.append(float(a[2]))


plt.plot(population, incidents, 'o')
plt.ylabel('Number of Incidents')
plt.ylim(0,125000)
plt.title('Filtered Data: Number of Incidents ~ Population')
##plt.savefig('Parta.png',dpi = 300)
plt.show()
plt.savefig('Parta.png',dpi = 300)


