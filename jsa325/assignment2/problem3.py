# Don't add datasets to repository

# Create dictionary in which key = zipcode, value = population

filePopulation = open('zipCodes_tr.csv', 'r')
linesPopulation = []

for line in filePopulation:
  linesPopulation.append(line)
filePopulation.close()

zipPopulationDict = {}  # create dictionary
num_linesPopulation = len(linesPopulation)

for i in range(1, num_linesPopulation):
  if linesPopulation[i].split(',')[10] != '\n':
    zipPopulationDict[linesPopulation[i].split(',')[0] = (float(linesPopulation[i].split(',')[10]))

# Create dictionary in wich key = zipcode, value = incident

fileIncident = open('Incidents_grouped_by_Address_and_Zip.csv','r')
linesIncident = []

for line in fileIncident:
  linesIncident.append(line)
fileIncident.close()

zipIncidentDict = {}  # create dictionary
num_linesIncident = len(linesIncident)

for i in range(1, num_linesIncident):
  if linesIncident[i].split(',')[10] != '\n':
    zipIncidentDict[linesIncident[i].split(',')[0] = (float(linesIncident[i].split(',')[10]))
    
# Create dictionary in which key = zipcode, value = borough

fileBorough = open('boroughs_tr.csv','r')
linesBorough = []

for line in fileBorough:
  linesBorough.append(line)
fileBorough.close()

zipBoroughDict = {}  # create dictionary
num_linesBorough = len(linesBorough)

for i in range(1, num_linesBorough):
  if linesBorough[i].split(',')[10] != '\n':
    zipBoroughDict[linesBorough[i].split(',')[0] = (float(linesBorough[i].split(',')[10]))
    
# Create dictionary in which key = borough, value = incidents
