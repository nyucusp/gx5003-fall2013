import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from operator import itemgetter
import numpy as np
from matplotlib import pyplot

data = open('microprocessors.dat','r')

arr_name = []   # Declaring the arrays required to capture data from the file & use it for plotting.
arr_year = []
arr_transistors = []
data.next()
dict1= {}
dict2= {}
for val1 in data:
    temp = val1.strip('\n').split(',')
    dict1[temp[0]] = int(temp[1])
    dict2[temp[0]] = int(temp[2])

for key,val2 in sorted(dict1.items(), key=itemgetter(1)): # Appending values in arrays defined for Year & Name; getting item values as key
    arr_year.append(val2)
    arr_name.append(key)
             
for val2 in sorted(dict2.values()):  # Appending values in arrays defined for Transistor data
    arr_transistors.append(val2)

legend = []  # Setting the legend values in the plot
for i in range(len(arr_name)):
    legend.append(i+1)

fig = plt.figure()

# Plotting values for the Year data
ax1 = fig.add_subplot(121)
ax1.plot(arr_year, legend, 'o')
ax1.yaxis.grid()
ax1.set_title('Processors by Year')
ax1.set_xlabel('Year')
plt.xlim([1960, 2010])
ax1.set_yticklabels(arr_name)
pyplot.yticks(np.arange(1, 15, 1))


# Plotting values for the Transistors data
ax2 = fig.add_subplot(122)
ax2.plot(arr_transistors, legend, 'o')
ax2.yaxis.grid()
ax2.set_xscale('log')
ax2.set_title('Transistors (Log)')
ax2.set_xlabel('number of transistors')
plt.yticks(legend)
pyplot.yticks(np.arange(1, 15, 1))


fig.tight_layout()
#plot
pyplot.savefig("Problem3.png")
plt.show()
