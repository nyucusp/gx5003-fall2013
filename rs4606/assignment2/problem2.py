import sys
import datetime



"""
We now open the file and save the lines in a list called "lines"
"""
myFile = open('zipCodes.csv', 'r')

lines = []
for line in myFile:
    lines.append(line)
myFile.close()

zip_dict = {}
num_lines = len(lines)

for i in range(1, num_lines):
    if lines[i].split(',')[10] != "\n":
        zip_dict[lines[i].split(',')[0]] = (float(lines[i].split(',')[10])/float(lines[i].split(',')[7]))

"""
This commented bit can display 'no data' for zip codes with no population display
"""
#    else:
#        zip_dict[lines[i].split(',')[0]] = "no data"

outputFile = open('output_density_problem2.txt', 'w')
for key in sorted(zip_dict.iterkeys()):
    outputFile.write("%s %s \n" % (key, zip_dict[key]))
outputFile.close()
