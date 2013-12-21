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

f = open('train.data','r')
features = []
letters = []
numLetters = 26
for line in f:
	data = line.split(',')
	floatdata = array(data[1:], dtype='|S4')
	features.append(floatdata.astype(np.float))
	letters.append(data[0])

cv = 10
chunksize = int(len(features)/cv)
cvscores = []
for trial in range(0,cv):
	train = features[:(trial*chunksize)]
	train.extend(features[((trial+1)*chunksize):])
	train = array(train)
	tletters = letters[:(trial*chunksize)]
	tletters.extend(letters[((trial+1)*chunksize):])
	validate = features[(trial*chunksize):((trial+1)*chunksize)]
	vletters = letters[(trial*chunksize):((trial+1)*chunksize)]

	whitened = whiten(train)

	#compute original centroids based on mean of individual letters
	centroids = []
	featuredict = {}
	for i in range(0,len(train)):
	        if tletters[i] in featuredict:
	                featuredict[tletters[i]].append(whitened[i])
	        else:
	                featuredict[tletters[i]] = [whitened[i]]
	
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
	for i in range(0,len(validate)):
		point = validate[i]
		prediction = ascii_uppercase[closest(point.astype(np.float),centroids)]
		if prediction != vletters[i]:
			numErrors = numErrors + 1
		numPredictions = numPredictions + 1
	print "CV #"+str(trial)+". Made " + str(numErrors) + " errors of " + str(numPredictions) + " predictions."
	cvscores.append(float(numErrors)/numPredictions)
print "Mean % error = "+str(np.array(cvscores).mean())
