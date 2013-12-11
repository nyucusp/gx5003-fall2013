import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#begining is the same as problemb.py but adding in the standard deviation
#and the RMSE on the whole training set

#import the data
data = open('labeled_data.csv', 'r')

#read through the data and put all the lines into a list
lines = []
for line in data:
	lines.append(line)

#predictor variable - population - read it into a list
pop =[]
for i in range(1,len(lines)):
	pop.append(float(lines[i].split(',')[1]))
#print pop

#target variable - incidents - read it into a list
inc=[]
for i in range(1,len(lines)):
	inc.append(float(lines[i].split(',')[2]))
#print inc

# cross validation for the mosdel
cv = sklearn.cross_validation.KFold(len(inc), n_folds=10, indices=False, shuffle=True)
poparray=np.array(pop)
incarray=np.array(inc)

# make lists for the RMSE, R Squared and Standard deviation
RMSEval = []
R2val = []
RMSEstd = []

#loop through the different models of the polynomial complexities from 1-5
#list of the RMSE and R squared for each fold of the model and polynomial value 
for i in range(1,6):
	RMSElist=[]
	R2list=[]
	for train,test in cv:
		#fits a polynomial to the training data, of order i
		trainpoly=np.polyfit(poparray[train], incarray[train],i)
		#uses the testing data to calculate the prediced values
		testy = np.polyval(trainpoly, poparray[test])
		#calculates the RMSE and adds these values to the list
		RMSE = sqrt(mean_squared_error(incarray[test], testy))
		RMSElist.append(RMSE)
		#clculate the R squared we need the average of the y values
		#and the Sum of Squares
		yavg=sum(incarray[test])/len(incarray[test])
		yavglist = []
		for j in range(0,len(incarray[test])):
			yavglist.append(yavg)
		SSreg = sum((testy-incarray[test])**2)
		SStot = sum((incarray[test] - yavglist)**2)
		R2list.append(1-(SSreg/SStot))
	#averages the RMSE's of each fold to get one RMSE for polynomial of order i
	RMSEval.append(sum(RMSElist)/len(RMSElist))
	R2val.append(sum(R2list)/len(R2list))
	#calculates the standard deviation
	stdev = np.std(RMSElist)
	RMSEstd.append(stdev)

#print "RMSE", RMSElist
print "RMSEval", RMSEval
print "RMSEstd", RMSEstd
print "R2val", R2val

#Based on these values we want the RMSE(error) to be the lowest and the
#R squared(level of prescision) to be closest to 1.  Each lists has 5 numbers
#which correspond to 1-5 order of polynomials that were used.  The third
#number has the lowest RMSE and highest R aquared value so we will use 
#the third order polynomial

RMSEall=[]
for i in range(1,6):
	trainpoly=np.polyfit(poparray,incarray, i)
	testy=np.polyval(trainpoly, poparray)
	RMSE = sqrt(mean_squared_error(incarray, testy))
	RMSEall.append(RMSE)
print "RMSEall", RMSEall

ind = np.arange(5)
width = .5
p1 = plt.bar(ind, RMSEval, width, color='b', yerr=RMSEstd, ecolor ='r')
p2 = plt.bar(ind, RMSEall, width, color='y')
plt.xlabel('Degree of Polynomial')
plt.ylabel('RMSE values')
plt.title('10 fold cross validated RMSE for 311 data of incidents by population size')
plt.xticks(ind+width/2., ('1','2','3','4','5'))
#plt.ylim([10000,16000])
plt.legend((p1,p2),('RMSE without cv','RMSE with cv'), loc=4)
plt.show()