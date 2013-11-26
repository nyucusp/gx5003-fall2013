import matplotlib.pyplot as plt
from pylab import *

# The ranking of genes with highest correlation to A are C, D, B (in descending order).

# read the genes data
genes = open('genes.dat','r')

# create empty lists to append the data
A = []
B = []
C = []
D = []
i = 1 # this will allow for iterating through the subplots
plots = []

genes.readline() # skip first row

for row in genes: #this will read the genes as floats.
	fields = row.strip().split(",") #make into fields
	A.append(float(fields[0]))
	B.append(float(fields[1]))
	C.append(float(fields[2]))
	D.append(float(fields[3]))

for x in range(16): # this is creating the subplots for the 4X4 matrix
	z = plt.subplot(4, 4, i)
	i = i +1
	plots.append(z)

xp = np.arange(0, 1, 0.05)

#it's time to start plotting the 4X4 matrix
plots[0].scatter(A, A, marker = '.', color = 'b')
plots[1].scatter(A, B, marker = '.', color = 'b')
plots[2].scatter(A, C, marker = '.', color = 'b')
plots[3].scatter(A, D, marker = '.', color = 'b')
plots[4].scatter(B, A, marker = '.', color = 'b')
line1 = np.poly1d(np.polyfit(B, A, 5))
plots[4].plot(xp, line1(xp), color ='r', linewidth = 1)

plots[5].scatter(B, B, marker = '.', color = 'b')
plots[6].scatter(B, C, marker = '.', color = 'b')
plots[7].scatter(B, D, marker = '.', color = 'b')
plots[8].scatter(C, A, marker = '.', color = 'b')
line2 = np.poly1d(np.polyfit(C, A, 1))
plots[8].plot(xp, line2(xp), color = 'r', linewidth = 1)

plots[9].scatter(C, B, marker = '.', color = 'b')
plots[10].scatter(C, C, marker = '.', color = 'b')
plots[11].scatter(C, D, marker = '.', color = 'b')
plots[12].scatter(D, A, marker = '.', color = 'b')
line3 = np.poly1d(np.polyfit(D, A, 3))
plots[12].plot(xp, line3(xp), color = 'r', linewidth = 1)

plots[13].scatter(D, B, marker = '.', color = 'b')
plots[14].scatter(D, C, marker = '.', color = 'b')
plots[15].scatter(D, D, marker = '.', color = 'b')

plots[0].set_ylabel('A', rotation = 'horizontal')
plots[4].set_ylabel('B', rotation = 'horizontal')
plots[8].set_ylabel('C', rotation = 'horizontal')
plots[12].set_ylabel('D', rotation = 'horizontal')
plots[12].set_xlabel('A')
plots[13].set_xlabel('B')
plots[14].set_xlabel('C')
plots[15].set_xlabel('D')


plt.suptitle('Gene Correlation Chart', size=16)

plt.show()
