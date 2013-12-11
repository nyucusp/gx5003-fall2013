import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import scipy as sp
import matplotlib.pylab as plt

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
zipc=[]
for i in range(1,len(lines)):
	zipc.append(float(lines[i].split(',')[0]))

# cross validation for the mosdel
cv = sklearn.cross_validation.KFold(len(inc), n_folds=10, indices=False, shuffle=True)
poparray=np.array(pop)
incarray=np.array(inc)
zipcarray=np.array(zipc)
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
#print "RMSEval", RMSEval
#print "R2val", R2val
zipRMSEval=[]
zipR2val =[]
#training for zipcode
for i in range(1,6):
	zipRMSElist=[]
	zipR2list=[]
	for train,test in cv:
		#fits a polynomial to the training data, of order i
		trainpoly=np.polyfit(zipcarray[train], incarray[train],i)
		#uses the testing data to calculate the prediced values
		testy = np.polyval(trainpoly, zipcarray[test])
		#calculates the RMSE and adds these values to the list
		RMSE = sqrt(mean_squared_error(incarray[test], testy))
		zipRMSElist.append(RMSE)
		#clculate the R squared we need the average of the y values
		#and the Sum of Squares
		yavg=sum(incarray[test])/len(incarray[test])
		yavglist = []
		for j in range(0,len(incarray[test])):
			yavglist.append(yavg)
		SSreg = sum((testy-incarray[test])**2)
		SStot = sum((incarray[test] - yavglist)**2)
		zipR2list.append(1-(SSreg/SStot))
	#averages the RMSE's of each fold to get one RMSE for polynomial of order i
	zipRMSEval.append(sum(zipRMSElist)/len(zipRMSElist))
	zipR2val.append(sum(zipR2list)/len(zipR2list))


#print "RMSE", RMSElist
print "zipRMSEval", zipRMSEval
print "zipR2val", zipR2val
#because the 5th order polynomial had the lowest RMSE and highest R squared value, I used those for my OLS model later on.

#Using this to predict what the number of incidents would
#be for a given zipcode and population
data = open('unlabeled_data.csv', 'r')

lines1 = []
for line in data:
	lines1.append(line)

pop1 =[]
for i in range(1,len(lines1)):
	pop1.append(float(lines1[i].split(',')[1]))

zipc1=[]
for i in range(1,len(lines1)):
	zipc1.append(float(lines1[i].split(',')[0]))

#plotting the predicted data (and the actual) based on the given polynomial order
def fitplot(unlabeledx, labeledx,labeledy,fit,data):
	coefficients = np.polyfit(labeledx,labeledy,fit)
	equation = np.poly1d(coefficients)
	predy= equation(unlabeledx)
	i=0
	while i<len(predy):
		print 'For ' +str(data)+' of: ' +str(unlabeledx[i])+', Predicted Number of Incidents are: '+str(predy[i])
		i=i+1
	plt.scatter(unlabeledx,predy,color='green', label='Predicted Number of Incidents')
	fitx=np.arange(min(unlabeledx),max(unlabeledx),1)
	plt.plot(fitx,equation(fitx), color='red', label='Order '+str(fit)+' Polynomial')
	#plt.xlim([0,120000])
	#plt.ylim([0,80000])
	plt.title('Predicted Number of Incidents based on ' +str(data))
	plt.scatter(labeledx,labeledy,color='blue',label='Actual Number of Incidents')
	plt.legend(loc='best')
	plt.xlabel(str(data))
	plt.ylabel('Number of Incidents')
	plt.show()

fitplot(pop1,pop,inc,3,'Population')
fitplot(zipc1,zipc,inc,5,'Zip Codes')
