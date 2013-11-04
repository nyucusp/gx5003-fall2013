"""
	assignment 4 problem2.py
	author: Christopher Jacoby
	Principles of Urban Informatics, Fall 2013

	Given a zip code as input in the command line, 
	compute the population density of that zip code. 

	You should NOT use a "select *" query and parse through the result.
"""

from dbmgr import dbMgr
import sys

def validate_input(zipInput):
	"""
	Returns true if zipInput is a valid numerical zip code. Else, false
	"""
	return zipInput.isdigit()

def main(args):
	if len(args) > 0:
		db = dbMgr()
		zipInput = args[0]
		if validate_input(zipInput):
			pass

		query = "select area, population from zipcodes where name={0}".format(zipInput)
		db.run_sql(query)

		results = db.results()
		if len(results) > 0:
			(area, population) = results[0]
			print "Zip Code: {0}\n Population: {1}\n Area: {2}\n Density: {3}".format(zipInput, population, area, population / area)
		else:
			print "No entry for this zip."

		db.close()
	else:
		print "Error: Invalid input. Please enter a zip code."

if __name__ == "__main__":
    main(sys.argv[1:])