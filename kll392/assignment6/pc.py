import numpy as np
import matplotlib.pyplot as plt
import csv
from pylab import *
from scipy import stats
from pb import *

fullSetRMSE = []
nOrders = [1, 2, 3, 4, 5]


# N = 1:

A = np.vstack([population, np.ones(len(population))]).T
w = np.linalg.lstsq(A, num_incidents)[0]
line = []
m = w[0]
b = w[1]
for entry in population:
    line.append(m*entry + b)

rmse1 = rmse(num_incidents, line)
fullSetRMSE.append(rmse1)


# N = 2:

p2 = np.poly1d(np.polyfit(population, num_incidents, 2))

yVals2 = []
for x in population:
    yVals2.append(p2(x))
rmse2 = rmse(num_incidents, yVals2)
fullSetRMSE.append(rmse2)


# N = 3:
p3 = np.poly1d(np.polyfit(population, num_incidents, 3))

yVals3 = []
for x in population:
    yVals3.append(p3(x))
rmse3 = rmse(num_incidents, yVals3)
fullSetRMSE.append(rmse3)


# N = 4:
p4 = np.poly1d(np.polyfit(population, num_incidents, 4))

yVals4 = []
for x in population:
    yVals4.append(p4(x))
rmse4 = rmse(num_incidents, yVals4)
fullSetRMSE.append(rmse4)


# N = 5:
p5 = np.poly1d(np.polyfit(population, num_incidents, 5))

yVals5 = []
for x in population:
    yVals5.append(p5(x))
rmse5 = rmse(num_incidents, yVals5)
fullSetRMSE.append(rmse5)

fig = plt.figure()

print stdErr
for i in range (0, 5):
    stdErr[i] = stdErr[i]/2

ax = fig.add_subplot(111)
ax.scatter(nOrders, cvRMSE, marker = "s", label = "10-fold Cross Validated RMSE")
ax.errorbar(nOrders, cvRMSE, yerr = stdErr)
ax.scatter(nOrders, fullSetRMSE, marker = "*", label = "Full Set RMSE")
ax.plot(nOrders, fullSetRMSE, 'k-')

ax.grid(True)
ax.legend()
fig.suptitle("RMSE and Model Complexity", fontsize=16)
ax.set_xlabel('Model Complexity', fontsize=14)
ax.set_ylabel('RMSE', fontsize=14)


plt.show()
