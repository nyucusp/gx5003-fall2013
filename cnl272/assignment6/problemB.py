import numpy as np
import matplotlib.pyplot as plt

myflie = open('labeled_data.csv','r')
header = myflie.readline()
zipcodes = []
population = []
incidents = []

for line in myflie:
	temp_data = line.split(",")
	zipcodes.append(temp_data[0])
	population.append(int(float(temp_data[1])))
	incidents.append(int(float(temp_data[2])))
myflie.close()

def validation(x,y,coefficient):
	outcome = {}
	n = np.poly1d(coefficient)
	yhat = n(x)
	ybar = np.sum(y)/len(y)
	ssreg = np.sum((yhat-ybar)**2)
	sstot = np.sum((y-ybar)**2)
	outcome['R2'] = ssreg/sstot
	outcome['RMSE'] = (np.sum((yhat-y)**2)/len(y))**0.5
	return outcome

dic_R2 = {}
dic_RMSE = {}
degree_list = []
average_square = []
average_RMSE = []
K = 10
for degree in range(1,6):
	degree_list.append(degree)
	R2 = []
	RMSE = []
	for k in xrange(K):
		trainX = [x for i, x in enumerate(population) if i % K !=k]
		validationX = [x for i, x in enumerate(population) if i % K == k]
		trainY = [y for i, y in enumerate(incidents) if i % K != k]
		validationY = [y for i, y in enumerate(incidents) if i % K == k]
		coefficient = np.polyfit(trainX,trainY,degree)
		R2.append(validation(trainX,trainY,coefficient)["R2"])
		RMSE.append(validation(validationX,validationY,coefficient)["RMSE"])
	dic_R2[degree] = R2
	dic_RMSE[degree]=RMSE
	avg_square = sum(R2)/float(len(R2))
	avg_RMSE = sum(RMSE)/float(len(RMSE))
	average_square.append(avg_square)
	average_RMSE.append(avg_RMSE)


fig, (ax1, ax2) = plt.subplots(nrows=2)
fig.suptitle("Average RMSE and R^2 Scores in 10-fold Cross Validation", fontsize = 15, fontweight='bold')
#label the axes of x and y, add the title for the both graphs
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(degree_list, average_square,'.',ms=9, color='Blue', label = 'Average R^2')
ax2.plot(degree_list, average_RMSE, '.',ms=9, color='Red', label='Average RMSE')
ax1.set_xlabel('Degree of Polynomial', fontsize = 14)
ax1.set_ylabel('Average R^2 Scores', fontsize=14)
ax2.set_xlabel('Degree of Polynomial', fontsize = 14)
ax2.set_ylabel('Average RMSE', fontsize=14)
ax1.legend(loc = 'upper left', prop={'size':9})
ax1.grid(which = 'both', color = '0.85', linestyle = '-')
ax2.legend(loc = 'upper left', prop={'size':9})
ax2.grid(which = 'both', color = '0.85', linestyle = '-')
ax2.set_xlim(0,6)
ax2.set_ylim(12500,14000)

ax1.set_xlim(0,6)

plt.show()


