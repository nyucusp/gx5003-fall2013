import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats

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
RMSE_se_all = []
RMSE_se_avg = []
RMSE_all = []
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

	coefficient_all = np.polyfit(population,incidents,degree)
	RMSE_all.append(validation(population,incidents,coefficient_all)["RMSE"])
	
	RMSE_se_avg = scipy.stats.sem(average_RMSE, axis=None, ddof=4)
	RMSE_se_all = scipy.stats.sem(RMSE_all, axis=None, ddof=4)


fig, ax = plt.subplots()
graph = fig.add_subplot(1,1,1)
plt.errorbar(degree_list,RMSE_all,yerr=RMSE_se_all, fmt = 'o', label = 'All Training Sets',color='blue')
plt.errorbar(degree_list,average_RMSE,yerr=RMSE_se_avg, fmt = 'o', label = '10-fold', color='red')
plt.scatter(degree_list,RMSE_all, 10,color='blue')
plt.scatter(degree_list,average_RMSE, 10, color='red')
plt.xlabel("Degree of Polynomial", fontsize = 14)
plt.title("RMSE of the Whole Training Set V.S. RMSE of 10-fold", fontsize = 15)
plt.ylabel("RMSE", fontsize=14)
ax.set_xlim(0,6)

plt.grid(which = 'both', color = '0.85', linestyle = '-')
plt.legend(loc = 'upper center', prop={'size':12})
plt.savefig('ProblemC.png')
plt.show()
