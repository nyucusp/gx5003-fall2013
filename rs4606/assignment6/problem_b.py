import sys
import numpy
import matplotlib.pyplot as plt
from sklearn import cross_validation, linear_model, datasets
from random import shuffle


"""
First we open the text file and save the lines to the list input_lines
"""

inputfile = open('labeled_data.csv', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()

#this is our predictor variable
pop_list = []
for i in range(1,len(input_lines)):
    pop_list.append(float(input_lines[i].split(',')[1]))

#this is our target variable
inc_list = []
for i in range(1, len(input_lines)):
    inc_list.append(float(input_lines[i].split(',')[2]))



"""
Now we set up our models and cross-validation and figure out RMSE and R^2 scores for 
OLS.  We also compute the Standard Deviation for RMSE (across the 10 folds), for use in
problem c.
"""
cv = cross_validation.KFold(len(inc_list), n_folds=10, shuffle=True)
pop_array = numpy.array(pop_list)
inc_array = numpy.array(inc_list)


RMSE_scores = []
R2_scores = []
RMSE_Std_scores = []
for i in range(1, 6):
    #these two lists will contain the 10 RMSE and R^2 values for each fold in model i
    RMSE_list = []
    R2_list = []
    
    for train, test in cv:
        #this fits a polynomial of order i to the training data
        train_poly = numpy.polyfit(pop_array[train], inc_array[train], i)        
        
        #this calculates the predicted values of the above poly on the test data
        test_y_vals = numpy.polyval(train_poly, pop_array[test])
        
        #compute rmse for this fold and this model
        rmse = (((test_y_vals - inc_array[test]) ** 2).mean(axis=None))**.5
        RMSE_list.append(rmse)
        
        #compute R^2 for this fold and this model
        y_avg = sum(inc_array[test])/len(inc_array[test])
        y_avg_list = []
        for j in range(0, len(inc_array[test])):
            y_avg_list.append(y_avg)
        SS_res = sum((test_y_vals - inc_array[test])**2)
        SS_tot = sum((inc_array[test] - y_avg_list)**2)
        R2_list.append(1-(SS_res/SS_tot))
    
        
        
    #now we average the values of RMSE_list and R2_list to get the final values for model i
    
    RMSE_scores.append(sum(RMSE_list)/len(RMSE_list))
    R2_scores.append(sum(R2_list)/len(R2_list))

    #here we compute the standard deviation of the values in RMSE_list.
    stdev = numpy.std(RMSE_list)
    RMSE_Std_scores.append(stdev)



"""
We find that [13372.764077424241, 13161.000496501243, 12978.143321384781, 13031.820885445572, 13365.200489293336]
is (a) list of RMSE_scores, and 
[0.56809724987946708, 0.58382961283776169, 0.59625876247195664, 0.59331017996281132, 0.5729441493561932]
is the corresponding list of R2_scores.  We can see that the degree 3 polynomial model has lowest RMSE, and also
lowest R2 score.  Hence we choose this as our model.  Note that although these results are pretty
consistent over multiple runs of the program, occasionally we get different results for which
model has highest R2 scores...
"""


"""
Now, also in preparation for problem c, we compute the RMSE values on *all* training data
for each model.
"""

RMSE_all_data = []
for i in range(1, 6):
    train_poly = numpy.polyfit(pop_array, inc_array, i)        
    test_y_vals = numpy.polyval(train_poly, pop_array)
    rmse = (((test_y_vals - inc_array) ** 2).mean(axis=None))**.5
    RMSE_all_data.append(rmse)

"""
Finally, we print everything we need for problem c
"""
print RMSE_scores
print R2_scores
print RMSE_Std_scores
print RMSE_all_data

"""
The values that we get from the above command are:
[13519.178949317729, 13247.82770615588, 13164.52846434755, 13405.996537917486, 14109.84815164765]
[0.56200736370308402, 0.5765497421094764, 0.57975713468038703, 0.56402979331596381, 0.51125609417622575]
[1515.2051976713724, 1536.1593441442926, 1662.8911854362129, 1925.7478724867913, 3262.5729874720264]
[13492.142190458173, 13118.850073678655, 12949.022276993384, 12934.207758865856, 12918.056857850648]
and we'll just manually import this data (except the R^2 scores) into the python code for 
problem c and graph this.
"""
