# !usr/bin/python

######################################################################
#																	
# Assignment 5 - Problem 3
# November 24th, 2013
#
# Michael Musick
#
#	Description: Microprocessor introduction year and production numbers
#	
#	Annotations: none requested
#	
#
######################################################################

# IMPORT NECCESSARY LIBRARIES
import matplotlib.pyplot as plt 
import numpy as np



# create global variables for value arrays
microName = []
microYear = []
microNum  = []

# MAIN FUNCTION
def main():
	microDict = {}
	# IMPORT THAT DATA
	data_fromFile = open('microprocessors.dat', 'r')
	for line in data_fromFile:		
		tempLine = line.strip().split(',')
		if tempLine[1].isdigit() and tempLine[2].isdigit():
			microDict[int(tempLine[1])] = [int(tempLine[2])]
			microDict[int(tempLine[1])].append(tempLine[0])

	microYear = sorted(microDict.keys())

	# print microDict

	for key in microYear:
		microName.append(microDict[key][1])
		microNum.append(microDict[key][0])



	fig, ax = plt.subplots(1,2, figsize=[10,10])

	ax[0].plot(microYear, np.arange(len(microYear)), 'ko')
	ax0Xmin = microYear[0]
	ax0Xmax = microYear[-1]
	y_ = np.arange(len(microNum))
	ax[0].set_yticks(y_)
	ax[0].set_yticklabels(microName)
	
	ax[1].plot(microNum, np.arange(len(microNum)), 'ko')
	ax[1].set_xscale('log')
	ax[1].set_yticks(y_)
	ax[1].set_yticklabels([])
	
	ax[0].grid(True)
	ax[1].grid(True)
	ax[0].margins(.05,.05)
	ax[1].margins(1,.05)
	x1bound = ax[1].get_xbound()
	ax[1].set_xbound(x1bound[0]-1000, x1bound[1])


	plt.subplots_adjust(left=0.25, bottom=None, right=0.95, top=None, wspace=0.01, hspace=None)


	fig.suptitle('Microprocessor Release Data', fontsize='18')
	ax[0].set_xlabel('Year of introduction')
	ax[1].set_xlabel('Number of transistors')

	fig.patch.set_facecolor('white')
	fig.savefig('Problem3.png')
	plt.show()





# EXECUTE THE PROGRAM
if __name__ == "__main__":
    main()        