# !usr/bin/python

######################################################################
#																	
# Assignment 6 - Problem b
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
import math
import random

plot_on = False

def main():
	
	# IMPORT THAT DATA
	fileName = open('ML1Dataset/labeled_data.csv', 'r')
	# 	labeledData = zipcode, population, num_incidents 
	labeledMatrix = np.loadtxt( fileName, delimiter=',', dtype='longlong')

	# get total length
	totalShape = labeledMatrix.shape
	numOfDataPoints = totalShape[0]

	# create separate np.arrays for population and num_incidents
	populations   = np.array( labeledMatrix[:,1] )
	num_incidents = np.array( labeledMatrix[:,2] )

	# get the 1st order least square according to the method from the ML1 class notes
	X_nonlin_Pop = np.concatenate( ( np.matrix(populations).T,  np.ones((numOfDataPoints, 1)) ), axis=1 )
	w_ols_Pop    = np.linalg.lstsq( X_nonlin_Pop, num_incidents.T )[0]
	t_hat_popALL   = populations.T*w_ols_Pop[0]+w_ols_Pop[1]

	rmse_1 = get_rmse( num_incidents, t_hat_popALL )
	r2_1   = get_r2( num_incidents, t_hat_popALL )

	if plot_on:
		# plot the labeled data as num_incidents to population
		fig, ax = plt.subplots(2,5, figsize=[20,8], sharey=True, sharex=True )	


	# print rmse_1, r2_1

	num_validations = 10
	rmse_d1 = np.zeros( num_validations, dtype='longlong' )
	r2_d1   = np.zeros( num_validations, dtype='longfloat' )
	rmse_d2 = np.zeros( num_validations, dtype='longlong' )
	r2_d2   = np.zeros( num_validations, dtype='longfloat' )
	rmse_d3 = np.zeros( num_validations, dtype='longlong' )
	r2_d3   = np.zeros( num_validations, dtype='longfloat' )
	rmse_d4 = np.zeros( num_validations, dtype='longlong' )
	r2_d4   = np.zeros( num_validations, dtype='longfloat' )
	rmse_d5 = np.zeros( num_validations, dtype='longlong' )
	r2_d5   = np.zeros( num_validations, dtype='longfloat' )

	valNum = 0
	while valNum < num_validations:		
		# create a random set of indexes
		testSize = int( round( numOfDataPoints / num_validations ) )
		verifIdx = np.sort( np.array( random.sample(xrange(0, numOfDataPoints), testSize )) )			
		# print verifIdx

		trainPop = np.delete( populations, verifIdx)
		verifPop = populations[verifIdx]

		trainIncidents = np.delete( num_incidents, verifIdx)
		verifIncidents = num_incidents[verifIdx]

		train_size = trainPop.size

		# get the 1st order least square according to the method from the ML1 class notes
		X_nonlin_Pop = np.concatenate( ( np.matrix(trainPop).T,  np.ones((train_size, 1)) ), axis=1 )
		w_ols_Pop    = np.linalg.lstsq( X_nonlin_Pop, trainIncidents.T )[0]			
		t_hat_pop1   = verifPop.T*w_ols_Pop[0]+w_ols_Pop[1]
		# find the stats
		rmse_1 = get_rmse( verifIncidents, t_hat_pop1 )
		r2_1   = get_r2( verifIncidents, t_hat_pop1 )

		# get the 2nd order
		fitDegree  = 2
		t_hat_pop2 = np.poly1d( np.polyfit(trainPop, trainIncidents, fitDegree ) )
		rmse_2 = get_rmse( verifIncidents, t_hat_pop2(verifPop) )
		r2_2   = get_r2( verifIncidents, t_hat_pop2(verifPop) )
		fitDegree  = 3
		t_hat_pop3 = np.poly1d( np.polyfit(trainPop, trainIncidents, fitDegree ) )
		rmse_3 = get_rmse( verifIncidents, t_hat_pop3(verifPop) )
		r2_3   = get_r2( verifIncidents, t_hat_pop3(verifPop) )
		fitDegree  = 4
		t_hat_pop4 = np.poly1d( np.polyfit(trainPop, trainIncidents, fitDegree ) )
		rmse_4 = get_rmse( verifIncidents, t_hat_pop4(verifPop) )
		r2_4   = get_r2( verifIncidents, t_hat_pop4(verifPop) )
		fitDegree  = 5
		t_hat_pop5 = np.poly1d( np.polyfit(trainPop, trainIncidents, fitDegree ) )
		rmse_5 = get_rmse( verifIncidents, t_hat_pop5(verifPop) )
		r2_5   = get_r2( verifIncidents, t_hat_pop5(verifPop) )

		# ensure  0<=r2<=1 else recompute estimate
		if r2_1 > 0 and r2_1 < 1:
			rmse_d1[valNum] = rmse_1
			r2_d1[valNum]   = r2_1
			rmse_d2[valNum] = rmse_2
			r2_d2[valNum]   = r2_2
			rmse_d3[valNum] = rmse_3
			r2_d3[valNum]   = r2_3
			rmse_d4[valNum] = rmse_4
			r2_d4[valNum]   = r2_4
			rmse_d5[valNum] = rmse_5
			r2_d5[valNum]   = r2_5

			if plot_on:
				ax[valNum/5][valNum%5].plot(trainPop, trainIncidents, 'k+')
				ax[valNum/5][valNum%5].plot(verifPop, verifIncidents, 'k.')
				ax[valNum/5][valNum%5].plot(populations.T, t_hat_popALL.T, 'b')
				ax[valNum/5][valNum%5].plot(verifPop, t_hat_pop1, 'b')
				ax[valNum/5][valNum%5].plot(verifPop, t_hat_pop2(verifPop), 'g.')
				ax[valNum/5][valNum%5].plot(verifPop, t_hat_pop3(verifPop), 'y.')
				ax[valNum/5][valNum%5].plot(verifPop, t_hat_pop4(verifPop), 'r.')
				ax[valNum/5][valNum%5].plot(verifPop, t_hat_pop5(verifPop), 'k.')
			valNum += 1

		# print rmse_1, r2_1

	rmseMean_d1 = np.mean( rmse_d1 )
	r2Mean_d1   = np.mean( r2_d1 )
	rmseMean_d2 = np.mean( rmse_d2 )
	r2Mean_d2   = np.mean( r2_d2 )
	rmseMean_d3 = np.mean( rmse_d3 )
	r2Mean_d3   = np.mean( r2_d3 )
	rmseMean_d4 = np.mean( rmse_d4 )
	r2Mean_d4   = np.mean( r2_d4 )
	rmseMean_d5 = np.mean( rmse_d5 )
	r2Mean_d5   = np.mean( r2_d5 )
 	print "Degree RMSE R^2"
 	print "   1  " + str(rmseMean_d1) +" "+ str(r2Mean_d1)
 	print "   2  " + str(rmseMean_d2) +" "+ str(r2Mean_d2)
 	print "   3  " + str(rmseMean_d3) +" "+ str(r2Mean_d3)
 	print "   4  " + str(rmseMean_d4) +" "+ str(r2Mean_d4)
 	print "   5  " + str(rmseMean_d5) +" "+ str(r2Mean_d5)

 	if plot_on:
		fig.patch.set_facecolor('white')
		plt.subplots_adjust( left=0.08, bottom=None, right=0.95, top=None, wspace=0, hspace=0 )
		plt.show()






# return the RMSE
def get_rmse(t, t_hat):
	rms = math.sqrt( np.mean( (t - t_hat)**2 ) )
	return rms

# return r^2
def get_r2(t, t_hat):
	t_mean = np.mean( t )
	ss_res = np.sum( (t - t_hat)**2 )
	ss_tot = np.sum( ( t - t_mean )**2 )
	r2 = 1 - ( ss_res / ss_tot )
	# print t_mean, ss_res, ss_tot, r2
	return r2



		










# EXECUTE THE PROGRAM
if __name__ == "__main__":
    main()        