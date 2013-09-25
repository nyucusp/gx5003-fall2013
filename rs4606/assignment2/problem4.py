"""
Note that the borough and zipcode classes are separate python files which we import.
They are not defined in this python document (problem4.py).  Please make sure you have
both borough.py and zipcode.py in the same directory as problem4.py before running
problem4.py
"""

import sys
import borough
import zipcode

"""
We first take the user's input and make a borough object with the input as the name.
We make sure that we capitalize the user's input if necessary, and also just return
the first word (in case the user inputs "staten island", we just want "Staten")
"""

borough_name = sys.argv[1].split(" ",1)[0].capitalize()
given_borough = borough.Borough(borough_name)

"""
Next, as in problem 3, we make boroughs_zip_dict, which is a dictionary whose
keys are the zips and whose values are the borough names.  Note that every zip code in 
boroughs_tr.csv is duplicated twice, but these duplicates are removed when we populate
boroughs_zip_dict.  Note also that in the last line of the for loop, specifically
boroughs_lines[i].split(',')[1][:-1], the last [:-1] is necessary to remove 
the \n character at the end of the borough name.
"""

boroughs_file = open('boroughs_tr.csv', 'r')

boroughs_lines = []
for line in boroughs_file:
    boroughs_lines.append(line)
boroughs_file.close()

boroughs_zip_dict = {}
num_boroughs_lines = len(boroughs_lines)

for i in range(0, num_boroughs_lines):
    boroughs_zip_dict[boroughs_lines[i].split(',')[0]] = boroughs_lines[i].split(',')[1][:-1]
    

"""
(This step is also taken directly from problem 3)
We now open zipCodes and save the lines as elements in a list called zip_lines.

Next, we create a dict and populate it with zipcodes as keys and populations
as values.  We ignore those zipcodes that have no population information 
with the "if" clause.  

Note that there are apparently duplicate zip codes in the zipCodes file 
(meaning duplicate zip codes with *different* population values).  Since I have no 
idea what the correct population is, for a given zip code I am just
putting the *last* instance of it (the last instance in the order it appears in the 
zipCodes.csv file) in the dictionary below.
"""
myFile = open('zipCodes.csv', 'r')

zip_lines = []
for line in myFile:
    zip_lines.append(line)
myFile.close()

zip_pop_dict = {}
num_zip_lines = len(zip_lines)

for i in range(1, num_zip_lines):
    if zip_lines[i].split(',')[10] != "\n":
        zip_pop_dict[zip_lines[i].split(',')[0]] = (float(zip_lines[i].split(',')[10]))


"""
Now we populate our given_borough object with its corresponding zip code objects.  
Each zip code object has its name and population, where the population is taken
from zip_pop_dict.  Note that some zips from boroughs_tr.csv are *not* in 
zipCodes.csv (for instance, '10311', in Staten Island), so these are ignored
since they have no population data.
"""


for zip in boroughs_zip_dict:
    if boroughs_zip_dict[zip][0:5] == borough_name[0:5]:
        if zip in zip_pop_dict: 
            zip_code = zipcode.Zipcode(zip, zip_pop_dict[zip])
            given_borough.addZipcode(zip_code)

"""
Finally, we call the avgpop() method in the Borough class for given_borough
"""
given_borough.avgpop()
