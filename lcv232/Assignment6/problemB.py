import matplotlib.pyplot as plt
import numpy as np

cfile = open('labeled_data.csv','r')
header = cfile.readline()

popl = []
zipc = []
incd = []

for line in cfile:
	cd_data = line.split(",")
	zipc.append(cd_data[0])
	popl.append(int(float(cd_data[1])))
	incd.append(int(float(cd_data[2])))
cfile.close()

def validation(x,y,coefficient):
	outp = {}
	c1 = np.poly1d(coefficient)
	cx1 = c1(x)
	cx2 = np.sum(y)/len(y)
	creg = np.sum((cx1-cx2)**2)
	ctotal = np.sum((y-cx2)**2)
	outp['R2'] = creg/ctotal    
	outp['RMSE'] = (np.sum((cx1-y)**2)/len(y))**0.5
	return outp

c_R2 = {}
c_RMSE = {}
c_deglist = []    
c_avgsqr = []      
c_avgRMSE = []
K = 10
for degree in range(1,6):
	c_deglist.append(degree)
	R2 = []
	RMSE = []
	for k in xrange(K):
		trainX = [x for i, x in enumerate(popl) if i % K !=k]
		validationX = [x for i, x in enumerate(popl) if i % K == k]
		trainY = [y for i, y in enumerate(incd) if i % K != k]
		validationY = [y for i, y in enumerate(incd) if i % K == k]
		coefficient = np.polyfit(trainX,trainY,degree)
		R2.append(validation(trainX,trainY,coefficient)["R2"])
		RMSE.append(validation(validationX,validationY,coefficient)["RMSE"])
	c_R2[degree] = R2
	c_RMSE[degree] = RMSE
	avg_square = sum(R2)/float(len(R2))
	avg_RMSE = sum(RMSE)/float(len(RMSE))
	c_avgsqr.append(avg_square)
	c_avgRMSE.append(avg_RMSE)

ax1
fig, (c1, c2) = plt.subplots(nrows=2)
fig.suptitle("Average R^2 and RMSE Scores in 10-fold Cross Validation", fontsize = 15, fontweight='bold')

c1 = fig.add_subplot(2,1,1)   # Plotting & nomenclature of the x & y axes of the data that is plotted
c2 = fig.add_subplot(2,1,2)

c1.plot(c_deglist, c_avgsqr,'.',ms=9, color='Blue', label = 'Average R^2')
c2.plot(c_deglist, c_avgRMSE, '.',ms=9, color='Red', label='Average RMSE')

c1.set_xlabel('Degree of Polynomial', fontsize = 15)
c1.set_ylabel('Average R^2 Scores', fontsize=15)

c2.set_xlabel('Degree of Polynomial', fontsize = 15)
c2.set_ylabel('Average RMSE', fontsize=15)

c1.grid(which = 'both', color = '0.85', linestyle = '-')
c1.legend(loc = 'upper left', prop={'size':10})

c2.grid(which = 'both', color = '0.85', linestyle = '-')
c2.legend(loc = 'upper left', prop={'size':10})

c2.set_xlim(0,6)
c2.set_ylim(12500,14000)
c1.set_xlim(0,6)

plt.savefig('problemB.png')
plt.show()


