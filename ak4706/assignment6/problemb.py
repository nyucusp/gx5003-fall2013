import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import scipy as sp

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

# make lists for the RMSE and R Squared
RMSEval = []
R2val = []

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


#print "RMSE", RMSElist
print "RMSEval", RMSEval
print "R2val", R2val

#Based on these values we want the RMSE(error) to be the lowest and the
#R squared(level of prescision) to be closest to 1.  Each lists has 5 numbers
#which correspond to 1-5 order of polynomials that were used.  The third
#number has the lowest RMSE and highest R aquared value so we will use 
#the third order polynomial.
#Keep in mind that since I shuffled the data each time to make it as acurate
#as possible the answers will come out slightly different each time