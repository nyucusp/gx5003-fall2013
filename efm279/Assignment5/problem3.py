# Need to import the plotting package:

import matplotlib.pyplot as plt
from scipy import *
import csv
import math
import numpy
import operator

x1 = []
dates = []
ttor = []
bars = []
barcount=1

with open('microprocessors.dat', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    spamreader.next()
    spamreader = sorted(spamreader, key=operator.itemgetter(1), reverse=True)
    
    for row in spamreader:
            x1.append(row[0])
            bars.append(barcount)
            dates.append(row[1])
            ttor.append(row[2])
            barcount=barcount+1
plt.figure(figsize=(15,15), dpi=100)

ax1=plt.subplot(1, 2, 1)
ax1.plot(dates, bars,'o')
ax1.set_xlim(1960,2013)
ax1.set_ylim(0,14)
ax1.set_yticks(bars, x1)
ax1.set_title('Processor Release Year',fontsize=12)
ax1.set_xlabel('Year of Introduction')
ax1.set_ylabel('Processor')
ax1.grid(True)
fabio=0


ax2=plt.subplot(1, 2, 2,sharey=ax1)
ax2.plot(ttor, bars,'o')
ax2.set_ylim(0,14)
plt.yticks(bars, x1)
ax2.set_xscale('log', basex=10)
ax2.set_xlabel('Transistors (log10)')
ax2.set_title('Processor Number of Transistors',fontsize=12)
plt.setp(ax2.get_yticklabels(), visible=False)
fabio2=0

## The dot plot shows that there is a correlation between the number of transistors and release date as expected.
## Itanium which is released the latest has the highest number of transistors



ax2.grid(True)
plt.tight_layout()
plt.show()

