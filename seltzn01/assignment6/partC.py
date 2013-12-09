# Nathan Seltzer
# Homework 6
# partC.py

import numpy as np
import matplotlib.pyplot as plt

# example data

x = np.arange(1, 6, 1)

#Full Set RMSE computed using Stata -- see .do file
FullRMSE = [13531,13178,13031,13040,13048]
TenRMSE = [13618, 13194, 13205, 13323, 13973]


plt.errorbar(x, TenRMSE, yerr=115, fmt='o', c='b', drawstyle="steps")
plt.errorbar(x, FullRMSE, yerr=110, fmt='o', c='k')

plt.title("Full Dataset (black) vs. 10-Fold CV Set (blue)")
plt.ylabel("RMSE Value")
plt.xlabel("# Order Polynomial")

plt.show()