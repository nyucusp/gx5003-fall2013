import datetime as DT
from matplotlib import pyplot as plt
from dateutil.relativedelta import relativedelta

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

fig = plt.figure()

graph = fig.add_subplot(111)
graph.plot_date(x,y,'b-o')
fig.autofmt_xdate()
graph.set_xlabel('Month')
graph.set_ylabel('Apple Stock Price')

graph.spines['top'].set_color('none')
graph.spines['right'].set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')
#graph.set_xlim((x[0]+relativedelta(months=-1),x[-1]+relativedelta(months=+1)))

plt.show()
