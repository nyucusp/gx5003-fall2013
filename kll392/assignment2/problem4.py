#Kara Leary
#Urban Informatics
#Assignment 2 - Problem 4

import sys
import csv
from zipcode import Zipcode
from borough import Borough

#In this code, first I import the name of the borough from the command line.  I assume that Staten Island is being input simply as 'Staten'.  I set the input to the name of the Borough object 'borough'.  I define the same 'makeunique' function that I used in problem 3.  Next, I opened 'boroughs.csv' and read through each entry row by row.  I set the zip code of the entry to 'thiszip', and take the name of the borough listed.  I make the name lowercase as well, so that I can match it to the inputted borough without having to worry about differences in capitalization.  If the name matches the one inputted by the user, I use the 'borough.addZipcode method to add the zipcode to the list of that borough's zips.  I then employ the 'makeunique' function defined earlier to weed out any duplicates in that boroughs zipcode dictionary.  I then go through the file 'zipCodes.csv' row by row.  First I ensure that I am only looking at rows that have an entry for population; otherwise it is useless to me.  If the row has a population entry, I set the rowzip to that row's zipcode, and rowpop to that row's population.  i then go through the entries in the zipcode dictionary: if the row zipcode matches an entry in the dictionary, then it must be part of that borough, and I use the 'addPopulation' method to add the population to the borough's running total.  Finally, I use the borough.findAverage function to compute the average population of the zipcodes.


boroughname = sys.argv[1]
borough = Borough(boroughname.lower())

def makeunique(list):
    found = []
    keep = []
    for entry in list:
        if entry not in found:
            found.append(entry)
            keep.append(entry)
    return keep

with open('boroughs.csv') as f:
    rows = csv.reader(f, delimiter=',')
    for row in rows:
        thiszip = Zipcode(row[0])
        rowentry = row[1]
        if (rowentry.lower() == borough.name):
            borough.addZipcode(thiszip.number)

borough.zipcodes = makeunique(borough.zipcodes)

with open('zipCodes.csv') as f:
    rows = csv.reader(f, delimiter=',')
    rows.next()
    for row in rows:
        if (row[10] != ''):
            rowzip = row[1]
            rowpop = float(row[10].strip())
            for line in borough.zipcodes:
                if (int(rowzip) == int(line)):
                    borough.addPopulation(rowpop)


borough.findAverage()
print borough.average
