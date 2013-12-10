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
graph.set_xlabel('Polynomial degree')
graph.set_ylabel('RMSE')

rmse = []
rmse10 = []
rmse10std = []

cv = 10 #fold cross-validation
chunksize = int(len(pop)/cv)
polymax = 5

for i in range(1,polymax+1):
	coeffs = np.polyfit(pop,inc,i)
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
	rmse10std.append(np.std(cv_rmse))
	print "10-fold RMSE for polynomial degree "+str(i)+"="+str(rmse10[-1])

x = range(1,polymax+1)
plt.plot(x,rmse)
graph.annotate("Global RMSE",(x[-1],rmse[-1]),xytext=(30,0), textcoords = 'offset points', arrowprops=dict(facecolor='black', shrink=0.1))
plt.errorbar(x,rmse10,rmse10std)
graph.annotate("10-fold RMSE",(x[-1],rmse10[-1]),xytext=(30,0), textcoords = 'offset points', arrowprops=dict(facecolor='black', shrink=0.1))

plt.xlim((0,6))

plt.show()
fig.savefig('c.png')

print "From here, we can see that there is considerable variability in the RMSE upon cross validation between the different sets. However, on average the cross validated score drops until polymonial degree 3, then increases subsequently. In addition, we can see that the global RMSE decreases rapidly until polynomial 3, but after that there is not much improvement." 
