# !usr/bin/python

######################################################################
#																	
# Assignment 5 - Problem 2
# November 24th, 2013
#
# Michael Musick
#
#	Description: Histogram of submitted assignments
#	
#	How did I select the bins and why:
#		I chose 150 bins.  Although I should have used the formula to 
#		determine a statistically optimal number, 150 shows a great deal 
#		of detail while not being to high of resolution.
#	
#	What hypothesis can you make about the amount of 
#	work (i.e. number of actions) for the different 
#	assignments just by looking to this histogram?
#		As the assignments progressed through the semester it took students
#		more work to complete each one.  With many students completing
#		the assignments after the due dates.
#	
#	What pattern can you observe for the amount of 
#	work (i.e. number of actions) close to the deadlines?
#		The students would work primarily right at the deadline and
#		many would not give themselves enough time to finish as evident
#		by the number actions "right" after a deadline.
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
actionTimestamps = []
dueDates = {'1':"2007-09-18 12:00:00", '2':"2007-10-04 12:00:00", '3':"2007-10-25 12:00:00", '4':"2007-11-27 12:00:00", '5':"2007-12-15 12:00:00", '6':"2007-12-11 12:00:00"}

# MAIN FUNCTION
def main():
	# IMPORT THAT DATA
	data_fromFile = open('actions-fall-2007.dat', 'r')
	tempDateArr = []
	for line in data_fromFile:		
		datetime_checkAdd( line.strip() )
	
	# print actionTimestamps
	timestampArr = np.array(actionTimestamps)
	timestampArr = np.sort(timestampArr)

	dueDatesString = []
	dueDatesArr = []

	# get the due date ticks	
	for key in dueDates:
		date_ = dueDates[key]
		date_ = datetime.strptime(date_,"%Y-%m-%d %H:%M:%S")
		dueDatesString.append( key+" : "+date_.strftime("%m-%d-%Y") )
		dueDatesArr.append(float(date_.strftime('%s')))
		

	# fig = plt.figure()
	num_bins = 150	
	fig, ax = plt.subplots(figsize=[10,10])
	n, bins, patches = plt.hist(timestampArr, num_bins, histtype='bar', color='grey')

	histMax = max(n)

	ax.vlines(dueDatesArr, 0-histMax*0.02, histMax+histMax*0.02)
	ax.grid(True)

	box = ax.get_position()
	ax.set_position([box.x0, box.y0+box.height*0.2, box.width, box.height*0.8])

	ax.set_xticks(dueDatesArr)
	ax.set_xticklabels(dueDatesString, ha='right', rotation='30')
	
	fig.suptitle('Histogram of Assignment Actions (150 bins)', fontsize='18')
	ax.set_ylabel('Number of Actions')
	ax.set_xlabel('Assignment # and Due Date')

	plt.axis( [np.amin(timestampArr)-100000, np.amax(timestampArr)+100000, 0-histMax*0.02, histMax+histMax*0.02])
	plt.subplots_adjust(left=None, bottom=0.15, right=0.95, top=None, wspace=0.01, hspace=None)
	fig.patch.set_facecolor('white')
	fig.savefig('Problem2.png')
	plt.show()




# determine if a string is a valid timestamp, if so add to the array
def datetime_checkAdd( inDate ):
    try:
        tempdate = datetime.strptime( inDate, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return False
    
    actionTimestamps.append( float(tempdate.strftime('%s')) )
    return True



# EXECUTE THE PROGRAM
if __name__ == "__main__":
    main()        