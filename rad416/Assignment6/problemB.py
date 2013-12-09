import pandas as pd
from _collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.cross_validation import KFold
import numpy as np

def calc


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

train = np.array(labeledDataDF['population'])
target = np.array(labeledDataDF['incidents'])
kf = KFold(len(train), n_folds=10, shuffle=True)