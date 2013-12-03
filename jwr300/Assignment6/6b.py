#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 6, Exercise b

'''
Using the labeled dataset produce python codes that report the 
10-fold-Cross Validated RMSE and R^2 scores for 
OLS (num_incidents ~ f(population)) with polynomial models 
from 1 to 5th order (e.g. for second order t ~ w_0 + w_1*x1 + w2*x^2) 
and select a model complexity (polynomial order) based on these scores.
'''


from sklearn import datasets
from sklearn import svm
from sklearn import cross_validation
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np


def cross_fold_validation(train, target):


	svc = svm.SVC(C=1,kernel='linear')
	svc.fit(train, target)

	cv = cross_validation.KFold(len(train), k=10, indices=False)



def main():


	labeled_data = []
	unlabeled_data = []

	with open('labeled_data.csv','r') as myFile:
	    myFile.readline()
	    for line in myFile:
	        line = line.strip().split(",")
	        labeled_data.append([float(x) for x in line])

	train = [j[1] for j in labeled_data]
	target = [i[2] for i in labeled_data]

	X_train = np.array(train).reshape(len(train),1)
	Y_target = np.array(target).reshape(len(target),1)

	cv = cross_validation.KFold(len(train), n_folds=10, indices=False)

	scores = [svc.fit(X_train[traincv], Y_target[traincv]).score(X_train[testcv],Y_target[testcv]) for traincv, testcv in cv]






if __name__ == "__main__":
	main()