# !usr/bin/python

######################################################################
#																	
# Assignment 5 - Problem 1a
# November 24th, 2013
#
# Michael Musick
#
#	Description: Plot Apple Stock Prices
#	
#	Plotting Principles Used: 
#		Improving Vision, Principle 1 - Reduce Clutter: 
#					This was managed by making both plot and image 
#					background color white.  I also drew data using 
#					black in order to maximize contrast.
#		Improving Vision, Principle 3 - Proper Scale Lines:
#					The scale is set appropriately. With a suitable, 
#					but not superfluous number of ticks on either 
#					scale.  Additionally, the data is set just off the
#					scale lines in order to preserve Principle 1 and 
#					keep the data easy to read.
#		Improving Understanding, Principle 1 - Provide Explanations
#					The captions/labels clearly identify what is being
#					plotted.  
#	
#	
#
######################################################################

# IMPORT NECCESSARY LIBRARIES
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from datetime import datetime, timedelta

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
	
	problem_1a();



def problem_1a():
	# get the min and max values
	appleMin = min(appleData)
	appleMax = max(appleData)

	dateMin = dateArr[len(dateArr)-1]
	dateMax = dateArr[1]
	
	fig, ax = plt.subplots(1, figsize=[10,10])
	ax.plot(dateArr, appleData, 'ko-')
	ax.axis( [monthdelta(dateMin, -1).toordinal(), monthdelta(dateMax, 2).toordinal(), appleMin-5, appleMax+5 ])
	fig.autofmt_xdate()
	ax.fmt_xdata = mdates.DateFormatter('%Y-%m')
	plt.xlabel('Date')
	plt.ylabel('Stock Price Value')
	fig.suptitle('Apple Inc. (APPL) Stock Prices', fontsize='18')
	plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=None, wspace=0.01, hspace=None)	
	fig.patch.set_facecolor('white')
	fig.savefig('Problem1a.png')
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