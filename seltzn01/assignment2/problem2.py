#Nathan Seltzer
#Assignment 2, Problem 2

#open zipCodes.csv, read
myFile = open('c:\\Users\\Nathan\\desktop\\zipCodes.csv','r')

for line in myFile: # reads each line, loop
	# print line
	column = line.split(',') #delineates each value in spreadsheet by removing comma
	area = column[7] # 7 refers to the area column
	pop = column[10] # 10 refers to the population column
	print area
"""
My python fluency is still not the best (I've been working hard
at it!), but, I can anticipate the logic of the next steps:

(1) divide population by area for each line in 
	order to get the population density,
(2) use and If/Else statement to tell python to ignore
	zip codes with no population,
(3) organize the zip codes (column 0) lexicographically,
(4) and create an output file to print to, which I did
	figure out, as seen below:
"""
outputFile = open('output_density_problem2.txt', 'w') #create output file

outputFile.close()