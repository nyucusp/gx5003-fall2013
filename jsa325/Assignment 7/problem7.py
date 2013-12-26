from itertools import islice
import numpy as np
import matplotlib.pyplot as plt
import pylab

from sklearn.cross_validation import cross_val_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

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
listTrain = list(islice(fileLetter, 1000))
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

svc = SVC(kernel='rbf', random_state=None)
scoreSVC = cross_val_score(svc, trainClean, trainTarget, cv=10)
functionAdd(np.mean(scoreSVC), np.std(scoreSVC))

print "SVC cross-validation score =", format(scores[0], '.2f')

# K-NN classifier

kn = KNeighborsClassifier(weights='distance', n_neighbors=4, \
    algorithm='ball_tree')
scoreKN = cross_val_score(kn, trainClean, trainTarget, cv=10)
functionAdd(np.mean(scoreKN), np.std(scoreKN))

print "K-NN cross-validation score =", format(scores[1], '0.2f')

# Logistic Regression classifier

lr = LogisticRegression()
scoreLR = cross_val_score(lr, trainClean, trainTarget, cv=10)
functionAdd(np.mean(scoreLR), np.std(scoreLR))

print "Logistic Regression cross-validation score =", format(scores[2], '0.2f')

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
# plt.show()

# Logistic Regression performs substantially worse than both SVC and K-NN.
# Both SVC and K-NN perform decently well. 

# Logistic Regression could be performing poorly because it's a linear model.
# If I set kernel='linear' for the SVC classifier, the cross-validation score 
# drops from 0.970875 to 0.8525. While we're on the topic, the SVC classifier
# performs best when the kernel parameter is left unspecified (the parameter
# defaults to kernel='rbf').

# Prediction performance on last 4,000 data entries

print "\nPERFORMANCE:\n------------"

def functionPerformance(model):
	model.fit(trainClean, trainTarget) # fit model according to training data
	print "model accuracy is", model.score(predictClean, predictTarget)
	# gives mean accuracy on test data, labels
	predictedTargets = model.predict(predictClean) # perform classification
	print "Model performance report:\n"
	return classification_report(predictTarget, predictedTargets, \
		target_names=alphabet)

# SVC performance

print "SVC", functionPerformance(svc), '\n', '-'*80, '\n'

# K-NN performance

print "K-NN", functionPerformance(kn), '\n', '-'*80, '\n'

# Logistic Regression performance

print "Logistic Regression", functionPerformance(lr), '\n', '-'*80, '\n'

# SVC model accuracy is 97% 
# K-NN model accuracy is 96%
# LR model accuracy is 71%

# TO DO:

# Cross-Validation
# + [ ] explain model parameters, results
# + [ ] define single cross-validation function that calls each model

# Plotting
# + [ ] fix decimal places in plot labels

# Performance
# + [ ] explain model parameters, results
# + [ ] return accuracy rounded to second decimal place
# + [x] classification_report retuning "None"
# + [ ] bring calls into functionPerformance
