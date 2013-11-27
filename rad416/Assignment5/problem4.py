import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 3 #set linewidth to be wider

genes = pd.read_csv('genes.dat')

#polyfit
fitac = np.polyfit(genes['A'],genes['C'],1) # Gene C is most correlated A
fitad = np.polyfit(genes['A'],genes['D'],3) # Gene D is the second most correlated A
fitab = np.polyfit(genes['A'],genes['B'],5) # Gene B is the least correlated to A

#fit functions for the lines
fit_fn_ac = np.poly1d(fitac)
fit_fn_ad = np.poly1d(fitad)
fit_fn_ab = np.poly1d(fitab)

xvals = np.linspace(min(genes['A']) - 0.1, max(genes['A']) + 0.1, 100)

axes = pd.scatter_matrix(genes,alpha=0.7,figsize=(9,9), diagonal='None')
axes[1,0].plot(xvals,fit_fn_ab(xvals),'-')
axes[2,0].plot(genes['A'],fit_fn_ac(genes['A']),'-')
axes[3,0].plot(xvals,fit_fn_ad(xvals),'-')

plt.savefig('Problem_4.png')

