"""
Awais Malik
Assignment 6
Problems b, c and d
Collaborated with Ender Faruk Morgul
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import KFold

# Part b
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
    sum=0
    sum2=0
    it=1
    print "n= "+str(d)
    cats[d]=[]
    for ribery, robben in kf:
        p = np.poly1d(np.polyfit(data['population'][ribery[0]:ribery[len(ribery)-1]],data['num_incidents'][ribery[0]:ribery[len(ribery)-1]] , deg=d))
        a=p(data['population'][robben[0]:robben[len(robben)-1]])
        
        print "CV k="+ str(i) +" RMSE: " + str(RMSE(a,data['num_incidents'][robben[0]:robben[len(robben)-1]])) + " R^2:" +str(R2(data['population'][ribery[0]:ribery[len(ribery)-1]],data['num_incidents'][ribery[0]:ribery[len(ribery)-1]],p))
        sum=sum+RMSE(a,data['num_incidents'][robben[0]:robben[len(robben)-1]])
        sum2=sum2+R2(data['population'][ribery[0]:ribery[len(ribery)-1]],data['num_incidents'][ribery[0]:ribery[len(ribery)-1]],p)

        cats[d].append(RMSE(a,data['num_incidents'][robben[0]:robben[len(robben)-1]]))
        it=it+1

    at[d]=[sum/10,sum2/10]
    full[d]=[RMSE(p(data['population']),data['num_incidents']),R2(data['population'],data['num_incidents'],p)]
    
for ender in at.keys():
    print "K-fold Average for Poly. degree "+str(ender)+" Avg. RMSE: "+str(at[ender][0])+" Avg. R^2:" + str(at[ender][1])
    print "Full model for Poly. degree " +str(ender)+" Avg. RMSE: "+str(full[ender][0])+" Avg. R^2:" + str(full[ender][1])
    
ats=[]
fts=[]
pats=[]
for d in degrees:
    ats.append(at[d][0])
    fts.append(full[d][0])
    pats.append(np.std(cats[d])/2)

# Part c 
plt.figure()
plt.errorbar(degrees,ats,yerr=pats,label='10-fold CV Average',color='r',linestyle='-.', linewidth=1.5)
plt.plot(degrees,fts,label='RSME entire data',color='b', linewidth=2.0)
plt.xlim(0,6)
plt.ylim(9000,19000)
plt.xlabel('Degree of Polynomial Fit')
plt.ylabel('RMSE')
plt.title('Number of 311 Incidents vs. Population')
plt.ylim(9000,19000)
plt.grid()
plt.legend( loc='best' )
plt.show()
plt.savefig('Problemc.jpg', dip = 300)

# Part d
d=3
data=data.sort(['population'])
p = np.poly1d(np.polyfit(data['population'],data['num_incidents'] , deg=d))

plt.figure()
plt.plot(data['population'],data['num_incidents'],'s',label='Actual Data')
plt.plot(p(data['population']),data['num_incidents'],'o',label='Predicted Values')
plt.ylim(0,130000)
plt.xlim(0,130000)
plt.title('Number of 311 Incidents vs. Population')
plt.legend( loc='upper right' )
plt.show()
plt.savefig('Problemd.jpg',dpi = 300)