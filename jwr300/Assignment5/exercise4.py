#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 5, Exercise 4
#Scatterplot Matrix for Gene Expression A-D

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

os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin/latex'

#Clearing plot figure and setting pylab formatting pyrameters
clf()
params = {'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 13,
          'xtick.labelsize': 6,
          'ytick.labelsize': 6,
          'xtick.direction': 'out',
          'text.usetex': True}

pylab.rcParams.update(params)



def main():
	geneA = []
	geneB = []
	geneC = []
	geneD = []

	#pass gene expression data to list and then to dataframe
	with open('genes.dat','r') as myFile4:
		header = myFile4.readline().strip().split(',')
		for line in myFile4:
			geneA.append(float(line.strip().split(',')[0]))
			geneB.append(float(line.strip().split(',')[1]))
			geneC.append(float(line.strip().split(',')[2]))
			geneD.append(float(line.strip().split(',')[3]))
	    
	df4 = pd.DataFrame({str(header[0]):geneA, str(header[1]):geneB, str(header[2]):geneC, str(header[3]):geneD})
	df4 = df4.sort(['A','B','C','D'])

	#Calling scattermatrix method on the data frame
	axes = scatter_matrix(df4, alpha=0.2, figsize=(4, 4), diagonal='histogram')

	coeff_AB = np.polyfit(df4['B'],df4['A'],5)
	df4_sort = df4.sort(['B'])
	linreg_AB = np.polyval(coeff_AB, df4_sort['B'])
	AB = axes[0,1]
	AB.plot(df4_sort['B'], linreg_AB, c='red', label='Best fit, 5th degree')
	AB.legend(loc='best', frameon=False, fontsize=3, numpoints=1)
	yticks(ha='right')
	xticks(ha='left')

	coeff_AC = np.polyfit(df4['C'],df4['A'],1)
	df4_sort = df4.sort(['C'])
	linreg_AC = np.polyval(coeff_AC, df4_sort['C'])
	AC = axes[0,2]
	AC.plot(df4_sort['C'], linreg_AC, c='red', label='Best fit, 1st degree')
	AC.legend(loc='best', frameon=False, fontsize=3, numpoints=1)

	yticks(ha='right')
	xticks(ha='left')

	coeff_AD = np.polyfit(df4['D'],df4['A'],3)
	df4_sort = df4.sort(['D'])
	linreg_AD = np.polyval(coeff_AD, df4_sort['D'])
	AD = axes[0,3]
	AD.plot(df4_sort['D'], linreg_AD, c='red', label='Best fit, 3rd degree')
	AD.legend(loc='best', frameon=False, fontsize=3, numpoints=1)
	plt.subplots_adjust(left=0.16, bottom=0.16, right=None, top=None, wspace=0.14, hspace=0.14)
	yticks(ha='right')
	xticks(ha='left')

	#plt.show()
	plt.suptitle('Gene Expressions of A, B, C, D', fontsize=14)
	plt.savefig('Problem4.png',dpi=400)



if __name__ == "__main__":
	main()

'''
Annotations
Based on visual analysis, gene A is best correlated with C, 
less correlated with D, and most likely not correlated with B.
'''