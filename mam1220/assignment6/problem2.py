# !usr/bin/python

######################################################################
#																	
# Assignment 6 - Problem a
# November 30th, 2013
#
# Michael Musick
#
#	Description: report the 10-fold-Cross Validated RMSE and R^2 scores 
#				for OLS with polynomial models from 1 to 5th order
#	
#######################################################################	
#	
#		
#	
#	
#
######################################################################


# IMPORT NECCESSARY LIBRARIES
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import numpy as np




# MAIN FUNCTION
def main():
	
	# IMPORT THAT DATA
	fileName = open('ML1Dataset/labeled_data.csv', 'r')
	# 	labeledData = zipcode, population, num_incidents 
	labeledMatrix = np.loadtxt( fileName, delimiter=',', dtype='int32')
	
	fileName = open('ML1Dataset/unlabeled_data.csv', 'r')
	# 	unlabeledData = [ zipcode, population ]
	unlabeledMatrix = np.loadtxt( fileName, delimiter=',', dtype='int32')


	# concat values for full arrays
	combinedZips = np.concatenate( (labeledMatrix[:,0], unlabeledMatrix[:,0]), axis=1 )
	combinedPops = np.concatenate( (labeledMatrix[:,1], unlabeledMatrix[:,1]), axis=1 )

	# get lengths
	matShape     = labeledMatrix.shape
	matLen       = matShape[0]
	unShape      = unlabeledMatrix.shape
	unlabeledLen = unShape[0]
	# print matLen
	# print unlabeledLen

	# create individual matrix
	labeledZip           = np.matrix( labeledMatrix[:,0] )
	unlabeledZip         = np.matrix( unlabeledMatrix[:,0] )
	labeledPop           = np.array( labeledMatrix[:,1] )
	unlabeledPop         = np.array( unlabeledMatrix[:,1] )
	labeled_numIncidents = np.array( labeledMatrix[:,2] )
	# print labeledZip
	# print labeledPop
	# print labeled_numIncidents

	# create matrix to pass to lastsq function
	numOfOnes = 1
	# X_nonlin_labeled   = np.concatenate( ( labeledZip.T, labeledPop.T, np.ones((matLen, numOfOnes)) ), axis=1 )
	# X_nonlin_Zip       = np.concatenate( ( labeledZip.T, np.ones((matLen, numOfOnes)) ), axis=1 )
	# X_nonlin_Pop       = np.concatenate( ( np.ones((matLen, numOfOnes)), labeledPop.T ), axis=1 )
	# X_nonlin_Pop       = np.concatenate( ( labeledPop.T,  np.ones((matLen, numOfOnes)) ), axis=1 )
	# X_nonlin_unlabeled = np.concatenate( ( unlabeledZip.T, unlabeledPop.T, np.ones((unlabeledLen, numOfOnes)) ), axis=1 )

	# get 1st order ols
	# w_ols     = np.linalg.lstsq( X_nonlin_labeled, labeled_numIncidents.T )[0]
	# w_ols_Zip = np.linalg.lstsq( X_nonlin_Zip, labeled_numIncidents.T )[0]
	# w_ols_Pop = np.linalg.lstsq( X_nonlin_Pop, labeled_numIncidents.T )[0]
	
	# print w_ols
	# print w_ols_Pop
	# print "OLS for labeled data is " + str(w_ols[0])+", "+str(w_ols[1])+", "+str(w_ols[2])

	# create t_hat sets
	# t_hat_labeled   = X_nonlin_labeled.dot(w_ols)
	# t_hat_Zip       = X_nonlin_Zip.dot(w_ols_Zip)
	# t_hat_Pop       = X_nonlin_Pop.dot(w_ols_Pop)
	# t_hat_unlabeled = X_nonlin_unlabeled.dot( w_ols )



	# 1st order linear regression of population
	# order1_pop = labeledPop.T*w_ols_Pop[0]+w_ols_Pop[1]
	# print order1_pop
	
	print type(labeledPop)
	print labeledPop

	# get 2nd order regression of pop
	numOfOnes    = 5
	# X_nonlin_Pop = np.concatenate( ( labeledPop.T,  np.ones(matLen) ), axis=1 )
	# w_pop        = np.linalg.lstsq( X_nonlin_Pop, labeled_numIncidents.T )[0]
	# print w_pop
	# order2_pop   = labeledPop.T**2*w_pop[0] + labeledPop.T*w_pop[1] + w_pop[2]
	# print labeledPop.T
	# order2_pop   = np.power( labeledPop.T, 2 )*w_pop[2] + labeledPop.T*w_pop[1] + w_pop[0] 
	# labeledPop2 = np.array( labeledPop[0,0] )
	# labeled_numIncidents = np.array( labeled_numIncidents[0] )
	order2_pop   = np.poly1d( np.polyfit(labeledPop, labeled_numIncidents, numOfOnes ) )
	# print order2_pop


	#### PLOTTING ####
	# get min, max, and range for plotting
	zipcodeMin         = np.min( combinedZips )
	zipcodeMax         = np.max( combinedZips )
	zipcodeRange       = zipcodeMax - zipcodeMin
	populationMin      = np.min( combinedPops )
	populationMax      = np.max( combinedPops )
	populationRange    = populationMax - populationMin
	num_incidentsMin   = np.min( labeledMatrix[:,2] )
	num_incidentsMax   = np.max( labeledMatrix[:,2] )
	num_incidentsRange = num_incidentsMax - num_incidentsMin
	# print np.shape( labeledMatrix )
	# print str(populationMax)+" : "+str(populationMin)+" : "+str(populationRange)
	# print str(num_incidentsMax)+" : "+str(num_incidentsMin)+" : "+str(num_incidentsRange)

	regInput = np.linspace( populationMin, populationMax, populationRange )

	# plot the labeled data as num_incidents to population
	fig, ax = plt.subplots(1,1, figsize=[10,10], sharey=True )	
	# 1. pop X num_incidents
	ax.plot(labeledPop, labeled_numIncidents, 'k.')
	# ax.plot(labeledPop.T, order1_pop, 'r')
	ax.plot(regInput, order2_pop(regInput), 'b')
	# format plot
	marginRatio = 0.05
	axX_min = round( populationMin - populationRange*marginRatio )
	axX_max = round( populationMax + populationRange*marginRatio )
	ax.set_xbound( axX_min, axX_max )
	axY_min = round( num_incidentsMin - num_incidentsRange*marginRatio )
	axY_max = round( num_incidentsMax + num_incidentsRange*marginRatio )
	# print str(axY_min)+":"+str(axY_max)
	ax.set_ybound( axY_min, axY_max )
	# ax.set_ylim( 1e-1, 1e6 )
	# ax.set_yscale('log')
	ax.grid(True)
	ax.set_xlabel( 'Population' )
	ax.set_ylabel( 'Number of Incidents')
	ax.set_title('As a function of population')



	# # plot the labeled data as num_incidents to population
	# fig, ax = plt.subplots(1,2, figsize=[20,10], sharey=True )
	
	# # 1. pop X num_incidents
	# ax[0].plot(labeledPop, labeled_numIncidents, 'k.')
	# ax[0].plot(labeledPop.T, t_hat_labeled, 'r+')
	# ax[0].plot(labeledPop.T, order1_pop, 'b-+')
	# # format plot
	# marginRatio = 0.05
	# axX_min = round( populationMin - populationRange*marginRatio )
	# axX_max = round( populationMax + populationRange*marginRatio )
	# ax[0].set_xbound( axX_min, axX_max )
	# axY_min = round( num_incidentsMin - num_incidentsRange*marginRatio )
	# axY_max = round( num_incidentsMax + num_incidentsRange*marginRatio )
	# # print str(axY_min)+":"+str(axY_max)
	# ax[0].set_ybound( axY_min, axY_max )
	# # ax[0].set_ylim( 1e-1, 1e6 )
	# # ax[0].set_yscale('log')
	# ax[0].grid(True)
	# ax[0].set_xlabel( 'Population' )
	# ax[0].set_ylabel( 'Number of Incidents')
	# ax[0].set_title('As a function of population')

	# # 2. zip X num_incidents
	# ax[1].plot(labeledZip, labeled_numIncidents, 'k.' )
	# ax[1].plot(labeledZip.T, t_hat_labeled, 'r+' )
	# ax[1].plot(labeledZip.T, t_hat_Zip, 'b-+' )
	# # format plot
	# marginRatio = 0.05
	# axX_min = round( zipcodeMin - zipcodeRange*marginRatio )
	# axX_max = round( zipcodeMax + zipcodeRange*marginRatio )
	# ax[1].set_xbound( axX_min, axX_max )
	# axY_min = round( num_incidentsMin - num_incidentsRange*marginRatio )
	# axY_max = round( num_incidentsMax + num_incidentsRange*marginRatio )
	# # print str(axY_min)+":"+str(axY_max)
	# ax[1].set_ybound( axY_min, axY_max )
	# # ax[1].set_ylim( 1e-1, 1e6 )
	# # ax[1].set_yscale('log')
	# ax[1].grid(True)
	# ax[1].set_xlabel( 'Zipcode' )
	# ax[1].set_ylabel( '')
	# ax[1].set_title('As a function of zipcode')

	# format figure
	fig.suptitle( 'NYC 311 Reported Incidents', fontsize='18' )
	fig.patch.set_facecolor('white')
	plt.subplots_adjust( left=0.1, bottom=None, right=0.95, top=None, wspace=0.01, hspace=None )

	# save a show the plot
	# fig.savefig('Problem2_1stOrder.png')
	# plt.show()


	
	# # create arrays for 3d plottings (matrix wont work???)
	# labeled_NI_npArr      = np.array(labeled_numIncidents)
	# t_hat_npArr           = np.array(t_hat_labeled)
	# t_hat_unlabeled_npArr = np.array(t_hat_unlabeled)

	# fig = plt.figure()
	# ax = fig.gca(projection='3d')
	# ax.scatter(labeledZip, labeledPop, labeled_NI_npArr, c='k', marker='.')
	# ax.scatter(labeledZip, labeledPop, t_hat_npArr, c='r', marker='+')
	# ax.scatter(unlabeledZip, unlabeledPop, t_hat_unlabeled_npArr, c='b', marker='+')
	# ax.set_xlabel('Zipcode')
	# ax.set_ylabel('Popultion')
	# ax.set_zlabel('Number of Incidents')
	
	# show both plots
	plt.show()


# return sorted matrix
def sortMatrixByColumnNum( matrix, colNum ):
	col = colNum
	return matrix[np.array(matrix[:,col].argsort(axis=0).tolist()).ravel()]

# EXECUTE THE PROGRAM
if __name__ == "__main__":
    main()        