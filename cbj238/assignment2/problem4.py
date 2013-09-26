from zipcodes import *
import sys

if len(sys.argv) > 1:
	selectedborough = sys.argv[1]
else:
	print "Invalid Input"
	exit(-1)

# Get the dicts we need to work with
zipBorough = GetZipsBorough()
zipPopulation = GetZipPopulation()

# zipBorough is { zip->borough }. need to get the unique boroughs from it.
boroughSet = set(zipBorough.values())
boroughs = [ Borough(x) for x in boroughSet]

# we need to connect the borough names to the borough classes
boroughMap = dict(zip(boroughSet, boroughs))

for zipCode in zipPopulation:
	if zipCode in zipBorough:
		boroughMap[zipBorough[zipCode]].addPopulation(zipPopulation[zipCode])
	
# for i in boroughMap:
print boroughMap[selectedborough].getAveragePopulation()
