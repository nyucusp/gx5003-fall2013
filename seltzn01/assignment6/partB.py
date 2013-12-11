# Nathan Seltzer
# Homework 6
# partB.py

"""
Since we are now able to use any other "language" to solve
this assignment, I've decided to use Stata for some more
efficient data analysis. (see the accompanying .do file).

Essentially, I used a user-created command, "crossfold",
which I set to have 10-fold cross-validation for each
polynomial model. It generated the Root MSE and R-Squared
values for each K-1 group. I then exported the raw output
to excel where I summed each RMSE and R2. I did this for
both the full dataset "labeled_data.csv" and for my
updated dataset "updated_labeled_data.csv" which dropped
the 176 observations that had num_incident values close
to zero.

The following are inputed values reached from my analysis
on Stata (RMSE and R2), and code for creating charts
"""


import matplotlib.pyplot as plt
import numpy as np
from pylab import *


""" First, for the provided dataset (labeled_data.csv)

The first values "13000" and "0.0610" I arbitrarily set, so that the RMSE and R2 values
would be aligned 1 to 5 -- It will not be seen when I pan the graph for the final
.png image """

TenCVRMSE = [13000, 13618.372, 13194.3817, 13205.565, 13323.1562, 13973.0393]
TenCVR2 = [0.610, 0.61769558, 0.63104889, 0.64130723, 0.63648605, 0.62604344]

subplot(2,1,1)
grid(True)
plt.title("1st Through 5th Order Polynomial RMSE and R-Squared")
plt.ylabel("RMSE")
plot(TenCVRMSE, linewidth=0, marker = 'o', c = 'k')
xticks(range(1,6,1))


subplot(2,1,2)
grid(True)
plt.ylabel("R-Squared")
plt.xlabel("# Order Polynomial")
plot(TenCVR2, linewidth=0, marker = 'o', c = 'k')
xticks(range(1,6,1))


plt.show()

"""Second, my updated dataset with dropped observations
"updated_labeled_data.csv"

Again, the first observations are  somewhat arbitary, 
just so that the labeling would align.

"""

TenCVRMSE_2 = [11500, 11721.531, 12258.2266, 12142.9492, 12628.6216, 14003.8357]
TenCVR2_2 = [ 0.60, 0.78905593, 0.70407944, 0.72639624, 0.71503719, 0.64685166]

subplot(2,1,1)
grid(True)
plt.title("1st Through 5th Order Polynomial RMSE and R-Squared \n (updated dataset)")
plt.ylabel("RMSE")
plot(TenCVRMSE_2, linewidth=0, marker = 'o', c = 'k')
xticks(range(1,6,1))


subplot(2,1,2)
grid(True)
plt.ylabel("R-Squared")
plt.xlabel("# Order Polynomial")
plot(TenCVR2_2, linewidth=0, marker = 'o', c = 'k')
xticks(range(1,6,1))

plt.show()