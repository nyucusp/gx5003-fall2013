from itertools import islice
import numpy as np
import matplotlib.pyplot as plt
import pylab

from sklearn.cross_validation import cross_val_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# Set formatting parameters

params = {'axes.labelsize': 11,
		  'text.fontsize': 13,
		  'legend.fontsize': 13,
		  'xtick.labelsize': 12,
		  'ytick.labelsize': 12,
		  'text.usetex': True,
		  'font.family': 'serif',
		  'font.serif': ['Palatino']}

pylab.rcParams.update(params)

# Define formatting functions

def functionFormat(axes):
	axes.spines['top'].set_visible(False)
	axes.spines['bottom'].set_visible(False)
	axes.spines['right'].set_visible(False)
	axes.spines['left'].set_visible(False)
	axes.xaxis.set_ticks_position('bottom')
	axes.yaxis.set_ticks_position('left')

def functionLabel(title, ylabel, xlabel, axes):
	t = axes.set_title(title)
	t.set_y(1.03)
	xlabel = axes.set_xlabel(xlabel, labelpad=15)
	ylabel = axes.set_ylabel(ylabel, labelpad=7)
	top_height = 0.95 - float(len(title.splitlines()))/20
	plt.subplots_adjust(left=0, top=top_height, right=1, bottom=0.1)

# Read and format data

fileLetter = open('letter-recognition.data', 'rU')
listTrain = list(islice(fileLetter, 16000))
listPredict = list(fileLetter)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numAlphabet = {}
for index, letter in enumerate(alphabet):
	numAlphabet[letter] = index

def functionClean(listSample):
	dataClean = []
	targetClean = []
	for line in listSample:
		lineClean = line.split(',')
		targetClean.append(numAlphabet[lineClean.pop(0)])
		lineClean[-1] = lineClean[-1].strip('\n')
		lineInt = [int(x) for x in lineClean]
#		print lineInt
		dataClean.append(lineInt)
	return dataClean, targetClean

trainClean, trainTarget = functionClean(listTrain)
predictClean, predictTarget = functionClean(listPredict)

trainTarget = np.array(trainTarget)
predictTarget = np.array(predictTarget)

# Select most appropriate model using cross-validation on first 16,000 
# data entries.

print "\nCROSS-VALIDATION SCORES:\n------------------------"

scores = []
stdev = []

def functionAdd(mean, variance):
	scores.append(mean)
	stdev.append(variance)

# Support Vector Classifier (SVC)

svc = SVC(kernel='sigmoid', random_state=None)
scoreSVC = cross_val_score(svc, trainClean, trainTarget, cv=10)
functionAdd(np.mean(scoreSVC), np.std(scoreSVC))

print "SVC cross-validation score = ", scores[0]

# K-NN classifier

kn = KNeighborsClassifier(weights='distance', n_neighbors=4, \
	algorithm='ball_tree')
scoreKN = cross_val_score(kn, trainClean, trainTarget, cv=10)
functionAdd(np.mean(scoreKN), np.std(scoreKN))

print "K-NN cross-validation score = ", scores[1]

# Logistic Regression classifier

lr = LogisticRegression()
scoreLR = cross_val_score(lr, trainClean, trainTarget, cv=10)
functionAdd(np.mean(scoreLR), np.std(scoreLR))

print "Logistic Regression cross-validation score = ", scores[2]

# On the first 16,000 data entries:
# SVC cross-validation score = 0.970875
# K-NN cross-validation score = 0.9560625
# Logistic Regression cross-validation score = 0.7196875

# Plot results of cross-validation

labels = ["Support Vector Classification", "K-Nearest Neighbors", \
	"Logistic Regression"]
for index, item in enumerate(scores):
    plt.bar(index, scores[index], width=0.45, color='dimgray', \
            zorder=1, align='center', ec='none')
    plt.errorbar(index, scores[index], yerr=stdev[index], \
                 zorder=3, capsize=6, ms=10, elinewidth=1.5, mew=1.5, \
                 c='tomato', ecolor = 'tomato', fmt='|')
    plt.text(index, scores[index]-0.02, str(scores[index]), color='white', \
             ha='center')

ax = plt.subplot(111)
ax.set_xlim([-0.49,2.49])
ax.set_ylim([0.69, 0.98])

functionFormat(ax)

plt.tick_params(\
    axis='x',         
    which='both',     
    bottom='off',     
    top='off')
plt.tick_params(\
    axis='y',
    which='both',
    left='off',
    right='off',
    labelleft='off')

functionLabel("10-Fold Cross-Validation Accuracy", "", "", ax)
pylab.xticks([0,1,2], labels)

plt.savefig('CV for Classification Methods.png', dpi=300)
plt.show()

# Logistic Regression performs substantially worse than both SVC and K-NN.
# Both SVC and K-NN perform decently well. 

# Logistic Regression could be performing poorly because it is a linear model.
# If I set kernel='linear' for the SVC classifier, the cross-validation score 
# drops from 0.970875 to 0.8525. While we're on the topic, the SVC classifier
# performs best when the kernel parameter is left unspecified (the parameter
# defaults to kernel='rbf').

# Predictions on last 4,000 data entries

print "\nPREDICTIONS:\n------------"

# SVC predictions

svc.fit(trainClean, trainTarget) # fit model according to training data
print "SVC model accuracy is ", svc.score(predictClean, predictTarget), '\n'
# gives mean accuracy on test data, labels

countActual = 0
countPredicted = 0
type1 = 0
type2 = 0

predictedTargets = svc.predict(predictClean) # perform classification
for line in zip(predictTarget, predictedTargets):
    if line[0] == 0:
        countActual += 1
        if line[0] != line[1]:
            type2 += 1
    if line[1] == 0:
        countPredicted += 1
        if line[0] != line[1]:
            type1 += 1

precision = float(countPredicted - type1)/countPredicted
recall = float(countActual - type2)/countActual

print "Total predicted A's:", countPredicted
print "Total actual A's:", countActual
print "Type 1 Errors:", type1
print "Type 2 Errors:", type2, '\n'
print 'Precision:', precision
print 'Recall:', recall

scoreF = 2*precision*recall/(precision+recall)
print 'F-score:', scoreF, '\n'

# K-NN predictions

kn.fit(trainClean, trainTarget) # fit model according to training data
print "K-NN model accuracy is ", kn.score(predictClean, predictTarget), '\n'
# gives mean accuracy on test data, labels

countActual = 0
countPredicted = 0
type1 = 0
type2 = 0

predictedTargets = kn.predict(predictClean) # perform classification
for line in zip(predictTarget, predictedTargets):
    if line[0] == 0:
        countActual += 1
        if line[0] != line[1]:
            type2 += 1
    if line[1] == 0:
        countPredicted += 1
        if line[0] != line[1]:
            type1 += 1

precision = float(countPredicted - type1)/countPredicted
recall = float(countActual - type2)/countActual

print "Total predicted A's:", countPredicted
print "Total actual A's:", countActual
print "Type 1 Errors:", type1
print "Type 2 Errors:", type2, '\n'
print 'Precision:', precision
print 'Recall:', recall

scoreF = 2*precision*recall/(precision+recall)
print 'F-score:', scoreF, '\n'

# Logistic Regression predictions

lr.fit(trainClean, trainTarget) # fit model according to training data
print "Logistic Regression model accuracy is ", lr.score(predictClean, \
	predictTarget), '\n' # gives mean accuracy on test data, labels

countActual = 0
countPredicted = 0
type1 = 0
type2 = 0

predictedTargets = lr.predict(predictClean)
for line in zip(predictTarget, predictedTargets):
    if line[0] == 0:
        countActual += 1
        if line[0] != line[1]:
            type2 += 1
    if line[1] == 0:
        countPredicted += 1
        if line[0] != line[1]:
            type1 += 1

precision = float(countPredicted - type1)/countPredicted
recall = float(countActual - type2)/countActual

print "Total predicted A's:", countPredicted
print "Total actual A's:", countActual
print "Type 1 Errors:", type1
print "Type 2 Errors:", type2, '\n'
print 'Precision:', precision
print 'Recall:', recall

scoreF = 2*precision*recall/(precision+recall)
print 'F-score:', scoreF, '\n'

# SVC model accuracy is 97% 
# Precision: 0.99358974359
# Recall: 0.99358974359
# F-score: 0.99358974359 

# K-NN model accuracy is 96%
# Precision: 0.987179487179
# Recall: 0.987179487179
# F-score: 0.987179487179

# LR model accuracy is 71%
# Precision: 0.88
# Recall: 0.846153846154
# F-score: 0.862745098039

# TO DO: set model parameters for each classifier
# TO DO: justify parameters chosen for each classifier
# TO DO: use built-in libraries to compute accuracy, precision, recall, F-score
# TO DO: explain results of cross-validation, predictions
