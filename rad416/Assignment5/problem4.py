import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 3 #set linewidth to be wider

genes = pd.read_csv('genes.dat')

#polyfit and polyval
fitac = np.polyfit(genes['A'],genes['C'],1)
fitad = np.polyfit(genes['A'],genes['D'],3)
fitab = np.polyfit(genes['A'],genes['B'],5)

#fit functions for the lines
fit_fn = np.poly1d(fitac)
fit_fn_ad = np.poly1d(fitad)
fit_fn_ab = np.poly1d(fitab)

xvals = np.linspace(min(genes['A']), max(genes['A']), 100)

fig, axes = plt.subplots(4,4,figsize=(10,10))
ax12 = fig.add_subplot(4,4,2)
ax12.plot(genes['B'], genes['A'],'o')
ax13 = fig.add_subplot(4,4,3)
ax13.plot(genes['C'], genes['A'],'o')
ax14 = fig.add_subplot(4,4,4)
ax14.plot(genes['D'], genes['A'],'o')
ax21 = fig.add_subplot(4,4,5)
ax21.plot(genes['A'],genes['B'],'o',xvals,fit_fn_ab(xvals),'-')
ax23 = fig.add_subplot(4,4,7)
ax23.plot(genes['C'], genes['B'],'o')
ax24 = fig.add_subplot(4,4,8)
ax24.plot(genes['D'], genes['B'],'o')
ax31 = fig.add_subplot(4,4,9)
ax31.plot(genes['A'],genes['C'],'o',genes['A'],fit_fn(genes['A']),'k--')
ax32 = fig.add_subplot(4,4,10)
ax32.plot(genes['B'], genes['C'],'o')
ax34 = fig.add_subplot(4,4,12)
ax34.plot(genes['D'], genes['C'],'o')
ax41 = fig.add_subplot(4,4,13)
ax41.plot(genes['A'],genes['D'],'o',xvals,fit_fn_ad(xvals),'-')
ax42 = fig.add_subplot(4,4,14)
ax42.plot(genes['B'], genes['D'],'o')
ax43 = fig.add_subplot(4,4,15)
ax43.plot(genes['C'], genes['D'],'o')
plt.savefig('Problem_4.png')

