import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import cross_val_score, KFold
from sklearn.cross_validation import train_test_split

# Import data from labeled_data.csv
data = pd.read_table('labeled_data.csv', sep=',', index_col=0)
col1 = data['population']
col2 = data['num_incidents']

# plot data to check the relationship between col1 and col2 as the basic analysis on the data
#plt.scatter(x=col1, y=col2)

##################################################################################################
#########   Find the appropriate polynomial order for the model using cross-validation  ##########
#########   Compute the RMSE on the whole training set (all your data)                  ##########   
##################################################################################################

# Split matrice into random train and test subsets with 70:30 
xtrain, xtest, ytrain, ytest = train_test_split(col1, col2, test_size=0.3)

# Make the function for calculating Root Mean Square Error
def rmse(x, y, coefs):
    yfit = np.polyval(coefs, x)
    return np.sqrt(np.mean((y - yfit) ** 2))

# Suppress warnings from Polyfit
import warnings
warnings.filterwarnings('ignore', message='Polyfit*')

# Set the polynomial order for the model from 1st to 5th.
# To find the Y value associated with degree of 1,2,3,4, and 5 in the X-axis, I set the 'np.arange' as 6   
degrees = np.arange(6)
train_err = np.zeros(len(degrees))
validation_err = np.zeros(len(degrees))

for i, d in enumerate(degrees):
    p = np.polyfit(xtrain, ytrain, d)

    train_err[i] = rmse(xtrain, ytrain, p)
    validation_err[i] = rmse(xtest, ytest, p)

# Plot the result
fig, ax = plt.subplots()

# Define axis labels
ax.plot(degrees, validation_err, lw=2, label = 'cross-validation error')
ax.plot(degrees, train_err, lw=2, label = 'training error')
ax.legend(loc=0)
ax.set_xlabel('degree of fit')
ax.set_ylabel('rms error')


####################################################################################################
############# Plot data with polynomial order for the model using 10-fold cross-validation #########
####################################################################################################

# Select K as 10 for K-fold cross validation 
#kfolds = 10
#fig, axes = plt.subplots(1, kfolds, figsize=(14,6))
#for i, fold in enumerate(KFold(len(data), n_folds=kfolds, shuffle=True)):
#    training, validation = fold
#    y, x = data.values[training].T
#    axes[i].plot(y, x, 'ro')
#    y, x = data.values[validation].T
#    axes[i].plot(y, x, 'bo')

##########################################################################################################
############# Find the appropriate polynomial order for the model using 10-fold cross-validation #########
##########################################################################################################

import warnings
warnings.filterwarnings('ignore', message='Polyfit*')

# set the highest polynomial order as 6 with 10-fold cross validation because it gives result of 5th degree in the X axis in the result
k = 10
degrees = np.arange(6)
k_fold_err = np.empty(len(degrees))

for i, d in enumerate(degrees):
    
    error = np.empty(k)

    for j, fold in enumerate(KFold(len(data), n_folds=k)):

        training, validation = fold
        
        y_train, x_train = data.values[training].T
        y_test, x_test = data.values[validation].T
        
        p = np.polyfit(x_train, y_train, d)
        
        error[j] = rmse(x_test, y_test, p)

    k_fold_err[i] = error.mean()
        
# plot the result
fig, ax = plt.subplots()

ax.plot(degrees, k_fold_err, lw=2)
ax.set_xlabel('degree of fit')
ax.set_ylabel('average rms error')

plt.show()

