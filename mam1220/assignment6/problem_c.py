# !usr/bin/python

######################################################################
#																	
# Assignment 6 - Problem c
# November 30th, 2013
#
# Michael Musick
#
#	Description: Plot the 10-Fold CV RMSE scores with STD error bars
#				of the various models (ie. 1st-5th order polynomials) 
#				using all data (I am assuming this means both population
#				and zipcode)
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
import warnings
import math
import random

plot_3d = True


def main():

	# IMPORT THAT DATA
	fileName = open('ML1Dataset/labeled_data.csv', 'r')
	# 	labeledData = zipcode, population, num_incidents 
	labeledMatrix = np.loadtxt( fileName, delimiter=',', dtype='ulonglong')

	# get total length
	totalShape = labeledMatrix.shape
	numOfDataPoints = totalShape[0]

	# create separate np.arrays for population and num_incidents
	populations   = np.matrix( labeledMatrix[:,1].T, dtype='ulonglong' )
	zipcodes      = np.matrix( labeledMatrix[:,0].T, dtype='ulonglong' )
	num_incidents = np.matrix( labeledMatrix[:,2].T, dtype='ulonglong' )


	num_validations = 10


	# create arrays for the RMSE values
	rmse_d1 = np.zeros( num_validations, dtype='longlong' )
	rmse_d2 = np.zeros( num_validations, dtype='longlong' )
	rmse_d3 = np.zeros( num_validations, dtype='longlong' )
	rmse_d4 = np.zeros( num_validations, dtype='longlong' )
	rmse_d5 = np.zeros( num_validations, dtype='longlong' )
	stdErr_d1 = np.zeros( num_validations, dtype='longlong' )
	stdErr_d2 = np.zeros( num_validations, dtype='longlong' )
	stdErr_d3 = np.zeros( num_validations, dtype='longlong' )
	stdErr_d4 = np.zeros( num_validations, dtype='longlong' )
	stdErr_d5 = np.zeros( num_validations, dtype='longlong' )


	verifStart = 0
	testSize = int( round( (numOfDataPoints / num_validations) * (num_validations-1)  ) )
	verifRange = numOfDataPoints - testSize
	randomSampleOrder = random.sample(xrange(0, numOfDataPoints), numOfDataPoints)
	# print randomSampleOrder


	valNum = 0
	while valNum < num_validations:		
	
		# OPTION 1 for Cross Validation
		# CREATE A RANDOM SET OF INDEXES EACH TIME
		# testSize = int( round( numOfDataPoints * 0.9 ) )
		# verifIdx = np.sort( np.array( random.sample(xrange(0, numOfDataPoints), testSize )) )	

		# OPTION 2 for Cross Validation
		# PULL SETS IN ORDER FROM THE WHOLE RANDOMIZED DATA SET
		# This ensures that each sample is touched once
		verifEnd = verifStart + verifRange
		if verifEnd > numOfDataPoints:
			verifEnd = numOfDataPoints
		verifIdx = randomSampleOrder[ verifStart:verifEnd ]
		# print verifIdx
		# print verifStart, verifEnd

		# calculate all matrix manipulations once and reassign to x1, x2 	
		t = np.delete( num_incidents, verifIdx ).T
		t_v = num_incidents[:,verifIdx]
		verifSize = t.size 

		# training data
		x1   = np.delete( zipcodes, verifIdx ).T
		x2   = np.delete( populations, verifIdx ).T
		x1_2 = np.power( x1, 2 )
		x2_2 = np.power( x2, 2 )
		x1_3 = np.power( x1, 3 )
		x2_3 = np.power( x2, 3 )
		x1_4 = np.power( x1, 4 )
		x2_4 = np.power( x2, 4 )
		x1_5 = np.power( x1, 5 )
		x2_5 = np.power( x2, 5 )

		# verify/test data
		x1_v = zipcodes[:,verifIdx].T
		x2_v = populations[:,verifIdx].T
		x1_v2 = np.power( x1_v, 2 )
		x2_v2 = np.power( x2_v, 2 )
		x1_v3 = np.power( x1_v, 3 )
		x2_v3 = np.power( x2_v, 3 )
		x1_v4 = np.power( x1_v, 4 )
		x2_v4 = np.power( x2_v, 4 )
		x1_v5 = np.power( x1_v, 5 )
		x2_v5 = np.power( x2_v, 5 )
		

		# print verifIdx
		# print testSize
		# print numOfDataPoints
		# print x1.shape
		# print x2.shape
		# print verifSize

		# 1st order
		X_nonlin_1 = np.concatenate(( x1, x2, np.ones((verifSize, 1)) ), axis=1 )
		w_ols_1    = np.linalg.lstsq( X_nonlin_1, t )[0]
		t_hat_1plot= w_ols_1[2] + x2*w_ols_1[1] + x1*w_ols_1[0]
		t_hat_1    = w_ols_1[2] + x2_v*w_ols_1[1] + x1_v*w_ols_1[0]
		
		# 2nd order
		X_nonlin_2 = np.concatenate(( x1_2, x2_2, x1, x2, np.ones((verifSize, 1)) ), axis=1 )
		w_ols_2    = np.linalg.lstsq( X_nonlin_2, t )[0]
		t_hat_2plot= w_ols_2[4] + x2*w_ols_2[3] + x1*w_ols_2[2] + x2_2*w_ols_2[1] + x1_2*w_ols_2[0]
		t_hat_2    = w_ols_2[4] + x2_v*w_ols_2[3] + x1_v*w_ols_2[2] + x2_v2*w_ols_2[1] + x1_v2*w_ols_2[0]

		# 3nd order
		X_nonlin_3 = ( np.concatenate(( x1_3, x2_3, x1_2, x2_2, x1, x2, 
			np.ones((verifSize, 1)) ), axis=1 ) )
		w_ols_3    = np.linalg.lstsq( X_nonlin_3, t )[0]
		t_hat_3plot= ( w_ols_3[6] + x2*w_ols_3[5] + x1*w_ols_3[4] 
			+ x2_2*w_ols_3[3] + x1_2*w_ols_3[2] + x2_3*w_ols_3[1] + x1_3*w_ols_3[0] )
		t_hat_3    = ( w_ols_3[6] + x2_v*w_ols_3[5] + x1_v*w_ols_3[4] 
			+ x2_v2*w_ols_3[3] + x1_v2*w_ols_3[2] + x2_v3*w_ols_3[1] + x1_v3*w_ols_3[0] )

		# 4nd order
		X_nonlin_4 = ( np.concatenate(( x1_4, x2_4, x1_3, x2_3, x1_2, x2_2, x1, x2, 
			np.ones((verifSize, 1)) ), axis=1 ) )
		w_ols_4    = np.linalg.lstsq( X_nonlin_4, t )[0]
		t_hat_4plot= ( w_ols_4[8] + x2*w_ols_4[7] + x1*w_ols_4[6] 
			+ x2_2*w_ols_4[5] + x1_2*w_ols_4[4] + x2_3*w_ols_4[3] + x1_3*w_ols_4[2] 
			+ x2_4*w_ols_4[1] + x1_4*w_ols_4[0] )
		t_hat_4    = ( w_ols_4[8] + x2_v*w_ols_4[7] + x1_v*w_ols_4[6] 
			+ x2_v2*w_ols_4[5] + x1_v2*w_ols_4[4] + x2_v3*w_ols_4[3] + x1_v3*w_ols_4[2] 
			+ x2_v4*w_ols_4[1] + x1_v4*w_ols_4[0] )

		# 5nd order
		X_nonlin_5 = ( np.concatenate(( x1_5, x2_5, x1_4, x2_4, x1_3, x2_3, x1_2, x2_2, x1, x2, 
			np.ones((verifSize, 1)) ), axis=1 ) )
		w_ols_5    = np.linalg.lstsq( X_nonlin_5, t )[0]
		t_hat_5plot= ( w_ols_5[10] + x2*w_ols_5[9] + x1*w_ols_5[8] 
			+ x2_2*w_ols_5[7] + x1_2*w_ols_5[6] + x2_3*w_ols_5[5] + x1_3*w_ols_5[4] 
			+ x2_4*w_ols_5[3] + x1_4*w_ols_5[2] + x2_5*w_ols_5[1] + x1_5*w_ols_5[0] )
		t_hat_5    = ( w_ols_5[10] + x2_v*w_ols_5[9] + x1_v*w_ols_5[8] 
			+ x2_v2*w_ols_5[7] + x1_v2*w_ols_5[6] + x2_v3*w_ols_5[5] + x1_v3*w_ols_5[4] 
			+ x2_v4*w_ols_5[3] + x1_v4*w_ols_5[2] + x2_v5*w_ols_5[1] + x1_v5*w_ols_5[0] )
		
		rmse_1 = get_rmse( np.array(t_v), np.array(t_hat_1) )
		rmse_2 = get_rmse( np.array(t_v), np.array(t_hat_2) )
		rmse_3 = get_rmse( np.array(t_v), np.array(t_hat_3) )
		rmse_4 = get_rmse( np.array(t_v), np.array(t_hat_4) )
		rmse_5 = get_rmse( np.array(t_v), np.array(t_hat_5) )

		# Sometime there are power errors due to the x^5.  Ignore these test sets and recompute
		if rmse_1<50000 or rmse_2<50000 or rmse_3<50000 or rmse_4<50000 or rmse_5<50000:		
			rmse_d1[valNum] = rmse_1
			rmse_d2[valNum] = rmse_2
			rmse_d3[valNum] = rmse_3
			rmse_d4[valNum] = rmse_4
			rmse_d5[valNum] = rmse_5


			verifStart = verifEnd
			valNum += 1
		# print valNum
		
		### END CROSS VALIDATION LOOP ###
	
	# print rmse_d1 
	# print rmse_d2
	# print rmse_d3
	# print rmse_d4
	# print rmse_d5 

	# print stdErr_d1 
	# print stdErr_d2
	# print stdErr_d3
	# print stdErr_d4
	# print stdErr_d5


	# get the mean for the arrays
	rmseResults = ( [ np.mean(rmse_d1), np.mean(rmse_d2), np.mean(rmse_d3), 
		np.mean(rmse_d4), np.mean(rmse_d5) ] )
	# stdErrResults = ( [ np.mean(stdErr_d1), np.mean(stdErr_d2), np.mean(stdErr_d3), 
		# np.mean(stdErr_d4), np.mean(stdErr_d5) ] )
	# print rmseResults
	# print stdErrResults

	# standard error of the cv-rmse set  
	stdErrResults = ( [ np.std( rmse_d1 ), np.std( rmse_d2 ), np.std( rmse_d3 ),
		 np.std( rmse_d4 ), np.std( rmse_d5 ) ] )


	fig, ax = plt.subplots(figsize=[10,10])
	width = 0.9
	complexity = np.array((1,2,3,4,5))
	barPlot = ax.bar( complexity, rmseResults, width, color='r', yerr=stdErrResults )
	# barPlot = ax.bar( complexity, rmseResults, width, color='r', yerr=menStd)
	yMin = min(rmseResults) - min(stdErrResults)
	yMax = max(rmseResults) + max(stdErrResults)
	yRange = yMax-yMin
	margin = 0.05 * yRange
	yMin -= margin
	yMax += margin
	ax.set_ybound(yMin, yMax)
	ax.set_xbound(0.9, 6)
	ax.set_xticks(complexity+width*0.5)
	ax.set_xticklabels( ('X^1', 'X^2', 'X^3', 'X^4', 'X^5') )
	ax.set_xlabel('Model Complexity')
	ax.set_ylabel('Mean RMSE')

	fig.suptitle( 'RMSE Scores for '+str(num_validations)+'-fold CV on \n( num of incidents ~ f(population, zipcodes))', fontsize='18' )
	fig.patch.set_facecolor('white')
	plt.subplots_adjust( left=0.15, bottom=None, right=0.95, top=0.85, wspace=0.01, hspace=None )
	fig.savefig('Problem_c_2d.png')
	
	if plot_3d:
		zipcodes = np.array(zipcodes)
		populations = np.array(populations)
		num_incidents = np.array(num_incidents)
		t = np.array(t)
		t_hat_1plot = np.array(t_hat_1plot)
		t_hat_2plot = np.array(t_hat_2plot)
		t_hat_3plot = np.array(t_hat_3plot)
		t_hat_4plot = np.array(t_hat_4plot)
		t_hat_5plot = np.array(t_hat_5plot)
		fig = plt.figure( )
		ax = fig.gca(projection='3d')
		ax.scatter(x1, x2, t, c='k', marker='.')
		ax.scatter(x1, x2, t_hat_1plot, c='b', marker='+', label='1st degree')
		# ax.scatter(x1, x2, t_hat_2plot, c='g', marker='+')
		# ax.scatter(x1, x2, t_hat_3plot, c='r', marker='+')
		# ax.scatter(x1, x2, t_hat_4plot, c='c', marker='+')
		ax.scatter(x1, x2, t_hat_5plot, c='m', marker='+', label='5th degree')
		ax.set_xlabel('Zipcode')
		ax.set_ylabel('Popultion')
		ax.set_zlabel('Number of Incidents')
		fig.patch.set_facecolor('white')	
		fig.suptitle( '3d representation of \n( num_incidents ~ f( population, zip code ) )', fontsize='18' )
		# show both plots
	
	plt.show()
	
	
	
	

# return the RMSE
def get_rmse(t, t_hat):
	rms = math.sqrt( np.mean( (t - t_hat)**2 ) )
	return rms



warnings.filterwarnings("ignore")
# EXECUTE THE PROGRAM
if __name__ == "__main__":
    main()        