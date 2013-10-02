#Katherine Elliott
#ke638
#Assignment 2 Problem 3

#creat diction for each file, beginnign with zip code to match zipcode and population    
zipFile = open('zipcode.csv','r')# run zip code file
pop_lines = []

for line in zipFile:
    pop_lines.append(line)

zipFile.close()

zip_id = pop_lines[0].split(',')# store relevant column title

zip_length = len(zip_id)#strips column titles
for j in range(0,zip_length):
    zip_id[j] = zip_id[j].strip

zip_index = zip_id.index('zip code tabulation area')# indices
pop_index = zip_id.index('Total Population per ZIP Code')#

population = {} #population by zipcode dictionary

zipFile_length = len(pop_lines)

for j in range(1,zipFile_length):
    if pop_lines[j].split(',')[10] != '\n':
        population[pop_lines[j].split(',')[zip_index]] = (float(pop_lines[j].split(',')[pop_index].strip()))

#borough dictionary to match zip codes to borough
boroughFile = open('boroughs.csv','r')
borough_lines = []

for line in boroughFile:
    borough_lines.append(line)
boroughFile.close()

borough_zip_index = 0
borough_index = 1

borough = {}

boroughFile_length = len(borough_lines)
for j in range(1, boroughFile_length):
    if borough_lines[j].split(',')[borough_index] != '\n':
        borough[borough_lines[j].split(',')[borough_zip_index]] = (float(borough_lines[j].split(',')[borough_index].strip()))

#runs zip code population pair and adds borough
borough_pop = {'Manhattan': 0.0,'Brooklyn': 0.0,'Queens': 0.0,'Bronx': 0.0,'Staten': 0.0}#run through key zipcodes

for key in population:
    if borough.has_key(key):
        borough_zip[borough[key].strip()] = borough_zip[borough[key].strip()] + population[key]

#incident dictionary to match with zipcodes        
incidentFile = open('incidents.csv','r')

incident_lines = []#store column titles
for line in incidentFile:
    incident_lines.append(line)
    
incident_id = incident_lines[0].split(',')
incident_id_length = len(incident_id)

for j in range(0,incident_length):#strips column titles
    incident_id[j] = incident_id[j].strip()

incident_count_index = incident_id.index('Unique Key')
incident_index = incident_id.index('Incident Zip')

incident_length = len(incident_lines)

incident_zip = {}# create incident dictionary

for j in range(1,incident_length):
    if (incident_lines[j].split(',')[incident_zip] !=''):
        if (incident_zip.has_key(incident_lines[j].split)(',')[incident_index][0:5] == False and borough.has_key(incident_lines[j].split(',')[incident_index][0:5])):
            incident_zip[incident_lines[j].split(',')[incident_index][0:5]] = int(incident_lines[j].split(',')[incident_count_index].strip())
        else:
            if (borough.has_key(incident_lines[j].split(',')[incident_index][0:5])):
                if (incident_lines[j].split(',')[incident_count_index] != ''):
                    incident_zip[incident_lines[j].split(',')[incident_index][0:5]] = incident_zip[incident_lines[j].split(',')[incident_index][0:5]] + int(incident_lines[j].split(',')[incident_count_index].strip())

borough_incident = {'Manhattan': 0.0,'Brooklyn': 0:0,'Queens': 0.0,'Bronx': 0.0,'Staten': 0.0}

for key in incident_zip:
    if borough.has_key(key):
        borough_incident[borough[key].strip()] = borough_incident[borough[key].strip()] + incident_zip[key]

#dictionary of incident density by borough
borough_incident_density = {'Manhattan': 0.0,'Brooklyn': 0.0,'Queens': 0.0,'Bronx': 0.0,'Staten': 0.0}

for key in borough_incident_density:
    borough_incident_density[key] = (borough_incident[key] / borough_zip_pop[key])

outputFile = open('output_problem3.txt','w')

for key in sorted(borough_incident_density.iterkeys()):
    outputFile.write('%s %s \n' % key, borough_incident_density[key])

#errors in file because of undefined variables, potentially not recognizing column titles, comments show process - similar to problem2 but repeated for more files and addition of key

outputFile.close()



