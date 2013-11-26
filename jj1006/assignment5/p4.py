import numpy as np
import matplotlib.pyplot as plt

finput = open('Hw1data/genes.dat','r')
name = finput.readline()
name = name.split(',')
ngenes = len(name)+1
data = ngenes*[[] for _ in range(len(name))]
for line in finput:
	tokens = line.split(',')
	for i in range(len(name)):
		data[i].append(float(tokens[i]))

fig = plt.figure()
for i in range(len(name)):
	for j in range(len(name)):
		graph = fig.add_subplot(ngenes,ngenes,i*ngenes+j+1)
		plt.plot(data[i],data[j],'kx')
		graph.set_xlabel(name[i])
		graph.set_ylabel(name[j])
		plt.xticks([min(data[i]), max(data[i])])
		for tick in graph.xaxis.get_major_ticks():
			tick.label.set_fontsize(8)
		for tick in graph.yaxis.get_major_ticks():
                        tick.label.set_fontsize(8)
		
		#include best fit lines for C, D, and B
		if j==2 and i==0:
			coeffs = np.polyfit(data[i],data[j],1)
			print coeffs
			x2 = np.arange(min(data[i])-0.01,max(data[i])+0.01, .01)
			y2 = np.polyval(coeffs,x2)
			plt.plot(x2,y2,'r')
                if j==3 and i==0:
                        coeffs = np.polyfit(data[i],data[j],3)
                        print coeffs
                        x2 = np.arange(min(data[i])-0.01,max(data[i])+0.01, .01)
                        y2 = np.polyval(coeffs,x2)
                        plt.plot(x2,y2,'r')
                if j==1 and i==0:
                        coeffs = np.polyfit(data[i],data[j],5)
                        print coeffs
                        x2 = np.arange(min(data[i])-0.01,max(data[i])+0.01, .01)
                        y2 = np.polyval(coeffs,x2)
                        plt.plot(x2,y2,'r')

fig.tight_layout(pad=0.1)
fig.text(.1,0.1,'From here, we can see that C correlates best with A, followed by D then B')
plt.show()
fig.savefig('p4.png')
