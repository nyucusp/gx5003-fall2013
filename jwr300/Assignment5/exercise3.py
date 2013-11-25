#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 5, Exercise 3
#Dot Plot

import pandas as pd
from scipy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import pylab
from pylab import *
from matplotlib.dates import MonthLocator, DateFormatter, YearLocator
from matplotlib.ticker import FixedLocator, FixedFormatter
from pandas.tools.plotting import scatter_matrix
from numpy import polyval, polyfit

os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin/latex'

#Clearing plot figure and setting pylab formatting pyrameters
clf()
params = {'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 13,
          'xtick.labelsize': 6,
          'ytick.labelsize': 6,
          'xtick.direction': 'out',
          'text.usetex': True}

pylab.rcParams.update(params)

def main():
	processor = []
	year = []
	num_transistor = []
	header = []
	with open('microprocessors.dat','r') as myFile3:
		header = myFile3.readline().strip().split(',')
		
		for line in myFile3:
		    processor.append(line.strip().split(',')[0])
		    year.append(line.strip().split(',')[1])
		    num_transistor.append(log10(int(line.strip().split(',')[2])))
		
	#creating dataframe 
	df3 = pd.DataFrame({str(header[0]):processor, str(header[1]):year, str(header[2]):num_transistor})
	df3['Processor'] = df3['Processor'].map(lambda x: x.rstrip(' processor'))
	df3.sort(['Year of Introduction'], ascending=True, inplace=True)
	df3 = df3.reset_index(drop=False)

	
	fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)

	#setting 1st subplot format
	ax1.plot(df3['Transistors'],range(1,len(df3['Transistors'])+1),'o')
	ticklist = range(1,14)
	ticknums = FixedLocator((range(1,14)))
	ax1.yaxis.set_major_locator(ticknums)
	ticknames = FixedFormatter(df3['Processor'])
	ax1.yaxis.set_major_formatter(ticknames)

	ax1.set_title('Transistors Count (Log Scale)')

	ax1.set_ylim(0,14)
	ax1.spines['top'].set_visible(False)
	ax1.xaxis.set_ticks_position('bottom')
	ax1.spines['right'].set_visible(False)
	ax1.spines['left'].set_visible(False)
	ax1.yaxis.set_ticks_position('none')
	ax1.yaxis.grid(b=True, which='major', linestyle='--')  

	#Setting 2nd subplot format
	ax2.plot(df3['Year of Introduction'],range(1,len(df3['Year of Introduction'])+1),'o')
	ax2.set_ylim(0,14)
	ax2.set_title('Year of Introduction')
	ax2.set_yticklabels(df3['Processor'])
	ax2.spines['top'].set_visible(False)
	ax2.xaxis.set_ticks_position('bottom')
	ax2.spines['right'].set_visible(False)
	ax2.spines['left'].set_visible(False)
	ax2.yaxis.set_ticks_position('none')
	ax2.yaxis.grid(b=True, which='major', linestyle='--')  


	plt.savefig('Problem3.png',dpi=200)


if __name__ == "__main__":
	main()