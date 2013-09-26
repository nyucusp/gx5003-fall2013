import sys

"""
We now open the file and save the lines in a list called "lines"
"""
myFile = open('zipCodes.csv', 'r')

lines = []
for line in myFile:
    lines.append(line)
myFile.close()

"""
We create a dict and populate it with zipcodes as keys and densities as values.  We
ignore those zipcodes that have no population information with the "if" clause.

Note that there are apparently duplicate zip codes in the zipCodes file 
(meaning duplicate zip codes with *different* population values).  Since I have no 
idea what the correct population is, for a given zip code I am just
putting the *last* instance of it (the last instance in the order it appears in the 
zipCodes.csv file) in the dictionary below.
"""
zip_dict = {}
num_lines = len(lines)

for i in range(1, num_lines):
    if lines[i].split(',')[10] != "\n":
        zip_dict[lines[i].split(',')[0]] = (float(lines[i].split(',')[10])/float(lines[i].split(',')[7]))


"""
Finally we output and sort at the same time
"""
outputFile = open('output_density_problem2.txt', 'w')
for key in sorted(zip_dict.iterkeys()):
    outputFile.write("%s %s \n" % (key, zip_dict[key]))
outputFile.close()
