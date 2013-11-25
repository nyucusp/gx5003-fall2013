import matplotlib.pyplot as plt
import math
from _collections import defaultdict

mpFile = open('microprocessors.dat','r')
next(mpFile) # dump header file

processorDict = defaultdict(list)
for line in mpFile:
    lineSplit = line.split(",")
    processorDict[lineSplit[0]] = [ lineSplit[1], lineSplit[2].rsplit() ]
mpFile.close()

rangeList = []
for i in range(1, len(processorDict) + 1):
    rangeList.append(i)

years = []
for k,v in processorDict.iteritems():
    years.append(v[0])

sorted_years = sorted(years)

transLog10 = []
for k,v in processorDict.iteritems():
    transLog10.append(math.log10(int(v[1][0])))

transLog10_sort = sorted(transLog10)

processorRankList = []
for k in sorted(processorDict.items(), key=lambda x: x[1]):
    processorRankList.append( k[0] )


fig = plt.figure(figsize = (25,10), )
ax1 = fig.add_subplot(1,2,1)
ax1.plot(sorted_years, rangeList, 'o')
ax1.grid(True,which='both')
plt.yticks(rangeList, processorRankList)
ax2 = fig.add_subplot(122)
ax2.plot(transLog10_sort, rangeList, 'o')
ax2.grid(True,which='both')
ax1.tick_params(axis='both', direction='out', labelsize=10)
ax2.tick_params(axis='both', direction='out', labelsize=10)
plt.yticks(rangeList, processorRankList)
plt.savefig('Problem_3.png')