# !usr/bin/python

######################################################################
#																	
# Assignment 6 - Problem d
# November 30th, 2013
#
# Michael Musick
#
#	Description: Final OLS model
#				This uses population, Adjusted Gross Income, 
#				and  zip code as predictors
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
import math
import random
import csv

# plot a 3d representation
# note: because I am using 3 features as predictors this is not as informative
plot_3d = False


def main():
	
	# IMPORT THAT DATA
	fileName = open('ML1Dataset/labeled_data.csv', 'r')
	# 	labeledData = zipcode, population, num_incidents 
	labeledMatrix = np.loadtxt( fileName, delimiter=',', dtype='longlong')
	
	fileName = open('ML1Dataset/unlabeled_data.csv', 'r')
	# 	unlabeledData = [ zipcode, population ]
	unlabeledMatrix = np.loadtxt( fileName, delimiter=',', dtype='longlong')


	# get lengths
	matShape        = labeledMatrix.shape
	numOfDataPoints = matShape[0]
	unShape         = unlabeledMatrix.shape
	unlabeledLen    = unShape[0]
	

	# create individual matrix
	labeledZip           = np.array( labeledMatrix[:,0], dtype='longlong' )
	unlabeledZip         = np.array( unlabeledMatrix[:,0], dtype='longlong' )
	labeledPop           = np.array( labeledMatrix[:,1], dtype='longlong' )
	unlabeledPop         = np.array( unlabeledMatrix[:,1], dtype='longlong' )
	labeled_numIncidents = np.array( labeledMatrix[:,2], dtype='longlong' )


	# read in the AGI.txt file
	agiDict = readInAGI()

	# get AGI into an array according to the zip order from labeled
	labeledAGI = np.array( np.zeros(numOfDataPoints) )
	for i in range(numOfDataPoints):
		if labeledZip[i] in agiDict:
			labeledAGI[i] = agiDict[labeledZip[i]]

	unlabeledAGI = np.array( np.zeros(unlabeledLen) )
	for i in range(unlabeledLen):
		if unlabeledZip[i] in agiDict:
			unlabeledAGI[i] = agiDict[unlabeledZip[i]]



	# get expected RMSE score through 10-fold CV
	num_validations = 10
	rmseArr = np.zeros( num_validations, dtype='longlong' )
	verifStart = 0
	testSize = int( round( (numOfDataPoints / num_validations) * (num_validations-1)  ) )
	verifRange = numOfDataPoints - testSize
	randomSampleOrder = random.sample(xrange(0, numOfDataPoints), numOfDataPoints)

	valNum = 0
	while valNum < num_validations:		
		verifEnd = verifStart + verifRange
		if verifEnd > numOfDataPoints:
			verifEnd = numOfDataPoints
		verifIdx = randomSampleOrder[ verifStart:verifEnd ]

		# calculate all matrix manipulations once and reassign to x1, x2 	
		t = np.delete( labeled_numIncidents, verifIdx ).T
		t_v = labeled_numIncidents[:,verifIdx]
		verifSize = t.size 
	
		# training data
		cvx1   = np.delete( labeledPop, verifIdx ).T
		cvx2   = np.delete( labeledAGI, verifIdx ).T
		cvx3   = np.delete( labeledZip, verifIdx ).T
		# cvx1_2 = np.power( cvx1, 2 )
		# cvx2_2 = np.power( cvx2, 2 )
		# cvx3_2 = np.power( cvx3, 2 )

		# test data
		cvx1_t = labeledPop[:,verifIdx].T
		cvx2_t = labeledAGI[:,verifIdx].T
		cvx3_t = labeledZip[:,verifIdx].T
		# cvx1_2t = np.power( cvx1_t, 2 )
		# cvx2_2t = np.power( cvx2_t, 2 )
		# cvx3_2t = np.power( cvx3_t, 2 )	

		# X_nonlin_2 = np.concatenate(( np.matrix(cvx1_2).T, np.matrix(cvx2_2).T, np.matrix(cvx3_2).T, np.matrix(cvx1).T, np.matrix(cvx2).T, np.matrix(cvx3).T, np.ones((testSize, 1)) ), axis=1 )
		# w_ols_2    = np.linalg.lstsq( X_nonlin_2, t )[0]
		# t_hat_2    = w_ols_2[6] + cvx3_t*w_ols_2[5] + cvx2_t*w_ols_2[4] + cvx1_t*w_ols_2[3] + cvx3_2t*w_ols_2[2] + cvx2_2t*w_ols_2[1] + cvx1_2t*w_ols_2[0]
		X_nonlin_2 = np.concatenate( (np.matrix(cvx1).T, np.matrix(cvx2).T, np.matrix(cvx3).T, np.ones((testSize, 1)) ), axis=1 )
		w_ols_2    = np.linalg.lstsq( X_nonlin_2, t )[0]
		t_hat_2    = w_ols_2[3] + cvx3_t*w_ols_2[2] + cvx2_t*w_ols_2[1] + cvx1_t*w_ols_2[0]

		rmse_1 = get_rmse( np.array(t_v), np.array(t_hat_2) )
		if rmse_1<50000:
			rmseArr[valNum] = rmse_1
			verifStart = verifEnd
			valNum += 1

	expectedRMSE = np.mean(rmseArr)

	### TRAIN ON WHOLE SET AND GET THE PREDICTED VALUES ###
	# training data
	x1   = labeledPop.T
	x2   = labeledAGI.T
	x3 = labeledZip.T
	# x1_2 = np.power( x1, 2 )
	# x2_2 = np.power( x2, 2 )
	# x3_2 = np.power( x3, 2 )

	# test data
	x1_t = unlabeledPop.T
	x2_t = unlabeledAGI.T
	x3_t = unlabeledZip.T
	# x1_2t = np.power( x1_t, 2 )
	# x2_2t = np.power( x2_t, 2 )
	# x3_2t = np.power( x3_t, 2 )

	X_nonlin_2 = np.concatenate(( np.matrix(x1).T, np.matrix(x2).T, np.matrix(x3).T, np.ones((numOfDataPoints, 1)) ), axis=1 )
	w_ols_2    = np.linalg.lstsq( X_nonlin_2, labeled_numIncidents )[0]
	t_hat_2    = w_ols_2[3] + x3_t*w_ols_2[2] + x2_t*w_ols_2[1] + x1_t*w_ols_2[0]

	# create a dict with the zip and predicted number of incidents
	predictedArray = np.array(t_hat_2)
	predicted_values = {}
	for i in range(unlabeledLen):
		predicted_values[ unlabeledZip[i] ] = predictedArray[i]
		print 'zipcode', unlabeledZip[i], 'predicted # of incidents:', predictedArray[i]
	print 'Expected RMSE on test set is', expectedRMSE
	# print predicted_values
	# print np.max(predictedArray)
	# print np.max(labeled_numIncidents)
 
 	# updated on 12/19 
 	# mirroring changes in output specifications 
 	# data is now saved to a .csv file for predictions
	# write predictions.csv
	with open('predictions.csv', 'wb') as csvfile:
		csv_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		# write column headers
		csv_writer.writerow(['zipcode', 'number_incidents_prediction'])
		# write the data 
		for i in range(unlabeledLen):
			csv_writer.writerow([unlabeledZip[i], predictedArray[i]])




	if plot_3d:

		fig = plt.figure()
		ax = fig.gca(projection='3d')
		ax.scatter(labeledPop, labeledAGI, labeled_numIncidents, c='k', marker='.')
		ax.scatter(unlabeledPop, unlabeledAGI, predictedArray, c='b', marker='+')
		ax.set_xlabel('Popultion')
		ax.set_ylabel('AGI')
		ax.set_zlabel('Number of Incidents')	
		# show both plots
	
	plt.show()




# read in this totally messed up Adjusted Gross Income File
# and produce a value that is = AGI
def readInAGI():	
	csvFile = open('ny_state_AGI_2.txt', 'r')
	all_agi_data = {}

	# allAGI = csv.DictReader(fileName)
	# print csvFile

	lineNum = 0
	for line in csvFile:
		lineNum += 1
		tempLine = line.strip().split('\t')
		# if str(tempLine[0])
		if len(str(tempLine[0])) == 1:
			zip_ = tempLine[1].strip()
			# print zip_
			# print len(zip_)
			if len(zip_)==11:
				zip__ = []
				for char in zip_:
					# print char
					if char != '\x00':
						zip__.append(char)
				zip_ = int(''.join(zip__))
				numRet_ = tempLine[2].strip()
				numRet__ = []
				for char in numRet_:
					# print char
					if char != '\x00' and char.isdigit():
						numRet__.append(char)
				numRet_ = float(''.join(numRet__))
				agi_ = tempLine[3].strip()
				agi__ = []
				for char in agi_:
					# print char
					if char != '\x00' and char.isdigit():
						agi__.append(char)
				agi_ = float(''.join(agi__))
				# print zip_, numRet_, agi_, agi_/numRet_
				# all_agi_data[zip_] =  agi_/numRet_
				all_agi_data[zip_] =  agi_
	return all_agi_data

# return the RMSE
def get_rmse(t, t_hat):
	rms = math.sqrt( np.mean( (t - t_hat)**2 ) )
	return rms


# EXECUTE THE PROGRAM
if __name__ == "__main__":
    main()        