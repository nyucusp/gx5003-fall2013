import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import stats

cfile = open('labeled_data.csv','r')
header = cfile.readline()

zipc = []
popl = []
incd = []

for line in cfile:
	cd_data = line.split(",")
	zipc.append(cd_data[0])
	popl.append(int(float(cd_data[1])))
	incd.append(int(float(cd_data[2])))
cfile.close()

def validation(x,y,coefficient):
	outp = {}
	c = np.poly1d(coefficient)
	cx1 = c(x)
	cx2 = np.sum(y)/len(y)
	creg = np.sum((cx1-cx2)**2)
	ctotal = np.sum((y-cx2)**2)
	outp['R2'] = cre/ctotal
	outp['RMSE'] = (np.sum((cx1-y)**2)/len(y))**0.5
	return outp

c_R2 = {}
c_RMSE = {}
c_deglist = []
c_avgsqr = []
c_avgRMSE = []
c_RMSEall = []
c_RMSEavg = []
RMSE_ev = []
K = 10
for degree in range(1,6):
	c_deglist.append(degree)
	R2 = []
	RMSE = []
	for k in xrange(K):
		cx_1 = [x for i, x in enumerate(popl) if i % K !=k]
		valX = [x for i, x in enumerate(popl) if i % K == k]
		cx_2 = [y for i, y in enumerate(incd) if i % K != k]
		valY = [y for i, y in enumerate(incd) if i % K == k]
		coefficient = np.polyfit(cx_1,cx_2,degree)
		R2.append(validation(cx_1,cx_2,coefficient)["R2"])
		RMSE.append(validation(valX,valY,coefficient)["RMSE"])
	c_R2[degree] = R2
	c_RMSE[degree]=RMSE
	avg_square = sum(R2)/float(len(R2))
	avg_RMSE = sum(RMSE)/float(len(RMSE))
	
	c_avgsqr.append(avg_square)
	c_avgRMSE.append(avg_RMSE)    

	coefficient_all = np.polyfit(popl,incd,degree)
	RMSE_ev.append(validation(popl,incd,coefficient_all)["RMSE"])
	
	c_RMSEavg = scipy.stats.sem(c_avgRMSE, axis=None, ddof=4)
	c_RMSEall = scipy.stats.sem(RMSE_ev, axis=None, ddof=4)


fig, ax = plt.subplots()
graph = fig.add_subplot(1,1,1)

plt.errorbar(c_deglist,RMSE_ev,yerr=c_RMSEall, fmt = 'o', label = 'All Sets',color='blue')
plt.errorbar(c_deglist,c_avgRMSE,yerr=c_RMSEavg, fmt = 'o', label = '10-fold', color='red')

plt.scatter(c_deglist,RMSE_ev, 10,color='blue')
plt.scatter(c_deglist,c_avgRMSE, 10, color='red')

plt.title("RMSE all Vs RMSE of 10-fold", fontsize = 15)
plt.xlabel("Degree of Polynomial", fontsize = 14)
plt.ylabel("RMSE", fontsize = 14)
ax.set_xlim(0,6)

plt.legend(loc = 'upper center', prop={'size':12})
plt.grid(which = 'both', color = '0.85', linestyle = '-')

plt.savefig('problemC.png')
plt.show()
