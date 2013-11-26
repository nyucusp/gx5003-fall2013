from datetime import  datetime
from matplotlib.dates import date2num
import calendar
import numpy
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import matplotlib.dates as mdates
from collections import Counter
from matplotlib import pyplot

f = open("actions-fall-2007.dat","r")
dates = []
f.next()
for row in f:
    a = row.split(' ')
    dates.append(a[0])

deadline=["2007-09-18 12:00:00","2007-10-04 12:00:00","2007-10-25 12:00:00","2007-11-27 12:00:00","2007-12-15 12:00:00","2007-12-11 12:00:00"]
list1 = []
for element in deadline:
    temp = datetime.strptime(element.strip(), '%Y-%m-%d %H:%M:%S')
    temp2 = date2num(temp)
    list1.append(temp2)

counts = Counter()
for sentence in dates:
    counts.update(word.strip('.,?!"\'').lower() for word in sentence.split())

dict={}
for value in counts:
    dict[value]=counts[value]


a = sorted(dict.items())

date = []
commit = []
for item in a:
    commit.append(item[1])
    a = datetime.strptime(item[0],"%Y-%m-%d")
    date.append(a)


fig = plt.figure()
fig.subplots_adjust(bottom=0.2)          # Remark 1
ax = fig.add_subplot(111)
plt.title('Scientific Visualization Assignment Actions in 2007')
plt.xlabel('Date')
plt.ylabel('Number of Commits')
ax.bar(date2num(date),commit)
ax.ticklabel_format(style='plain')       # Remark 2
ax.set_xticklabels(date[0:10], rotation=45)
ax.set_ylim(0,14000)

for deadline in list1:
    plt.vlines(deadline, 0, 14000, colors = 'r', linestyles = 'solid')
plt.vlines(list1[0], 0, 14000, colors = 'r', linestyles = 'solid', label = 'Assignment Due Date')
plt.legend(loc='upper left')

#plot
pyplot.savefig('problem2.png', dpi=200)
plt.show()


#Annotation

'I select the bins as the end of the each activity day. The commits made in the same \
day are summed up and reflect one number.\
\
In the middle of the term, students face with the hardest assignment.\
\
When deadlines are closer, the amount of work increases.\
'
