# Awais Malik
# Assignment 5
# Problem 3
# Annotations at the end of the code
# Open Plot in Full Screen Mode

import pandas as pd
import matplotlib.pyplot as plt

data_file = pd.read_csv('microprocessors.dat')
year_list = data_file[['Processor','Year of Introduction']]
year_index = year_list.set_index('Year of Introduction')
year_index = year_index.sort()

transistor_list = data_file[['Processor','Transistors']]
transistor_index = transistor_list.set_index('Transistors')
transistor_index = transistor_index.sort()

rank_list = []
for i in range(1,14):
    rank_list.append(i)
    
year_index['Rank'] = rank_list
transistor_index['Rank'] = rank_list

#print year_index
#print transistor_index

plt.figtext(0.5, 0.94, 'Microprocessors', fontsize = 'x-large', ha = 'center')

ax0 = plt.subplot(1, 2, 1)
ax0 = year_index['Rank'].plot(style='o')
#ax0.axes.get_yaxis().set_ticks([])
names=['','4004','8008','8080','8086','286','386TM','486TM DX','Pentium','Pentium II','Pentium III','Pentium 4','Xeon','Itanium','']
plt.yticks(range(len(names)), names, size='medium')

ax1 = plt.subplot(1, 2, 2)
ax1 = transistor_index['Rank'].plot(style='o', logx = True)
blanks = ['','','','','','','','','','','','','','','']
plt.yticks(range(len(blanks)), blanks, size='medium')
#ax1.axes.get_yaxis().set_ticks([])

plt.show()

""" Annotations:
This was tricky problem, as subplotting in matplotlib is very tedious.
The shortcut in pandas (subplots=True) only creates vertically juxtaposed
subplots. I created separate lists of the names of the processors and
one with blanks because matplotlib by default does not accept strings
as y values on a plot.
I feel that subplotting in MATLAB is much less annoying. """