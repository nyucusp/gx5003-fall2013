from matplotlib import pyplot
import numpy

#return the R-squre and RMSE
def validate(x,y,coeffs):
    results = {}
    #R-square
    p = numpy.poly1d(coeffs)
    yhat = p(x)                        
    ybar = numpy.sum(y)/len(y)  
    ssreg = numpy.sum((yhat-ybar)**2)  
    sstot = numpy.sum((y - ybar)**2)
    results['rSquare'] = ssreg / sstot
    #RMSE
    results['RMSE']=(numpy.sum((yhat-y)**2)/len(y))**0.5  
    return results

# read data form dat file
inputFile = open('labeled_data.csv','r')
header = inputFile.readline()

zip=[]
pop=[]
inci=[]
sampleNum=0

for line in inputFile:
        term = line.split(",")
        zip.append(term[0])
        pop.append(float(term[1]))
        inci.append(float(term[2]))
        sampleNum+=1
inputFile.close()

#10-fold cross-validation
K=10
rSquareDic={}
RMSEDic={}
degreeList=[]
avgrSquareList=[]
avgRMSEList=[]
RMSEseList=[]
RMSEAll=[]

for degree in range(1,6):
    degreeList.append(degree)
    rSquare=[]
    RMSE=[]
    for k in range(0,K):
        trainx = [x for i, x in enumerate(pop) if i % K != k]
        valix = [x for i, x in enumerate(pop) if i % K == k]
        trainy = [y for i, y in enumerate(inci) if i % K != k]
        valiy = [y for i, y in enumerate(inci) if i % K == k] 
        coeffs = numpy.polyfit(trainx,trainy,degree)
        rSquare.append(validate(trainx,trainy,coeffs)["rSquare"])
        RMSE.append(validate(valix,valiy,coeffs)["RMSE"])

    rSquareDic[degree]=rSquare
    RMSEDic[degree]=RMSE
    avgrSquare=sum(rSquare)/float(len(rSquare))
    avgRMSE=sum(RMSE)/float(len(RMSE))
    RMSEse=numpy.std(RMSE) #get the standard error for each polynomial degree
    avgrSquareList.append(avgrSquare)
    avgRMSEList.append(avgRMSE)
    RMSEseList.append(RMSEse)

    #RMSE based on all dataset
    coeffsAll = numpy.polyfit(pop,inci,degree)
    RMSEAll.append(validate(pop,inci,coeffsAll)["RMSE"])

outputFile=open('output.csv','w')
outputFile.write(str(RMSEDic))

#plot
fig = pyplot.figure()
fig.suptitle("RMSE of all training set VS RMSE of 10-fold",fontsize=15)
graph = fig.add_subplot(1,1,1)
graph.errorbar(degreeList,avgRMSEList,yerr=RMSEseList,fmt='o',label='10-fold')
graph.plot(degreeList,RMSEAll,'o',color='r',label='All training set')
graph.grid(True)#Add the gridlines to make the plot clearer 
graph.set_xlabel('Degree of Polynomial',fontweight='bold')
graph.set_ylabel('RMSE',fontweight='bold')
graph.set_xlim(0,6)
graph.legend(loc="upper left",shadow=False)
#graph.set_ylim(12500,14000)
fig.patch.set_facecolor('white') 

pyplot.savefig('problem_c.png', dpi=200)
pyplot.show()

"""
Answer:
I observed as the degree of polynomial increase, the RMSE of all dataset decrease. However, for the 10-fold validation, third degree of polynomial has the minimum of RMSE 
"""
