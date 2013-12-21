# Exercise 1: Principles of plotting and connected symbols plot, generated after group tutoring session

import pandas #use of Pandas approved by email from Fabio on November 20. The point is to leverage indexing and DataFrame objects in such problems.
import matplotlib.pyplot as pplt

#Reading in the file with read_csv takes a .csv as input and returns a pandas DataFrame. This is one of the main advantages.
#This is because the stocks.dat files contains column headers, which means pandas automatically labels the indexes.
stocks = pandas.read_csv('stocks.dat') 


#(a) Generate a simple connected symbol plot for all Apple's stock quotes in the file stocks.dat.

#Generating a simple connected symbol plot indicates the discrete nature of data points, meaning it is not a continuous plot
#Gridlines make the graph "reader friendly"
#Below is setting the index, generating the plot, and saving the plot
stockApple = stocks[['month','apple']]
stockApple.columns = ['Monthly Snapshots (Jan, 2006 - Sep, 2008)', 'Apple']
appleplot = stockApple.set_index('Monthly Snapshots (Jan, 2006 - Sep, 2008)').sort_index().plot(style='o--',ylim=[50,210],title="1a - Apple Stock Prices",legend=False)
pplt.savefig('Problem_1a.png') # To save the output as .png file. 


#(b) Using the quote of January 2006 as a baseline, directly compare the progress of Apple's and Microsoft's stock price.

#Using Jan 2006 prices as baseline means subtracting them from all others to obtain the price offset we need to plot
stocks['appleDelta'] = stocks['apple'].map(lambda x: x-75.51) 
stocks['microsoftDelta'] = stocks['microsoft'].map(lambda x: x-27.06)

stockDelta = stocks[['month','appleDelta', 'microsoftDelta']]
stockDelta.columns = ['Monthly Snapshots (Jan, 2006 - Sep, 2008)','Apple','Microsoft']
deltaPlot = stockDelta.set_index('Monthly Snapshots (Jan, 2006 - Sep, 2008)').sort_index().plot(style='o--',title="1b - Apple & Microsoft Stock Prices as Offset from Jan, 2006")

#Superposing two simple connected symbol graphs allows direct comparison of the two stock prices. 
pplt.savefig('Problem_1b.png')

#(c) Repeat item b, but now using juxtaposition: split the two curves into two different plots. 

stockDelta = stocks[['month','appleDelta', 'microsoftDelta']]
stockDelta.columns = ['Monthly Snapshots (Jan, 2006 - Sep, 2008)','Apple','Microsoft']
deltaPlot = stockDelta.set_index('Monthly Snapshots (Jan, 2006 - Sep, 2008)').sort_index().plot(style='o--',ylim=[-30,160],subplots=True,title="1c - Apple & Microsoft Stock Prices as Offset from Jan, 2006")
#Superposition is better and more intuitive at fulfilling the purposes of comparison

pplt.savefig('Problem_1c.png') 