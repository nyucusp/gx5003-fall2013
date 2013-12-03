#Aliya Merali
#Urban Informatics
#Assignment 6
#Part B - Using the labeled dataset produce python codes that report 
#the 10-fold-Cross Validated RMSE and R^2 scores for OLS (num_incidents ~ f(population)) 
#with polynomial models from 1 to 5th order (e.g. for second order t ~ w_0 + w_1*x1 + w2*x^2) 
#and select a model complexity (polynomial order) based on these scores.


import csv
import numpy as np

data_temp = open('labeled_data.csv','r')
data = csv.DictReader(data_temp,['# zipcode','population','num_incidents'])
zips = []
pop = []
num_inc = []

for item in data:
    zips.append(item['# zipcode'])
    pop.append(item['population'])
    num_inc.append(item['num_incidents'])

del zips[0]
del pop[0]
del num_inc[0]
zips = [int(float(val)) for val in zips]
pop = [float(val) for val in pop]
num_inc = [float(val) for val in num_inc]


def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def R2(x, y, fit):#Should be done with TRAINX and TRAINY!!
    yhat = fit(x)        
    ybar = np.sum(y)/len(y) 
    ssreg = np.sum((yhat-ybar)**2)  
    sstot = np.sum((y - ybar)**2) 
    r2 = ssreg / sstot
    return r2

def fit_and_error(trainx, trainy, valx, valy, max_degree, cross_val_iter):
    i = 1
    while i <= max_degree: #Iterates through all polynomial fits from 1 - max deg.
        coeffs = np.polyfit(trainx, trainy, i) #does poly git to nth deg
        fit_eq = np.poly1d(coeffs) #Eqn from fit
        r2 = R2(trainx, trainy, fit_eq)
        predictions = fit_eq(valx) #Predictions using eqn and validation x
        targets = valy #validation y's
        rmse = RMSE(predictions, targets)
        results = cross_val_iter + 1, r2, rmse
        if i not in fit_results:
            fit_results[i] = []
            fit_results[i].append([results])
        else:
            fit_results[i].append([results])
        i = i + 1

def k_fold_cross_validation(X, Y, K, n): #Where X is all X set, Y is all Y set, K is validation fold, n is max degree of polyfit
	for k in xrange(K):
		trainingx = [x for i, x in enumerate(X) if i % K != k] #Creates Training set of X less 1/Kth
		validationx = [x for i, x in enumerate(X) if i % K == k] #Creates validation set of 1/Kth of X
		#print 'Training X  = ' + str(trainingx)
                #print 'Validation X = ' + str(validationx)
                trainingy = [y for i, y in enumerate(Y) if i % K != k] #Creates Training set of Y less 1/Kth
		validationy = [y for i, y in enumerate(Y) if i % K == k] #Creates validation set of 1/Kth of Y
		#print 'Training Y  = ' + str(trainingy)
                #print 'Validation Y = ' + str(validationy)
                fit_and_error(trainingx, trainingy, validationx, validationy, n, k)


fit_results = {}#of form {degree: [k, RMSE, R2],[K,RMSE,R2]...., degree:...}
k_fold_cross_validation(pop, num_inc, 10, 5)
print fit_results
"""
for key in fit_results:
    print 'n = ' + str(key)
    value = fit_results[key]
    print 'value for second iteration = ' + str(value[0])
"""
