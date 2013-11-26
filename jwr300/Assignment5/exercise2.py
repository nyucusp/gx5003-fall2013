#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 5, Exercise 2
#Histogram

import pandas as pd
from scipy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import pylab
from pylab import *
from matplotlib.dates import MonthLocator, DateFormatter
from collections import Counter
from dateutil.parser import parse

os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin/latex'

clf()
params = {'axes.labelsize': 12,
          'text.fontsize': 12,
          'legend.fontsize': 13,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12,
          'xtick.direction': 'out',
          'text.usetex': True}

pylab.rcParams.update(params)

def main():

	actions = []
	with open('actions-fall-2007.dat','r') as myFile2:
	    myFile2.readline()
	    for line in myFile2:
	        actions.append(parse(str(line.strip().split()[0]+" "+line.strip().split()[1])))

	actions_byday = []
	for item in actions:
	    actions_byday.append(item.strftime("%m-%d"))

	actions_dict = Counter(actions_byday)

	df2 = pd.DataFrame.from_dict(actions_dict, orient='index')
	df2.columns = ['Timestamp']

	df2 = df2.sort()


	ax = df2.plot(kind='bar', grid=False, legend=False)
	ax.xaxis.set_major_locator(MonthLocator())
	ax.xaxis.set_major_formatter(DateFormatter('%B'))
	xlabel('Date')

	ax.text(0.5, 1.06, 'Histogram of Actions',
         horizontalalignment='center',
         fontsize=16,
         transform = ax.transAxes)
	ax.set_ylabel('No. of Actions')


	ax.vlines(x = 9, ymin = 0, ymax = 14000,\
	linestyles = 'dashed', colors='k', label='Assignments 0,1')
	ax.annotate('Assigns 0,1', xy=(10,14010))

	ax.vlines(x = 24, ymin = 0, ymax = 14000,\
	linestyles = 'dashed', colors='k', label='Assignment 2')
	ax.annotate('Assign 2', xy=(25,14010))

	ax.vlines(x = 35, ymin = 0, ymax = 14000,\
	linestyles = 'dashed', colors='k', label='Assignments 3')
	ax.annotate('Assign 3', xy=(36,14010))

	ax.vlines(x = 53, ymin = 0, ymax = 14000,\
	linestyles = 'dashed', colors='k', label='Assignments 4')
	ax.annotate('Assign 4', xy=(49,14010))

	ax.vlines(x = 67, ymin = 0, ymax = 14000,\
	linestyles = 'dashed', colors='k', label='Assignments 5')
	ax.annotate('Assign 5', xy=(66,14010))

	ax.vlines(x = 63, ymin = 0, ymax = 14000,\
	linestyles = 'dashed', colors='k', label='Assignments 6')
	ax.annotate('Assign 6', xy=(59,14010))

	plt.savefig('Problem2.png', dpi=400)


if __name__ == "__main__":
	main()

