#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 6, Exercise a

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


#Creating Problem 1b Figure
def PopIncident(df):

	scatter(df['Population'],df['Incidents'], marker='o')
	title('Population vs 311 Call Incidents')
	xlabel('Population')
	ylabel('# of 311 Call Incidents')
	xlim((min(df['Population'])-3000,max(df['Population']+2000)))
	ylim(min(df['Incidents'])-3000,max(df['Incidents']+3500))
	plt.savefig('6a_Pop_vs_Incident.png', dpi=400)
	clf()

#Creating Problem 1c Figure
def ZipIncident(df):

	df['Incidents'].plot(grid=False, legend=False,kind='bar', color='blue')
	title('Zipcode vs 311 Call Incidents')
	xlabel('Zipcode')
	ylabel('No. of 311 Call Incidents')
	ticks = sorted(zipcode)[::20]
	xticks(np.arange(1,len(zipcode),20),ticks,rotation=35) 
	plt.savefig('6a_Zip_vs_Incident.png', dpi=400)
	clf()

def main():

	zipcode = []
	incidents = []
	pop = []

	with open('labeled_data.csv','r') as myFile:
	    myFile.readline()
	    for line in myFile:
	        zipcode.append(float(line.strip().split(',')[0]))
	        pop.append(float(line.strip().split(',')[1]))
	        incidents.append(float(line.strip().split(',')[2]))
	        
	df = pd.DataFrame({'Zipcode':zipcode, 'Population':pop, 'Incidents':incidents})
	df = df.sort(columns=['Population','Zipcode'])

	PopIncident(df)
	ZipIncident(df)


if __name__ == "__main__":
	main()



