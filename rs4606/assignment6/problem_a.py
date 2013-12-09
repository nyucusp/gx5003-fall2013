import sys
import numpy
import matplotlib.pyplot as plt
import datetime as DT
from matplotlib.dates import date2num, MonthLocator, DateFormatter


"""
First we open the text file and save the lines to the list input_lines
"""

inputfile = open('labeled_data.csv', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()

pop_list = []
for i in range(1,len(input_lines)):
    pop_list.append(float(input_lines[i].split(',')[1]))

inc_list = []
for i in range(1, len(input_lines)):
    inc_list.append(float(input_lines[i].split(',')[2]))


"""
Simple scatterplot of population vs. number of incidents
"""
"""
chart = plt.figure()

ax = plt.subplot(1, 1, 1)
ax.scatter(pop_list, inc_list, color='blue',s=5,edgecolor='none')

plt.xlabel('Population')
plt.ylabel('Number of incidents')
plt.title('All Labeled Data: Population vs. Number of Incidents for NY Zip Codes')
plt.show()
"""

"""
Now let's only consider the entries with, say, more than 50 incidents
"""

pop_inc_dict = {}
for i in range(0, len(pop_list)):
    pop_inc_dict[pop_list[i]] = inc_list[i]

pop_list_2 = []
inc_list_2 = []
for key in pop_inc_dict:
    if pop_inc_dict[key] > 50:
        pop_list_2.append(key)
        inc_list_2.append(pop_inc_dict[key])

chart = plt.figure()

ax = plt.subplot(1, 1, 1)
ax.scatter(pop_list_2, inc_list_2, color='blue',s=5,edgecolor='none')
plt.xlabel('Population')
plt.ylabel('Number of incidents')
plt.title('Population vs. Incidents for Zip Codes with more than 50 incidents')
plt.show()

