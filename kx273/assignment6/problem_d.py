from matplotlib import pyplot
import numpy

# read data form dat file
inputFile = open('labeled_data.csv','r')
header = inputFile.readline()
zip=[]
pop=[]
inci=[]

for line in inputFile:
        term = line.split(",")
        zip.append(term[0])
        pop.append(int(float(term[1])))
        inci.append(int(float(term[2])))
inputFile.close()

inputFile = open('unlabeled_data.csv','r')
header = inputFile.readline()
popPredic=[]
for line in inputFile:
        term = line.split(",")
        popPredic.append(int(float(term[1])))
inputFile.close()


#According to the previous analysis, third degree polynomial is chosen as the best model. 
coeffs= numpy.polyfit(pop,inci,3)
fit_eq = numpy.poly1d(coeffs)
xArray=numpy.arange(0,110000,500)
inciFit = fit_eq(xArray) 

inciPredic=fit_eq(popPredic) 


fig = pyplot.figure()

graph1 = fig.add_subplot(2,1,1)
graph1.plot(pop,inci,'.',ms=5,color='b',label="Observed")
graph1.plot(xArray,inciFit,'--',ms=9,color='r',label="Fitted")
graph1.legend(loc="upper left",shadow=False)
#fig.autofmt_xdate()#Automatically adjust the x tick labels to avoid overlap
graph1.grid(True)#Add the gridlines to make the plot clearer 
graph1.set_xlabel('Population',fontweight='bold')
graph1.set_ylabel('Incident',fontweight='bold')
graph1.set_title("Model incident using population",fontsize=15)

graph2 = fig.add_subplot(2,1,2)
graph2.plot(popPredic,inciPredic,'.',ms=5,color='b')
graph2.grid(True)#Add the gridlines to make the plot clearer 
graph2.set_xlabel('Population',fontweight='bold')
graph2.set_ylabel('Incident',fontweight='bold')
graph2.set_title("Predict incidents using unlabeled data",fontsize=15)

fig.tight_layout()
fig.patch.set_facecolor('white') 
pyplot.savefig('problem_d.png', dpi=200)
pyplot.show()

"""
Note:
The third degree polinomial which had the best performance in the previous analysis was chosen to model the incident number by population. 

Then, this model was used to predict the incident number for zones in the unlabeled data
"""
