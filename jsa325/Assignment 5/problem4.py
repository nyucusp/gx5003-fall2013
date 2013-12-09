# Import packages

import pandas as pd
from scipy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import pylab
from pylab import *
from matplotlib.dates import MonthLocator, DateFormatter
from pandas.tools.plotting import scatter_matrix
from numpy import polyval, polyfit

params = {'axes.labelsize': 10, 'text.fontsize': 10, 'legend.fontsize': 13, 'xtick.labelsize': 6, 'ytick.labelsize': 6, 'xtick.direction': 'out', 'text.usetex': True}

pylab.rcParams.update(params)

geneA = []
geneB = []
geneC = []
geneD = []

with open('/Users/JSadams/Downloads/Hw1data/genes.dat', 'r') as genesFile:
    header = genesFile.readline().strip().split(',')
    for line in genesFile:
        geneA.append(float(line.strip().split(',')[0]))
        geneB.append(float(line.strip().split(',')[1]))
        geneC.append(float(line.strip().split(',')[2]))
        geneD.append(float(line.strip().split(',')[3]))
    genesFile.close()

dfGenes = pd.DataFrame({str(header[0]):geneA, str(header[1]):geneB, str(header[2]):geneC, str(header[3]):geneD})
dfGenes = dfGenes.sort(['A','B','C','D'])

axes = scatter_matrix(dfGenes, alpha=0.3, figsize=(4, 4), diagonal='histogram')

# Part 2: draw linear best fit line between A and C 

y = polyfit(dfGenes['C'],dfGenes['A'],1)
fity = polyval(y, dfGenes.sort(['C']))
AC = axes[0,2]
AC.plot(dfGenes.sort(['C']), fity, c='red', label='Linear Best Fit')
AC.legend(loc='best', frameon=False, fontsize=3, numpoints=1)
yticks(ha='right')
xticks(ha='left')

# Part 3: draw cubic best fit curve between A and D

z = polyfit(dfGenes['D'],dfGenes['A'],3)
fitz = polyval(z, dfGenes.sort(['D']))
AD = axes[0,3]
AD.plot(dfGenes.sort(['D']), fitz, c='red', label='Best Cubic Fit')
AD.legend(loc='best', frameon=False, fontsize=3, numpoints=1)
yticks(ha='right')
xticks(ha='left')

# Part 4: draw degree-5 polynomial best fit curve between A and B

p = polyfit(dfGenes['B'],dfGenes['A'],5)
fitp = polyval(p, dfGenes.sort(['B']))
AB = axes[0,1]
AB.plot(dfGenes.sort(['B']), fitp, c='red', label='Best 5-Degree Polynomial Fit')
AB.legend(loc='best', frameon=False, fontsize=3, numpoints=1)
yticks(ha='right')
xticks(ha='left')

# FINAL: create 4x4 matrix

plt.suptitle('Expression of Genes A, B, C, D', fontsize=14)
plt.savefig('Problem 4.png')
plt.show()
plt.close()

"""                                                                                                      Visual analysis give the following in descending order of correlation to A: C, D, B.                     

"""
