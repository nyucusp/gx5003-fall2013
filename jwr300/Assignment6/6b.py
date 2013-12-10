#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 6, Exercise b

'''
Using the labeled dataset produce python codes that report the 
10-fold-Cross Validated RMSE and R^2 scores for 
OLS (num_incidents ~ f(population)) with polynomial models 
from 1 to 5th order (e.g. for second order t ~ w_0 + w_1*x1 + w2*x^2) 
and select a model complexity (polynomial order) based on these scores.
'''


from sklearn import cross_validation
import numpy as np

fit_results = {}

def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets)**2).mean())
    
def rsquared(x,y,fit):
    yhat = fit(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y-ybar)**2)
    r2 = ssreg / sstot
    return r2


def polynomial_fit(degree, fit_results, trainx, testx, trainy, testy):
    #loop through all polynomial degrees 
    
    for i in range (1,degree+1):
        
        coeffs = np.polyfit(trainx, trainy, i)
        fit_equation = np.poly1d(coeffs)
        print fit_equation
        r2 = rsquared(trainx, trainy, fit_equation)
        predictions = fit_equation(testx)
        targets = testy
        rmse = RMSE(predictions, targets)
    
        if i not in fit_results:
            fit_results[i] = []
            fit_results[i].append([r2,rmse])
        else:
            fit_results[i].append([r2,rmse])



def cross_fold_validation(X_train, Y_target,train, target, poly_degree, folds, fit_results):
    #10 fold cross validation 
    
    cv = cross_validation.KFold(len(train), n_folds=folds, indices=False, shuffle=True)
    
    for traincv, testcv in cv:
        polynomial_fit(poly_degree,fit_results,np.squeeze(X_train[traincv]),np.squeeze(X_train[testcv]),\
                       np.squeeze(Y_target[traincv]),np.squeeze(Y_target[testcv]))


def results(fit_results):
    
   for key in fit_results:
        value = fit_results[key]
        r2_avg = []
        rmse_avg = []
        for item in value:
            r2_avg.append(float(item[0]))
            rmse_avg.append(item[1])
        print "Polynomial Fit Order %s: R^2: %.2f, RMSE: %d" % (key,sum(r2_avg)/len(r2_avg),sum(rmse_avg)/len(rmse_avg))
    

def main(fit_results):


    labeled_data = []
    poly_degree = 5
    folds = 10
    
    
    with open('labeled_data.csv','r') as myFile:
        myFile.readline()
        for line in myFile:
            line = line.strip().split(",")
            labeled_data.append([float(x) for x in line])
    
    train = [i[1] for i in labeled_data] # population
    target = [j[2] for j in labeled_data] # num incidents
    
    X_train = np.array(train).reshape(len(train),1)
    Y_target = np.array(target).reshape(len(target),1)

    cross_fold_validation(X_train, Y_target, train, target, poly_degree, folds, fit_results)
    results(fit_results)

if __name__ == "__main__":
    main(fit_results)