# !usr/bin/python

######################################################################
#																	
# Assignment 5 - Problem 1c
# November 24th, 2013
#
# Michael Musick
#
#	Description: Plot Apple and Microsoft Stock Changes as separate plots
#	
#	Which visualization makes most sense:
#			For this data superposition, or placing the data on the same
#			plot makes most sense.  By having the data on the same plot
#			it is far easier to visualize the relative relationship changes
#			to each other.  Whereas the separate plots allows Microsoft to
#			appear as though it has similar change behavior because the 
#			y_axis scales are adjusted accordingly for each set of data
#	
#	
#
######################################################################

# IMPORT NECCESSARY LIBRARIES
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np


# create global variables for value arrays
dateArr = []
appleData = []
mcrstData = []

# MAIN FUNCTION
def main():
	# IMPORT THAT DATA
	data_fromFile = open('stocks.dat', 'r')
	tempDateArr = []
	for line in data_fromFile:
		lineArray = line.strip().split(',')
		if isfloat(lineArray[1]) and isfloat(lineArray[2]):
			tempDateArr.append(lineArray[0])
			appleData.append(float(lineArray[1]))
			mcrstData.append(float(lineArray[2]))

	# convert date strings to datetime objects
	for date in tempDateArr:
		dateArr.append(datetime.strptime( date, "%Y-%m"))
	
	problem_1c();


# Problem Specific Function
def problem_1c():

	# Reverse all data sets
	dateArr.reverse()
	appleData.reverse()
	mcrstData.reverse()

	# print dateArr
	# print appleData
	# print mcrstData

	# Create arrays that can be efficiently manipulated
	appleArray = np.array(appleData)
	mcrstArray = np.array(mcrstData)

	# get data relative to baseline
	appleArray = appleArray - appleArray[0]
	mcrstArray = mcrstArray - mcrstArray[0]
	
	dateMin = dateArr[1]
	dateMax = dateArr[len(dateArr)-1]
	

	fig, ax = plt.subplots(2, sharex=True, figsize=[10,10])
	fig.suptitle('Apple Inc. (APPL) and Microsoft Corporation (MSFT)\nStock Price Changes from January 2006 to August 2008', fontsize='18')
	fig.subplots_adjust(top=0.85)
	ax[0].plot(dateArr, appleArray, 'ko-', label='APPL')
	ax[0].set_title('APPL')
	ax[0].axis( [monthdelta(dateMin, -2).toordinal(), monthdelta(dateMax, 1).toordinal(), np.amin(appleArray)-5, np.amax(appleArray)+5 ])
	ax[1].set_title('MSFT')
	ax[1].plot(dateArr, mcrstArray, 'ko-', label='MSFT')
	ax[1].axis( [monthdelta(dateMin, -2).toordinal(), monthdelta(dateMax, 1).toordinal(), np.amin(mcrstArray)-1, np.amax(mcrstArray)+1 ])
	fig.autofmt_xdate()
	ax[1].fmt_xdata = mdates.DateFormatter('%Y-%m')
	plt.xlabel('Date')
	ax[0].set_ylabel('Amount of Value Change')
	ax[1].set_ylabel('Amount of Value Change')
	fig.patch.set_facecolor('white')
	plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=None, wspace=0.01, hspace=None)	
	fig.savefig('Problem1c.png')
	plt.show()




# determine if a string is a float
def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


# get altered datetimes
def monthdelta(date, delta):
	yearDelta = 0
	tempMonth = ((date.month-1)+delta)
	if tempMonth > 11:
		yearDelta = tempMonth/12
	elif tempMonth < 0:
		yearDelta = (tempMonth/12)
	month = (tempMonth%12)+1
	year = date.year + yearDelta
	dateString = str(year)+"-"+str(month)
	date = datetime.strptime(dateString, "%Y-%m")
	return date



# EXECUTE THE PROGRAM
if __name__ == "__main__":
    main()        