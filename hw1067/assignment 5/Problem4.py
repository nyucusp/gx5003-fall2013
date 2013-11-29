# -*- coding: utf-8 -*-
#Haozhe Wang
#Problem 4


import pandas as pd
import matplotlib.pyplot as plt
import pylab
import numpy as np
from scipy import polyfit

genesfile = pd.read_csv('genes.dat')

data = genesfile[['A','C','D','B']]

cool = pd.scatter_matrix(data, figsize = (8,8), diagonal = 'kde', color = 'k', alpha = 0.3)
#cool.set_title('Genes correalted to Group A')

#Fitting lines
B_coefficients = polyfit(genesfile['B'],genesfile['A'],5)
Bx_sort = sorted(genesfile['B'])
By_values = polyval(B_coefficients, Bx_sort)
cool[0,3].plot(Bx_sort, By_values, 'g-', label = '5th degree')
cool[0,3].legend(loc='upper left', fontsize='x-small')

C_coefficients = polyfit(genesfile['C'],genesfile['A'],1)
Cx_sort = sorted(genesfile['C'])
Cy_values = polyval(C_coefficients, Cx_sort)
cool[0,2].plot(Cx_sort, Cy_values, 'g-', label = 'Linear')
cool[0,2].legend(loc='upper left', fontsize='x-small')

D_coefficients = polyfit(genesfile['D'],genesfile['A'],3)
Dx_sort = sorted(genesfile['D'])
Dy_values = polyval(D_coefficients, Dx_sort)
cool[0,1].plot(Dx_sort, Dy_values, 'g-', label = '3rd degree')
cool[0,1].legend(loc='upper left', fontsize='x-small')


pd.scatter_matrix.savefig('Problem4.png', dpi = 300)

# <codecell>


