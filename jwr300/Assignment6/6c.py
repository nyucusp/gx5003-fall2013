#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 6, Exercise c

'''
Compute the RMSE on the whole training set (all your data)
and plot it against the 10-fold CV average (with standard 
error-bars) as a function of model complexity (y-axis RMSE,
 x-axis order of polynomial). What do you observe?
'''


from sklearn import cross_validation
import numpy as np
import pandas as pd
from scipy import *
import matplotlib.pyplot as plt
from matplotlib import *
import pylab
from pylab import *

os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin/latex'

clf()
params = {'axes.labelsize': 16,
          'text.fontsize': 14,
          'legend.fontsize': 16,
          'xtick.labelsize': 14,
          'ytick.labelsize': 16,
          'text.usetex': True}

pylab.rcParams.update(params)

fit_results = {}
fit_results_all = {}
rmse_dict = {}
rmse_all = {}
rmse_std = {}
rmse_std_all = {}

def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets)**2).mean())
    #return np.sqrt(mean_square_error.mean_square_error(targets,predictions))

def rsquared(x,y,fit):
    yhat = fit(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y-ybar)**2)
    r2 = ssreg / sstot
    return r2


def polynomial_fit(degree, fit_results, trainx, testx, trainy, testy):
    #loop for all polynomial degrees 
    
    for i in range (1,degree+1):
        
        coeffs = np.polyfit(trainx, trainy, i)
        fit_equation = np.poly1d(coeffs)
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

    
    cv = cross_validation.KFold(len(train), n_folds=folds, indices=False, shuffle=True)
    
    for traincv, testcv in cv:
        polynomial_fit(poly_degree,fit_results,np.squeeze(X_train[traincv]),np.squeeze(X_train[testcv]),\
                       np.squeeze(Y_target[traincv]),np.squeeze(Y_target[testcv]))


def results(fit_results, rmse, rmse_std):
    
   for key in fit_results:
        value = fit_results[key]
        r2_avg = []
        rmse_avg = []
        for item in value:
            r2_avg.append(float(item[0]))
            rmse_avg.append(item[1])
        print "Polynomial Fit Order %s: R^2: %.2f, RMSE: %d" % (key,sum(r2_avg)/len(r2_avg),sum(rmse_avg)/len(rmse_avg))
        rmse[key] = sum(rmse_avg)/len(rmse_avg)
        rmse_std[key] = np.std(rmse_avg)
        print np.std(rmse_avg)

def main(fit_results, fit_results_all):


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
    results(fit_results, rmse_dict, rmse_std)

    polynomial_fit(poly_degree,fit_results_all,np.squeeze(X_train),np.squeeze(X_train),np.squeeze(Y_target),np.squeeze(Y_target)) 
    results(fit_results_all, rmse_all, rmse_std_all)
    
    df = pd.DataFrame({'RMSE':rmse_all.values(),'RMSE w/ CV':rmse_dict.values()})
    df.plot(kind='bar', yerr = rmse_std.values())
    title('RMSE vs Model Complexity')
    xlabel('Model Complexity')
    ylabel('RMSE')
    plt.show()
    savefig('part_c.png',dpi=400)

if __name__ == "__main__":
    main(fit_results, fit_results_all)