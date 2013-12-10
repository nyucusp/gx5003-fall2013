#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 6, Exercise b

'''
Build your final OLS model (you can use as many 
predictor variables/features as you want or other 
external data matched by zip code, again be careful 
not to overfit) and submit your predictions for the 
number of incidents on the test data.
'''

import numpy as np


def polynomial_fit(degree, trainx, testx, trainy):

        
        coeffs = np.polyfit(trainx, trainy, degree)
        fit_equation = np.poly1d(coeffs)
        predictions = fit_equation(testx)
        return predictions
    

def main():

    labeled_data = []
    unlabeled_data = []
    poly_degree = 3

    
    with open('labeled_data.csv','r') as myFile:
        myFile.readline()
        for line in myFile:
            line = line.strip().split(",")
            labeled_data.append([float(x) for x in line])
    myFile.close()
    
    train = [i[1] for i in labeled_data] # population
    target = [j[2] for j in labeled_data] # num incidents
    
    X_train = np.squeeze(np.array(train).reshape(len(train),1))
    Y_target = np.squeeze(np.array(target).reshape(len(target),1))
    
    with open('unlabeled_data.csv','r') as myFile2:
        myFile2.readline()
        for line in myFile2:
            line = line.strip().split(",")
            unlabeled_data.append([float(x) for x in line])
    myFile2.close()
    
    test = [i[1] for i in unlabeled_data] # population
    zipcode = [i[0] for i in unlabeled_data] # zipcode
    
    X_test = np.squeeze(np.array(test).reshape(len(test),1))
    
    predictions = polynomial_fit(poly_degree,X_train, X_test,Y_target)
    incidents_predictions = zip(zipcode,test,predictions)
    
    outputFile = open('partd_predictions.txt', 'w')
    
    for item in incidents_predictions:
        outputFile.write("%0.f, %0.f, %0.f \n" % (item[0], item[1], item[2]))
    
    outputFile.close()

if __name__ == "__main__":
    main()