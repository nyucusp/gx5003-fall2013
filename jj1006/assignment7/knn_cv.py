import math
import numpy as np

def knn(point, data, k):
#returns the k closest points from data to point
	distances = []
	for d in data:
		dif = (np.array(d)-np.array(point))
		sqdif = dif**2
		distances.append((sqdif.sum(),d))
	s = sorted(distances)
	nn = [s[i][1] for i in range(0,k)]
	return nn

def vote(nn, d):
#returns the winner based on nearest neighbors nn and point->letter dictionary d
	scores = {}
	for n in nn:
		if d[n] in scores:
			scores[d[n]] = scores[d[n]]+1
		else:
			scores[d[n]]=1
	scorearray = []
	for l in scores:
		scorearray.append((scores[l],l))
	return max(scorearray)

######
f = open('test5000.data','r')
farray = []
larray = []
for line in f:
	data = line.split(',')
	intdata = [int(i) for i in data[1:]]
	farray.append(intdata)
	larray.append(data[0]) #hold on to these for cross-validation below

#misclassification error metric
cv = 10
chunksize = int(len(farray)/cv)
cvscores = []
for trial in range(0,cv):
        train = farray[:(trial*chunksize)]
        train.extend(farray[((trial+1)*chunksize):])
        tletters = larray[:(trial*chunksize)]
        tletters.extend(larray[((trial+1)*chunksize):])
        validation = farray[(trial*chunksize):((trial+1)*chunksize)]
        vletters = larray[(trial*chunksize):((trial+1)*chunksize)]

	features = {}#dict mapping locations to letters
	for i in range(0,len(validation)):
		features[tuple(train[i])] = tletters[i] #note, cannot deal with identical points

	k = 3 
	n = 0
	nErrors = 0
	for i in range(0,len(validation)):
		prediction = vote(knn(validation[i],features,k),features)
		if prediction[1] != vletters[i]:
			nErrors = nErrors+1
		n = n+1
	print "CV #"+str(trial)+". Made " + str(nErrors) + " errors of " + str(n) + " predictions."
	cvscores.append(float(nErrors)/n)
print "Mean % error = "+str(np.array(cvscores).mean())
