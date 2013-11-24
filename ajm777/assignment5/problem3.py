#Aliya Merali
#Urban Informatics
#Assignment 5
#Problem 3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#Parsing data to get 3 lists with info
data = open('microprocessors.dat','r')
label = []
yr_intro = []
num_trans = []
for element in data:
    temp = element.split(',')
    label.append(temp[0])
    yr_intro.append(temp[1])
    num_trans.append(temp[2])
del label[0]
del yr_intro[0]
del num_trans[0]

#Create a list of numbers to plot against
label_num = []
i = 1
while i <= len(label):
    label_num.append(i)
    i = i + 1

fig, (ax0, ax1) = plt.subplots(ncols=2, sharey=True)
fig.suptitle('Microprocessor Properties', fontsize=18)
fig.subplots_adjust(bottom=0.125, top=0.9, left=0.025, right=0.965)
plt.setp(ax0.get_yticklabels(), visible=False)

ax0.scatter(yr_intro, label_num)
ax0.set_xlabel('Year of Introduction')
ax0.set_title('Year Introduced', fontsize=14)
ax0.grid(which = 'major', color = '0.75', linestyle = '-')
ax0.set_xlim(1965, 2035)
ax0.set_ylim(0,15)
plt.setp(ax0.get_xticklabels(), rotation=20)
for i, txt in enumerate(label):
    ax0.annotate(txt, (yr_intro[i],label_num[i]), xytext = (-5, 1),
        textcoords = 'offset points', ha = 'left', va = 'bottom', alpha = 1, rotation=5)


ax1.scatter(num_trans, label_num)
ax1.set_xscale('log')
ax1.set_xlabel('Log of Number of Transistors')
ax1.set_title('Number of Transistors', fontsize=14)
ax1.grid(which = 'major', color = '0.75', linestyle = '-')
ax1.set_xlim(10000, 100000000000)
for i, txt in enumerate(label):
    ax1.annotate(txt, (num_trans[i],label_num[i]), xytext = (-5, 1),
        textcoords = 'offset points', ha = 'left', va = 'bottom', alpha = 1, rotation=5)

plt.show()

