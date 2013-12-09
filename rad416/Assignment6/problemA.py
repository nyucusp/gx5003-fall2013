import pandas as pd
from _collections import defaultdict
import matplotlib.pyplot as plt

labeledDataFile = open('labeled_data.csv','r')
next(labeledDataFile) #dump header

labeledDataDict = defaultdict(list)
for line in labeledDataFile:
    line = line.rstrip()
    line = line.split(',')
    lineSplitList = []
    for el in line:
        lineSplitList.append( int(float(el)) )
    labeledDataDict[lineSplitList[0]] = [ lineSplitList[1],lineSplitList[2] ]
labeledDataFile.close()

labeledDataDF = pd.DataFrame.from_dict(labeledDataDict, orient='index')
labeledDataDF.columns = ['population','incidents']
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.scatter(labeledDataDF['population'],labeledDataDF['incidents'])
ax.set_xlabel('Population')
ax.set_ylabel('311 Incidents')
plt.savefig('QuestionA.png')

