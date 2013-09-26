
#open zipCodes.csv, read
myFile = open('c:\\Users\\Nathan\\desktop\\zipCodes.csv','r')
myOtherFile = = open('c:\\Users\\Nathan\\desktop\\Incidents_grouped_by_Address_and_Zip.csv','r')
myOtherOtherFile = = open('c:\\Users\\Nathan\\desktop\\boroughs.csv','r')

for line in myFile: # reads each line, loop
	# print line
	column = line.split(',') #delineates each value in spreadsheet by removing comma
	area = column[7] # 7 refers to the area column
	pop = column[10] # 10 refers to the population column
	print area
"""
My python fluency is still not the best (I've been working hard
at it!), but, I can anticipate the logic of the next steps:

(1) reference the borough.csv file that links each zipcode to
	its particular burough,
(2) sum the number of incidents for each zipcode and have them
	link to a dictionary or list(?) that refers to each borough,
(3) create a function that dives number of incidents by population,
	thus creating the ratio
(4) and create an output file to print to, which I did
figure out, as seen below:
"""
outputFile = open('output_problem3.txt', 'w') #create output file

outputFile.close()