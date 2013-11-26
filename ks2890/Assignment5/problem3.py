import matplotlib.pyplot as plt
import numpy as np
import csv
import operator

# empty lists and the Counter for reading the file
pData = []
yData = []
tData = []
Counter = []
Number = 1

#opening the microprocessor data with csv
with open('microprocessors.dat', 'rb') as csvfile:
    processors = csv.reader(csvfile, delimiter = ',') # separating out the file by the comma
    processors.next() #skip the first line
    processors = sorted(processors, key = operator.itemgetter(1), reverse = False) # sort the results

    # reading through the file and appending items to the empty lists
    for row in processors:
		pData.append(row[0])
		yData.append(row[1])
		tData.append(row[2])
		Counter.append(Number)
		Number = Number + 1

# first chart showing year or release by Processor Name
plt.figure(figsize=(15,7))
chart1 = plt.subplot(1,2,1)
chart1.plot(yData, Counter, marker = 'o', color = 'b', linestyle = '--')
chart1.set_xlim(1960,2013)
chart1.set_ylim(0,14)
plt.yticks(Counter, pData, fontsize = 10)
chart1.set_title('Processor Year of Release',fontsize = 12)
chart1.set_xlabel('Realse Date (Year)', fontsize = 10)
chart1.set_ylabel('Processor Name', fontsize = 10)

# second cart showing log 10 of transistor by Processor Name
chart2 = plt.subplot(1,2,2)
chart2.plot(tData, Counter,marker = 'o', color = 'r',linestyle = '--')
chart2.set_ylim(0,14)
chart2.set_xscale('log', basex = 10)
chart2.set_title('Processor Transistor Numbers',fontsize = 12)
chart2.set_xlabel('Transistors (log 10)', fontsize = 10)
plt.setp(chart2.get_yticklabels(), visible=False)

plt.show()