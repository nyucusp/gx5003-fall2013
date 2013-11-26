"""
	assignment 4 problem6.py
	author: Christopher Jacoby
	Principles of Urban Informatics, Fall 2013

	 List the set of zip codes in Manhattan along with their population where incidents have occurred.
"""

from dbmgr import dbMgr
import sys

def main(args):
	db = dbMgr()
	print "Computing query (this may take a moment...)"
	query = "SELECT B.zipcode, Z.population from boroughs B, zipcodes Z, incidents I where B.borough = 'Manhattan' && B.zipcode = I.zip && B.zipcode = Z.zipcode;"
	db.run_sql(query)

	results = db.results()
	for item in results:
		print item[0], item[1]

	db.close()

if __name__ == "__main__":
    main(sys.argv[1:])