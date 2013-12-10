import sys
import numpy
import matplotlib.pyplot as plt
import datetime as DT
from matplotlib.dates import date2num, MonthLocator, DateFormatter

inputfile = open('microprocessors.dat', 'r')# open file

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()


#years list
year_list = []
for i in range(1, len(input_lines)):
    year_list.append(int(input_lines[i].split(',')[1]))
sorted_year_list = sorted(year_list)
#list of microprocessors
micropro_lst = []
for i in range(0, 13):
    micropro_lst.append(i)

for elt in year_list:
    for j in range(1, len(input_lines)):
        if int(input_lines[j].split(',')[1]) == elt:
            micropro_lst[sorted_year_list.index(elt)] = input_lines[j].split(',')[0]

#list of transistors in logarithm 10 base scale
trans_lst = []
for i in range(0, 13):
    trans_lst.append(i)

for elt in year_list:
    for j in range(1, len(input_lines)):
        if int(input_lines[j].split(',')[1]) == elt:
            trans_lst[sorted_year_list.index(elt)] = round(numpy.log10(float(input_lines[j].split(',')[2])), 2)

#y axis to be 13 integer
int_list = [i for i in range(0,13)]

chart = plt.figure()
chart.patch.set_facecolor('yellow')

ax = plt.subplot(1, 2, 1) #x Plot
ax.plot(sorted_year_list, int_list, 'bo')
ax.set_xlabel('Year of Introduction') #X Title

ax.axis([1965, 2010, -1, 16])

for i in int_list:
    if i < 6:
        ax.text(sorted_year_list[i] + 1, i, micropro_lst[i], fontsize=12)
    elif i < 11:
        ax.text(sorted_year_list[i] - len(micropro_lst[i])/2 - 5, i, micropro_lst[i], fontsize=12)
    else:
        ax.text(sorted_year_list[i] - len(micropro_lst[i])/2 - 3, i, micropro_lst[i], fontsize=12)
    
ax1 = plt.subplot(1, 2, 2)#y plot
ax1.plot(trans_lst, int_list, 'bo')
ax1.set_xlabel('Number of Transistors (log base 10)') #Y Title

ax1.axis([3, 10, -1, 16])
for i in int_list:
    if i < 6:
        ax1.text(trans_lst[i] + .25, i, micropro_lst[i], fontsize=12)
    elif i < 11:
        ax1.text(trans_lst[i] - len(micropro_lst[i])/13 - 1, i, micropro_lst[i], fontsize=12)
    else:
        ax1.text(trans_lst[i] - len(micropro_lst[i])/10 - .8, i, micropro_lst[i], fontsize=12)
    
ax.axes.get_yaxis().set_ticks([])
ax1.axes.get_yaxis().set_ticks([])

plt.margins(0.04)
chart.set_size_inches(16,8)
chart.suptitle('Year of Introduction and Number of Transistors')
plt.show()