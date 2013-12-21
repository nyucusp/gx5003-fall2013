from numpy import array
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
from string import ascii_uppercase

f = open('test1000.data')
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
print centroids

print kmeans(whitened,array(centroids))	

#misclassification error metric

numPredictions = 0
numErrors = 0

