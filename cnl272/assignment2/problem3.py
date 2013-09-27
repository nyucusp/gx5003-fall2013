import sys

def getpopulation():
	myFile = open('zipCodes.csv', 'r')
	zip_population = []
	count = 0
	dict_zip_population = {}

	for line in myFile:
		if count < 1:
			count = 1
		#read the file of zipCodes.csv from the second line
		else:
		
			line_without_return=line[:-1]
			splitted_line=line_without_return.split(",")
			#get zipcode
			zipcode = splitted_line[1]
			#get population
			population = splitted_line[10]
			if population =='':
				continue
				#ignore the missing data
			else:
				numerical_population=int(population)
				dict_zip_population[zipcode]=numerical_population

	myFile.close()
	return dict_zip_population

def getincident():
	incident_File = open('Incidents_grouped_by_Address_and_Zip.csv', 'r')
	zip_incidents = []
	count = 0
	dict_zip_incidents = {}
	for line in incident_File:
		if count < 1:
			count = 1
		else:
			line_without_return=line[:-1]
			splitted_line=line_without_return.split(",")
			#get zipcode
			zipcode = splitted_line[1]
			if zipcode =='':
				continue
				#ignore the missing data
			else:
				if zipcode in dict_zip_incidents:
					dict_zip_incidents[zipcode] = dict_zip_incidents[zipcode]+1
				else:
					dict_zip_incidents[zipcode]=1

	incident_File.close()
	return dict_zip_incidents

import os
def borough():
	borough_File = open('boroughs.csv', 'r')
	zip_borough = []

	dict_zip_borough = {}
	for line in borough_File:

		line_without_return = line[:-1]
		splitted_line = line_without_return.split(",")
		
		#classify zipcodes according to the five boroughs
		if splitted_line[1] not in dict_zip_borough:
			dict_zip_borough[splitted_line[1]]=[splitted_line[0]]
		else:
			dict_zip_borough[splitted_line[1]].append(splitted_line[0])
		
	borough_File.close()		
	return dict_zip_borough


borough_dict = borough()
incident_dict = getincident()
population_dict = getpopulation()

incident_zip=[]
#find the zipcodes that appear in both populaiton_dict and incident_dict, and add those zipcodes into incident_zip[]
for key in population_dict:
	if key in incident_dict:
		incident_zip.append(key)

dict_incident_ratio = {}
for  borough_key in borough_dict:

	zip_five_borough = []
	for key_zip in incident_zip:
		if key_zip in borough_dict[borough_key]:#value of dict_zip_borough
			zip_five_borough.append(key_zip)

	incident_borough = 0
	for key_inc in zip_five_borough:
		incident_borough=incident_borough+incident_dict[key_inc]
	#sum the numbers of incidents in each borough

	population_borough = 0
	for key_pop in zip_five_borough:
		population_borough = population_borough+population_dict[key_pop]

	incident_ratio = float(incident_borough)/population_borough
#divide population in each borough with numbers of incidents(sum of number of zipcodes) in each borough
	dict_incident_ratio[borough_key]=incident_ratio

lexi_incidentratio = []
for key in dict_incident_ratio:
	lexi_incidentratio.append((key, dict_incident_ratio[key]))
lexi_incidentratio = sorted(lexi_incidentratio)

outputFile = open('output_problem3.txt', 'w')
for ir in lexi_incidentratio:
	line_content = ir[0]+" "+str(ir[1])+"\n"
	outputFile.write(line_content)

outputFile.close()


