# Nathan Seltzer
# Homework 6
# assignment6b.py


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from pylab import *
from scipy import stats
import math
import random
from matplotlib.pyplot import *



f = open('labeled_data.csv', 'r') 
f.readline() 

zipcode = []
population = []
num_incidents = []
for line in f:
	header = line.split(',')
	zipcode.append(float(header[0]))
	population.append(float(header[1]))
	num_incidents.append(float(header[2]))

Zip = zipcode
Pop = population
Ni = num_incidents



"""some stuff i tried"""
# plt.figure()
# grid(True)

# cubicCoefs = np.polyfit(Pop,Ni, 2) #3 for cubic
# xp = np.linspace(-1,120000.1,1000, endpoint=True) #not too sure on the mechanics, but found this on scipy.org
# # np.linspace(start point, stop point, I think this is how many points make up the line (i.e. the more
# # included, the more accurate and "hi-def" the line will be), and endpoint=True makes sure the line stops) 
# p = np.poly1d(cubicCoefs)
# scatter(Pop,Ni)
# plt.plot(xp, p(xp), 'r') #red for contrast
# plt.title("title")
# plt.ylabel(" ")
# plt.xlabel(" ")
# plt.show()

# a, b, c = polyfit(x, y, 2)
# # y_pred = polyval([a, b, c], x)  


# # MSE = np.sqrt( np.sum((y_pred-y)**2)/10 )
# print MSE

# gradient, intercept, r_value, p_value, std_err = stats.linregress(Pop,Ni)

# print "Gradient and intercept", gradient, intercept
# print "R-squared", r_value**2
# print "p-value", p_value


# err=sqrt(sum((xr-xn)**2)/n) #mean square error

"""The I figured out a better way to do it"""

plt.figure()

grid(True)

"""
The following codes generate the OLS regression equations for polynomial
# models from the 1st to 5th order
"""
# kbgyr

plt.title("1st through 5th Polynomial Regression Lines")
plt.ylabel("Number of Incidents (311 Calls)")
plt.xlabel("Population of Zipcode")
scatter(Pop,Ni, c = 'k', marker = '.')

coefs1 = polyfit(Pop, Ni, 1)
xp = np.linspace(-1,120000,1000)
p1 = poly1d(coefs1)
print "p1: ", p1
m1 = plt.plot(xp, p1(xp), 'k')

coefs2 = polyfit(Pop, Ni, 2)
xp = np.linspace(-1,120000,1000)
p2 = poly1d(coefs2)
print "p2: ", p2
m2 = plt.plot(xp, p2(xp), 'b')

coefs3 = polyfit(Pop, Ni, 3)
xp = np.linspace(-1,120000,1000)
p3 = poly1d(coefs3)
print "p3: ", p3
m3 = plt.plot(xp, p3(xp), 'g')

coefs4 = polyfit(Pop, Ni, 4)
xp = np.linspace(-1,120000,1000)
p4 = poly1d(coefs4)
print "p4: ", p4
m4 = plt.plot(xp, p4(xp), 'y')

coefs5 = polyfit(Pop, Ni, 5)
xp = np.linspace(-1,120000,1000)
p5 = poly1d(coefs5)
print "p5: ", p5
m5 = plt.plot(xp, p5(xp), 'r')

# plt.legend([m1,m2,m3,m4,m5],['Linear Model','2nd Order Model','3rd Order Model','4th Order Model','5th Order Model'])

m1 = Rectangle((0, 0), 1, 1, fc="k", alpha=.8)
m2 = Rectangle((0, 0), 1, 1, fc="b", alpha=.8)
m3 = Rectangle((0, 0), 1, 1, fc="g", alpha=.8)
m4 = Rectangle((0, 0), 1, 1, fc="y", alpha=.8)
m5 = Rectangle((0, 0), 1, 1, fc="r", alpha=.8)
legend([m1,m2, m3, m4, m5],['Linear Model','2nd Order Model','3rd Order Model','4th Order Model','5th Order Model'], loc = 2)




"""
The following code produces the Root Mean Square Error and
the Coefficient of Determination, R-Squared (R2) value.

"""

from numpy.linalg import lstsq

x = np.array(Pop)
y = np.array(Ni)
n = np.max(x.shape)    # the number of observations

X = np.vstack([np.ones(n), x]).T
a = np.linalg.lstsq(X, y)[0]
resids = y - np.dot(X,a)       # e = y - Xa; 
RSS = sum(resids**2)           # residual sum of squares
TSS = sum((y - np.mean(y))**2) # total sum of squares
R2 = 1 - RSS/TSS
 
std_error = np.sqrt(RSS/(n-len(a)))
std_y = np.sqrt(TSS/(n-1)) 
R2_adj = 1 - (std_error/std_y)**2

print"R2: ", R2
print "Root Mean Square Error: ", std_error

print "Y = 2130 + 0.6929x"
print "y = -681 +"






"""This was an alternate way of plotting  the polynomial regression lines"""

# m1 = plt.plot(Pop, Ni, '.', mec='none', alpha=.8)
# coefs = np.polyfit(Pop, Ni, 1)
# xp = np.linspace(-1, 120000, 1000)
# yp = np.polyval(coefs, xp)
# plt.plot(xp, yp, 'k')

# # #standard deviation
# sig = np.std(Ni - np.polyval(coefs, Pop))
# # print sig
# plt.fill_between(xp, yp - sig, yp + sig, 
#                  color='k', alpha=0.2)
# plt.xlabel("Population")
# plt.ylabel("Number of Incident Calls")
# print "standard error 1", sig

# m2 = plt.plot(Pop, Ni, '.', mec='none', alpha=.8)
# coefs = np.polyfit(Pop, Ni, 2)
# xp = np.linspace(-1, 120000, 1000)
# yp = np.polyval(coefs, xp)
# plt.plot(xp, yp, 'b')
# plt.tight_layout()
# sig = np.std(Ni - np.polyval(coefs, Pop))
# # print sig
# plt.fill_between(xp, yp - sig, yp + sig, 
#                  color='b', alpha=0.2)
# plt.xlabel("Population")
# plt.ylabel("Number of Incident Calls")
# print "standard error 2", sig

# m3 = plt.plot(Pop, Ni, '.', mec='none', alpha=.8)
# coefs = np.polyfit(Pop, Ni, 3)
# xp = np.linspace(-1, 120000, 1000)
# yp = np.polyval(coefs, xp)
# plt.plot(xp, yp, 'g')
# sig = np.std(Ni - np.polyval(coefs, Pop))
# # print sig
# plt.fill_between(xp, yp - sig, yp + sig, 
#                  color='y', alpha=0.2)
# plt.xlabel("Population")
# plt.ylabel("Number of Incident Calls")
# print "standard error 3", sig


# m4 = plt.plot(Pop, Ni, '.', mec='none', alpha=.8)
# coefs = np.polyfit(Pop, Ni, 4)
# xp = np.linspace(-1, 120000, 1000)
# yp = np.polyval(coefs, xp)
# plt.plot(xp, yp, 'y')
# sig = np.std(Ni - np.polyval(coefs, Pop))
# # print sig
# plt.fill_between(xp, yp - sig, yp + sig, 
#                  color='y', alpha=0.2)
# plt.xlabel("Population")
# plt.ylabel("Number of Incident Calls")
# print "standard error 4", sig


# m5 = plt.plot(Pop, Ni, '.', mec='none', alpha=.8)
# coefs = np.polyfit(Pop, Ni, 5)
# xp = np.linspace(-1, 120000, 1000)
# yp = np.polyval(coefs, xp)
# plt.plot(xp, yp, 'r')
# sig = np.std(Ni - np.polyval(coefs, Pop))
# # print sig
# plt.fill_between(xp, yp - sig, yp + sig, 
#                  color='r', alpha=0.2)
# plt.xlabel("Population")
# plt.ylabel("Number of Incident Calls")
# print "standard error 5", sig

# m1 = Rectangle((0, 0), 1, 1, fc="k", alpha=.8)
# m2 = Rectangle((0, 0), 1, 1, fc="b", alpha=.8)
# m3 = Rectangle((0, 0), 1, 1, fc="g", alpha=.8)
# m4 = Rectangle((0, 0), 1, 1, fc="y", alpha=.8)
# m5 = Rectangle((0, 0), 1, 1, fc="r", alpha=.8)
# legend([m1,m2], loc = 2)

# plt.legend([m1,m2,m3,m4,m5],['Linear Model','2nd Order Model','3rd Order Model','4th Order Model','5th Order Model'])






print "p1 - R-sqaured = .6991 RMSE = 12077"
print "p2 - R-sqaured = .7018 RMSE = 12073"
print "p3 - R-sqaured = .7051 RMSE = 12055"
print "p4 - R-sqaured = .7053 RMSE = 12102"
print "p5 - R-sqaured = .7053 RMSE = 12153"




# y_pred = polyval([coefs], xp) 
 
# # how good is the fit?
# # calculate MSE:
# MSE = NP.sqrt( NP.sum((y_pred-y)**2)/10 )
# # MSE = .2
# print "MSE = ", MSE


# MSE = np.sqrt( np.sum((y_pred-y)**2)/10 )
# print MSE
# plt.plot(xp, p3(xp), 'r')
# scatter(Pop,Ni)
# plt.title("Scatter Plot of Genes A and Gene B \n with fifth-degree polynomial fitted line")
# plt.ylabel("Gene A")
# plt.xlabel("Gene B")
show()


# subplot(2,2,2)

# samp_x = []
# samp_y = []
# for i in range(len(Pop)):
# 	samp_x.append(random.choice(Pop))
# 	samp_y.append(random.choice(Ni))
# print samp_x, samp_y

