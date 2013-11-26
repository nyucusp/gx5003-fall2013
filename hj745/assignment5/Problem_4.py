import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange,array,ones,linalg
from pylab import plot,show
import numpy as np
import statsmodels.formula.api as sm


#import data file and set the delimiter in the data file
data = pd.read_table('genes.dat', sep=',', usecols=[0, 1, 2,3])

#plot the scatter plot of 'genes.dat'. Each column shows with different color of dots respectively.
#I saved output as 'Problem_4_scatterplot.png'
data.plot(style=['o','o','o','o'],title='Problem_4')
plt.show()

#calculate the 4 X 4 matrix with pairwise correlation of data (A,B,C,D). It shows every possible correlation value between each column
#I screen-captured and saved as 'Problem_4_Corr.png'
corr = data.corr() 
print corr

#rank the respective correlation of 'B','C',and 'D' to that to 'A' in descending order to 'A'
#I screen-captured and saved as 'Problem_4_Corr_Desc.png'
corr_rank = corr.sort(['A', 'B', 'C', 'D'], ascending=False)
print corr_rank

#confirm each correlation of 'B','C',and 'D' to'A' in the descending order to 'A'
#I screen-captured and saved as 'Problem_4_Corr_rank.png'
corrAA = data['A'].corr(data['A'])
corrAB = data['A'].corr(data['B'])
corrAC = data['A'].corr(data['C'])
corrAD = data['A'].corr(data['D'])

corrACDB = [corrAA, corrAC, corrAD, corrAB]
print corrACDB


#####################################################################################################################################
## From this part, it begins drawing a linear best fit line in the plots of A with its most correlated gene, which is column 'C'   ##
#####################################################################################################################################

# define variables that are used in making regression model
col1 = data['A']
col2 = data['C']

# this line is to make the best fit regression model
model = pd.ols(x=col1,y=col2,intercept=True)

# print the output of the regression
# Statistics related to the output of regression modeling
# I screen-captured and saved as 'Problem_4_stats_summary_linear.png'
print model

# draw linear fit line by using 'np.polyfit' with 'degree = 1' that means linear
# I saved output as 'Problem_4_linear_fit_line.png'
m, b = np.polyfit(col1, col2, 1)
plt.plot(col2, col1, '.')
plt.plot(col2, m*col2 + b, '-')
plt.show()

###########################################################################################################################################
## From this part, it begins drawing a cubic best fit line in the plots of A with its most second most related gene, which is column 'D' ##
###########################################################################################################################################

# define variables that are used in making regression model
col1 = data['A']
col2 = data['D']

# this line is to make the best fit regression model
model = pd.ols(x=col1,y=col2,intercept=True)

# print the output of the regression
# Statistics related to the output of regression modeling
# I screen-captured and saved as 'Problem_4_stats_summary_curve.png'
print model

# draw curve fit line by using 'np.polyfit' with degree = 3 that means curve
# I saved output as 'Problem_4_linear_fit_curve.png'
m, b = np.polyfit(col1, col2, 1)
plt.plot(col2, col1, '.')
plt.plot(col2, m*col2 + b, '-')
plt.show()

###################################################################################################################################################
## From this part, it begins drawing a degree-5 polynomial best fit curve in the plots of A with its most uncorrelated gene, which is column 'B' ##
###################################################################################################################################################

# define variables that are used in making regression model
col1 = data['A']
col2 = data['B']

# this line is to make the best fit regression model
model = pd.ols(x=col1,y=col2,intercept=True)

# print the output of the regression
# Statistics related to the output of regression modeling
# I screen-captured and saved as 'Problem_4_stats_summary_poly.png'
print model

# draw poly fit line by using 'np.polyfit' with 'degree = 5' that means poly
# I saved output as 'Problem_4_poly_fit_line.png'
m, b = np.polyfit(col1, col2, 1)

plt.plot(col2, col1, '.')
plt.plot(col2, m*col2 + b, '-')
plt.show()
