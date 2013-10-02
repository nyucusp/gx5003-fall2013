#Katherine Elliott
#ke638
#Assignment 2 Problem 4

import sys
import borough from Borough
import zipcode from Zipcode

ref_borough = sys.argv[1]

boroughFile = open('boroughs.csv','r')

borough_lines = []
for line in boroughFile:
    borough_lines.append(line)
boroughFile.close()

boroughs = {} # borough dictionary
borough_zipcodes = len(borough_lines)

for j in range(0, borough_zipcodes):
    boroughs[borough_lines[j].split(',')[0] = borough_lines[j].split(',')[1]]

#problem incomplete needs zipcode dictionary and outFile clause 