#Nathan Seltzer
#Homework 5
#Problem4.py
"""Note: To see new chart, you have to x out of the previous chart's window """

#import the neccesary modules
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from pylab import *


f = open('genes.dat', 'r') #opens file with intention of reading, but hasn't read yet
f.readline() #bypass header line
#i create indexes for each gene, and then place them into lists using a for loop
a = []
b = []
c = []
d = []
for line in f:
	header = line.split(',')
	a.append(float(header[0]))
	b.append(float(header[1]))
	c.append(float(header[2]))
	d.append(float(header[3]))

#to check whether this worked, i printed it out
print "Gene A"
print a

"""
The 4x4 scatterplot matrix should be set up so that 
it looks like the following:

AA AB AC AD
BA BB BC BD
CA CB CC CD
DA DB DC DD


I'll set up the subplot so that it is has 4 rows and 4 columns,
notated by (4,4,X), with X denoting the particular order that the
subplots will be inserted. 
"""


plt.title("Scatter Plot Matrix")
subplot(4,4,1)
scatter(a,a)
title("Gene A") # I labeled only the head titles of the first row
ylabel("Gene A") # I labeled only the y-labels for the first column
subplot(4,4,2)
scatter(a,b)
title("Gene B")
subplot(4,4,3)
scatter(a,c)
title("Gene C")
subplot(4,4,4)
scatter(a,d)
title("Gene D")
subplot(4,4,5)
scatter(b,a)
ylabel("Gene B")
subplot(4,4,6)
scatter(b,b)
subplot(4,4,7)
scatter(b,c)
subplot(4,4,8)
scatter(b,d)
subplot(4,4,9)
scatter(c,a)
ylabel("Gene C")
subplot(4,4,10)
scatter(c,b)
subplot(4,4,11)
scatter(c,c)
subplot(4,4,12)
scatter(c,d)
subplot(4,4,13)
scatter(d,a)
ylabel("Gene D")
subplot(4,4,14)
scatter(d,b)
subplot(4,4,15)
scatter(d,c)
subplot(4,4,16)
scatter(d,d)

show()
"""
It should be noted that correlation matrices are symmetric and equal to
their transpose, so the upper right side of the diagonal is redundant.
The diagnoal is also meaningless, since any variable correlated with itself
will always be 1.0 .

Visually inspecting the scaterplot correlation matrix, the genes
# with the highest correlation with Gene A are:
# 	(1) Gene C 
# 	(2) Gene D
# 	(3) Gene B

# Moving on, I'll now create a new scatterplot of Gene A and Gene C with 
# a regression line.
# """
#add a grid for 
plt.figure()
grid(True)

# I use this fancy equation which sets up the data so that y = mx + b
(m,b)=polyfit(a,c,1)
print (b)
# this gives us the intercept, which is .025
print (m)
#this gives us the coefficient x, which is .947


#this actually creates the predicted values for the regression line
yp = polyval([m,b],a)

plot(a,yp, 'r') #red for contrast
scatter(a,c)
plt.title("Scatter Plot of Genes A and Gene C")
plt.ylabel("Gene A")
plt.xlabel("Gene C")
# polyfit(a, c, 1)

plt.show()

"""Next: A cubic best fit curve for Gene A and Gene D, the second most correlated Gene"""

plt.figure()
grid(True)

cubicCoefs = np.polyfit(a,d,3) #3 for cubic
xp = np.linspace(-0.1,1.1,1000, endpoint=True) #not too sure on the mechanics, but found this on scipy.org
# np.linspace(start point, stop point, I think this is how many points make up the line (i.e. the more
# included, the more accurate and "hi-def" the line will be), and endpoint=True makes sure the line stops) 
p = np.poly1d(cubicCoefs)
scatter(a,d)
plt.plot(xp, p(xp), 'r') #red for contrast
plt.title("Scatter Plot of Genes A and Gene D \n with cubic fitted line")
plt.ylabel("Gene A")
plt.xlabel("Gene D")
plt.show()


"""And Finally: A fifth degree best fit polynomial curve for Gene A and Gene B, the most uncorrelated Gene.

Unfortunately, this wouldn't work inside this file. It does work, however, in an auxiliary file
I created, called problem4_auxiliary.py.
But here is the code:


plt.figure()
grid(True)
coefs = polyfit(a, b, 5)
xp = np.linspace(0,1,1000)
p3 = poly1d(coefs)
print p3

plt.plot(xp, p3(xp), 'r')
scatter(a,b)
plt.title("Scatter Plot of Genes A and Gene B \n with fifth-degree polynomial fitted line")
plt.ylabel("Gene A")
plt.xlabel("Gene B")
show()



"""