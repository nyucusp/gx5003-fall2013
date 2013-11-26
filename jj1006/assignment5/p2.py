import datetime as DT
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from dateutil import rrule

data = []
finput = open('Hw1data/actions-fall-2007.dat','r')
header = finput.readline() #get rid of header

#input data
for line in finput:
	#example line: "2007-09-15 21:24:56"
	date = DT.datetime.strptime(line.rstrip(),"%Y-%m-%d %H:%M:%S")
	data.append(date)
data = sorted(data)

#reformat data into bins
min = data[0]
max = data[-1]
x = []
y = []
i = 0
for t in rrule.rrule(rrule.DAILY, dtstart=min, until=max):
	x.append(t)
	n = 0
	while (i<len(data)):
		if (data[i].date()==t.date()):
			n = n+1
			i = i+1
		else:
			break
	y.append(n)

#now plot
fig = plt.figure(figsize = (8,7))

graph = fig.add_axes((.1,.45,.8,.5))
graph.bar(x,y,color='k')
graph.xaxis_date()
fig.autofmt_xdate()
graph.set_xlabel('Day')
graph.set_ylabel('# assignments turned in')

graph.spines['top'].set_color('none')
graph.spines['right'].set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')

#add requested highlights
plt.axvline(mdates.date2num(DT.datetime.strptime('2007-09-18', '%Y-%m-%d')),color='r',ls='--',zorder=0)
plt.axvline(mdates.date2num(DT.datetime.strptime('2007-10-04', '%Y-%m-%d')),color='r',ls='--',zorder=0)
plt.axvline(mdates.date2num(DT.datetime.strptime('2007-10-25', '%Y-%m-%d')),color='r',ls='--',zorder=0)
plt.axvline(mdates.date2num(DT.datetime.strptime('2007-11-27', '%Y-%m-%d')),color='r',ls='--',zorder=0)
plt.axvline(mdates.date2num(DT.datetime.strptime('2007-12-15', '%Y-%m-%d')),color='r',ls='--',zorder=0)
plt.axvline(mdates.date2num(DT.datetime.strptime('2007-12-11', '%Y-%m-%d')),color='r',ls='--',zorder=0)

cap = '''
I chose to use days as the increment because they allow one to view
the entire time range of the data (unlike hours) while at the same 
time providing a level of detail one wouldn't get by using weeks or
months. For example, from this kind of plot one can tell that the 
assignment due on Oct 25 was likely the most work, as it resulted in
the most action at (or slightly after) the due date. In all cases,
there is a slow ramp up of action leading up to the due date, then a
spike the day of or the day after the due date, followed by a rapid 
decline in action.
'''
fig.text(.1,0.01,cap)

plt.show()
fig.savefig('p2.png')
