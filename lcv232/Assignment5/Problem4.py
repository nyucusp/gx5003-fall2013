import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import numpy as np
from numpy import polyval, polyfit


data = pd.read_csv('genes.dat')
data_column = data[['A','B','C','D']]  # Splitting data by columns
boxplot = [10,10] # Setting the grid size for each plot in the output
plot_grid = scatter_matrix(data_column, alpha=0.2, figsize = boxplot, grid=True, diagonal = '') # Creating the grid of 4x 4 matrix
plt.suptitle("Gene Correlation Matrix: Best Fit Lines at Polynomials of Degree N", size = 20) # The title for the output plot

rel_AB = polyfit(data_column['B'], data_column['A'], 5) # Making use of the function 'polyfit' from numpy to create the best fit line for AB, AC, and AD
rel_AC = polyfit(data_column['C'], data_column['A'], 1)
rel_AD = polyfit(data_column['D'], data_column['A'], 3)

plotGene1 = sorted(data_column['B']) # Plotting data by degree of expression
plotGene2 = sorted(data_column['C'])
plotGene3 = sorted(data_column['D'])

check_Val1 = polyval(rel_AB,plotGene1)  # Checking at various data points
check_Val2 = polyval(rel_AC,plotGene2)
check_Val3 = polyval(rel_AD,plotGene3)

plot_grid[0,1].plot(plotGene1, check_Val1, 'r-', label = 'N = 5', linewidth = 2) # Plotting the bestfit values on the respective corresponding axis
plot_grid[0,2].plot(plotGene2, check_Val2, 'b-', label = 'N = 1', linewidth = 2)
plot_grid[0,3].plot(plotGene3, check_Val3, 'm-', label = 'N = 3', linewidth = 2)
plot_grid[0,1].legend(loc='best', fontsize='small')
plot_grid[0,2].legend(loc='best', fontsize='small')
plot_grid[0,3].legend(loc='best', fontsize='small')

plt.savefig("Problem4.png")
