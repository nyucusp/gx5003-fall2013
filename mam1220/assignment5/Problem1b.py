# !usr/bin/python

######################################################################
#																	
# Assignment 5 - Problem 1b
# November 24th, 2013
#
# Michael Musick
#
#	Description: Plot Apple and Microsoft Stock Changes
#	
#	Conclusions Drawn From Plot:
#				Apples stock has tended to be more volatile over this
#				time period, with much larger falls and rises, compared 
#				Microsoft whose value has remained relatively constant
#				
#				This does not give us an idea as to the actual value
#				but rather shows that Apple tends to have large value
#				swings.  
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
	
	problem_1b();


# Problem Specific Function
def problem_1b():

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

	# get the min and max values
	dataMin = min( [np.amin(appleArray), np.amin(mcrstArray)] )
	dataMax = max( [np.amax(appleArray), np.amax(mcrstArray)] )
	
	dateMin = dateArr[1]
	dateMax = dateArr[len(dateArr)-1]
	
	fig, ax = plt.subplots(1, figsize=[10,10])
	ax.plot(dateArr, appleArray, 'bo-', label='APPL')
	ax.plot(dateArr, mcrstArray, 'ro-', label='MSFT')
	ax.axis( [monthdelta(dateMin, -2).toordinal(), monthdelta(dateMax, 1).toordinal(), dataMin-5, dataMax+5 ])
	fig.autofmt_xdate()
	ax.fmt_xdata = mdates.DateFormatter('%Y-%m')
	plt.xlabel('Date')
	plt.ylabel('Amount of Value Change')
	fig.suptitle('Apple Inc. (APPL) and Microsoft Corporation (MSFT)\nStock Price Changes from January 2006 to August 2008', fontsize='18')
	fig.patch.set_facecolor('white')
	# change positioning
	# box = ax.get_position()
	# ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
	ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	plt.subplots_adjust(left=0.1, bottom=0.1, right=0.85, top=None, wspace=0.01, hspace=None)
	fig.savefig('Problem1b.png')
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