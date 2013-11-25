
import matplotlib.pyplot as plt
import pylab
import csv
import math
import numpy as np


x1=[]
x2=[]
x3=[]
x4=[]

with open('genes.dat', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    spamreader.next() 
    for row in spamreader:
            x1.append(row[0])
            x2.append(row[1])
            x3.append(row[2])
            x4.append(row[3])

def poly_fit(dat1, dat2, order):
     dat1 = np.array(dat1)
     dat2 = np.array(dat2)
     dat1=dat1.astype(np.float)
     dat2=dat2.astype(np.float)
     z=np.polyfit(dat1,dat2,order)
     f=np.poly1d(z)
     x_new = np.linspace(min(dat2), max(dat2), 50)
     y_new = f(x_new)
     return (x_new,y_new)

def example_plot(ax, dat1, dat2, gen1, gen2, fontsize=12):
     gendic={0:"A",1:"B",2:"C",3:"D"}   
     ax.scatter(dat1,dat2,s=5)
     ax.locator_params(nbins=12)
     ax.set_xlabel('Gene '+gendic[gen1], fontsize=fontsize)
     ax.set_ylabel('Gene '+gendic[gen2], fontsize=fontsize)
     if gen1==0 and gen2==2:
             claudio=poly_fit(dat1,dat2,1)
             ax.plot(claudio[0],claudio[1],label='Best Fit:Linear')
             ax.legend(loc='best', fontsize='xx-small')
     if gen1==0 and gen2==3:
             claudio=poly_fit(dat1,dat2,3)
             ax.plot(claudio[0],claudio[1], label='Best Fit: 3rd Degree Poly.')
             ax.legend(loc='upper left', fontsize='xx-small')
     if gen1==0 and gen2==1:
             claudio=poly_fit(dat1,dat2,5)
             ax.plot(claudio[0],claudio[1], label='Best Fit: 5th Degree Poly.')
             ax.legend(loc='upper left', fontsize='xx-small')

plt.figure(figsize=(15,15))
investigate=['x1','x2','x3','x4']
fabio=0
nivan=0
for i in range(16):
    ax=plt.subplot(4,4,i+1)
    example_plot(ax,eval(investigate[fabio]),eval(investigate[nivan]),fabio,nivan)
    if fabio!=3:
            fabio=fabio+1
    elif fabio==3:
            fabio=0
            nivan=nivan+1
    if nivan==4:
            nivan=1
    plt.ylim([0,1])
    plt.xlim([0,1])
    
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.5)
plt.subplots_adjust(top=0.94)
plt.suptitle('Correlation Graphs for Genes A,B,C,and D')
plt.show()

## Visually Gene C is the mostly correlated gene with Gene A
## Gene D has the second best correlation
## Gene B has the lowest correlatio with Gene A
## Best fits are provided as requested
