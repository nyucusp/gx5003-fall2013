from matplotlib import pyplot
from math import log
import numpy as np

# read data form dat file
inputFile = open('Hw1data/microprocessors.dat','r')
header = inputFile.readline()
sequence=[]
data=[]
i=0

for line in inputFile:
        term = line.split(",")
        data.append([term[0],int(term[1]),float(term[2])])
        i+=1
        sequence.append(i)
#plot
fig = pyplot.figure(figsize=(4*3.13,1.8*3.13))

sortedYear=sorted(data,key=lambda tup:tup[1]) #sorted the data by year
year=zip(*sortedYear)[1]
label=zip(*sortedYear)[0]
graph1 = fig.add_subplot(1,2,1)
graph1.plot(year,sequence,"o", color='b')
graph1.set_yticklabels(label)
pyplot.yticks(np.arange(1, 15, 1))
graph1.set_title('Processor vs Year')
graph1.set_xlabel('Year',fontweight='bold')
graph1.yaxis.grid()

sortedTransistor=sorted(data,key=lambda tup:tup[2])#sorted the data by tansistor
transistor=zip(*sortedYear)[2]
label=zip(*sortedYear)[0]
graph2 = fig.add_subplot(1,2,2)
graph2.plot(transistor,sequence, "o",color='r')
graph2.set_yticklabels(label)
graph2.set_xscale('log')
pyplot.yticks(np.arange(1, 15, 1))
graph2.set_title('Processor vs Transistor')
graph2.set_xlabel('Transistor',fontweight='bold')
graph2.yaxis.grid()


#improve the plot
fig.tight_layout()
fig.autofmt_xdate()
fig.patch.set_facecolor('white')

#output
pyplot.savefig('problem 3.png', dpi=200)
pyplot.show()

"""
Annotation:
The key of drawing this dot plot is to sort the dataset (by year or transistor)first before plotting.The whole procedure of CPU development will be extremely clear in this way.   
"""
