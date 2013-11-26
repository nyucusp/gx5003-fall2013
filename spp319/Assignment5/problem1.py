
#Notes/scrap/
import matplotlib.pyplot as plt
import pandas as pd

myfile = pd.read_csv('stocks.dat')

#grab prices, adjust for baseline (using map), then zipto recombine

header = myfile.next

#print header
# savefig to store as a png

#2nd
#convert into a list of datetime
#then create dict of keys of date and values of the number of instances.
# dictionary = pd.DataFrame.from_dict(dictionary, orient = 'index')

#4th
#scatter_matrix for groups of graphstogether
#using matplotlib for transisotr problem, matplot lib discourages y values which are not numeric
#
print "This is not an assignment submission"
