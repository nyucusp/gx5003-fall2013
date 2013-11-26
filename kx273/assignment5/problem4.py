from matplotlib import pyplot
import numpy

# read data form dat file
inputFile = open('Hw1data/genes.dat','r')
header = inputFile.readline()
data=[]

for line in inputFile:
        term = line.split(",")
        data.append([float(term[0]),float(term[1]),float(term[2]),float(term[3])])

dataInv=zip(*data) #inverse the data matrix
geneName=['A','B','C','D']
sequence=numpy.arange(0,1,0.01)

#plot
fig,graphArray = pyplot.subplots(4,4,figsize=(3*3.13,3*3.13))

for i in range(0,4):
        for j in range(0,4):
                graph = graphArray[i,j]
                x=dataInv[i]
                y=dataInv[j]
                graph.plot(x,y,'.',color='black')
                graph.set_title("Gene "+geneName[i]+" vs "+geneName[j])

curve=graphArray[0,1]
x=dataInv[0]
y=dataInv[1]
coeff=numpy.polyfit(x,y,5)#degree-5 polynomial
yCurve=numpy.polyval(coeff,sequence)
curve.plot(sequence,yCurve,color="r")

curve=graphArray[0,2]
x=dataInv[0]
y=dataInv[2]
coeff=numpy.polyfit(x,y,1)#linear
yCurve=numpy.polyval(coeff,sequence)
curve.plot(sequence,yCurve,color="r")

curve=graphArray[0,3]
x=dataInv[0]
y=dataInv[3]
coeff=numpy.polyfit(x,y,3)#cubic curve
yCurve=numpy.polyval(coeff,sequence)
curve.plot(sequence,yCurve,color="r")


#improve the plot
fig.tight_layout()
#fig.suptitle('Correlation Scatterplot of Four Genes')
fig.patch.set_facecolor('white')

#output
pyplot.savefig('problem 4.png', dpi=200)
pyplot.show()
