from zipcodes import *

outputFile="output_problem3.txt"
print "Reading Boroughs"
zipBorough = GetZipsBorough()
print "Reading Incidents"
zipIncidents = GetZipIncidentsFromFile()
print "Reading populations"
zipPopulation = GetZipPopulation()

# Calculate the ratio of number of incidents to population for a borough.
print "Calculating Results"
results = {}
# For each incident listing
for zipCode in zipIncidents.keys():
	# find the associated borough
	borough = None
	if zipCode in zipBorough:
		borough = zipBorough[zipCode]

	population = None
	if zipCode in zipPopulation:
		population = zipPopulation[zipCode]

	if borough is not None and population is not None:
		if borough in results:
			results[borough][0] += float(zipIncidents[zipCode])
			results[borough][1] += float(population)
		else:
			results[borough] = [float(zipIncidents[zipCode]), float(population)]

output = open(outputFile, 'w')
for brgh in sorted(results.keys()):
	items = results[brgh]
	output.write(brgh + " " + str(items[0] / items[1]) + "\n")
output.close()