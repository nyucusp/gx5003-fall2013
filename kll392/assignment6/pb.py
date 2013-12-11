import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab
from scipy import stats

def rmse(pred, obsv):
    size = len(pred)
    total = 0
    for x in range (0, size):
        incErr = pred[x] - obsv[x]
        incErr = incErr**2
        total = total + incErr
    return float(np.sqrt(total/(size-1)))

def findMean(values):
    total = 0
    for row in values:
        total += row
    return total/(len(values)-1)

def rSquared(line, obsv):
    slope, intercept, r_value, p_value, std_err = stats.linregress(obsv, line)
    return r_value**2

def findErrors(n):
    num_folds = 10
    subset_size = len(num_incidents)/num_folds
    RMSE = []
    Rsquared = []
    for i in range(num_folds):
        testing_incidents = num_incidents[i*subset_size:][:subset_size]
        testing_population = population[i*subset_size:][:subset_size]
        training_incidents = num_incidents[:i*subset_size] + num_incidents[(i+1)*subset_size:]
        training_population = population[:i*subset_size] + population[(i+1)*subset_size:]
        pn = np.poly1d(np.polyfit(training_population, training_incidents, n))
        yVals = []
        for x in testing_population:
            yVals.append(pn(x))
        thisRMSE = rmse(testing_incidents, yVals)
        RMSE.append(thisRMSE)
        thisRsq = rSquared(testing_incidents, yVals)
        Rsquared.append(thisRsq)
#    print "Order n = ", n
#    print "RMSE = ", findMean(RMSE)
#    print "R^2 = ", findMean(Rsquared)
    Rsq.append(findMean(Rsquared))
    stdErr.append(np.sqrt(np.var(RMSE)))
    return findMean(RMSE)


zipcode = []
population = []
num_incidents = []
with open("labeled_data.csv", 'r') as f:
    rows = csv.reader(f, delimiter = ',')
    rows.next()
    for row in rows:
        zipC = float(row[0])
        pop = float(row[1])
        num = float(row[2])
        zipcode.append(int(zipC))
        population.append(int(pop))
        num_incidents.append(int(num))

cvRMSE = []
stdErr = []
Rsq = []
orders = [1, 2, 3, 4, 5]

for i in range(1, 6):
    thisRMSE = findErrors(i)
    cvRMSE.append(thisRMSE)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.scatter(orders, cvRMSE, label = '10-fold Cross Validated RMSE')
ax1.legend(loc = 2)
plt.xlabel('Order Complexity')
plt.ylabel('RMSE')
ax2 = fig.add_subplot(212)
ax2.scatter(orders, Rsq, label = 'R^2')
ax2.legend(loc = 2)
plt.xlabel('Order Complexity')
plt.ylabel('R Squared')

fig.suptitle('RMSE and R^2 for 10-fold Cross Validated OLS', size = 14)

plt.show()

'''
The results of the 10-fold cross validated ols are shown below:

Order n =  1
RMSE =  15491.0430959
R^2 =  0.580097910838
Order n =  2
RMSE =  15089.5517115
R^2 =  0.608143936298
Order n =  3
RMSE =  14969.0856119
R^2 =  0.619930162454
Order n =  4
RMSE =  15178.4245866
R^2 =  0.615980366831
Order n =  5
RMSE =  15608.9741065
R^2 =  0.608348168643

Based on these results in conjunction with the figure produced for the varying orders, it is best to use a model with n = 3 in order to minimise the root mean squared error and maximize the r squared value.  

'''
