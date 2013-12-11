# !usr/bin/python

######################################################################
#																	
# Assignment 6 - Problem a
# November 30th, 2013
#
# Michael Musick
#
#	Description: Plot The Data and Reason About it
#	
#######################################################################	


# IMPORT NECCESSARY LIBRARIES
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import numpy as np



# MAIN FUNCTION
def main():
	# IMPORT THAT DATA
	# labeledData = zipcode, population, num_incidents 
	fileName = open('ML1Dataset/labeled_data.csv', 'r')
	labeledMatrix = np.loadtxt( fileName, delimiter=',', dtype='int32')

	# get min, max, and range
	zipcodeMin         = np.min( labeledMatrix[:,0] )
	zipcodeMax         = np.max( labeledMatrix[:,0] )
	zipcodeRange       = zipcodeMax - zipcodeMin
	populationMin      = np.min( labeledMatrix[:,1] )
	populationMax      = np.max( labeledMatrix[:,1] )
	populationRange    = populationMax - populationMin
	num_incidentsMin   = np.min( labeledMatrix[:,2] )
	num_incidentsMax   = np.max( labeledMatrix[:,2] )
	num_incidentsRange = num_incidentsMax - num_incidentsMin
	# print np.shape( labeledMatrix )
	# print str(populationMax)+" : "+str(populationMin)+" : "+str(populationRange)
	# print str(num_incidentsMax)+" : "+str(num_incidentsMin)+" : "+str(num_incidentsRange)


	# # plot the labeled data as num_incidents to population
	fig, ax = plt.subplots(1,2, figsize=[20,10], sharey=True )

	# 1. pop X num_incidents
	ax[0].plot(labeledMatrix[:,1], labeledMatrix[:,2], 'k.')
	# format plot
	marginRatio = 0.05
	axX_min = round( populationMin - populationRange*marginRatio )
	axX_max = round( populationMax + populationRange*marginRatio )
	ax[0].set_xbound( axX_min, axX_max )
	axY_min = round( num_incidentsMin - num_incidentsRange*marginRatio )
	axY_max = round( num_incidentsMax + num_incidentsRange*marginRatio )
	# print str(axY_min)+":"+str(axY_max)
	ax[0].set_ybound( axY_min, axY_max )
	ax[0].grid(True)
	ax[0].set_xlabel( 'Population' )
	ax[0].set_ylabel( 'Number of Incidents')
	ax[0].set_title('As a function of population')

	# 2. zip X num_incidents
	ax[1].plot(labeledMatrix[:,0], labeledMatrix[:,2], 'k.')
	# format plot
	marginRatio = 0.05
	axX_min = round( zipcodeMin - zipcodeRange*marginRatio )
	axX_max = round( zipcodeMax + zipcodeRange*marginRatio )
	ax[1].set_xbound( axX_min, axX_max )
	axY_min = round( num_incidentsMin - num_incidentsRange*marginRatio )
	axY_max = round( num_incidentsMax + num_incidentsRange*marginRatio )
	# print str(axY_min)+":"+str(axY_max)
	ax[1].set_ybound( axY_min, axY_max )
	ax[1].grid(True)
	ax[1].set_xlabel( 'Zipcode' )
	ax[1].set_ylabel( '')
	ax[1].set_title('As a function of zipcode')



	# format figure
	fig.suptitle( 'NYC 311 Reported Incidents', fontsize='18' )
	fig.patch.set_facecolor('white')
	plt.subplots_adjust( left=0.08, bottom=None, right=0.95, top=None, wspace=0.01, hspace=None )

	# # save a show the plot
	fig.savefig('Problem_a_2d.png')



	# 3. 3d
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	# plt.figure(1)
	ax.scatter(labeledMatrix[:,0], labeledMatrix[:,1], labeledMatrix[:,2], c='k', marker='.')
	ax.set_xlabel('Zip Code')
	ax.set_ylabel('Population')
	ax.set_zlabel('Number of Incidents')		
	fig.patch.set_facecolor('white')
	plt.show()

# return sorted matrix
def sortMatrixByColumnNum( matrix, colNum ):
	col = colNum
	return matrix[np.array(matrix[:,col].argsort(axis=0).tolist()).ravel()]

# EXECUTE THE PROGRAM
if __name__ == "__main__":
    main()        