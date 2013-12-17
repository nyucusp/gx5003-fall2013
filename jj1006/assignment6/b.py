import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import random

finput = open('ML1Dataset/labeled_data.csv','r')
finput.readline()
zip = []
pop = []
inc = []
for line in finput:
	tokens = line.split(',')
	zip.append(float(tokens[0]))
	pop.append(float(tokens[1]))
	inc.append(float(tokens[2]))

fig = plt.figure()
graph = fig.add_subplot(111)
plt.plot(pop,inc,'kx')
graph.set_xlabel('population')
graph.set_ylabel('# incidents')

rmse = []
rmse10 = []

cv = 10 #fold cross-validation
chunksize = int(len(pop)/cv)
polymax = 5

for i in range(1,polymax+1):
	coeffs = np.polyfit(pop,inc,i)
	x2 = np.arange(min(pop)-0.1,max(inc)+0.1, .1)
	y2 = np.polyval(coeffs,x2)
	plt.plot(x2,y2,'r')
	graph.annotate(str(i), (x2[-1],y2[-1]), xytext=(30,0), textcoords = 'offset points', arrowprops=dict(facecolor='black', shrink=0.1))

	#compute global RMSE
	yp = np.polyval(coeffs,pop)
	rmse.append(sqrt(np.mean((np.array(inc)-np.array(yp))*(np.array(inc)-np.array(yp)))))
	print "RMSE for polynomial degree "+str(i)+"="+str(rmse[-1])
	print "R^2 for polynomial degree "+str(i)+"="+str(1-(rmse[-1]*rmse[-1])/np.var(inc))

	#compute 10-fold cross validation
	ri = range(0,len(pop))
	random.shuffle(ri)
	cv_rmse = []
	for j in range(0,cv):
		vpop = pop[(j*chunksize):((j+1)*chunksize)]
		tpop = pop[0:(j*chunksize)]
		tpop.extend(pop[((j+1)*chunksize):-1])
		vinc = inc[(j*chunksize):((j+1)*chunksize)]
		tinc = inc[0:(j*chunksize)]
		tinc.extend(inc[((j+1)*chunksize):-1])
		coeffs = np.polyfit(tpop,tinc,i)
		yp = np.polyval(coeffs,vpop)
		cv_rmse.append(sqrt(np.mean((np.array(vinc)-np.array(yp))*(np.array(vinc)-np.array(yp)))))
	rmse10.append(np.mean(cv_rmse))
	print "10-fold RMSE for polynomial degree "+str(i)+"="+str(rmse10[-1])

plt.show()
fig.savefig('b.png')

print "From here, it appears that polynomial degree 3 is the best model, as it has the lowest cross-validated RMSE score (see c for further details)"
