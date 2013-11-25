#Aliya Merali
#Urban Informatics
#Assignment 5
#Problem 4

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.pylab import *

#Parsing data to get 3 lists with info
data = open('genes.dat','r')

A = []
B = []
C = []
D = []
for gene in data: 
    A.append(gene.split(',')[0])
    B.append(gene.split(',')[1])
    C.append(gene.split(',')[2])
    D.append(gene.split(',')[3])
del A[0]
del B[0]
del C[0]
del D[0]

i=0
for gene in A: 
    A[i] = float(gene)
    i = i +1
i=0
for gene in B: 
    B[i] = float(gene)
    i = i +1
i=0
for gene in C: 
    C[i] = float(gene)
    i = i +1
i=0
for gene in D: 
    D[i] = float(gene)
    i = i +1



x = [-7.30000, -4.10000, -1.70000, -0.02564,
     1.50000, 4.50000, 9.10000]
y = [-0.80000, -0.50000, -0.20000, 0.00000,
     0.20000, 0.50000, 0.80000]



#___PLOTTING
plt.subplot2grid((4,4),(0,0))
plt.scatter(A, A, color = '0.25') #xfit, fit(xfit), 'r-', lw=2)
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene A vs. A', fontsize=11)

#___BEST FIT LINE 5TH ORDER
fifth=np.polyfit(A,B,5)
xp = np.linspace(0,1,10000)
p = np.poly1d(fifth)
plt.subplot2grid((4,4),(0,1))
plt.scatter(A, B, color = '0.25')
plt.plot(xp, p(xp), 'r', label = 'Best Fit'"\n"'5th deg')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene A vs. B', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})


#___BEST FIT LINE LINEAR
first = np.polyfit(A,C,1)
xp = np.linspace(0,1,10000)
p = np.poly1d(first)
plt.subplot2grid((4,4),(0,2))
plt.scatter(A, C, color = '0.25')
plt.plot(xp, p(xp), 'r', label = 'Best Fit'"\n"'1st deg')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene A vs. C', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})

#___BEST FIT LINE CUBIC
third =np.polyfit(A,D,3)
xp = np.linspace(0,1,10000)
p = np.poly1d(third)
plt.subplot2grid((4,4),(0,3))
plt.scatter(A, D, color = '0.25')
plt.plot(xp, p(xp), 'r', label = 'Best Fit'"\n"'3rd deg')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene A vs. D', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})

plt.subplot2grid((4,4),(1,0))
plt.scatter(B, A, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene B vs. A', fontsize=11)

plt.subplot2grid((4,4),(1,1))
plt.scatter(B, B, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene B vs. B', fontsize=11)

plt.subplot2grid((4,4),(1, 2))
plt.scatter(B, C, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene B vs. C', fontsize=11)

plt.subplot2grid((4,4),(1, 3))
plt.scatter(B, D, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene B vs. D', fontsize=11)

plt.subplot2grid((4,4),(2, 0))
plt.scatter(C, A, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene C vs. A', fontsize=11)

plt.subplot2grid((4,4),(2, 1))
plt.scatter(C, B, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene C vs. B', fontsize=11)

plt.subplot2grid((4,4),(2, 2))
plt.scatter(C, C, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene C vs. C', fontsize=11)

plt.subplot2grid((4,4),(2, 3))
plt.scatter(C, D, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene C vs. D', fontsize=11)

plt.subplot2grid((4,4),(3, 0))
plt.scatter(D, A, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene D vs. A', fontsize=11)

plt.subplot2grid((4,4),(3, 1))
plt.scatter(D, B, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene D vs. B', fontsize=11)

plt.subplot2grid((4,4),(3, 2))
plt.scatter(D, C, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene D vs. C', fontsize=11)

plt.subplot2grid((4,4),(3, 3))
plt.scatter(D, D, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.setp(plt.gca(), xticklabels = ['0.00', '0.25','0.50','0.75','1.00'], yticks=(0.00, 0.25, 0.50, 0.75, 1.00), yticklabels = ['0.00', '0.25', '0.50','0.75','1.00'], xticks=(0.00, 0.25, 0.50, 0.75, 1.00))
plt.setp(plt.xticks()[1], rotation=10, fontsize = 10)
plt.setp(plt.yticks()[1], rotation=0, fontsize = 10)
plt.title('Gene D vs. D', fontsize=11)

plt.tight_layout()
plt.suptitle('Gene Activity Correlations', fontsize=15)
plt.subplots_adjust(top=0.9)
plt.show()

