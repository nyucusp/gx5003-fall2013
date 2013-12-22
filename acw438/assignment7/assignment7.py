# Alex Chohlas-Wood, Assignment 7.

# ----------------------------------------------------------------------------
# Initial setup

from itertools import islice
import numpy as np
import matplotlib.pyplot as plt
import pylab

from sklearn.decomposition import PCA
from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

params = {'axes.labelsize': 11,
          'text.fontsize': 13,
          'legend.fontsize': 13,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12,
          'text.usetex': True, 
          'font.family': 'serif',
          'font.serif': ['Palatino']}
pylab.rcParams.update(params)

#Create formatting functions:
def addgrid_removespines(axes):
    # Remove all spines
    axes.spines['top'].set_visible(False)
    axes.xaxis.set_ticks_position('bottom')
    axes.spines['right'].set_visible(False)
    axes.yaxis.set_ticks_position('left')
    axes.spines['left'].set_visible(False)
    axes.spines['bottom'].set_visible(False)

def add_labels(titl, ylab, xlab, axes):
    # Add labels
    t = axes.set_title(titl)
    t.set_y(1.03)
    ylab = axes.set_ylabel(ylab, labelpad=7)
    xlab = axes.set_xlabel(xlab, labelpad=15)
    top_height = 0.95-float(len(titl.splitlines()))/20
    plt.subplots_adjust(left=0, top=top_height, right=1, bottom=0.1)



# ----------------------------------------------------------------------------
# Import, format data

letter_file = open('letter-recognition.data', 'rU')
training_list = list(islice(letter_file, 16000))
prediction_list = list(letter_file)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = {}
for index, letter in enumerate(alphabet):
    alphanum[letter] = index

def data_cleaner(sample_list):
    clean_data = []
    targets = []
    for line in sample_list:
        clean_line = line.split(',')
        targets.append(alphanum[clean_line.pop(0)])
        clean_line[-1] = clean_line[-1].strip('\n')
        int_line = [int(x) for x in clean_line]
        #print int_line
        clean_data.append(int_line)
    return clean_data, targets

clean_training, targets_training = data_cleaner(training_list)
clean_predict, targets_predict = data_cleaner(prediction_list)

targets_training = np.array(targets_training)
targets_predict = np.array(targets_predict)



# ----------------------------------------------------------------------------
# Cross-Validation to select most appropriate model from first 16,000 entries

pca = PCA(n_components='mle')
pca_data = pca.fit_transform(clean_training)

scores = []
stdev = []

def addtolist(mean, variance):
    scores.append(mean)
    stdev.append(variance)


# Decision Tree Classifier
dt = DecisionTreeClassifier()
dt_score = cross_val_score(dt, clean_training, targets_training, cv=10)
addtolist(np.mean(dt_score), np.std(dt_score))
print "Decision Tree done."


# K-NN Classifier
kn = KNeighborsClassifier(weights='distance', n_neighbors=4, \
                          algorithm='ball_tree')
kn_score = cross_val_score(kn, clean_training, targets_training, cv=10)
addtolist(np.mean(kn_score), np.std(kn_score))
# This was my way of finding the best parameters for k-nn:
    # for x in [x*5 for x in range(1,10)]:
    #     kn = KNeighborsClassifier(weights='distance', n_neighbors=4, \
        #                               algorithm='ball_tree', leaf_size=x)
    #     kn_score = cross_val_score(kn, clean_data, targets, cv=10)
    #     print np.mean(kn_score), np.std(kn_score)
    #     print x, "neighbors.", '\n'
print "K-NN done."


# Logistic Regression
lr = LogisticRegression()
lr_score = cross_val_score(lr, clean_training, targets_training, cv=10)
addtolist(np.mean(lr_score), np.std(lr_score))
print "Logistic Regression done."



# ----------------------------------------------------------------------------
# Plot results of cross-validation

labels = ["Decision Tree", "K-Nearest neighbors", "Logistic Regression"]
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
ax.set_ylim([0.69, 0.97])
addgrid_removespines(ax)
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
add_labels("10-Fold Cross Validation Accuracy", "", "", ax)
pylab.xticks([0,1,2], labels)

plt.savefig('CV for 3 Classification Methods.png', dpi=300)

# Clearly, the k-nn model does a much better job of classifying than
# the other models do. The documentation describes the data like so:

    # "The character images were based on 20 different fonts and each
    # letter within these 20 fonts was randomly distorted to produce a
    # file of 20,000 unique stimuli."

# Since we are dealing with 20 different fonts, it's possible that a
# decision-tree model or logistic regression wouldn't do a good job of
# classifying the data. Letters in different fonts could have starkly
# different appearances, and so it might be hard for these models to
# make a uniform declaration about what an A looks like.

# On the other hand, k-nn's simplicity prevents it from trying to
# generalize for all A's. We just look at the nearest 4 neighbors in
# the training set and see what label they predict. This allows for
# markedly different appearances to predict the same letter.

# On another note, the algorithms used here are still a little opaque
# to me. For example, I tried using PCA on the predictor variables --
# I thought it would help the algorithms parse out the most important
# information. But it didn't seem to help. Also, I wasn't able to
# tweak the Decision Tree model to perform any better than it did
# automatically; however, I was able to bring up the k-nn score by a
# percentage point or two just by tweaking the parameters. I'm sure
# that more practice and study of the algorithms will help me better
# understand what's going on.


# ----------------------------------------------------------------------------
# Predictions on final 4,000 entries

print "\nPREDICTIONS:"
kn = KNeighborsClassifier(weights='distance', n_neighbors=4, \
                          algorithm='ball_tree')

kn.fit(clean_training, targets_training)
print "Accuracy for k-nn model is", kn.score(clean_predict, targets_predict), \
    '\n'

count_actual = 0
count_predicted = 0
type_1 = 0
type_2 = 0

targets_predicted = kn.predict(clean_predict)
for line in zip(targets_predict, targets_predicted):
    if line[0] == 0:
        count_actual += 1
        if line[0] != line[1]:
            type_2 += 1
    if line[1] == 0:
        count_predicted += 1
        if line[0] != line[1]:
            type_1 += 1

precision = float(count_predicted - type_1)/count_predicted
recall = float(count_actual - type_2)/count_actual
print "Total predicted A's:", count_predicted
print "Total actual A's:", count_actual
print "Type 1 Errors:", type_1
print "Type 2 Errors:", type_2, '\n'
print 'Precision:', precision
print 'Recall:', recall, '\n'

f1_score = 2*precision*recall/(precision+recall)
print 'F1 score:', f1_score

# Using the k-nn method I was able to get a reasonable accuracy for
# the last 4,000 entries: 95.755%, and an F1 score of 0.987.

# For the A's, there were two type 1 errors and two type 2 errors, out
# of 156 actual A's. I'm guessing that the F1 score is fairly high,
# but not sure what an acceptable score would be. 

# While almost 96% accuracy sounded at first like a decent score, it's
# worth noting that it still misses roughly 1 out of every 25
# letters. In an application setting, I can imagine this accuracy
# score being still too low. For example, if this algorithm were used
# for OCR, it would require a significant amount of editing after the
# OCR was completed, which might be almost as slow as just typing
# something out by hand.

# One potential way to improve this score would be to generate more
# metrics from the original letter images, although there is probably
# a limit on what kind of metrics are useful. Another would be to have
# a bigger training dataset, so that a k-nn model have even more
# training sample points to choose from.
