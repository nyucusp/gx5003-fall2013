# !usr/bin/python

######################################################################
#																	
# Assignment 5 - Problem 4
# November 24th, 2013
#
# Michael Musick
#
#	Description: Generate a 4 x 4 matrix of subplots showing gene data
#				set correlations.  Then add regression curves
#				
#	Annotations: Most Correlated  - C
#				 Second most      - D
#				 Least Correlated - B
#	
#
######################################################################

# IMPORT NECCESSARY LIBRARIES
import matplotlib.pyplot as plt 
import numpy as np


# MAIN FUNCTION
def main():
	
	# get the dtat set labels
	dataLabels = ['A', 'B', 'C', 'D']

	# these are temp arrays to build the numpy arrays with
	a_ = []
	b_ = []
	c_ = []
	d_ = []

	# IMPORT THAT DATA
	data_fromFile = open('genes.dat', 'r')
	for line in data_fromFile:		
		tempLine = line.strip().split(',')
		if isfloat(tempLine[1]):
			a_.append(float(tempLine[0]))
			b_.append(float(tempLine[1]))
			c_.append(float(tempLine[2]))
			d_.append(float(tempLine[3]))
	# create an empty matrix
	dataMat = np.zeros([len(a_), 4])
	# move that data in
	dataMat[:,0] = np.array(a_)	
	dataMat[:,1] = np.array(b_)
	dataMat[:,2] = np.array(c_)
	dataMat[:,3] = np.array(d_)
	# find the min and max values for axis scale purposes
	dataMin = np.amin(dataMat)
	dataMax = np.amax(dataMat)
	
	# create a subplot matrix 
	fig, ax = plt.subplots(4,4, figsize=[10,10])

	# populate the subplots
	for col in range(4):
		for row in range(4):			
			ax[col][row].plot(dataMat[:, col], dataMat[:, row], 'k.' )
			ax[col][row].set_title( str(dataLabels[col]) + ' x ' + str(dataLabels[row])  )
			if col != 3:
				plt.setp( ax[col][row].get_xticklabels(), visible=False)
			if row != 0:
				plt.setp( ax[col][row].get_yticklabels(), visible=False)
			plt.setp( ax[col][row].xaxis.get_majorticklabels(), rotation=30)
			ax[col][row].set_xbound(dataMin-0.08, dataMax+0.08)
			ax[col][row].set_ybound(dataMin-0.08, dataMax+0.08)

	# draw linear fit for most correlated gene set 'A'
	# This is gene set 'C'	
	x = dataMat[:,0]
	aMin = np.amin(x)
	aMax = np.amax(x)
	aRange = aMax-aMin
	xRange = np.linspace(aMin, aMax, 100)
	y = dataMat[:,2]
	fit = np.polyfit( x, y, 1 )
	fit_fn = np.poly1d(fit) # fit_fn is now a function which takes in x and returns an estimate for y
	ax[0][2].plot(xRange, fit_fn(xRange), '-r')
	
	# draw cubic best fit for 'D'
	y = dataMat[:,3]
	fit = np.polyfit( x, y, 3 )
	fit_fn = np.poly1d(fit)
	ax[0][3].plot(xRange, fit_fn(xRange), '-r')
	
	# draw 5-degree polynomial for 'B'
	y = dataMat[:,1]
	fit = np.polyfit( x, y, 5 )
	fit_fn = np.poly1d(fit)
	ax[0][1].plot(xRange, fit_fn(xRange), '-r')

	# adjust the plotting spacing
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=0.87, wspace=0.3, hspace=0.3)
	# add a super title
	fig.suptitle('Correlation of Four Gene Sets [A, B, C, D]', fontsize=16)

	# change the backgournd to white
	fig.patch.set_facecolor('white')
	fig.savefig('Problem4.png')
	plt.show()


# determine if a string is a float
def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False



# EXECUTE THE PROGRAM
if __name__ == "__main__":
    main()        