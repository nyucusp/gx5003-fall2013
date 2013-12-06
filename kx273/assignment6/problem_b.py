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
    avgrSquareList.append(avgrSquare)
    avgRMSEList.append(avgRMSE)
   # print "For polynomial of degree "+str(degree)+", the average R-Square is "+str(avgrSquare)+", and the average RMSE is "+str(avgRMSE)


fig = pyplot.figure()
fig.suptitle("Cross-Validation",fontsize=15)
graph1 = fig.add_subplot(2,1,1)
graph2 = fig.add_subplot(2,1,2)
graph1.plot(degreeList,avgrSquareList,'.',ms=9,color='r')
graph2.plot(degreeList,avgRMSEList,'.',ms=9,color='b')
graph1.grid(True)#Add the gridlines to make the plot clearer 
graph2.grid(True)#Add the gridlines to make the plot clearer 
graph1.set_xlabel('Degree of Polynomial',fontweight='bold')
graph1.set_ylabel('Average R-Square',fontweight='bold')
graph2.set_xlabel('Degree of Polynomial',fontweight='bold')
graph2.set_ylabel('Average RMSE',fontweight='bold')
graph1.set_xlim(0,6)
graph2.set_xlim(0,6)
graph2.set_ylim(12500,14000)

fig.patch.set_facecolor('white') 

pyplot.savefig('problem_b.png', dpi=200)
pyplot.show()

"""
According to the average R-Square and average RMSE, the polynomial with third degree has the best performance. 

"""
