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

		lexi_pop_den = []
		for key in dict_zip_popdensity:
			lexi_pop_den.append((key, dict_zip_popdensity[key]))
		lexi_pop_den = sorted(lexi_pop_den)

outputFile=open('output_density_problem2.txt', 'w')
for tp in lexi_pop_den:
	line_content = tp[0] + " " + str(tp[1]) + "\n"
	outputFile.write(line_content)

outputFile.close()
