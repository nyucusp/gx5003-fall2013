# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:19:47 2013

@author: yilong
"""


from math import *
from numpy import *
path=""

#Read The Data
import csv



def alphabet_to_array(labels):#turn alphabet label into an array
    alphabet=[i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    arraylabel=zeros((len(labels),26))

    for i in range(len(labels)):
        #print labels[i],alphabet.index(labels[i])
        arraylabel[i][alphabet.index(labels[i])]=1
    return arraylabel


def number_to_alphabet(n):#turn alphabet label into an array
    alphastr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphastr[n]



def Sigmoid(z):
    return 1.0 / (1.0 + exp(-z))


def CostFun(realtheta,*args):
    theta=realtheta.copy()
    X,y,lamb=args
    m = float(len(y)) # number of training samples
    y.shape=(m,1)

    
    theta.shape=(17,1)

    z=X.dot(theta)
    
    h=Sigmoid(z)
    theta=realtheta.copy()
    theta[0]=0
    Cost=(1.0/m)*sum((-y*log(h)-(1-y)*log(1-h)))+lamb/(2.0*m)*sum(theta.T*theta)


    return Cost

def GradFun(realtheta,*args):
    theta=realtheta.copy()
    X,y,lamb=args
    m =float(len(y)) # number of training samples
    y.shape=(m,1)


    theta.shape=(17,1)    
    z=X.dot(theta)

    theta[0]=0    
    h=Sigmoid(z)

    beta=h-y
    grad=(1.0/m)*(X.T.dot(beta))+lamb/m*theta

    
    return grad.flatten()
    
from scipy.optimize import fmin_cg

def neural_network(X, y, num_labels, lamb):
    m = X.shape[0]
    n = X.shape[1]
    #return the following variables correctly 
    all_theta = zeros((num_labels, n + 1));

    # Add ones to the X data matrix
    
    X =vstack((ones(m),X.T)).T

    # Set options for fminunc
    #options = optimset('GradObj', 'on', 'MaxIter', 50);


    for i in range(num_labels):#26 optimal beta vectors should be found to predict 26 labels
        # Set Initial theta as random number
        initial_theta = rand(n + 1)-0.5

        #print "Initial Theta",initial_theta.shape

        yi=array([line[i] for line in y])
        args=(X,yi,lamb)

        #Conjucated Gradient Optimazing Method
        print "Training for \"",number_to_alphabet(i),"\""

        temptheta=fmin_cg(CostFun,initial_theta.flatten(),fprime=GradFun,args=args,disp=True)#shape=17,1
        all_theta[i]=temptheta.T

    return all_theta



# ================ Training  ================
print "\n\n================ Training  ================\n"

print 'Loading and Visualizing Data ...'
count=0;traindata=[];trainlabel=[];testdata=[];testlabel=[]
with open(path+"letter-recognition.data.txt", 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if count<16000:
            trainlabel.append(row[0])
            traindata.append(array([int(i) for i in row[1:]]))
        else:
            testlabel.append(row[0])
            testdata.append(array([int(i) for i in row[1:]]))
        count+=1
        
traindata=array(traindata);testdata=array(testdata)
print "traindata.shape","testdata.shape"
print traindata.shape,testdata.shape

#preparing the labeled data for training
trainlabel2=trainlabel
trainlabel=alphabet_to_array(trainlabel)

print "trainlabel.shape"
print trainlabel.shape

# Setup the parameters
input_layer_size  = 16;  
num_labels = 26;          # 26 labels, from A to Z

m = size(traindata, 1);#number of the training samples


#
lamb = 0.1
trained_theta = neural_network(traindata, trainlabel, num_labels, lamb);
print trained_theta


print "Training over 16000 samples have finished."

# ================ Predict  ================

print "\n\n================ Predict  ================\n"

print "Prediting using the trainned Result"

def predict(theta,data):
    m=data.shape[0]
    data =vstack((ones(m),data.T)).T

    h=Sigmoid(data.dot(theta.T))

    p=[]
    for i in h:
        li=list(i)
        p.append(number_to_alphabet(li.index(max(li))))
    return p
    
    
pred = predict(trained_theta, traindata);
total=len(traindata);count=0
for i in range(total):
    if pred[i]==trainlabel2[i]:
        count+=1

print 'Training Set Accuracy: ', float(count)/total*100,"%"

    
pred = predict(trained_theta, testdata);
total=len(testdata);count=0
for i in range(total):
    if pred[i]==testlabel[i]:
        count+=1

print 'Testing Set Accuracy: ', float(count)/total*100,"%"

