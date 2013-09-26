from zipcodes import *
import sys

selectedborough = sys.argv[1]

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