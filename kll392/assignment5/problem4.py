import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pylab import *
import numpy as np

'''
The genes rank in correlation to A by C, D, B.  The plot of AxC shows a linear best fit, AxD shows a cubic best fit curve and AxB shows a 5th degree polynomial best fit.  
'''

aa, bb, cc, dd = [], [], [], []

with open('genes.dat', 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        aa.append(row[0])
        bb.append(row[1])
        cc.append(row[2])
        dd.append(row[3])

aa = np.array(aa, np.float)
bb = np.array(bb, np.float)
cc = np.array(cc, np.float)
dd = np.array(dd, np.float)

fig = plt.figure()

ax11 = fig.add_subplot(4, 4, 1)
ax12 = fig.add_subplot(4, 4, 2)
ax13 = fig.add_subplot(4, 4, 3)
ax14 = fig.add_subplot(4, 4, 4)
ax21 = fig.add_subplot(4, 4, 5)
ax22 = fig.add_subplot(4, 4, 6)
ax23 = fig.add_subplot(4, 4, 7)
ax24 = fig.add_subplot(4, 4, 8)
ax31 = fig.add_subplot(4, 4, 9)
ax32 = fig.add_subplot(4, 4, 10)
ax33 = fig.add_subplot(4, 4, 11)
ax34 = fig.add_subplot(4, 4, 12)
ax41 = fig.add_subplot(4, 4, 13)
ax42 = fig.add_subplot(4, 4, 14)
ax43 = fig.add_subplot(4, 4, 15)
ax44 = fig.add_subplot(4, 4, 16)

plotArray = [ax11, ax12, ax13, ax14, ax21, ax22, ax23, ax24, ax31, ax32, ax33, ax34, ax41, ax42, ax43, ax44]

xp = np.arange(0, 1, 0.05)

ax11.scatter(aa, aa, marker='.', color='black')

ax12.scatter(aa, bb, marker='.', color='black')
p5 = np.poly1d(np.polyfit(aa, bb, 5))
ax12.plot(xp, p5(xp), 'r', linewidth = 2)

ax13.scatter(aa, cc, marker='.', color='black')
p = np.poly1d(np.polyfit(aa, cc, 1))
ax13.plot(xp, p(xp), 'r', linewidth = 2)

ax14.scatter(aa, dd, marker='.', color='black')
p3 = np.poly1d(np.polyfit(aa, dd, 3))
ax14.plot(xp, p3(xp), 'r', linewidth = 2)

ax21.scatter(bb, aa, marker='.', color='black')
ax22.scatter(bb, bb, marker='.', color='black')
ax23.scatter(bb, cc, marker='.', color='black')
ax24.scatter(bb, dd, marker='.', color='black')
ax31.scatter(cc, aa, marker='.', color='black')
ax32.scatter(cc, bb, marker='.', color='black')
ax33.scatter(cc, cc, marker='.', color='black')
ax34.scatter(cc, dd, marker='.', color='black')
ax41.scatter(dd, aa, marker='.', color='black')
ax42.scatter(dd, bb, marker='.', color='black')
ax43.scatter(dd, cc, marker='.', color='black')
ax44.scatter(dd, dd, marker='.', color='black')

ax11.set_ylabel('A', rotation = 'horizontal')
ax21.set_ylabel('B', rotation = 'horizontal')
ax31.set_ylabel('C', rotation = 'horizontal')
ax41.set_ylabel('D', rotation = 'horizontal')
ax41.set_xlabel('A')
ax42.set_xlabel('B')
ax43.set_xlabel('C')
ax44.set_xlabel('D')

for plot in plotArray:
    plot.set_xticklabels('')
    plot.set_yticklabels('')

plt.suptitle('Gene Correlation', size=18)

plt.show()


