#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 4, Problem 2
#Connects to MySQL and computes the population density for a given zipcode


import MySQLdb
import sys



def main():

	inputZipcode = sys.argv[1]

	db = MySQLdb.connect(host="localhost", # your host, usually localhost
	                  user="jwr300", # your username
	                   passwd="jwr300", # your password
	                   db="coursedb") # name of the data base
	
	cur = db.cursor()
	

	cur.execute('''SELECT Total_Population_per_ZIP_Code FROM coursedb.zipcodes WHERE name = %s''', inputZipcode)
	population = cur.fetchall()
	population = population[0][0]
	
	cur.execute('''SELECT area FROM coursedb.zipcodes WHERE name = %s''', inputZipcode)
	area = cur.fetchall()
	area = area[0][0]
	

	pop_density = float(population)/float(area)
	print pop_density

	db.commit()
	db.close()



if __name__ == "__main__":
	main()
