import matplotlib.pyplot as plt 
import numpy as np

readdata=[]
myfile = open('labeled_data.csv','r')
for line in myfile:
    readdata.append(line)

zip=[]
pop=[]
inc=[]

for i in range(1,len(readdata)):
    zip.append(readdata[i].split(",")[0])
    pop.append(float(readdata[i].split(",")[1]))
    inc.append(float(readdata[i].split(",")[2]))
        
myfile.close()


# define functions of r^2, RMSE
def vali(x,y,coeffs):
    results = {}
    #R^2
    p = np.poly1d(coeffs)
    #fit values and mean
    yhat = p(x)                        
    ybar = np.sum(y)/len(y)  
    ssreg = np.sum((yhat-ybar)**2)  
    sstot = np.sum((y - ybar)**2)
    results['r^2'] = ssreg / sstot
    #RMSE
    results['RMSE']=(np.sum((yhat-y)**2)/len(y))**0.5  
    return results

n=10

degree_list=[]
r2dict={}
average_rsquare=[]
RMSEdict={}
average_RMSE=[]
aversquare=[]
aveRMSE=[]
sd=[]

allcoeffs=[]
allRMSE=[]
for degree in range(1,6):
    degree_list.append(degree)
    rsquare=[]
    RMSE=[]
    
    for j in range(0,n):
        trainx=[x for i, x in enumerate(pop) if i % n !=j]
        validationx=[x for i, x in enumerate(pop) if i % n ==j]
        
        trainy=[y for i, y in enumerate(inc) if i % n !=j]
        validationy=[y for i, y in enumerate(inc) if i % n ==j]
        
        #calculate standard deviation and RMSE of all data
        coeffs=np.polyfit(trainx, trainy, degree)
        rsquare.append(vali(trainx,trainy,coeffs)["r^2"])
        RMSE.append(vali(validationx,validationy,coeffs)["RMSE"])
   
        
    r2dict[degree]=rsquare
    RMSEdict[degree]=RMSE
    average_rsquare=sum(rsquare)/float(len(rsquare))
    average_RMSE=sum(RMSE)/float(len(RMSE))
    
    aversquare.append(average_rsquare)
    aveRMSE.append(average_RMSE)
    
    sd.append(np.std(RMSE))
    allcoeffs=np.polyfit(pop,inc,degree)
    allRMSE.append(vali(pop,inc,allcoeffs)["RMSE"])
   
print aversquare,aveRMSE,sd,allRMSE    

#plot
chart1=plt.figure()
chart1=plt.subplot(1,1,1)
chart1.set_title('RMSE of All Training Data and RMSE of 10-flod CV data')
chart1.plot(degree_list,allRMSE,'o--',color='b',label='All')
chart1.errorbar(degree_list, aveRMSE,yerr=sd,fmt='o--',color='y',label='10-fold')
chart1.set_xlabel('Polynomial Degree')
chart1.set_xlim(0,6)
chart1.set_ylabel('RMSE')
chart1.legend(loc='best')
chart1.grid()



plt.show()
                  