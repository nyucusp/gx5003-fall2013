#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 5, Exercise 1
#Principles of plotting and connected symbols plot

import pandas as pd
from scipy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import pylab
from pylab import *

os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin/latex'

clf()
params = {'axes.labelsize': 16,
          'text.fontsize': 14,
          'legend.fontsize': 16,
          'xtick.labelsize': 14,
          'ytick.labelsize': 16,
          'text.usetex': True}

pylab.rcParams.update(params)

#Creating Problem 1a Figure
def Problem1a(df):

	df['AAPL'].plot(marker='o',ms=8,ls='-')
	title('Problem1a')
	ylabel('Stock Price')
	legend(loc=2,frameon=False)
	xlabel('Date')
	xticks(ha='left')

	savefig('Problem1a.png', dpi=400)
	clf()

#Creating Problem 1b Figure
def Problem1b(df):

	df['AAPL Ret'].cumsum().plot(marker='o',ms=8,ls='-')
	df['MSFT Ret'].cumsum().plot(marker='o',ms=8,ls='-')
	title('Problem1b')
	ylabel('Log Returns')
	legend(loc=2,frameon=False)
	xlabel('Date')
	xticks(ha='left')

	plt.savefig('Problem1b.png', dpi=400)
	clf()

#Creating Problem 1c Figure
def Problem1c(df):

	subplot(211)
	df['AAPL Ret'].plot(marker='o',ms=8,ls='-')
	title('Problem 1c')
	ylabel('Log Returns')
	legend(loc=3,frameon=False)
	xticks(ha='left')


	subplot(212)
	df['MSFT Ret'].plot(marker='o',ms=8,ls='-', c='green')
	legend(loc=1,frameon=False)
	ylabel('Log Returns')
	xlabel('Date')
	xticks(ha='left')


	plt.savefig('Problem1c.png', dpi=400)
	clf()

def main():


	date = []
	aapl = []
	msft = []

	with open('stocks.dat','r') as myFile:
	    myFile.readline()
	    for line in myFile:
	        date.append(line.strip().split(',')[0])
	        aapl.append(float(line.strip().split(',')[1]))
	        msft.append(float(line.strip().split(',')[2]))

	df = pd.DataFrame({'AAPL':aapl, 'MSFT':msft}, index=date)
	df = df.sort()
	df['AAPL Ret']=log(df['AAPL']/df['AAPL'].shift(1))
	df['MSFT Ret']=log(df['MSFT']/df['MSFT'].shift(1))
	df['AAPL Ret']['2006-01'] = 0
	df['MSFT Ret']['2006-01'] = 0

	Problem1a(df)
	Problem1b(df)
	Problem1c(df)




if __name__ == "__main__":
	main()


