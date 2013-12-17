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
plot_data = data[['# zipcode','population','num_incidents']]
i=0
Y=data['num_incidents']
X=data['population']

degrees = [1, 2, 3, 4, 5]
at=dict((el,0) for el in degrees)
full=dict((el,0) for el in degrees)
cats=dict((el,0) for el in degrees)

kf = KFold(len(Y), n_folds=10, indices=True)


for d in degrees:
    #print("%s %s" % (train, test))
    sum=0
    sum2=0
    it=1
    print "n= "+str(d)
    cats[d]=[]
    for train, test in kf:
        p = np.poly1d(np.polyfit(data['population'][train[0]:train[len(train)-1]],data['num_incidents'][train[0]:train[len(train)-1]] , deg=d))
        a=p(data['population'][test[0]:test[len(test)-1]])
        
        print "CV k="+ str(i) +" RMSE: " + str(RMSE(a,data['num_incidents'][test[0]:test[len(test)-1]])) + " R^2:" +str(R2(data['population'][train[0]:train[len(train)-1]],data['num_incidents'][train[0]:train[len(train)-1]],p))
        sum=sum+RMSE(a,data['num_incidents'][test[0]:test[len(test)-1]])
        sum2=sum2+R2(data['population'][train[0]:train[len(train)-1]],data['num_incidents'][train[0]:train[len(train)-1]],p)

        cats[d].append(RMSE(a,data['num_incidents'][test[0]:test[len(test)-1]]))
        it=it+1

    at[d]=[sum/10,sum2/10]
    full[d]=[RMSE(p(data['population']),data['num_incidents']),R2(data['population'],data['num_incidents'],p)]
    
    #print str(sum/10)
    #print str(sum2/10)

for zagorakis in at.keys():
    print "K-fold Average for Poly. degree "+str(zagorakis)+" Avg. RMSE: "+str(at[zagorakis][0])+" Avg. R^2:" + str(at[zagorakis][1])
    print "Full model for Poly. degree " +str(zagorakis)+" Avg. RMSE: "+str(full[zagorakis][0])+" Avg. R^2:" + str(full[zagorakis][1])   
    
ats=[]
fts=[]
pats=[]
for d in degrees:
    ats.append(at[d][0])
    fts.append(full[d][0])
    pats.append(np.std(cats[d])/2)


#Part_c
    
plt.figure()
plt.errorbar(degrees,ats,yerr=pats,label='10-fold cross validated',color='g',linestyle='-.', linewidth=1.5)
plt.plot(degrees,fts,label='Full model',color='r', linewidth=2.0)
plt.xlim(0,6)
plt.ylim(9000,19000)
plt.xlabel('Fitted Polynomial Degree')
plt.ylabel('RMSE')
plt.title('311 Data: Number of Incidents as a function of population')
plt.ylim(9000,19000)
plt.grid()
plt.legend( loc='upper left' )
plt.show()

#Part_d
d=3
data=data.sort(['population'])
p = np.poly1d(np.polyfit(data['population'],data['num_incidents'] , deg=d))

plt.figure()
plt.plot(data['population'],data['num_incidents'],'o',label='original data')
plt.plot(p(data['population']),data['num_incidents'],'s',label='predicted')
plt.ylim(0,130000)
plt.xlim(0,130000)
plt.title('311 Data: Number of Incidents as a function of population: Final Model')
plt.legend( loc='upper right' )
plt.show()
plt.savefig('unfiltered.png',dpi = 300)


prediction=[]
prediction.append(['population','actual_no_of_incidents','predicted_no_of_incidents'])
for uu in range(0,len(data['population'])):
    prediction.append([data['population'][uu],data['num_incidents'][uu],p(data['population'][uu])])
    
with open('predictions.csv', 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(prediction)

