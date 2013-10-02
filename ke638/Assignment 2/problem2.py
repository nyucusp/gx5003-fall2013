#Katherine Elliott
#ke638
#Assignment 2 Problem 2

import sys

myFile= open('zipcode.csv' , 'r')
lines = []

for line in myFile:
    lines.append(line)
myFile.close()

title = lines[0].split(',') #stores relevantt column titles

title_length = len(title) #strips column titles
for k in range(0,title_length):
    title[k] = title[k].strip()
    
zipcode_index = title.index('zip code tabulation area')
area_index = title.index('area')
pop_index = title.index('Total Population per ZIP Code')

density = {}#creates dictionary

length = len(lines)

for k in range(1,length):
    if lines[k].split(',')[10] != '\n':
        density[lines[k].split(',')[zipcode_index]]= (float(lines[k].split(',')[pop_index].strip())/float(lines[k].split(',')[area_index].strip()))

outputFile = open('output_density_problem2.txt','w')

for key in sorted(density.iterkeys()):
    outputFile.write('%s %s \n' % (key, density[key]))

outputFile.close()
