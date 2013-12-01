# Import packages

import matplotlib.pyplot as plt
import numpy as np
import scipy
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import pylab

params = {'axes.labelsize': 12, 'text.fontsize': 12, 'legend.fontsize': 12, 'xtick.labelsize': 10, 'ytick.labelsize': 10, 'text.usetex': True}

pylab.rcParams.update(params)

# Read data

stocksFile = pd.read_table('/Users/JSAdams/Downloads/Hw1data/stocks.dat', sep = ',')
stocksFile['month'] = pd.to_datetime(stocksFile['month'])

# 1a

fig, ax = plt.subplots()
ax.plot(stocksFile['month'], stocksFile['apple'], 'o-', alpha=0.5)
fig.autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.title('Apple Stock Growth by Month')
plt.savefig('Problem 1a.png')
# plt.show()
plt.close()

"""
To make this plot clear, I chose a simple color (blue) on a white background.
The axes, ticks, and labels are in black sans-serif font.

"""

# 1b

fig, ax = plt.subplots()
stockA = stocksFile['apple'].map(lambda x: x - 75.51)
stockM = stocksFile['microsoft'].map(lambda x: x - 27.06)
# plt.axhline(y=0, color='red')
ax.plot(stocksFile['month'], stockA, 'o-', label='Apple', alpha=0.5)
ax.plot(stocksFile['month'], stockM, 'o-', label='Microsoft', alpha=0.5)
fig.autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Relative Stock Price (USD)')
plt.title('Stock Growth')
plt.legend(loc=0)
plt.savefig('Problem 1b.png')
# plt.show()
plt.close()

"""
One conclusion that can be drawn from this plot is that though Apple's stock
declined more than Microsoft's in the beginning, it rebounded with greater 
growth later on. While Microsoft's stock does not deviate very far from the 
Jan 2006 baseline, Apple's stock does, and periods of sharp decline are followed
by periods of sharp growth. This can be interpreted as adaptation or innovation
driven by necessity.

"""

# 1c

fig, (ax1,ax2) = plt.subplots(1,2,sharey=False)

fig.autofmt_xdate()
fig.set_size_inches(9.60,3.60)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.8, hspace=None)

ax1.plot(stocksFile['month'], stockA, 'o-', color='blue', label='Apple', alpha=0.5)
# plt.axhline(y=0, color='red')
ax1.set_xlabel('Date')
ax1.set_ylabel('Relative Stock Price (USD)')
ax1.set_title('Apple Stock Growth since Jan 2006')
ax1.set_ylim(-50,150)
ax1.legend(loc=2)

ax2.plot(stocksFile['month'], stockM, 'o-', color='green', label='Microsoft', alpha=0.5)
# plt.axhline(y=0, color='red')
ax2.set_xlabel('Date')
ax2.set_ylabel('Relative Stock Price (USD)')
ax2.set_title('Microsoft Stock Growth since Jan 2006')
ax2.set_ylim(-10,30)

plt.legend(loc=2)
plt.savefig('Problem 1c.png')
# plt.show()
plt.close()

"""
I think superposition makes more sense here. In order to fit two subplots side-by-side
in a single figure, and to show the data in those subplots, you have to adjust the y-axis
limits. This makes it difficult to visually compare the two subplots, which is the whole
point.

"""
