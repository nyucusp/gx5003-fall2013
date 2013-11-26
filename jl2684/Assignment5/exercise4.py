import pylab
import scipy
import csv
import sys
import scipy
import array
from matplotlib import *
from pylab import *
from scipy import *
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.ticker as mticker 
from matplotlib import dates 
import datetime 
from scipy import stats
import dateutil.parser as dparser
from matplotlib import pyplot as PLT 
import collections 
import itertools
from matplotlib.dates import date2num
import matplotlib as mpl 

genes_file = open('genes.dat', 'rU')
genes_lines = csv.reader(genes_file)


list_a = [] 
list_b = [] 
list_c = [] 
list_d = [] 

for x in genes_lines:
	list_a.append(x[0])
	list_b.append(x[1])
	list_c.append(x[2])
	list_d.append(x[3])

list_a = list_a[1:]
list_b = list_b[1:]
list_c = list_c[1:]
list_d = list_d[1:]


list_a_float = [] 
list_b_float = [] 
list_c_float = [] 
list_d_float = []

for x in list_a:
	list_a_float.append(float(x)) 
for x in list_b:
	list_b_float.append(float(x)) 

for x in list_c:
	list_c_float.append(float(x)) 

for x in list_d:
	list_d_float.append(float(x)) 


print list_a_float
print list_b_float
print list_c_float
print list_d_float

fig = PLT.figure() 

ticks_x = [0.00, 0.25, 0.50, 0.75, 1.00]
## A ## 
ax1 = plot.subplot2grid((4,4),(0,0))
ax1.scatter(list_a_float, list_a_float, 5, color='blue', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax1.grid(True)
ax1.set_xticks(ticks_x) 
ax1.set_yticks(ticks_x)
ax1.set_title('A vs A')

ax2 = plot.subplot2grid((4,4),(1,0))
### Degree 5 ### 
p5 = np.poly1d(np.polyfit(list_a_float, list_b_float,5))
ax2.plot(ticks_x, p5(ticks_x), color='red')
###
ax2.scatter(list_a_float, list_b_float, 5, color='blue', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax2.grid(True)
ax2.set_xticks(ticks_x) 
ax2.set_yticks(ticks_x)
ax2.set_title('A vs B')


ax3 = plot.subplot2grid((4,4),(2,0))
ax3.scatter(list_a_float, list_c_float, 5, color='blue', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax3.grid(True)
### Linear ### 
(m,b)=polyfit(list_a_float, list_d_float, 1)
yp=polyval([m,b],list_a_float)
ax3.plot(list_a_float,yp, color='red')
###
ax3.set_xticks(ticks_x)
ax3.set_yticks(ticks_x)
ax3.set_title('A vs C')


ax4 = plot.subplot2grid((4,4),(3,0))
### CUBE 
p3 = np.poly1d(np.polyfit(list_a_float, list_d_float,3))
ax4.plot(ticks_x, p3(ticks_x), color='red')
###
ax4.scatter(list_a_float, list_d_float, 5, color='blue', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax4.grid(True)
ax4.set_xticks(ticks_x)
ax4.set_yticks(ticks_x)
ax4.set_title('A vs D')


### Cube ### 
#xp = np.linspace(-2,6,100) 
#p3 = np.poly1d(np.polyfit(list_a_float, list_d_float,3))
#ax4.plot(list_a_float, list_d_float, '-', xp, p3(xp), '--')
#cube =polyfit(list_a_float, list_d_float, 3)
#polynomial3 = poly1d(cube)
#yp=polyval([m,b],list_a_float)
#ax3.plot(list_a_float, list_d_float, 'list_a_float', polynomial3(list_a_float), '-')
###

## B ## 
ax5 = plot.subplot2grid((4,4),(0,1))
ax5.scatter(list_b_float, list_a_float, 5, color='yellow', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax5.grid(True)
ax5.set_xticks(ticks_x)
ax5.set_yticks(ticks_x)
ax5.set_title('B vs A')



ax6 = plot.subplot2grid((4,4),(1,1))
ax6.scatter(list_b_float, list_b_float, 5, color='yellow', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax6.grid(True)
ax6.set_xticks(ticks_x)
ax6.set_yticks(ticks_x)
ax6.set_title('B vs B')


ax7 = plot.subplot2grid((4,4),(2,1))
ax7.scatter(list_b_float, list_c_float, 5, color='yellow', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax7.grid(True)
ax7.set_xticks(ticks_x)
ax7.set_yticks(ticks_x)
ax7.set_title('B vs C')


ax8 = plot.subplot2grid((4,4),(3,1))
ax8.scatter(list_b_float, list_d_float, 5, color='yellow', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax8.grid(True)
ax8.set_xticks(ticks_x)
ax8.set_yticks(ticks_x)
ax8.set_title('B vs D')


## C ## 
ax9 = plot.subplot2grid((4,4),(0,2))
ax9.scatter(list_c_float, list_a_float, 5, color='green', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax9.grid(True)
ax9.set_xticks(ticks_x)
ax9.set_yticks(ticks_x)
ax9.set_title('C vs A')


ax10 = plot.subplot2grid((4,4),(1,2))
ax10.scatter(list_c_float, list_b_float, 5, color='green', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax10.grid(True)
ax10.set_xticks(ticks_x)
ax10.set_yticks(ticks_x)
ax10.set_title('C vs B')


ax11 = plot.subplot2grid((4,4),(2,2))
ax11.scatter(list_c_float, list_c_float, 5, color='green', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax11.grid(True)
ax11.set_xticks(ticks_x)
ax11.set_yticks(ticks_x)
ax11.set_title('C vs C')


ax12 = plot.subplot2grid((4,4),(3,2))
ax12.scatter(list_c_float, list_d_float, 5, color='green', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax12.grid(True)
ax12.set_xticks(ticks_x)
ax12.set_yticks(ticks_x)
ax12.set_title('C vs D')


## D ## 
ax13 = plot.subplot2grid((4,4),(0,3))
ax13.scatter(list_d_float, list_a_float, 5, color='cyan', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax13.grid(True)
ax13.set_xticks(ticks_x)
ax13.set_yticks(ticks_x)
ax13.set_title('D vs A')


ax14 = plot.subplot2grid((4,4),(1,3))
ax14.scatter(list_d_float, list_b_float, 5, color='cyan', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax14.grid(True)
ax14.set_xticks(ticks_x)
ax14.set_yticks(ticks_x)
ax14.set_title('D vs B')


ax15 = plot.subplot2grid((4,4),(2,3))
ax15.scatter(list_d_float, list_c_float, 5, color='cyan', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax15.grid(True)
ax15.set_xticks(ticks_x)
ax15.set_yticks(ticks_x)
ax15.set_title('D vs C')

ax16 = plot.subplot2grid((4,4),(3,3))
ax16.scatter(list_d_float, list_d_float, 5, color='cyan', alpha= 0.5)
plot.setp(plot.xticks()[1], rotation = 40)
ax16.grid(True)
ax16.set_xticks(ticks_x)
ax16.set_yticks(ticks_x)
ax16.set_title('D vs D')



fig.suptitle('Problem 4', fontsize = 14)

plot.tight_layout()

plt.show()

fig.savefig('Problem_4.png')

genes_file.close