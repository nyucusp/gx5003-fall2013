import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

actionsFile = open('actions-fall-2007.dat', 'r')
actionsFile.readline()
dateTimeList = []
for line in actionsFile:
    thisDateTime = time.strptime(line, "%Y-%m-%d %H:%M:%S\n")
    dateTimeList.append(thisDateTime)

hist, edges = np.histogram(dateTimeList, 4)

print hist, edges

plt.hist(dateTimeList)

fig = pyplot.figure()
ax = fig.add_subplot(111) 
fig.autofmt_xdate()
