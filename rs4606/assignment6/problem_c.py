import numpy
import matplotlib.pyplot as plt

"""
The lists of values that we'll graph are:
[13519.178949317729, 13247.82770615588, 13164.52846434755, 13405.996537917486, 14109.84815164765]
[1515.2051976713724, 1536.1593441442926, 1662.8911854362129, 1925.7478724867913, 3262.5729874720264]
[13492.142190458173, 13118.850073678655, 12949.022276993384, 12934.207758865856, 12918.056857850648]
The first is the RMSE scores for 10-fold cross validation for a polynomial model of degree 1,2,3,4,5.
The second is the Standard deviation for the computation in the first list, where the deviation is computed over the 10 RMSEs for each fold (see problem_b code).
The third is the RMSE scores for a polynomial model of degree 1,2,3,4,5 trained on *all* the data (without 10-fold cross validation).
"""


RMSE_list_with_cv = numpy.array([13519.178949317729, 13247.82770615588, 13164.52846434755, 13405.996537917486, 14109.84815164765])
RMSE_list_without_cv = numpy.array([13492.142190458173, 13118.850073678655, 12949.022276993384, 12934.207758865856, 12918.056857850648])
RMSE_list_with_cv_stdev = numpy.array([1515.2051976713724, 1536.1593441442926, 1662.8911854362129, 1925.7478724867913, 3262.5729874720264])

#since we're going to display the y values from 11,000 in the graph, we need to scale the stdev error bars
temp_list = ([11000, 11000, 11000, 11000, 11000])
RMSE_scaled_stdevs = RMSE_list_with_cv_stdev*((RMSE_list_with_cv - temp_list)/RMSE_list_with_cv)

#compute Standard Deviation of RMSE_list
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ind = numpy.arange(5)    # the x locations for the groups
width = 0.35       

p1 = plt.bar(ind, RMSE_list_with_cv,   width, color='b', yerr=RMSE_scaled_stdevs, ecolor='r')
p2 = plt.bar(ind, RMSE_list_without_cv, width, color='y')


plt.ylabel('RMSE values')
plt.title('10-fold Cross-Validated RMSE for 311 Labeled Data by Polynomial Model Degree')
plt.xticks(ind+width/2., ('Deg 1', 'Deg 2', 'Deg 3', 'Deg 4', 'Deg 5') )
plt.yticks(numpy.arange(11000,18000,1000))
ax.set_ylim([11000, 18000])
plt.legend( (p1[0], p2[0]), ('with cv', 'without cv'), loc='best' )

plt.show()
