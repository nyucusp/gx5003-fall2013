from numpy import array
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
from string import ascii_uppercase

def closest(point, centroids):
#returns the index of the closest centroid from centroids to point
        distances = []
        for d in centroids:
                dif = (np.array(d)-np.array(point))
                sqdif = dif**2
                distances.append(sqdif.sum())
        return distances.index(min(distances))

f = open('test10000.data','r')
features = []
letters = []
numLetters = 26
for line in f:
	data = line.split(',')
	floatdata = array(data[1:], dtype='|S4')
	features.append(floatdata.astype(np.float))
	letters.append(data[0])
features = array(features)

whitened = whiten(features)
#print kmeans(whitened,numLetters)

#compute original centroids based on mean of individual letters
centroids = []
featuredict = {}
for i in range(0,len(features)):
        if letters[i] in featuredict:
                featuredict[letters[i]].append(whitened[i])
        else:
                featuredict[letters[i]] = [whitened[i]]

for l in ascii_uppercase:
	c = []
	for i in range(0,len(featuredict[l][0])):
		temp = []
		for j in range(0,len(featuredict[l])):
			temp.append(featuredict[l][j][i])
		c.append(np.array(temp).mean())
	centroids.append(c)
centroids = kmeans(whitened,array(tuple(centroids)))[0]
#misclassification error metric
numPredictions = 0
numErrors = 0

f = open('train.data','r')
for line in f:
	data = line.split(',')
	point = array(data[1:],dtype = '|S4')
	prediction=ascii_uppercase[closest(point.astype(np.float),centroids)]
	if prediction != data[0]:
		numErrors = numErrors + 1
	numPredictions = numPredictions + 1
print "Made " + str(numErrors) + " errors of " + str(numPredictions) + " predictions."
