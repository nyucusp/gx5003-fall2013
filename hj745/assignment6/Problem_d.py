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
#### Plot fitted line in the original scatter plot with polynomial models of 5th order   #########
##################################################################################################

fig, axes = plt.subplots(1, 2, figsize=(14,6))

xvals = np.arange(col1.min(), col1.max())

# polynomial models with 1st order 
fit1 = np.polyfit(col1, col2, 1)
p1 = np.poly1d(fit1)
axes[0].plot(xvals, p1(xvals))
axes[0].scatter(x=col1, y=col2)

# polynomial models with 2nd order 
fit2 = np.polyfit(col1, col2, 5)
p2 = np.poly1d(fit2)
axes[1].plot(xvals, p2(xvals))
axes[1].scatter(x=col1, y=col2)

######################################################################################
###### Find R-Square value and coefficients for the model of degree of 5th order #####
######################################################################################

# Define function for finding R-Square in Polynomial Regression
def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)

    # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                      # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot
    return results
# Find R-Square value and coefficients for the model of degree of 5th order
print polyfit(x=col1,y=col2,degree=5) 

plt.show()

