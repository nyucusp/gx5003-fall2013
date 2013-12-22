import numpy as np
import cv2
from sklearn.cross_validation import train_test_split
from sklearn import svm


# import data (I downloaded the 'letter-recognition.data' from UCI website,
# but the last row in the dataset had only 12 columns so that I just deleted the last row.
# Please use the submitted 'letter-recognition.data' when you run my code.
data = np.loadtxt('letter-recognition.data', np.float32, delimiter=',', converters={ 0 : lambda ch : ord(ch)-ord('A') })

#in the dataset, numeric values are x variables and letter is y variable. 
x, y = data[:,1:], data[:,0]

# Split matrice into random train and test subsets to make the proportion of train size as 16K/20K*100 = 80% (0.8) and test size 0.2
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

samples = xtrain
responses = ytrain

# 10-fold Cross-validation % accuracy on the first 16K samples from Decision Tree
model0=cv2.RTrees()
sample_n, var_n = samples.shape
var_types = np.array([cv2.CV_VAR_NUMERICAL] * var_n + [cv2.CV_VAR_CATEGORICAL], np.uint8)
params = dict(max_depth=10,cv_folds=10 )
model0.train(samples, cv2.CV_ROW_SAMPLE, responses, varType = var_types, params = params)
result0=np.float32( [model0.predict(s) for s in samples] )
print ("Accuracy of Decision Tree: %0.2f (+/- %0.2f)" % (result0.mean(), result0.std() * 2))

# 10-fold Cross-validation % accuracy on the first 16K samples from K-Nearest Neighbor
model1 = cv2.KNearest()
retval = model1.train(samples,responses)
retval, results1, neigh_resp, dists = model1.find_nearest(samples, k = 10)
result1= results1.ravel()
print ("Accuracy of K-Nearest Neighbor: %0.2f (+/- %0.2f)" % (result1.mean(), result1.std() * 2))

# 10-fold Cross-validation % accuracy on the first 16K samples from SVM
model2 = cv2.SVM()
params = dict( kernel_type = cv2.SVM_LINEAR,svm_type = cv2.SVM_C_SVC,C = 1,k_fold=10 )
model2.train(samples, responses, params = params)
result2 = np.float32( [model2.predict(s) for s in samples] )
print ("Accuracy of SVM: %0.2f (+/- %0.2f)" % (result2.mean(), result2.std() * 2))

# K-Nearest Neighbor gives the smallest standard deviation,
# so I use the model for re-train on all 16K samples to predict on the remaining
# 4K test set and report the accuracy

model3 = cv2.KNearest()
retval = model3.train(xtest , ytest)
retval, results3, neigh_resp, dists = model3.find_nearest(xtrain, k = 10)
result3= results3.ravel()
print ("Re-Train: Accuracy of K-nearest Neighbor: %0.2f (+/- %0.2f)" % (result3.mean(), result3.std() * 2))

# calculate F1 score

clf = svm.SVC(kernel='linear', C=1).fit(xtrain, ytrain)
F1 = clf.score(xtest, ytest)
print F1

