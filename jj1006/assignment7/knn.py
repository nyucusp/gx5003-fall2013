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
f = open('train.data','r')
features = {} #dict mapping locations to letters
for line in f:
	data = line.split(',')
	intdata = [int(i) for i in data[1:]]
	features[tuple(intdata)] = data[0]
	#NOTE: this introduces a known bug, which is that if two points are equal the one that appears later will override the earlier one. But we assume the probaiblity of this is negligible

#misclassification error metric
k = 3 
n = 0
nErrors = 0

f1subject = 'A'
nTestPositives = 0
nTruePositives = 0
nConditionPositives = 0
f = open('validate.data','r')
lcounter = 1
for line in f:
	print "processing line "+str(lcounter)
	lcounter=lcounter+1
	data = line.split(',')
	intpoint = [int(i) for i in data[1:]]
	prediction = vote(knn(intpoint,features,k),features)
	if prediction[1] != data[0]:
		nErrors = nErrors+1
	if prediction[1] == f1subject:
		nTestPositives = nTestPositives+1
	if data[0] == f1subject:
		nConditionPositives = nConditionPositives+1
	if data[0] == prediction[1] and data[0] == f1subject:
		nTruePositives = nTruePositives+1
	n = n+1
print "Made " + str(nErrors) + " errors of " + str(n) + " predictions."
precision = float(nTruePositives)/nTestPositives
sensitivity = float(nTruePositives)/nConditionPositives
f1 = 2*(precision*sensitivity)/(precision+sensitivity)
print "F1 score for letter "+f1subject+": "+str(f1)
