import matplotlib.pyplot as plt
import numpy as np
import csv

#Set pylab formatting parameters
import pylab
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
    # Remove top & right spines
    axes.spines['top'].set_visible(False)
    axes.xaxis.set_ticks_position('bottom')
    axes.spines['right'].set_visible(False)
    axes.yaxis.set_ticks_position('left')

    # Add grid
    axes.grid(which='both', color='0.65', linestyle=':', zorder=0)
    axes.set_axisbelow(True)

def add_labels(titl, ylab, xlab, axes):
    # Add labels
    t = axes.set_title(titl)
    t.set_y(1.03)
    ylab = axes.set_ylabel(ylab, labelpad=7)
    xlab = axes.set_xlabel(xlab, labelpad=15)
    top_height = 0.95-float(len(titl.splitlines()))/20
    plt.subplots_adjust(left=.11, top=top_height, right=.95, bottom=.13)


# -------------------------------------------------------------------------------------
# Part 0: Import, process data

class zipIncidents:
    def __init__(self, filename, labeled):
        data_file = open(filename, 'rU')
        data = csv.reader(data_file)
        next(data, None)
        self.zips, self.pop, self.incid = ([] for x in range(3))
        for line in data:
            self.zips.append(int(float(line[0])))
            self.pop.append(int(float(line[1])))
            if labeled:
                self.incid.append(int(float(line[2])))

l = zipIncidents('labeled_data.csv', True)
u = zipIncidents('unlabeled_data.csv', False)


# -------------------------------------------------------------------------------------
# Part A: Plot the data

# I chose to plot a series of different rough charts to get a quick
# handle on the characteristics of the data.

# First, I started by examining the number of incidents in all
# zipcodes. The majority of zipcodes only reported one incident total.
# There are also a few extremes, with a couple zipcodes reporting 100k
# incidents or more. Most of the remaining zips report incidents in
# the 15k - 70k range.

# "Distribution of Incidents"
ax = plt.subplot(111)
plt.hist(l.incid, 40, color='dimgray', edgecolor='none')
ax.set_xlim([-1000,120000])
ax.set_ylim([0,200])
addgrid_removespines(ax)
add_labels('Distribution of Incidents', 'Zipcode Count', 'Number of Incidents', ax)
plt.savefig('Part A Distribution of Incidents.png', dpi=300)
plt.clf()

# Next, I looked at distribution of population per zip. Most of the
# zips have population between 5k-40k, with one or two having
# populations above 100k.

# "Distrubution of Population"
ax = plt.subplot(111)
plt.hist(l.pop, 40, color='dimgray', edgecolor='none')
ax.set_xlim([-1000,120000])
ax.set_ylim([0,23])
addgrid_removespines(ax)
add_labels('Distribution of Population', 'Zipcode Count', 'Population', ax)
plt.savefig('Part A Distribution of Population.png', dpi=300)
plt.clf()

# Although zipcodes aren't really numeric values, I also plotted a
# histogram of zipcodes. Oddly enough, although 311 is based in the
# city of New York, there are incidents reported in zipcodes outside
# of the city (i.e. >= 11501, with the exception of the 1169_
# zips). In fact, given the quick output from the next line, almost
# half (118 out of 300) zipcodes are from outisde the city.

# print sorted(l.zips).index(11501), len(l.zips)

# "Distribution of Zipcodes"
ax = plt.subplot(111)
plt.hist(l.zips, 40, color='dimgray', edgecolor='none')
ax.set_xlim([9950,15000])
ax.set_ylim([0,45])
addgrid_removespines(ax)
add_labels('Distribution of Zipcodes', 'Zipcode count', 'Zipcodes', ax)
plt.savefig('Part A Distribution of Zipcodes.png', dpi=300)
plt.clf()

# I decided to look closer at these zipcodes outside of the city. I
# plotted a distribution of incidents for these zips, and found that
# most of them had relatively small incident values (50 or less). None
# of them had zero reported incidents, which is probably why they were
# included even though they aren't within city boundaries.

extracity = sorted(zip(l.zips, l.incid), key=lambda x: x[0])[182:]
index_11694 = extracity.index((11694, 16962))
extracity.pop(index_11694)
extracity_zips, extracity_incid = zip(*extracity)

# "Incidents vs extra-city zips"
ax = plt.subplot(111)
plt.plot(extracity_zips, extracity_incid, 'o', color='tomato', mec='none')
ax.set_xlim([11450,15000])
ax.set_ylim([0,50])
addgrid_removespines(ax)
add_labels('Incidents vs extra-city zips', 'Incident count', 'Zipcodes', ax)
plt.savefig('Part A Incidents vs extra-city zips.png', dpi=300)
plt.clf()

# I next chose to understand the basic relationship between some of
# the parameters. I first looked at Incidents vs Population. There is
# some obvious relationship between incidents and population, although
# the significant portion of zipcodes with only one reported incident
# is sure to throw a wrench in fitting this data nicely. Also, a
# notable feature of this plot is that the range of possible incidents
# gets bigger as population grows, resulting in a cone shape.

# Incidents vs. Population"
ax = plt.subplot(111)
plt.plot(l.pop, l.incid, '.', color='tomato', mec='none', alpha=0.7)
ax.set_xlim([-9000,130000])
ax.set_ylim([-4000,130000])
addgrid_removespines(ax)
add_labels('Incidents vs. Population', 'Incident count', 'Population', ax)
plt.savefig('Part A Incidents vs Population.png', dpi=300)
plt.clf()

# Next, again ignoring the question of whether zipcodes can be treated
# as numeric values, I looked at Incidents vs Zipcode. There does seem
# to be some clustering happening around certain values, perhaps
# reflecting the crude geographic approximations of zipcodes -- they
# tend to be around the same number in the same geographic area.

# "Incidents vs. Zipcode"
ax = plt.subplot(111)
plt.plot(l.zips, l.incid, 'o', color='tomato', mec='none')
ax.set_xlim([9900,15000])
ax.set_ylim([-4000,130000])
addgrid_removespines(ax)
add_labels('Incidents vs. Zipcode', 'Incident count', 'Zipcodes', ax)
plt.savefig('Part A Incidents vs Zipcode.png', dpi=300)
plt.clf()

# Finally, I wanted to understand a little more about the low incident
# count zipcodes. I mapped all the NY State zips (using CartoDB) that
# had only one incident. 

oneZips = open('oneZips.csv', 'w')
for line in zip(l.incid, l.zips):
    if line[0] == 1:
        oneZips.write(str(line[1])+'\n')

# <<stuff in CartoDB>>

# Part A One-Incident Zips 1.jpg
# Part A One-Incident Zips 2.jpg

# None of the zipcodes with one incident were located inside New York
# City! But how about zipcodes with more than one incident? I decided
# to look at these as well.

allZips = open('allZips.csv', 'w')
allZips.write('Incidents,Zipcodes\n')
for line in zip(l.incid, l.zips):
    allZips.write(str(line[0]) + ',' + str(line[1]) + '\n')

# <<stuff in CartoDB>>

# Part A Low-Incident Zips 1.jpg (>100 shown in green, <100 shown in orange)
# Part A Low-Incident Zips 2.jpg (>100 shown in green, <100 shown in orange)

# And in fact, there were at most 82 incidents for any zipcode outside
# of New York City. There were at least 702 incidents for zipcodes
# inside the city. This shouldn't be too surprising -- I'm not sure
# why external zipcodes would receive 311 complaints, but we shouldn't
# expect too many for any external zipcode if it exists outside New
# York City.

# This may be justification for ignoring these values completely, as
# their presence is not important to predicting 311 complaints, a
# service provided by the city of New York. OR, incidents for external
# zipcodes should be modeled separately, as they are NOT part of the
# same I.I.D. grouping as zipcodes inside New York.


# ------------------------------------------------------------------------------
# Part B: Cross-validation
print '\nBlind Model\nFor all zips:'

# Create validation/training sets:

def kfolds(num_folds, x_list, y_list):
    num_folds = num_folds
    cv_size = len(x_list)/num_folds
    validation_array = []
    training_array = []

    for x in range(num_folds):
        data = zip(y_list, x_list)
        lower_bound = cv_size * x
        upper_bound = cv_size * (x+1)
        validation_set = data[lower_bound:upper_bound]
        validation_array.append(validation_set)
        training_set = data[:lower_bound]
        training_set.extend(data[upper_bound:])
        training_array.append(training_set)

    return num_folds, cv_size, validation_array, training_array

# Create RMSE & Rsq calculator function:
def RMSE_Rsq_calc(x, y, val_x = None, val_y = None, degree = 0, do_rsq=True):

    # If no validation set, conduct analysis on x & y
    if val_x==None:
        val_x = x
        val_y = y

    # Fit to training set
    coeff = np.polyfit(x, y, degree)

    # Get residuals on validation set
    resid_sq_sum = sum((val_y - np.polyval(coeff,val_x))**2)

    # Calculate RMSE from validation set on training reression
    RMSE = resid_sq_sum/len(val_x)
    RMSE = RMSE**(0.5)

    # Calculate R^2 from validation set on training regression
    if do_rsq:
        validation_avg = sum(val_y)/len(val_y)
        sq_sum_list = [(yi - validation_avg)**2 for yi in val_y]
        total_sq_sum = sum(sq_sum_list)
        Rsq = 1 - (resid_sq_sum/total_sq_sum)
    else:
        Rsq = 0

    return RMSE, Rsq, coeff


# Get RMSE for each degree polynomial:
def validation_calc(degree, do_rsq=True):

    RMSE_list = []
    Rsq_list = []

    for k in range(num_folds):
        
        # Calculate values
        RMSE, Rsq, coeff = RMSE_Rsq_calc(zip(*training_array[k])[1], \
                                         zip(*training_array[k])[0], \
                                         val_x = zip(*validation_array[k])[1], \
                                         val_y = zip(*validation_array[k])[0], \
                                         degree = degree, do_rsq = do_rsq)

        # Add values to total
        Rsq_list.append(Rsq)
        RMSE_list.append(RMSE)

    Rsq_avg = sum(Rsq_list)/num_folds
    RMSE_avg = sum(RMSE_list)/num_folds
    RMSE_std = np.std(RMSE_list)
    return RMSE_avg, Rsq_avg, RMSE_std

# Get RMSE, Rsq, etc. for polynomials of degrees 1-5:
num_folds, cv_size, validation_array, training_array = kfolds(10, l.pop, l.incid)

def poly_degree_iterator(lbound, ubound, full_x, full_y, do_rsq=True):
    results = []
    for deg in range(lbound, ubound+1):
        RMSE, Rsq, RMSE_std = validation_calc(deg, do_rsq=do_rsq)
        RMSE_full, Rsq_full, coeff = RMSE_Rsq_calc(full_x, full_y, degree=deg)
        results.append((deg, RMSE, RMSE_std, RMSE_full, coeff))
        print 'Degree', str(deg) + ':\tVal. RMSE =', RMSE, '\tR^2 =', Rsq, \
              '\tTotal RMSE =', RMSE_full
    return results

results = poly_degree_iterator(1, 5, l.pop, l.incid)

# Output:
# Degree 1:	RMSE = 13707.6037981 	R^2 = 0.19916212028
# Degree 2:	RMSE = 13352.3349636 	R^2 = 0.251992472431
# Degree 3:	RMSE = 13245.73778 	R^2 = 0.258049613549 *****
# Degree 4:	RMSE = 13430.9761598 	R^2 = 0.232364634994
# Degree 5:	RMSE = 13811.9577501 	R^2 = 0.178798541407

# Based on this output, we choose a polynomial of degree 3 as the best-fit.

# I thought it would be useful to plot this polynomial, for comparison
# later with part D.

ax = plt.subplot(111)
plt.plot(l.pop, l.incid, '.', color='red', mec='none', zorder=1, alpha=0.5)

x_vals = np.arange(0, 130000, 100)
y_vals = np.polyval(results[2][4], x_vals)
plt.plot(x_vals, y_vals, '-', color='dimgray', zorder=2)

ax.set_xlim([-9000,130000])
ax.set_ylim([-9000,130000])
addgrid_removespines(ax)
add_labels('Best fit for Part B, Incidents vs. Zipcode Population', 'Incidents', 'Zipcode Population', ax)
plt.savefig('Part B Best Fit.png', dpi=300)
plt.clf()

# Okay, this was a really good idea to plot the model. As a third
# degree polynomial, the prediction actually DECREASES for populations
# above ~130k. This is a huge concern -- if there is a zipcode with a
# population way above the others, this would likely be a very poor
# estimation. It also increases for negative population, although this
# is less of a concern since this isn't possible. This is probably
# a sign of overfitting.


# ------------------------------------------------------------------------------
# Part C: RMSE, R^2 on whole dataset. Then plot results.

# RMSE, R^2, RMSE_std for whole dataset.
plt.bar(zip(*results)[0], zip(*results)[3], width=0.6, color='dimgray', \
        zorder=1, align='center', label='RMSE (Complete Dataset)', ec='none')
plt.bar(zip(*results)[0], zip(*results)[1], width=0.3, color='darkgray', \
        zorder=2, align='edge', label='RMSE (Validation Avg.)', ec='none')
plt.errorbar(zip(*results)[0], zip(*results)[1], yerr=zip(*results)[2], \
             zorder=3, capsize=6, ms=10, elinewidth=1.5, mew=1.5, \
             c='tomato', ecolor = 'tomato', fmt='|', \
             label='RMSE Validation Avg. Error')

# Add formatting
ax = plt.subplot(111)
ax.set_xlim([0.5,5.5])
ax.set_ylim([9000, 19000])
ax.legend(frameon=False, fontsize='small', numpoints=1)
addgrid_removespines(ax)
add_labels('RMSE for polynomials of degree 1 thru 5', 'RMSE (Number of Incidents)', \
           'Degree Polynomial', ax)
plt.savefig('Part C RMSE Calculations.png', dpi=300)
plt.clf()

# The chart shows that total RMSE values continue to drop with
# polynomial degree. This is an example of overfitting. However, it
# also appears that the validation RMSE averages have a high amount of
# variance. It is entirely possible that even though OUR third degree
# polynomial has the lowest validation RMSE, another 10-fold test with
# the same data (broken up in a different manner) may produce a
# different result.

# Notably, I compared these results with Ravi Shroff's results. The
# only difference between our algorithms is that he shuffled the
# dataset before splitting it into 10 folds. I decided not to shuffle
# for this section to see how different my results would be on section D.

# Ravi's R^2 values were dramatically higher than mine. This may point
# to some kind of pre-existing structure in the data that is
# minimizing the R^2 value. If my validation sets are capturing fairly
# similar tuples, then the SStot value will be smaller, and thus my
# R^2 values will be smaller.

# This is an argument for doing more folds, or for doing 10-fold tests
# on randomized versions of the data. Or, since this dataset is fairly
# small, it may not be very expensive to do LOOCV.



# ------------------------------------------------------------------------------
# Part D: RMSE, R^2 on whole dataset. Then plot results.
print '\nFinal OLS model'

# Given my findings above, I will do two things to improve
# prediction. First, I will split the data into two sets: zipcodes
# inside New York, and those outside. I will conduct this split based
# on the number of incidents: choosing the halfway point between the
# external zipcodes and internal zipcodes, this is 400 incidents.

# Based on the argument that zipcodes inside and outside New York are
# not identically distributed, I think this is a valid change in the
# analysis. This will result in two regressions, depending on whether
# the zip is located in New York City or not.

# Second, I will conduct LOOCV rather than 10-fold
# validation. However, since LOOCV is equivalent to K-folds where
# k=len(data), I will use the same algorithm. Notably, with LOOVC the
# order of the data doesn't matter since our validation is only one
# datapoint at a time.


int_incid = []
int_pop = []
ex_incid = []
ex_pop = []

# Split lists by incident count:
for index, incid in enumerate(l.incid):
    if incid > 400:
        int_incid.append(l.incid[index])
        int_pop.append(l.pop[index])
    elif incid <= 400:
        ex_incid.append(l.incid[index])
        ex_pop.append(l.pop[index])
    else:
        print "Error with splitting function."
int_zipct = len(int_incid)
ex_zipct = len(ex_incid)




# Choose model for internal zips:
print 'Model for internal zips:'
num_folds, cv_size, validation_array, training_array = kfolds(int_zipct, \
                                                              int_pop, int_incid)
results = poly_degree_iterator(1, 5, int_pop, int_incid, do_rsq=False)

# Output:
# Degree 1:	Val. RMSE = 8472.4396491 ****
# Degree 2:	Val. RMSE = 8672.4035718
# Degree 3:	Val. RMSE = 8594.88308533
# Degree 4:	Val. RMSE = 8778.96978526
# Degree 5:	Val. RMSE = 9290.47363274

# This new method chose a linear relationship between population and
# incidents, much different than the previous method.

int_coefficients = results[0][4]

ax = plt.subplot(111)
plt.plot(int_pop, int_incid, '.', color='red', mec='none', zorder=1, alpha=0.5)

x_vals = np.arange(0, 130000, 100)
y_vals = np.polyval(int_coefficients, x_vals)
plt.plot(x_vals, y_vals, '-', color='dimgray', zorder=2)

ax.set_xlim([-9000,130000])
ax.set_ylim([0,130000])
addgrid_removespines(ax)
add_labels('Best fit for Part D, Incidents vs. Internal Zipcode Population', 'Incidents', 'Zipcode Population', ax)
plt.savefig('Part D Internal Zips Best Fit.png', dpi=300)
plt.clf()





# Choose model for external zips:
print '\nModel for external zips:'
num_folds, cv_size, validation_array, training_array = kfolds(ex_zipct, \
                                                              ex_pop, ex_incid)
results = poly_degree_iterator(1, 5, ex_pop, ex_incid, do_rsq=False)

# Output:
# Degree 1:	Val. RMSE = 6.03926456046 ***
# Degree 2:	Val. RMSE = 5.806479764  
# Degree 3:	Val. RMSE = 5.85993706641
# Degree 4:	Val. RMSE = 5.77633736935 xxx
# Degree 5:	Val. RMSE = 5.79800360548

# Oddly, the model chose a fourth degree polynomial for external
# zipcodes. I would argue that these zips are so unpredicatable, and
# the counts are so low (there are 64 with only one incident!) that
# they should be ignored. Since the RMSE values are so close to each
# other, I am going to choose degree 1 to prevent possible
# overfitting.

ex_coefficients = results[0][4]

ax = plt.subplot(111)
plt.plot(ex_pop, ex_incid, '.', color='red', mec='none', zorder=1, alpha=0.5)

x_vals = np.arange(0, 70000, 1000)
y_vals = np.polyval(ex_coefficients, x_vals)
plt.plot(x_vals, y_vals, '-', color='dimgray', zorder=2)

ax.set_ylim([-3,85])
addgrid_removespines(ax)
add_labels('Best fit for Part D, Incidents vs. External Zipcode Population', 'Incidents', 'Zipcode Population', ax)
plt.savefig('Part D External Zips Best Fit.png', dpi=300)
plt.clf()


print '\n'


# ------------------------------------------------------------------------------
# Part E: Summary

# Based on the output of the final OLS model, I expect to achieve RMSE
# around 12k on the internal zips. For zips outside of NYC, I don't
# expect a great RMSE but it could be around 10. Without having tested
# on an unlabeled dataset, I'm not sure how these values would
# compare.

# I would try to do a few more things with more
# time/resources/data. Number one -- what do "incidents" mean? At
# first I assumed these were only incidents about other people, but
# it's possible they include reports of broken sewer lines,
# malfunctioning traffic signals, etc. 

# Understanding what constitutes an "incident" really affects the next
# step: looking for more predictor variables. For example, if these
# are largely crime- or people-related incidents, maybe these would
# scale with density -- so understanding the area of a zipcode might
# matter. Even if the many of the incidents aren't people- related,
# there may be significant correlations with data like income and
# distribution of uses (residential vs commerical, for example).

# I'd also guess that the number of incidents in a zip from previous
# years would be a fairly good predictor. Perhaps these would need to
# be normalized every year by the total number of incidents, so that
# they represent fraction of total incidents.

# Finally, I would try to understand the goal of the prediction, and
# the intended audience of the analysis. The external zipcodes really
# throw predictions off. If we only care about incidents from NYC, it
# makes sense to ignore these incidents completely. But answering the
# question "Do external zipcodes matter?" requires knowing who the
# analysis is for.
