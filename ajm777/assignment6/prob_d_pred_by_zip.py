#Aliya Merali
#Urban Informatics
#Assignment 6
#Part D - for predictions based on zip code

import csv
import numpy as np
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
zips = [int(float(val)) for val in zips]
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

def fit_and_error(trainx, trainy, valx, valy, max_degree, cross_val_iter, fit_results):
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

#__Call the above functions in the k-fold cross validation
def k_fold_cross_validation(X, Y, K, n, result_dict): 
#Where X is all X set, Y is all Y set, K is validation fold, n is max degree of polyfit
	for k in xrange(K):
		trainingx = [x for i, x in enumerate(X) if i % K != k] #Training set of X less 1/Kth
		validationx = [x for i, x in enumerate(X) if i % K == k] #validation set of 1/Kth of X
                trainingy = [y for i, y in enumerate(Y) if i % K != k] #Training set of Y less 1/Kth
		validationy = [y for i, y in enumerate(Y) if i % K == k] #validation set of 1/Kth of Y
                fit_and_error(trainingx, trainingy, validationx, validationy, n, k, result_dict)

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
def avg_scores_plot(fit_results, predictor_variable):
    n_array = []
    r2_array = []
    rmse_array = []
    for key in fit_results:
        value = fit_results[key]
        i = 0
        sum_r2 = 0
        sum_rmse = 0
        while i < len(value):
            sum_r2 = float(sum_r2) + value[i][1]
            sum_rmse = float(sum_rmse) + value[i][2]
            i = i + 1
        avg_r2 = sum_r2/len(value)
        avg_rmse = sum_rmse/len(value)
        n_array.append(key)
        r2_array.append(avg_r2)
        rmse_array.append(avg_rmse)
        print 'For n = ' + str(key) + ': Average R^2 = ' + str(avg_r2) + ', Average RMSE = ' + str(avg_rmse)  
    print 'Minimum Average RMSE is '+str(min(rmse_array))
    #Plot Average Values to determine best fit
    f, ax = plt.subplots(2, sharex=True)
    ax[0].scatter(n_array, r2_array, color='r', label='Average R^2 Value')
    ax[0].set_ylabel('Average R^2 Value')
    ax[0].xaxis.grid()
    ax[0].yaxis.grid()
    ax[1].scatter(n_array, rmse_array, color='blue', label='Average RMSE Value')
    ax[1].set_ylabel('Average RMSE Value')
    ax[1].xaxis.grid()
    ax[1].yaxis.grid()
    plt.xlabel('Polynomial Fit Order')
    ax[0].set_title('Avg. R^2 & RMSE in ' + str(len(value))+ '-fold Cross Validation of ' + str(predictor_variable) + ' to No. 311 Incidents')
    plt.show()
        

#_____Run the functions with data above for population & zip code - this is what I used to determine the order of fit to use
fit_results_pop = {}
k_fold_cross_validation(pop, num_inc, 13, 12, fit_results_pop)
print_results(fit_results_pop)
avg_scores_plot(fit_results_pop, 'Population')

#fit_results_zip = {}
#k_fold_cross_validation(zips, num_inc, 13, 12, fit_results_zip)
#print_results(fit_results_zip)
#avg_scores_plot(fit_results_zip, 'Zip-Code')


#_______ADDING IN UNLABELED DATA
#__Reading in file and formatting it into 3 formatted lists
data_temp_2 = open('unlabeled_data.csv','r')
unlabeled_data = csv.DictReader(data_temp_2,['# zipcode','population'])
unlabeled_zips = []
unlabeled_pop = []

for item in unlabeled_data:
    unlabeled_zips.append(item['# zipcode'])
    unlabeled_pop.append(item['population'])
del unlabeled_zips[0]
del unlabeled_pop[0]
unlabeled_zips = [int(float(val)) for val in unlabeled_zips]
unlabeled_pop = [float(val) for val in unlabeled_pop]

def fit_plot_unlabeled_data(unlabeled_data_x, labeled_data_x, labeled_data_y, fit_order, data_type, other_data_list, other_data_name):
    output = open('predictions_by_zip.csv','wb')
    coeffs = np.polyfit(labeled_data_x, labeled_data_y, fit_order) #does poly git to nth deg on labeled data
    fit_eq = np.poly1d(coeffs) #Eqn from fit
    predicted_y = fit_eq(unlabeled_data_x)
    i = 0
    writer = csv.writer(output,delimiter=',')
    header = [str(data_type),str(other_data_name),'Predicted_Num_Inc']
    writer.writerow(header)
    while i < len(predicted_y):
        output_data = [unlabeled_data_x[i],other_data_list[i],predicted_y[i]]
        writer.writerow(output_data)
        print 'For '+str(data_type)+' of: '+str(unlabeled_data_x[i])+', Predicted Number of Incidents is: '+str(predicted_y[i])
        i = i + 1
    plt.scatter(unlabeled_data_x, predicted_y, color='blue', label='Predicted Number of Incidents')
    fit_line_x = np.arange(min(unlabeled_data_x), max(unlabeled_data_x), 1)
    plt.plot(fit_line_x, fit_eq(fit_line_x), color='red',linestyle='dashed',label=' Order '+str(fit_order)+' Polynomial Fit')
#____Use below line to plot actual data also!! 
    #plt.scatter(labeled_data_x, labeled_data_y, color='green', label='Actual Incident Report Data')
    plt.title('Predicted Number of 311 Incidents by '+str(data_type))
    plt.xlabel(str(data_type))
    plt.ylabel('Number of 311 Incidents')
    plt.grid()
    plt.xlim([min(unlabeled_data_x)-1500, max(unlabeled_data_x)+1500])
    plt.legend(loc='upper left')
    plt.show()

#Fit on the unlabeled data with chosen fit order
#fit_plot_unlabeled_data(unlabeled_pop, pop, num_inc, 3, 'Population', unlabeled_zips, 'Zip Code')
fit_plot_unlabeled_data(unlabeled_zips, zips, num_inc, 9, 'Zip Code', unlabeled_pop, 'Population')
