import matplotlib.pyplot as plt
import math

finput = open('Hw1data/microprocessors.dat','r')
finput.readline()
name = []
year = []
transistors = []
for line in finput:
	tokens = line.split(',')
	name.append(tokens[0])
	year.append(int(tokens[1]))
	transistors.append(math.log(float(tokens[2])))

fig = plt.figure(figsize = (12,6))

graph = fig.add_subplot(121)
graph.plot(year, range(len(name)), 'bo')
plt.yticks(range(len(name)), name, size='small')
plt.ylim([-1, len(name)+1])
graph.spines['top'].set_color('none')
graph.spines['right'].set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')
graph.set_xlabel('Year')

graph = fig.add_subplot(122)
graph.plot(transistors, range(len(name)), 'ro')
plt.ylim([-1, len(name)+1])
graph.axes.get_yaxis().set_visible([])
graph.spines['top'].set_color('none')
graph.spines['right'].set_color('none')
graph.xaxis.set_ticks_position('bottom')
graph.yaxis.set_ticks_position('left')
graph.set_xlabel('log(# transistors)')

plt.show()

fig.savefig('p3.png')
