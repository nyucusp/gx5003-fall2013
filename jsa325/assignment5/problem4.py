# Import packages

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import pylab
import numpy as np
from numpy import polyfit, polyval
import scipy
import pandas as pd
from datetime import timedelta, datetime
import math

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

# Part 1: plot correlations between the four genes

plt.subplot(221)
plt.plot(geneA, geneB,'or',alpha = 0.5)
plt.xlabel('Gene A')
plt.ylabel('Gene B')

plt.subplot(222)
plt.plot(geneA, geneC,'ob',alpha = 0.5)
plt.xlabel('Gene A')
plt.ylabel('Gene C')

plt.subplot(223)
plt.plot(geneA, geneD,'og',alpha = 0.5)
plt.xlabel('Gene A')
plt.ylabel('Gene D')

figname = 'Problem 4a.png'
# plt.show()
plt.close()

"""
Visual analysis give the following in descending order of correlation to A: C, D, B.

"""

# Part 2: draw linear best fit line between A and C 

(m,b) = polyfit(geneA, geneC, 1)
# print(m)
# print(b)
fity = polyval([m,b], geneA)

plt.plot(geneA, fity, '-', color = 'red', label = 'Linear Fit')
plt.scatter(geneA, geneC)
plt.xlabel('Gene A')
plt.ylabel('Gene C')
figname = 'Problem 4b.png'
# plt.show()
plt.close()

# Part 3: draw cubic best fit curve between A and D

z = polyfit(geneA, geneD, 3)
fitz = np.poly1d(z)
 
plt.plot(z, '-', color = 'red', label = 'Cubic Fit')
plt.scatter(geneA, geneD)
plt.xlabel('Gene A')
plt.ylabel('Gene D')
figname = 'Problem 4c.png'
# plt.show()
plt.close()

# Part 4: draw degree-5 polynomial best fit curve between A and B

p = polyfit(geneA, geneB, 5)
fitp = np.poly1d(p)

plt.plot(p, '-', color = 'red', label = 'Degree-5 Polynomial Fit')
plt.scatter(geneA, geneB)
plt.xlabel('Gene A')
plt.ylabel('Gene B')
figname = 'Problem 4c.png'
# plt.show()
plt.close()

# FINAL: create 4x4 matrix

fig, axarr = plt.subplots(4, 4)
fig.set_size_inches(8, 8.5)
plt.subplots_adjust(top = 0.92)
plt.suptitle('Gene Expressions', fontsize = 14)
plt.savefig('Problem4.png')
