import datetime as DT
from matplotlib import pyplot as plt
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
fig = plt.figure()

graph = fig.add_subplot(111)
graph.bar(x,y)
graph.xaxis_date()
fig.autofmt_xdate()
graph.set_xlabel('Day')
graph.set_ylabel('# assignments turned in')

graph.spines['top'].set_color('none')
graph.spines['right'].set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')

#graph.annotate('45 degrees for visual emphasis', (x[17],y[17]), xytext=(30,-50), textcoords = 'offset points', arrowprops=dict(facecolor='black', shrink=0.1))
#graph.annotate('Axis labels formatted for readability', (x[-10],40), xytext=(0, 30), textcoords = 'offset points', arrowprops=dict(facecolor='black', shrink=0.1))

plt.show()
fig.savefig('p2.png')
