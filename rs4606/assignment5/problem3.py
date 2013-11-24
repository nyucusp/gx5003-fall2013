"""
Note: annotations that answer the questions in the assignment are at the *bottom* of this
code.
"""

import sys
import numpy
import matplotlib.pyplot as plt
import datetime as DT
from matplotlib.dates import date2num, MonthLocator, DateFormatter


"""
First we open the text file and save the lines to the list input_lines
"""

inputfile = open('microprocessors.dat', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()



#make a list of years sorted from earliest to most recent
year_list = []
for i in range(1, len(input_lines)):
    year_list.append(int(input_lines[i].split(',')[1]))
sorted_year_list = sorted(year_list)


#make a list of processor names sorted in the same order as the corresponding year
processor_list = []
for i in range(0, 13):
    processor_list.append(i)

for elt in year_list:
    for j in range(1, len(input_lines)):
        if int(input_lines[j].split(',')[1]) == elt:
            processor_list[sorted_year_list.index(elt)] = input_lines[j].split(',')[0]

#make a list of log (base 10) of transistor quantities, sorted in the same order as the 
#corresponding year, rounded to two decimal places.
transistor_list = []
for i in range(0, 13):
    transistor_list.append(i)

for elt in year_list:
    for j in range(1, len(input_lines)):
        if int(input_lines[j].split(',')[1]) == elt:
            transistor_list[sorted_year_list.index(elt)] = round(numpy.log10(float(input_lines[j].split(',')[2])), 2)

#make a list of integers from 0 to 13, this will serve as the data graphed on the y-axis.
int_list = [i for i in range(0,13)]


"""
Now we make the two dot plots
"""
chart = plt.figure()
chart.patch.set_facecolor('white')



ax1 = plt.subplot(1, 2, 1)
ax1.plot(sorted_year_list, int_list, 'bo')
ax1.set_xlabel('Year of introduction')

ax1.axis([1965, 2010, -1, 16])

for i in int_list:
    if i < 6:
        ax1.text(sorted_year_list[i] + 1, i, processor_list[i], fontsize=11)
    elif i < 11:
        ax1.text(sorted_year_list[i] - len(processor_list[i])/2 - 5, i, processor_list[i], fontsize=11)
    else:
        ax1.text(sorted_year_list[i] - len(processor_list[i])/2 - 3, i, processor_list[i], fontsize=11)
    
ax2 = plt.subplot(1, 2, 2)
ax2.plot(transistor_list, int_list, 'bo')
ax2.set_xlabel('Number of transistors (log base 10)')

ax2.axis([3, 10, -1, 16])
for i in int_list:
    if i < 6:
        ax2.text(transistor_list[i] + .25, i, processor_list[i], fontsize=11)
    elif i < 11:
        ax2.text(transistor_list[i] - len(processor_list[i])/13 - 1, i, processor_list[i], fontsize=11)
    else:
        ax2.text(transistor_list[i] - len(processor_list[i])/10 - .8, i, processor_list[i], fontsize=11)
    

ax1.axes.get_yaxis().set_ticks([])
ax2.axes.get_yaxis().set_ticks([])

plt.margins(0.04)
chart.set_size_inches(16,8)
chart.suptitle('Microprocessors: Year of Introduction and Quantity of Transistors')
plt.show()

