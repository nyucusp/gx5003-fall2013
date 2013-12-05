import pylab
import csv
import sys
import scipy
import array
from matplotlib import *
from pylab import *
from scipy import *
import numpy as np
#import matplotlib.pyplot as plot
import matplotlib.ticker as mticker 
#from matplotlib import dates 
#import datetime 
from scipy import stats
#import dateutil.parser as dparser
from matplotlib import pyplot as plt
import collections 
import itertools
#from matplotlib.dates import date2num
import matplotlib as mpl 

from sklearn.metrics import mean_squared_error
from math import sqrt

#from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation

from sklearn.cross_validation import KFold
from sklearn.linear_model import LinearRegression

from random import shuffle


#unlabeled_file = open('unlabeled_data.csv', 'rU')
#unlabeled_line = csv.reader(unlabeled_file)

labeled_file = open('labeled_data.csv', 'rU')
labeled_lines = csv.reader(labeled_file)

#zip_n_file = open('zip_neigh.csv', 'rU')
#z_n_line = csv.reader(zip_n_file)


#list_unlabeled = [] 
list_labeled = [] 
list_z_n_line = [] 


#for x in unlabeled_line:
#	list_unlabeled.append(x)

for x in labeled_lines:
	list_labeled.append(x)

#for x in z_n_line:
#	list_z_n_line.append(x)

#list_unlabeled = list_unlabeled[1:]
list_labeled = list_labeled[1:]
#list_z_n_line = list_z_n_line[1:]

#list_u_zip = []
#list_u_pop = [] 




#for x in list_unlabeled:
#	list_u_zip.append(float(x[0]))
#	list_u_pop.append(float(x[1]))


#for x in list_labeled:
#	list_l_zip.append(float(x[0]))
#	list_l_pop.append(float(x[1]))
#	list_l_inc.append(float(x[2]))


#d_list = np.arange(0,100,1)




''' R ^ 2 '''

def polyfit(x, y, degree):
    results = {}

    coeffs = np.polyfit(x, y, degree)
     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()
    results['coeffs'] = coeffs

    # r-squared
    p = numpy.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = numpy.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = numpy.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = numpy.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot
    results['ssreg'] = ssreg
    results['sstot'] = sstot
    results['yhat'] = yhat
    return results



''' K FOLD CROSS '''

list_validation = [] 
list_training = [] 

def k_fold_cross_validation(items, k, randomize=False):
    if randomize:
        items = list(items)
        shuffle(items)

    slices = [items[i::k] for i in xrange(k)]

    for i in xrange(k):
        validation = slices[i]
        training = [item
                    for s in slices if s is not validation
                    for item in s]
        list_validation.append(validation)
        list_training.append(training)




## Zip 0
## Pop 1 
## Inc 2 

k_fold_cross_validation(list_labeled,10)

all_results = {} 
list_all_results = [] 
i = 0 
while i <= 9: 
### Trial 1 ### 
#    print 'TRIAL'
    list_training_pop = [] 
    list_training_inc = [] 
    for x in list_training[i]:
        list_training_pop.append(float(x[1]))
        list_training_inc.append(float(x[2]))

    list_validation_pop = [] 
    list_validation_inc = [] 
    for x in list_validation[i]:
        list_validation_pop.append(float(x[1]))
        list_validation_inc.append(float(x[2]))

    v = 1
    while v <=5:
        polyfit_result = polyfit(list_training_pop, list_training_inc, v)
#        print 'R^2'
#        print polyfit_result['coeffs']
#        print polyfit_result['ssreg']
#        print polyfit_result['sstot']
 #       print polyfit_result['determination']

##RMSE##
        list_validation_inc_predicted = [] 

        for x in list_validation_pop:
            p = np.poly1d(polyfit_result['coeffs'])
            list_validation_inc_predicted.append(p(x))
        rms = sqrt(mean_squared_error(list_validation_inc, list_validation_inc_predicted))
  #      print 'RMS'
   #     print rms 

        item = {}
        item[v] = [(i+1), polyfit_result['determination'], rms]
#        all_results.update({v : item[v]})
        list_all_results.append({v:item[v]})
        v = v + 1 

    i = i + 1 


#print all_results
#print list_all_results

o = 1 
while o <= 5: 
    all_results[o] = []
    for x in list_all_results:
        for key, value in x.iteritems():

            if key == o: 
                all_results[o].append(value)
    o = o + 1 

#print all_results

b = 1 

list_avg_r_square = [] 
list_avg_rsme = []

for key, value in all_results.iteritems():
    list_r_square = [] 
    list_rsme = []
    if key == b:
#        print value[1]
        for x in value: 
            list_r_square.append(x[1]) 
            list_rsme.append(x[2])
        avg_r_square = sum(list_r_square)/ len(list_r_square)
        avg_rsme = sum(list_rsme) / len(list_rsme)
        print("For Order %s, AVG R^2 is %s and AVG RSME is %s" %(b, avg_r_square, avg_rsme))
        list_avg_r_square.append(avg_r_square)
        list_avg_rsme.append(avg_rsme)
        b = b + 1 

print all_results
list_order = [1,2,3,4,5]

#print list_avg_r_square
#print list_avg_rsme


### Order vs RMSE 
plt.scatter(list_order, list_avg_rsme, 10, color='red', alpha= 0.5, label='AVG RSME')
#plt.scatter(list_order, list_rsme_avg, 10, color='blue', alpha= 0.5, label='RSME MODEL AVG')
#plt.errorbar(list_order, list_rsme_total, yerr=se_rsme_total, fmt='o', color='red', alpha= 0.5, label='STD ERROR = 217.24')
#plt.errorbar(list_order, list_rsme_avg, yerr=se_rsme_avg, fmt='o', color='blue', alpha= 0.5, label='STD ERROR = 188.87')

plt.legend(loc='upper center', prop={'size':10})
plt.xlabel("Order")
plt.ylabel("AVG RSME")
plt.title("Order vs. AVG RSME")
plt.tight_layout()
plt.grid()
plt.savefig('Problem B Order vs. AVG RSME.png')
plt.show()

### Order vs R ^ 2 

plt.scatter(list_order, list_avg_r_square, 10, color='red', alpha= 0.5, label='AVG R^2')
#plt.scatter(list_order, list_rsme_avg, 10, color='blue', alpha= 0.5, label='RSME MODEL AVG')
#plt.errorbar(list_order, list_rsme_total, yerr=se_rsme_total, fmt='o', color='red', alpha= 0.5, label='STD ERROR = 217.24')
#plt.errorbar(list_order, list_rsme_avg, yerr=se_rsme_avg, fmt='o', color='blue', alpha= 0.5, label='STD ERROR = 188.87')

plt.legend(loc='upper center', prop={'size':10})
plt.xlabel("Order")
plt.ylabel("AVG R^2")
plt.title("Order vs. AVG R^2")
plt.tight_layout()
plt.grid()
plt.savefig('Problem B Order vs. AVG R^2.png')
plt.show()

#zip_n_file.close
#unlabeled_file.close
labeled_file.close 
