"""
Awais Malik
Assignment 6
Problem a
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the data file
data = pd.read_csv('labeled_data.csv')

pop_data = data[['population','num_incidents']]
index = pop_data.set_index('population')
pop_index = index.sort()

incident_data = data[['# zipcode','num_incidents']]
index2 = incident_data.set_index('# zipcode')
incident_index = index2.sort()

plot = pop_index.plot(style = "o")
plot.set_title('311 Incidents vs Population of Zip Codes')
plot.set_xlabel('Population')
plot.set_ylabel('311 Incidents')
plot.figure.savefig('Problema1.jpg',dpi = 300)

plot2 = incident_index.plot(kind = 'bar')
plot2.set_title('Number of 311 Incidents per Zipcode')
plot2.set_ylabel('Number of Incidents')
plot2.set_xlabel('Zip Codes')
plot2.figure.savefig('Problema2.jpg',dpi = 300)
plt.xticks(np.arange(1,300, 10))
plt.ylim(0,125000)