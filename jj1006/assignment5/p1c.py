import datetime as DT
from matplotlib import pyplot as plt

data = []
finput = open('Hw1data/stocks.dat','r')
header = finput.readline()

for line in finput:
	tokens = line.split(",")
	date = DT.datetime.strptime(tokens[0],"%Y-%m")
	apl = float(tokens[1])
	msf = float(tokens[2])
	data.append((date,apl,msf))


x = [date for (date, apl, msf) in data]
y = [apl for (date, apl, msf) in data]
z = [msf for (date, apl, msf) in data]
fig = plt.figure()

graph = fig.add_subplot(211)
graph.plot_date(x,y,'b-o',label='APPLE')
graph2 = fig.add_subplot(212)
graph2.plot_date(x,z,'r-o',label='MICROSOFT')
fig.autofmt_xdate()
graph.set_xlabel('Month')
graph.set_ylabel('Apple Stock Price')
graph2.set_ylabel('Microsoft Stock Price')

graph.spines['top'].set_color('none')
graph.spines['right'].set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')

graph2.spines['top'].set_color('none')
graph2.spines['right'].set_color('none')
graph2.xaxis.set_ticks_position('bottom')
graph2.yaxis.set_ticks_position('left')

fig.text(.01,.01,"In this case, it is better to use juxtaposition, since the scale of the Y axis would otherwise \nmake changes in Microsoft's stock price insignificant.")

plt.show()
fig.savefig('p1c.png')
