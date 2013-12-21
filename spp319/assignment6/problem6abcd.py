
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inc311 = pd.read_csv('labeled_data.csv')
#divide up data for indexing
population = inc311[['population','num_incidents']]
incidents = inc311[['# zipcode','num_incidents']]
index1 = population.set_index('population')
index2 = incidents.set_index('# zipcode')
style1 = ['r^']
style2 = ['r']
sortedPop = index1.sort()
sortedInc = index2.sort()
#create both plots
firstfig = sortedPop.plot(style = style1)
secondfig = sortedInc.plot(kind = 'bar', color = style2)

firstfig.set_title('Incidents as a Function of Population')
secondfig.set_title('Incidents as a Function of Zipcode')

firstfig.set_xlabel('POPULATION')
secondfig.set_ylabel('INCIDENTS')

firstfig.set_ylabel('INCIDENTS')
secondfig.set_xlabel('ZIPCODES')

plt.ylim(0,125000)
firstfig.figure.savefig('Problema_IncPop.jpg')

plt.tight_layout()
plt.xticks(np.arange(1,250,25))
plt.ylim(0,130000)
secondfig.figure.savefig('ProblemaIncZip.jpg')




