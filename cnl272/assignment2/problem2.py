import sys

myFile = open('zipCodes.csv', 'r')
count = 0
dict_zip_popdensity = {}

for line in myFile:
	if count < 1:
		count = 1
	#read the file of zipCodes.csv from the second line
	else:
	
		line_without_return=line[:-1]
		splitted_line=line_without_return.split(",")
		#get zipcode
		zipcode = splitted_line[1]
		#get area
		area = splitted_line[7]
		numerical_area = float(area)
		#get population
		population = splitted_line[10]
		if population =='':
			continue
			#ignore the missing data
		else:
			numerical_population=int(population)
		
		population_density=numerical_population/numerical_area
		dict_zip_popdensity[zipcode] = population_density


outputFile=open('population_density_problem2.txt', 'w')
for key in dict_zip_popdensity:
	line_contant = key + " " + str(dict_zip_popdensity[key]) + "\n"
	outputFile.write(line_contant)

outputFile.close()
