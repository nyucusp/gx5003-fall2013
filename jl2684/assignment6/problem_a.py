import pylab
import csv
import sys
import scipy
import array
from matplotlib import *
from pylab import *
from scipy import *
import numpy as np
#import matplotlib.pyplot as plot
import matplotlib.ticker as mticker 
#from matplotlib import dates 
#import datetime 
from scipy import stats
#import dateutil.parser as dparser
from matplotlib import pyplot as plt
import collections 
import itertools
#from matplotlib.dates import date2num
import matplotlib as mpl 


unlabeled_file = open('unlabeled_data.csv', 'rU')
unlabeled_line = csv.reader(unlabeled_file)

labeled_file = open('labeled_data.csv', 'rU')
labeled_lines = csv.reader(labeled_file)

zip_n_file = open('zip_neigh.csv', 'rU')
z_n_line = csv.reader(zip_n_file)


list_unlabeled = [] 
list_labeled = [] 
list_z_n_line = [] 


for x in unlabeled_line:
	list_unlabeled.append(x)

for x in labeled_lines:
	list_labeled.append(x)

for x in z_n_line:
	list_z_n_line.append(x)

list_unlabeled = list_unlabeled[1:]
list_labeled = list_labeled[1:]
list_z_n_line = list_z_n_line[1:]

list_u_zip = []
list_u_pop = [] 

list_l_zip = []
list_l_pop = [] 
list_l_inc = []

list_ny_zip = [] 

for x in list_unlabeled:
	list_u_zip.append(float(x[0]))
	list_u_pop.append(float(x[1]))

for x in list_labeled:
	list_l_zip.append(float(x[0]))
	list_l_pop.append(float(x[1]))
	list_l_inc.append(float(x[2]))

for y in list_z_n_line:
	list_ny_zip.append(y[2])

list_ny_zip_split = [] 
for x in list_ny_zip:
	list_ny_zip_split.append(x.split(','))

list_ny_zipcode = [] 
for y in list_ny_zip_split:
	for x in y: 
		list_ny_zipcode.append(int(x))



def polyfit(x, y, degree):
    results = {}

    coeffs = np.polyfit(x, y, degree)
     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    correlation = numpy.corrcoef(x, y)[0,1]

     # r
    results['correlation'] = correlation
     # r-squared
    results['determination'] = correlation**2
    return results


pf = polyfit(list_l_pop,list_l_inc, 2)

print pf 







### ZIP VS INCIDENTS SCATTER

plt.scatter(list_l_zip, list_l_inc, 3, color='red', alpha= 0.5, label='Number of Incidents')

plt.legend(loc='upper right', prop={'size':12})
plt.xlabel("Zipcode")
plt.ylabel("Incidents")
plt.title("Zipcode vs. Incidents")
plt.tight_layout()
plt.savefig('Problem A Zipcode vs. Incidents [Scatter].png')
plt.show()


### POP VS INCIDENTS SCATTER

plt.scatter(list_l_pop, list_l_inc, 3, color='blue', alpha= 0.5, label='Number of Incidents')

plt.legend(loc='upper right', prop={'size':12})
plt.xlabel("Population")
plt.ylabel("Incidents")
plt.title("Population vs. Incidents")
plt.tight_layout()
plt.savefig('Problem A Population vs. Incidents [Scatter].png')
plt.show()


### ZIP VS INCIDENTS BAR 

dict_zip_inc = dict(zip(list_l_zip,list_l_inc))
dict_zip_inc_ordered = collections.OrderedDict(sorted(dict_zip_inc.items()))

list_l_inc_ordered = [] 
list_l_zip_ordered = []


for key, value in dict_zip_inc_ordered.iteritems():
	list_l_inc_ordered.append(value)
	list_l_zip_ordered.append(int(key))


d_list = numpy.arange(0,len(list_l_zip_ordered),1)

plt.bar(d_list, list_l_inc_ordered, 1, color='blue', alpha= 0.5, label='Number of Incidents')
plt.legend(loc='upper right', prop={'size':12})
plt.xlabel("Zipcode")
plt.ylabel("Incidents")
plt.title("Zipcode vs. Incidents")

plt.xticks(d_list[::30], list_l_zip_ordered[::30], rotation = -10)
plt.tight_layout()
plt.savefig('Problem A Zipcode vs. Incidents [Bar].png')
plt.grid()
plt.show()



zip_n_file.close
unlabeled_file.close
labeled_file.close 


