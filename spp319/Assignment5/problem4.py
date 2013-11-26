import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import numpy as np
from numpy import polyval, polyfit



#grab file
rawData = pd.read_csv('genes.dat')
#divide data up by gene column
geneColumn = rawData[['A','B','C','D']]
#sizeparam
fSize = [10,10]
#create 4x4 matrix
plotMatrix = scatter_matrix(geneColumn, alpha=0.2, figsize = fSize, grid=True, diagonal = '')
#throw the title over the entire matrix
plt.suptitle("Gene Correlation Matrix: Best Fit Lines at Polynomials of Degree N", size = 20)

#use polyfit from numpy to create a best fit line for AB, AC, and AD
relationAB = polyfit(geneColumn['B'], geneColumn['A'], 5)
relationAC = polyfit(geneColumn['C'], geneColumn['A'], 1)
relationAD = polyfit(geneColumn['D'], geneColumn['A'], 3)
#organize data by gene degree of expression
sortedGene1 = sorted(geneColumn['B'])
sortedGene2 = sorted(geneColumn['C'])
sortedGene3 = sorted(geneColumn['D'])
#evaluate at data points
evaluateValues1 = polyval(relationAB,sortedGene1)
evaluateValues2 = polyval(relationAC,sortedGene2)
evaluateValues3 = polyval(relationAD,sortedGene3)
#plot the bestfits on the corresponding axes
plotMatrix[0,1].plot(sortedGene1, evaluateValues1, 'r-', label = 'N = 5', linewidth = 2)
plotMatrix[0,2].plot(sortedGene2, evaluateValues2, 'b-', label = 'N = 1', linewidth = 2)
plotMatrix[0,3].plot(sortedGene3, evaluateValues3, 'm-', label = 'N = 3', linewidth = 2)
plotMatrix[0,1].legend(loc='best', fontsize='small')
plotMatrix[0,2].legend(loc='best', fontsize='small')
plotMatrix[0,3].legend(loc='best', fontsize='small')

plt.savefig('Problem4.png', dpi=300)
