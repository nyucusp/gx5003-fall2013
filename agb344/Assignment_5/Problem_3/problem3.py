import matplotlib
import pylab
import math

microFile = open('microprocessors.dat','r')
microFile.readline()

processorDict = []
yearDict = {}
transistorDict = {}
for line in microFile:
    thisList = line.split(',')
    thisName = thisList[0]
    thisYear = int(thisList[1])
    thisTransistors = int(thisList[2])
    processorDict.append((thisName, thisYear, thisTransistors))

processorDict.sort(key = lambda tup: tup[1])



#print processorDict

processorNames = [pro[0] for pro in processorDict]
processorYears = [pro[1] for pro in processorDict]
processorTransistors = [pro[2] for pro in processorDict]

'''
processorNames = processorDict.keys()
processorYears = [v[0] for v in processorDict.values()]
processorTransistors = [v[1] for v in processorDict.values()]
'''


logTransistors = map(math.log, processorTransistors)   

fig, ax = matplotlib.pyplot.subplots(1,2, sharex = True)
ax[0].plot(logTransistors)
ax[1].plot(processorYears, marker = 'o', linewidth = 0)
matplotlib.pyplot.xticks(range(0, len(processorYears)), processorNames, rotation = 30, fontsize = 8)
matplotlib.pyplot.grid()
matplotlib.pyplot.show()

