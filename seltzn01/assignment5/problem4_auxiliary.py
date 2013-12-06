#Nathan Seltzer
#Homework 5
#Problem4_auxiliary.py


"""The following code for the fifth degree polynomial wouldn't work inside the previous
python document, "problem4.py". It worked when I would "#" out the previous code, but not when I left
everything in. This is it included: """

#import the neccesary modules
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

#the following import form pylab will allow me to use the subplot function
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


plt.figure()
grid(True)
coefs = polyfit(a, b, 5)
xp = np.linspace(0,1,1000)
p3 = poly1d(coefs)
print p3

plt.plot(xp, p3(xp), 'r') # red for sharp contrast
scatter(a,b)
plt.title("Scatter Plot of Genes A and Gene B \n with fifth-degree polynomial fitted line")
plt.ylabel("Gene A")
plt.xlabel("Gene B")
show()