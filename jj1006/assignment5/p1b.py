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

graph = fig.add_subplot(111)
graph.plot_date(x,y,'b-o',label='APPLE')
graph.plot_date(x,z,'r-o',label='MICROSOFT')
graph.legend(loc="upper left")
fig.autofmt_xdate()
graph.set_xlabel('Month')
graph.set_ylabel('Stock Price')

graph.spines['top'].set_color('none')
graph.spines['right'].set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')

text = '''Apple alone appears to experience 
rapid growth (although Microsoft 
does too, see p1c)'''
graph.annotate(text, (x[17],y[17]), xytext=(30,-50), textcoords = 'offset points', arrowprops=dict(facecolor='black', shrink=0.1))
graph.annotate('Both companies are affected by recession', (x[7],30), xytext=(-15, 30), textcoords = 'offset points', arrowprops=dict(facecolor='black', shrink=0.1), verticalalignment='center', horizontalalignment='center')

plt.show()
fig.savefig('p1b.png')
