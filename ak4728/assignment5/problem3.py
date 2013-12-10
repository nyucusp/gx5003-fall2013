import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from operator import itemgetter
import numpy as np
from matplotlib import pyplot

f = open("microprocessors.dat","r")
name = []
year = []
trans = []
f.next()
mydict1= {}
mydict2= {}
for row in f:
    a = row.strip('\n').split(',')
    mydict1[a[0]] = int(a[1])
    mydict2[a[0]] = int(a[2])

for key,value in sorted(mydict1.items(), key=itemgetter(1)):
    year.append(value)
    name.append(key)
             
for value in sorted(mydict2.values()):     
    trans.append(value)

labels = []
for i in range(len(name)):
    labels.append(i+1)

fig = plt.figure()

#first plot
ax1 = fig.add_subplot(121)
ax1.plot(year, labels, 'o')
ax1.yaxis.grid()
ax1.set_title('Processors by Year')
ax1.set_xlabel('Year')
plt.xlim([1960, 2010])
ax1.set_yticklabels(name)
pyplot.yticks(np.arange(1, 15, 1))


#second plot
ax2 = fig.add_subplot(122)
ax2.plot(trans, labels, 'o')
ax2.yaxis.grid()
ax2.set_xscale('log')
ax2.set_title('Transistors(LOG)')
ax2.set_xlabel('Log of the numbe of transistors')
plt.yticks(labels)
pyplot.yticks(np.arange(1, 15, 1))


fig.tight_layout()
#plot
pyplot.savefig('problem3.png', dpi=200)
plt.show()


#Annotation
