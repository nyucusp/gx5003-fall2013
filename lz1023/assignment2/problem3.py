def incidents():#define a function of incidents
	myFile = open('Incidents_grouped_by_Address_and_Zip.csv','r')

	dict_inc = {}#dict of the incidents

	firstline = 0 #pass the first line
	for line in myFile:
		if firstline == 0:
			firstline = 1
		else:
			a = line.split(",") # split the line contents
			if a[1] != "": # ignored the zip codes with no incidents
				zipcode_incidents = a[1]#get the zip codes

				if zipcode_incidents in dict_inc:#put zipcode and incidents in to the dict
					dict_inc[zipcode_incidents] += 1 
				else:
					dict_inc[zipcode_incidents] = 1

	return dict_inc


def population():#define a function of population
	myFile = open('zipCodes.csv','r')

	dict_pop = {}#dict of the population

	firstline = 0#pass the first line
	for line in myFile:
		if firstline ==0:
			firstline = 1
		else:
			b = line.split(",")# split the line contents
			zipcode_pop = b[1]
			population = b[10][:-1]
			if population != '':#put zipcode and population in to the dict
				dict_pop[zipcode_pop] = int(population)
	return dict_pop

def borough():
	myFile = open('boroughs.csv','r')

	dict_bor = {}#dict of the borough

	for line in myFile:
		line=line[0:-1]
		c = line.split(",")
		zipcode= c[0]#zipcode
		borname = c[1]#borough of the current line
		if borname in dict_bor:#put zipcode and borough in to the dict
			dict_bor[borname].append(zipcode)
		else:
			dict_bor[borname]=[zipcode]
	return dict_bor

dict_inc = incidents()
dict_pop = population()
dict_bor = borough()

#after that I wanna get the zipcode where incidents happened 
#to get the related populations, and get the zipcode of every
#borough, then get the related number of incidents and population to calculate
#the ratio.
#but I don't know how to do...
		
			




