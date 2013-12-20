import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from math import log

myfile = open('microprocessors.dat','r')
header = myfile.readline()
sequence = []
data = []
count = 0
for line in myfile:
	temp_data = line.split(",")
	data.append([temp_data[0],int(temp_data[1]), float(temp_data[2])])
	count+=1
	sequence.append(count)

fig = plt.figure()
sortedYear=sorted(data,key=lambda tup:tup[1])
year_of_introduction = zip(*sortedYear)[1]
label_number = zip(*sortedYear)[0]
ax1 = fig.add_subplot(1,2,1)
ax1.plot(year_of_introduction, sequence,'.',ms=9, color='blue')
ax1.set_yticklabels(label_number)
ax1.set_xlabel('Year of Introduction', fontsize = 14)
plt.yticks(np.arange(1, 15, 1))
ax1.yaxis.grid()


ax2 = fig.add_subplot(1,2,2)
number_of_transistors=zip(*sortedYear)[2]
label_number=zip(*sortedYear)[0]
ax2.set_xlabel('Number of Trasistors(Log Base 10)', fontsize = 14)
ax2.plot(number_of_transistors, sequence, '.',ms=9, color='Red')
ax2.set_xscale('log')
ax2.set_yticklabels(label_number)
plt.yticks(np.arange(1, 15, 1))
ax2.yaxis.grid()

fig.tight_layout()
fig.autofmt_xdate()
plt.savefig('Problem3.png')
plt.show()
