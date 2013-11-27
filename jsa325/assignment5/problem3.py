# Import packages

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import pylab
import numpy as np
import scipy
import pandas as pd
from datetime import timedelta
from datetime import datetime
import math

params = {'axes.labelsize': 12, 'text.fontsize': 12, 'legend.fontsize': 12, 'xtick.labelsize': 7, 'ytick.labelsize': 5, 'text.usetex': True}

pylab.rcParams.update(params)

processor = []
year = []
number = []
header = []

with open('/Users/JSAdams/Downloads/Hw1data/microprocessors.dat', 'r') as microFile:
    header = microFile.readline().strip().split(',')

    for line in microFile:
        processor.append(line.strip().split(',')[0])
        year.append(line.strip().split(',')[1])
        number.append(line.strip().split(',')[2])

fig, (ax1, ax2) = plt.subplots(1, 2, sharey = True)

fig.set_size_inches(7.20, 3.60)
fig.subplots_adjust(left = 0.18, bottom = None, right = 0.95)

ax1.plot(year, processor, 'o', color='red', label='Year')
ax1.set_xlabel('Year')
ax1.set_ylabel('Processor')
ax1.set_ylim(-0.5, 12.5)
ax1.set_yticks(processor)
ax1.set_yticklabels(name)
ax1.legend(loc = 2)

fig.autofmt_xdate()

ax2.plot(number, year, 'o', color='blue', label='Transistors')
ax2.set_xlabel('Transistors')
ax2.set_xscale('log')

figname = 'Problem 3.png'

plt.legend(loc = 2)
plt.savefig(figname)
plt.show()
plt.close()
