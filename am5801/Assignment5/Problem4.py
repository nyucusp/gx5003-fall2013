# Awais Malik
# Assignment 5
# Problem 4
# Annotations at the end of the code
# Open Scatter Plot in Full Screen Mode

import pandas as pd
from pandas.tools.plotting import scatter_matrix
import numpy
from numpy import polyval, polyfit
import matplotlib.pyplot as plt
from matplotlib import *

# Import the stocks.dat file
gene_file = pd.read_csv('genes.dat')
genes = gene_file[['A','B','C','D']]

ender = scatter_matrix(genes, alpha=0.2, figsize=None, diagonal = 'kde')

# A vs B Correlation (5th degree poly fit)
B_coefficients = polyfit(genes['B'],genes['A'],5)
Bx_sort = sorted(genes['B'])
By_values = polyval(B_coefficients, Bx_sort)
ender[0,1].plot(Bx_sort, By_values, 'r-', label = '5th degree')
ender[0,1].legend(loc='upper left', fontsize='x-small')

# A vs C Correlation (Linear fit)
C_coefficients = polyfit(genes['C'],genes['A'],1)
Cx_sort = sorted(genes['C'])
Cy_values = polyval(C_coefficients, Cx_sort)
ender[0,2].plot(Cx_sort, Cy_values, 'r-', label = 'Linear')
ender[0,2].legend(loc='upper left', fontsize='x-small')

# A vs D Correlation (3rd degree poly fit)
D_coefficients = polyfit(genes['D'],genes['A'],3)
Dx_sort = sorted(genes['D'])
Dy_values = polyval(D_coefficients, Dx_sort)
ender[0,3].plot(Dx_sort, Dy_values, 'r-', label = '3rd degree')
ender[0,3].legend(loc='upper left', fontsize='x-small')

plt.figtext(0.5, 0.94, 'Correlation Scattor Plots of Genes A, B, C & D', fontsize = 'x-large', ha = 'center')

""" Annotations:
Pandas rescues me once again! The scatter_matrix function takes care of
all the mess involved in creating 12 subplots. However, I do not have the option
of putting scatter plots in the diagonals. I can either use Kernel Density curves
or histograms. I chose the kde option. I then used polyval and polyfit
to create the polynomial fits for the three plots. """