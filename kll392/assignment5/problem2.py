import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd

data = []

with open('actions-fall-2007.dat', 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        data.append(row)

#dates = []
#times = []
datadict = {}
datalist = []

for row in data:
    entry = str(row)
    year = int(entry[2:6])
    month = int(entry[7:9])
    day = int(entry[10:12])
    hour = int(entry[13:15])
    minute = int(entry[16:18])
    second = int(entry[19:21])
    d = datetime.datetime(year, month, day, hour, minute, second)
#    date = d.date
#    datadict[date] = 0
    datalist.append(d)

    #print d

for line in datadict:
    print line

#df = pd.DataFrame(newdata)

#plt.figure()
#df.hist()

'''for x in range (8,13):
    for line in newdata:
        if (line.month == x):
            for x in range (0,32):
                if 
'''
