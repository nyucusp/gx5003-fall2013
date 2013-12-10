import sys
import numpy
import math
import matplotlib.pyplot as plt
from sklearn import cross_validation, linear_model, datasets
from random import shuffle


"""
First we open the training data file and save the lines to the list input_lines
"""

inputfile = open('labeled_data.csv', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()




"""
Next we open the file boroughs.csv from assignments 2 and 4, and save the set of boroughs
as boroughs_set.  We assume all these boroughs are in NYC.
"""
inputfile1 = open('boroughs.csv', 'r')

input_lines1 = []
for line in inputfile1:
    input_lines1.append(line)
inputfile1.close()

boroughs_list = []
for elt in input_lines1:
    boroughs_list.append(elt[0:5])
boroughs_set = set(boroughs_list)


"""
Now we'll divide our training data into two sets that correspond to zip codes in NYC
and zip codes outside NYC.  We'll call the predictor variable for NYC pop_list_NYC and
the target variable inc_list_NYC, and the other variables lists will be pop_list_outside
and inc_list_outside.
"""

#creating the two predictor variable lists.
pop_list_NYC = []
pop_list_outside = []
for i in range(1,len(input_lines)):
    if str(int(float(input_lines[i].split(',')[0]))) in boroughs_set:
        pop_list_NYC.append(float(input_lines[i].split(',')[1]))
    else:
        pop_list_outside.append(float(input_lines[i].split(',')[1]))

#creating the two target variable lists.
inc_list_NYC = []
inc_list_outside = []
for i in range(1,len(input_lines)):
    if str(int(float(input_lines[i].split(',')[0]))) in boroughs_set:
        inc_list_NYC.append(float(input_lines[i].split(',')[2]))
    else:
        inc_list_outside.append(float(input_lines[i].split(',')[2]))


"""
Now we set up our models and cross-validation and figure out RMSE and R^2 scores for 
OLS.  We leave out some comments as the code is identical to that in problem_b.py
"""
#Setting up the NYC model with 10 folds
cv = cross_validation.KFold(len(inc_list_NYC), n_folds=10, shuffle=True)
pop_array_NYC = numpy.array(pop_list_NYC)
inc_array_NYC = numpy.array(inc_list_NYC)

RMSE_scores_NYC = []
R2_scores_NYC = []
for i in range(1, 6):
    RMSE_list = []
    R2_list = []
    for train, test in cv:
        train_poly = numpy.polyfit(pop_array_NYC[train], inc_array_NYC[train], i)        
        test_y_vals = numpy.polyval(train_poly, pop_array_NYC[test])
        rmse = (((test_y_vals - inc_array_NYC[test]) ** 2).mean(axis=None))**.5
        RMSE_list.append(rmse)
        
        #compute R^2 for this fold and this model
        y_avg = sum(inc_array_NYC[test])/len(inc_array_NYC[test])
        y_avg_list = []
        for j in range(0, len(inc_array_NYC[test])):
            y_avg_list.append(y_avg)
        SS_res = sum((test_y_vals - inc_array_NYC[test])**2)
        SS_tot = sum((inc_array_NYC[test] - y_avg_list)**2)
        R2_list.append(1-(SS_res/SS_tot))
    
    RMSE_scores_NYC.append(sum(RMSE_list)/len(RMSE_list))
    R2_scores_NYC.append(sum(R2_list)/len(R2_list))

#Setting up the outside model with 10 folds
cv = cross_validation.KFold(len(inc_list_outside), n_folds=10, shuffle=True)
pop_array_outside = numpy.array(pop_list_outside)
inc_array_outside = numpy.array(inc_list_outside)

RMSE_scores_outside = []
R2_scores_outside = []
for i in range(1, 6):
    RMSE_list = []
    R2_list = []
    for train, test in cv:
        train_poly = numpy.polyfit(pop_array_outside[train], inc_array_outside[train], i)        
        test_y_vals = numpy.polyval(train_poly, pop_array_outside[test])
        rmse = (((test_y_vals - inc_array_outside[test]) ** 2).mean(axis=None))**.5
        RMSE_list.append(rmse)
        
        #compute R^2 for this fold and this model
        y_avg = sum(inc_array_outside[test])/len(inc_array_outside[test])
        y_avg_list = []
        for j in range(0, len(inc_array_outside[test])):
            y_avg_list.append(y_avg)
        SS_res = sum((test_y_vals - inc_array_outside[test])**2)
        SS_tot = sum((inc_array_outside[test] - y_avg_list)**2)
        R2_list.append(1-(SS_res/SS_tot))
    
    RMSE_scores_outside.append(sum(RMSE_list)/len(RMSE_list))
    R2_scores_outside.append(sum(R2_list)/len(R2_list))


"""
Based on these scores we choose the *linear* model (polynomial degree 1) for the NYC 
zip codes (minimize RMSE and maximize R^2) and the *quadratic* model (polynomial degree
2) for the outside NYC zip codes (minimize RMSE, since R^2 is negative here).
"""
#now we train our models on the entire data sets.  This will give our FINAL OLS model.
train_poly_NYC = numpy.polyfit(pop_array_NYC, inc_array_NYC, 1)
train_poly_outside = numpy.polyfit(pop_array_outside, inc_array_outside, 2)



"""
Finally, we see how our models do on the unlabeled data!  Note that much of the code in this
section is devoted to awkwardly reassembling the predicted incident counts, zip codes, and populations
into a list which is in the same order as our original file 'unlabeled_data.csv'.
"""
inputfile2 = open('unlabeled_data.csv', 'r')

input_lines2 = []
for line in inputfile2:
    input_lines2.append(line)
inputfile2.close()

#here we split the populations into those from zip codes in NYC and those outside.  We keep track
#of the original index from input_lines2 for ease of recombining everything at the end.
real_nyc_pop_indexed = []
real_outside_pop_indexed = []
for i in range(1, len(input_lines2)):
    if str(int(float(input_lines2[i].split(',')[0]))) in boroughs_set:
        real_nyc_pop_indexed.append([float(input_lines2[i].split(',')[1]),i, 0])
    else:
        real_outside_pop_indexed.append([float(input_lines2[i].split(',')[1]),i, 0])

#here we remove the index from real_nyc_pop_indexed and its counterpart, so we can give it to polyval.
real_nyc_pop = []
real_outside_pop = []
for elt in real_nyc_pop_indexed:
    real_nyc_pop.append(elt[0])
for elt in real_outside_pop_indexed:
    real_outside_pop.append(elt[0])

#here we get the actual predicted values.
test_nyc_inc = numpy.polyval(train_poly_NYC, real_nyc_pop)
test_outside_inc = numpy.polyval(train_poly_outside, real_outside_pop)

#here is the first step to reassembling the list input_lines2, but now with predicted incident counts
for i in range(0,len(real_nyc_pop_indexed)):
    real_nyc_pop_indexed[i][2] = test_nyc_inc[i]
for i in range(0, len(real_outside_pop_indexed)):
    real_outside_pop_indexed[i][2] = test_outside_inc[i]

#this list is in the same order as input_lines2, and each entry consists of [pop, index, incident_count]
final_output_list = []
for i in range(1, len(input_lines2)):
    for elt in real_nyc_pop_indexed:
        if elt[1] == i:
            final_output_list.append(elt)
    for elt in real_outside_pop_indexed:
        if elt[1] == i:
            final_output_list.append(elt)


"""
Write our results to file.
"""
outputFile = open('test_data_predictions.txt', 'w')
for i in range(1, len(input_lines2)):
    outputFile.write("%s, %s, %s \n" % (input_lines2[i].split(',')[0], final_output_list[i-1][0], math.ceil(final_output_list[i-1][2])))
outputFile.close()
