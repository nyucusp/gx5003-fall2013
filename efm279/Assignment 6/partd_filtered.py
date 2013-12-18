import numpy as np
import pylab as pl
import pandas as pd
from matplotlib import ticker
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow
from random import shuffle
import csv
from sklearn.cross_validation import KFold


# Part_b
def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def R2(x, y, fit):
    yhat = fit(x)        
    ybar = np.sum(y)/len(y) 
    ssreg = np.sum((yhat-ybar)**2)  
    sstot = np.sum((y - ybar)**2) 
    r2 = ssreg / sstot
    return r2
    
data = pd.read_csv('labeled_data.csv')

d=3
data=data[data['num_incidents']>500]
p = np.poly1d(np.polyfit(data['population'],data['num_incidents'] , deg=d))
plt.plot(data['population'],data['num_incidents'],'o',label='original data')
plt.plot(p(data['population']),data['num_incidents'],'s',label='predicted')
plt.ylim(0,130000)
plt.xlim(0,130000)
plt.title('311 Data: Number of Incidents as a function of population: Filtered Model')
plt.legend( loc='upper right' )
plt.show()
plt.savefig('filtered.png',dpi = 300)

prediction=[]
prediction.append(['population','actual_no_of_incidents','predicted_no_of_incidents'])
for uu in data.index.values:
    prediction.append([data['# zipcode'][uu],[data['population'][uu],data['num_incidents'][uu],p(data['population'][uu])])
    
with open('filtered_predictions_Final.csv', 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(prediction)
