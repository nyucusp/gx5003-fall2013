"""
	assignment 4 problem5.py
	author: Christopher Jacoby
	Principles of Urban Informatics, Fall 2013

	 List addresses of all incidents that occurred in Manhattan.
"""

from dbmgr import dbMgr
import sys

def main(args):
	db = dbMgr()
	print "Computing query (this may take a moment...)"
	query = "SELECT I.address from boroughs B, incidents I where (B.borough = 'Bronx' || B.borough = 'Queens') && B.zipcode = I.zip && I.address IS NOT NULL;"
	db.run_sql(query)

	results = db.results()
	for item in results:
		print item[0]

	db.close()

if __name__ == "__main__":
    main(sys.argv[1:])