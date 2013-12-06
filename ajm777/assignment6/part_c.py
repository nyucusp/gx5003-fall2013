#Aliya Merali
#Urban Informatics
#Assignment 6
#Part C - Compute the RMSE on the whole training set (all your data) and plot it against the 10-fold CV average (with std error-bars) as a function of model complexity (y-axis RMSE, x-axis order of polynomial). 

import csv
import numpy as np
from scipy import stats
import matplotlib.pylab as plt

#__Reading in file and formatting it into 3 formatted lists
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
zips = [float(val) for val in zips]
pop = [float(val) for val in pop]
num_inc = [float(val) for val in num_inc]

#__Define functions to determine RMSE, Rsquared, and run the fits
def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def R2(x, y, fit):#Should be done with TRAINX and TRAINY
    yhat = fit(x)        
    ybar = np.sum(y)/len(y) 
    ssreg = np.sum((yhat-ybar)**2)  
    sstot = np.sum((y - ybar)**2) 
    r2 = ssreg / sstot
    return r2

def fit_and_error_CV(trainx, trainy, valx, valy, max_degree, cross_val_iter, fit_results):
    i = 1
    while i <= max_degree: #Iterates through all polynomial fits from 1 - max deg.
        coeffs = np.polyfit(trainx, trainy, i) #does poly git to nth deg
        fit_eq = np.poly1d(coeffs) #Eqn from fit
        r2 = R2(trainx, trainy, fit_eq)
        predictions = fit_eq(valx) #Predictions using eqn and validation x
        targets = valy #validation y's
        rmse = RMSE(predictions, targets)
        #Result Dicts of form {degree: [k, RMSE, R2],[K,RMSE,R2]...., degree:...}
        if i not in fit_results:
            fit_results[i] = []
            fit_results[i].append([cross_val_iter + 1, r2, rmse])
        else:
            fit_results[i].append([cross_val_iter + 1, r2, rmse])
        i = i + 1

def fit_and_error_no_CV(all_x, all_y, max_degree, fit_results):
    i = 1
    while i <= max_degree: #Iterates through all polynomial fits from 1 - max deg.
        coeffs = np.polyfit(all_x, all_y, i) #does poly git to nth deg
        fit_eq = np.poly1d(coeffs) #Eqn from fit
        r2 = R2(all_x, all_y, fit_eq)
        predictions = fit_eq(all_x) #Predictions using eqn and all x
        targets = all_y #target is all y values
        rmse = RMSE(predictions, targets)
        #Result Dicts of form {degree: [k, RMSE, R2],[K,RMSE,R2]...., degree:...}
        if i not in fit_results:
            fit_results[i] = []
            fit_results[i].append(['N/A: All Data', r2, rmse])
        else:
            fit_results[i].append(['N/A: All Data', r2, rmse])
        i = i + 1

#__Call the above functions in the k-fold cross validation
def k_fold_cross_validation(X, Y, K, n, result_dict): 
#Where X is all X set, Y is all Y set, K is validation fold, n is max degree of polyfit
	for k in xrange(K):
		trainingx = [x for i, x in enumerate(X) if i % K != k] #Training set of X less 1/Kth
		validationx = [x for i, x in enumerate(X) if i % K == k] #validation set of 1/Kth of X
                trainingy = [y for i, y in enumerate(Y) if i % K != k] #Training set of Y less 1/Kth
		validationy = [y for i, y in enumerate(Y) if i % K == k] #validation set of 1/Kth of Y
                fit_and_error_CV(trainingx, trainingy, validationx, validationy, n, k, result_dict)

#Nicely Print the Results of Cross Validation
def print_results(fit_results):
    for key in fit_results: 
        value = fit_results[key]
        i = 0 
        print 'n = ' + str(key)
        while i < len(value):
            print 'For CV Iteration ' + str(value[i][0])+': R^2 = '+str(value[i][1])+', RMSE = '+str(value[i][2])
            i = i + 1

#Average R^2 and RMSE scores to plot & determine best polynomial fit
def avg_scores_plot_multi(fit_results_no_CV, fit_results_CV, predictor_variable, CV_order):
    n_array_no_CV = []
    r2_array_no_CV = []
    rmse_array_no_CV = []
    n_array_CV = []
    r2_array_CV = []
    rmse_array_CV = []

    for key in fit_results_no_CV:
        value = fit_results_no_CV[key]
        i = 0
        sum_r2 = 0
        sum_rmse = 0
        while i < len(value):
            sum_r2 = float(sum_r2) + value[i][1]
            sum_rmse = float(sum_rmse) + value[i][2]
            i = i + 1
        avg_r2 = sum_r2/len(value)
        avg_rmse = sum_rmse/len(value)
        n_array_no_CV.append(key)
        r2_array_no_CV.append(avg_r2)
        rmse_array_no_CV.append(avg_rmse)
        print 'For fit with All Data: For n = ' + str(key) + ': Average R^2 = ' + str(avg_r2) + ', Average RMSE = ' + str(avg_rmse)

    for key in fit_results_CV:
        value = fit_results_CV[key]
        i = 0
        sum_r2 = 0
        sum_rmse = 0
        while i < len(value):
            sum_r2 = float(sum_r2) + value[i][1]
            sum_rmse = float(sum_rmse) + value[i][2]
            i = i + 1
        avg_r2 = sum_r2/len(value)
        avg_rmse = sum_rmse/len(value)
        n_array_CV.append(key)
        r2_array_CV.append(avg_r2)
        rmse_array_CV.append(avg_rmse)
        print 'For fit with CV: For n = ' + str(key) + ': Average R^2 = ' + str(avg_r2) + ', Average RMSE = ' + str(avg_rmse)

    #Plot Average Values of each against one another
    f, ax = plt.subplots()
    y_error_CV=stats.sem(rmse_array_CV, axis=None, ddof=4)
    y_error_no_CV = stats.sem(rmse_array_no_CV, axis=None, ddof=4)
    ax.errorbar(n_array_CV, rmse_array_CV, yerr=y_error_CV, fmt='o', color='r', label='Fit with '+str(CV_order)+'-fold Cross Validation')
    ax.errorbar(n_array_no_CV, rmse_array_no_CV, yerr=y_error_no_CV, fmt='o', color='blue', label='Fit on All Data')
    ax.set_ylabel('Average RMSE Value')
    ax.xaxis.grid()
    ax.yaxis.grid()
    miny = min(rmse_array_no_CV)-500
    maxy = max(rmse_array_no_CV)+500
    plt.ylim([miny, maxy])
    plt.xlim([0, 6])
    plt.xlabel('Polynomial Fit Order')
    plt.title('Avg. RMSE in ' + str(CV_order)+ '-fold Cross Validation and Polynomial Fit with All Data of ' + str(predictor_variable) + ' vs No. 311 Incidents')
    plt.legend()
    plt.show()
        
#___Find Fit & Error for Whole Data Set
fit_results_pop_no_CV = {}
fit_and_error_no_CV(pop, num_inc, 5, fit_results_pop_no_CV)
#print_results(fit_results_pop_no_CV)

fit_results_zip_no_CV = {}
fit_and_error_no_CV(zips, num_inc, 5, fit_results_zip_no_CV)
#print_results(fit_results_zip_no_CV)

#__Fit and Find Error with Cross Validation
fit_results_pop_CV = {}
k_fold_cross_validation(pop, num_inc, 10, 5, fit_results_pop_CV)
#print_results(fit_results_pop_CV)

fit_results_zip_CV= {}
k_fold_cross_validation(zips, num_inc, 10, 5, fit_results_zip_CV)
#print_results(fit_results_zip_CV)


#____Plot against each other
avg_scores_plot_multi(fit_results_pop_no_CV, fit_results_pop_CV, 'Population', 10)
avg_scores_plot_multi(fit_results_zip_no_CV, fit_results_zip_CV, 'Zip-Code', 10)
