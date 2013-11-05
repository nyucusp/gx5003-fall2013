"""
	assignment 4 problem3.py
	author: Christopher Jacoby
	Principles of Urban Informatics, Fall 2013

	Given a borough name, your task is to compute the ratio 
		between the number of incidents and the population in that borough. 

	You can use multiple SQL queries for obtaining appropriate data, 
	and you can process the data through python. 

	You should NOT use a "select *" query and parse through the result. 
	Joins are not mandatory.
"""

from dbmgr import dbMgr
import sys

BOROUGH_NAMES = ["Manhattan", "Staten", "Bronx", "Queens", "Brooklyn"]

def validate_input(boroughName):
	"""
	Returns true if zipInput is a valid numerical zip code. Else, false
	"""
	return boroughName in BOROUGH_NAMES

def main(args):
	if len(args) > 0:
		db = dbMgr()
		boroughName = args[0]
		if validate_input(boroughName):
			print "Computing query (this may take a moment...)"
			query = "SELECT SUM(Z.population), SUM(I.count) from boroughs B, zipcodes Z, incidents I where B.borough = '{0}' && Z.zipcode = B.zipcode && Z.zipcode = I.zip;".format(boroughName)
			db.run_sql(query)

			results = db.results()
			if len(results) > 0:
				(population, incidents) = results[0]
				print "Borough: {0}\n Population: {1}\n Incidents: {2}\n Ratio: {3}".format(boroughName, population, incidents, incidents / population)

			db.close()
		else:
			print "Input must be one of: {0}".format(BOROUGH_NAMES)
	else:
		print "Error: Invalid input. Must be one of {0}.".format(BOROUGH_NAMES)

if __name__ == "__main__":
    main(sys.argv[1:])