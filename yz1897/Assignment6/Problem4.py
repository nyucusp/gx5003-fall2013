# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 03:44:14 2013

@author: yilong
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pylab
import math
import random

'''
---------------
Get Data
---------------
'''
import matplotlib.pyplot as plt
import numpy as np
datapath=""
def get_labeled_data():
    zipcode=[];pop=[];inc=[];count=0
    for line in file(datapath+"labeled_data.csv"):
        if count==0:
            count=1
            continue
        spt=line[:-1].split(",")
        zipcode.append(str(int(float(spt[0]))))
        pop.append(float(spt[1]))#to caculate the population delsity, float will be better
        inc.append(float(spt[2]))
    return zipcode,pop,inc

def get_unlabeled_data():
    zipcode=[];pop=[];count=0
    for line in file(datapath+"unlabeled_data.csv"):
        if count==0:
            count=1
            continue
        spt=line[:-1].split(",")
        zipcode.append(str(int(float(spt[0]))))
        pop.append(float(spt[1]))#to caculate the population delsity, float will be better
    return zipcode,pop

#get the city, state and geolocation information of the zipcodes need to be analyzed from another dataset
def get_zip_infor(zips):
    zipinfor={}
    count=0;foundzip=[]
    for line in file(datapath+'zipcode.csv'):
        if count==0:
            count=1
            continue
        spt=line[:-1].split(",")
        z=str(spt[0][1:-1])
        
        if z in zips:
            foundzip.append(z)
            zipinfor[z]=[spt[1][1:-1],spt[2][1:-1],spt[3][1:-1],spt[4][1:-1]]
    if len(foundzip)==len(zips):
        print "All Zipcodes have find information"
    return zipinfor
        

zip1,pop1,inc=get_labeled_data()
zip2,pop2=get_unlabeled_data()
print "Finding zipcode information in Labeled Dataset..."
zipinfor1=get_zip_infor(zip1)


'''
---------------
Regression
---------------
'''



from scipy.optimize import minimize
def map_feature(x1, x2):
    '''
    Maps the two input features to quadratic features.
 
    Returns a new feature array with more features, comprising of
    X1, X2, X1 ** 2, X2 ** 2, X1*X2, X1*X2 ** 2, etc...
 
    Inputs X1, X2 must be the same size
    '''
    x1.shape = (x1.size, 1)
    x2.shape = (x2.size, 1)
    degree = 6
    out = np.ones(shape=(x1[:, 0].size, 1))
 
    m, n = out.shape
 
    for i in range(1, degree + 1):
        for j in range(i + 1):
            r = (x1 ** (i - j)) * (x2 ** j)
            out = np.append(out, r, axis=1) 
    return out

def sigmoid(X):
    '''Compute the sigmoid function '''
    #d = zeros(shape=(X.shape))
    den = 1.0 + math.e ** (-1.0 * X)
    d = 1.0 / den
    return d
 

def cost_function_reg2(theta, X, y, l):
    '''Compute the cost
    ''' 
    m,n=X.shape
    theta=np.array(theta)
    #print "Theta:",theta.shape
    theta.shape=(n,1)
    y.shape=(m,1)
    z=X.dot(theta)
    h=sigmoid(z)
    theta2=zeros(shape=(len(theta),1))
    theta2[1:]=theta[1:]
    #print "Theta list",theta.T
    
    J=(1.0/m)*(-y.T.dot(log(h))-(1-y.T).dot(log(1-h)))+l/(2*m)*(theta2.T.dot(theta2));
    
    return J


#prepare logistic regression trainning data
x1=[];x2=[];y=[]
for i in range(len(zip1)):
    z=zip1[i]
    x1.append(float(zipinfor1[z][3]))
    x2.append(float(zipinfor1[z][2]))
    if inc[i]<=0 or math.log(inc[i])<6:
        y.append(0)
    else:
        y.append(1)
        
        
#scale features        
x1=np.array(x1)
x2=np.array(x2)
w1=max(x1)-min(x1)
w2=max(x2)-min(x2)
mu1=-74;mu2=42
x1=(x1-mu1)/w1
x2=(x2-mu2)/w2



y=np.array(y)
y.shape=(len(y),1)
X=map_feature(x1,x2)
m, n = X.shape
initial_theta=[random.random()-0.5 for i in range(n)]
l=0.00000001


def cost(theta):
    return cost_function_reg2(theta, X, y, l)

print "minimizing the cost function..."
print "--------------------------"
result=minimize(cost,initial_theta,method='nelder-mead',options={'xtol': 1e-8, 'disp': True})
final_theta=result.x
print "--------------------------"

#Plot Boundary
print "Ploting Classifying Boundary"
u = np.linspace(-80, -72, 50)
v = np.linspace(40, 45, 50)

u2=(np.array(u)-mu1)/w1
v2=(np.array(v)-mu2)/w2

z = np.zeros(shape=(len(u), len(v)))
for i in range(len(u)):
    for j in range(len(v)):
        z[i, j] = (map_feature(np.array(u2[i]), np.array(v2[j])).dot(np.array(final_theta)))
        
z = z.T
plt.contour(u, v, z,levels=[0])

#show()

lats={1:[],2:[]};longs={1:[],2:[]}
for i in range(len(zip1)):
    if inc[i]<=0 or math.log(inc[i])<6:
        lats[2].append(zipinfor1[zip1[i]][2])
        longs[2].append(zipinfor1[zip1[i]][3])
    else:
        lats[1].append(zipinfor1[zip1[i]][2])
        longs[1].append(zipinfor1[zip1[i]][3])
        


plt.plot(longs[1],lats[1],'.',label="Class 1",alpha=0.5,markersize=5,color='r')
plt.plot(longs[2],lats[2],'.',label="Class 2",alpha=0.5,markersize=5,color='g')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(['y = 1', 'y = 0', 'Decision boundary'])

plt.savefig("Figure6.png",dpi=400)
plt.close()

'''
---------------
Seperately Train OLS model in two classes
---------------
'''

def classify(theta, X):
    '''Predict whether the label
    is 0 or 1 using learned logistic
    regression parameters '''
    m, n = X.shape
    p = np.zeros(shape=(m, 1))
 
    h = sigmoid(X.dot(theta.T))
 
    for it in range(0, h.shape[0]):
        if h[it] > 0.5:
            p[it, 0] = 1
        else:
            p[it, 0] = 0
 
    return p
    
    
#Seperating the data

ypre=classify(final_theta,X).flatten()
popli={0:[],1:[]}
incli={0:[],1:[]}

for i in range(len(pop1)): 
    popli[ypre[i]].append(pop1[i])
    incli[ypre[i]].append(inc[i])


#train the OLS
polyli={0:[],1:[]}
finalpredict=[];xfinal=[]

def ithfold(ith,rand,po,inc):
    trainx=[];trainy=[];testx=[];testy=[]
    for i in range(len(po)):
        if chose[i]==ith:
            testx.append(po[i]);testy.append(inc[i])
        else:
            trainx.append(po[i]);trainy.append(inc[i])
    return np.array(trainx),np.array(trainy),np.array(testx),np.array(testy)
    
def crosstest(chose,pop1,inc):
    crossresult=[];means=[]
    for i in range(5):
        result=[]
        for fold in range(10):
            trainx,trainy,testx,testy=ithfold(fold,chose,pop1,inc)
            polypara=np.polyfit(trainx,trainy,i+1)
            predict = np.poly1d(polypara)
            rmse=(((predict(testx)-testy)**2).mean())**(0.5)
            result.append(rmse)
        result=np.array(result)
        means.append(result.mean())
        crossresult.append((result.std(),result.mean()))
    return means

#visualze the trained result
polyparali=[]
for cl in range(2):
    #train one class:
    chose=[random.randrange(10) for i in range(len(popli[cl]))]
    mea=crosstest(chose,popli[cl],incli[cl])
    order=mea.index(min(mea))+1
    polypara=np.polyfit(popli[cl],incli[cl],order)
    polyparali.append(polypara)

for i in range(len(pop1)):
    pred = np.poly1d(polyparali[int(ypre[i])])
    result=pred(pop1[i])
    finalpredict.append(result)
    xfinal.append(pop1[i])
plt.plot(xfinal,finalpredict,'o',label='predict',alpha=0.5)

plt.plot(pop1,inc,"<",label='data',alpha=0.5)    
plt.legend(loc=0)
plt.xlabel("Population")
plt.ylabel("Incidents")
plt.savefig("Figure7.png",dpi=400)
plt.close()

plt.plot(inc,finalpredict,'o',label='predict vs data',alpha=0.5)
plt.plot([min(inc),max(inc)],[min(inc),max(inc)],'--',label='y=x',alpha=0.5)
    
plt.legend(loc=0)
plt.xlabel("Data")
plt.ylabel("Predict")
plt.savefig("Figure7.1.png",dpi=400)
plt.close()


#model 1



'''
---------------
Predict Unlabeled Data.
---------------
'''

def Predictor(theta,polyparali):
    #get geolocation of unlabed zipcode
    zipinfor2=get_zip_infor(zip2)
    x1=[];x2=[]
    for i in range(len(zip2)):
        z=zip2[i]
        x1.append(float(zipinfor2[z][3]))
        x2.append(float(zipinfor2[z][2]))

        
    #scale geo features        
    x1=np.array(x1)
    x2=np.array(x2)
    w1=max(x1)-min(x1)
    w2=max(x2)-min(x2)
    mu1=-74;mu2=42
    x1=(x1-mu1)/w1
    x2=(x2-mu2)/w2
    #map the feature, Xul=>X_unlabeled
    Xul=map_feature(x1, x2)

    #Classifying 

    ypre=classify(theta,Xul).flatten()
    popli={0:[],1:[]}

    for i in range(len(pop2)): 
        popli[ypre[i]].append(pop2[i])
        pred = np.poly1d(polyparali[int(ypre[i])])
        result=pred(pop2[i])
        finalpredict.append(result)
        xfinal.append(pop2[i])
    
 #   for cl in range(2):
 #       pred = np.poly1d(polyparali[cl])
 #       result=pred(popli[cl])
 #       finalpredict.extend(result)
 #       xfinal.extend(popli[cl])
    plt.plot(xfinal,finalpredict,'o',label='Class '+str(cl+1),alpha=0.5)

    
    plt.legend(loc=0)
    plt.title("Prediction to Unlabeled Data")
    plt.xlabel("Population")
    plt.ylabel("Incidents")
    plt.savefig("Figure8.png",dpi=400)
    print "Predicted Result saved in Figure8.png"
    plt.close()
    
    
    

print "Predicting unlabeled data"
Predictor(final_theta,polyparali)
f=open("predictions.csv","w")
for i in finalpredict:
    line=str(i)+'\n'
    f.write(line)
f.close()
   
