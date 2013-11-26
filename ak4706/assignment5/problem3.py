import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
import pandas as pd

df = pd.read_csv('microprocessors.dat', parse_dates=True, index_col=0)
#print df
data = df[['Year of Introduction', 'Transistors']]
# year = data.set_index('Year of Introduction')
# year = year.sort()
# trans = data.set_index('Transistors')
# trans = trans.sort()

fig, axs = plt.subplots(2,1, sharex=True)
#fig.subplots_adjust(hspace=.5)
data.sort('Year of Introduction', inplace=True)
data['Year of Introduction'].plot(ax=axs[0], style='o')

axs[0].set_ylabel('Year of Introduction')
plt.xlabel('')
axs[0].set_xlabel('')
axs[1].set_xlabel('')

plt.ylabel('Number of Transistors')
axs[1].set_yscale('log', basey=10)

data['Transistors'].plot(ax=axs[1], style='o')
#plt.title('Microsoft')
plt.suptitle('Microprocessors', fontsize=18)
names = ["4004", "8008", "8080", "8086", "286", "386TM", "486TM DX", "Pentium", "Pentium II", "Pentium III", "Pentium IV", "Xeon", "Itanium"]
loc, labels = plt.xticks(range(len(names)), names)
plt.setp(labels, rotation=30, fontsize=8)

plt.show()