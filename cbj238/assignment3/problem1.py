import numpy as np
from readInputFile import Problem1Input

def calculate_money_that_changed_hands(tripList):
	ret = []

	for trip in tripList:
		tripN = trip[0]
		tripArr = np.array(trip[1])

		# figure out how much each person owes... their value - the mean of the whole thing:
		person_owes = (tripArr - tripArr.mean()).round(2)

		# The total amount changed is either the positive or negative of the means from each... not both.
		#  Here we get rid of the negative, and sum the positive
		positive_values = person_owes > 0

		ret.append( person_owes[positive_values].sum() )

	return ret

inputTrips = Problem1Input()

resultList = calculate_money_that_changed_hands(inputTrips.data)
for result in resultList:
	print result