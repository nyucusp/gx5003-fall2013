import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
import pandas as pd
from pandas.tools.plotting import scatter_matrix
from pylab import *
from numpy import arange, array, ones, linalg


genes = pd.read_csv('genes.dat')
data = genes[['A', 'B', 'C', 'D']]

scatter = pd.scatter_matrix(genes, diagonal='kde', color='k', alpha=0.2)

#Based on the plot gene C is most correlated to gene A, then gene D, then B.
#making a linear best fit with A and C
xi=(genes['A'])
A=array([xi, ones(len(genes))])
y=(genes['C'])
w = linalg.lstsq(A.T,y)[0]

line=w[0]*xi+w[1]
scatter[2,0].plot(xi, line, 'r-', label = "Linear")
scatter[2,0].legend(loc='upper left', fontsize='x-small')

xi=(genes['C'])
A=array([xi, ones(len(genes))])
y=(genes['A'])
w = linalg.lstsq(A.T,y)[0]

line=w[0]*xi+w[1]
scatter[0,2].plot(xi, line, 'r-', label = "Linear")
scatter[0,2].legend(loc='upper left', fontsize='x-small')
#making a cubic best fit with A and D
import pylab

x=(genes['A'])
y=(genes['D'])
z3 = polyfit(x,y,3)
p3=poly1d(z3)
xx=linspace(0,1,100)
scatter[3,0].plot(xx,p3(xx), 'g-', label="3rd Degree")
scatter[3,0].legend(loc='upper left', fontsize='x-small')


x=(genes['D'])
y=(genes['A'])
z3 = polyfit(x,y,3)
p3=poly1d(z3)
xx=linspace(0,1,100)
scatter[0,3].plot(xx,p3(xx), 'g-', label="3rd Degree")
scatter[0,3].legend(loc='upper left', fontsize='x-small')

#making a fifth degree polynomial line of best fit for A and B
x=(genes['A'])
y=(genes['B'])
z5 = polyfit(x,y,5)
p5=poly1d(z5)
xx=linspace(0,1,100)
scatter[1,0].plot(xx,p5(xx), 'y-', label='5th Degree')
scatter[1,0].legend(loc='upper left', fontsize='x-small')

x=(genes['B'])
y=(genes['A'])
z5 = polyfit(x,y,5)
p5=poly1d(z5)
xx=linspace(0,1,100)
scatter[0,1].plot(xx,p5(xx), 'y-', label='5th Degree')
scatter[0,1].legend(loc='upper left', fontsize='x-small')

plt.suptitle('Correlation between Genes A,B,C and D', fontsize=18)
plt.show()