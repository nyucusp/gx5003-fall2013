import csv

zipFileRaw = open('zipCodes.csv', 'r')
zipFile = csv.DictReader(zipFileRaw)

incidentFileRaw = open('Incidents_grouped_by_Address_and_Zip.csv', 'r')
incidentFile = csv.DictReader(incidentFileRaw)

class Zip:
    zipPop = ""
    incidents = 0

    def __init__(self, zipPop):
         self.zipPop = zipPop

    def addIncident(self):
        self.incidents += 1

    def incidentProportion(self):
        if self.zipPop == 'n':
            return "Zip not included in zipCodes.csv."
        elif self.zipPop != '':
            self.zipPop = float(self.zipPop)
            return float(self.incidents/self.zipPop)
        else:
            return "Population not included in zipCodes.csv."

zipDict = {}
for line in zipFile:
    zipDict[line['name']] = Zip(line['Total Population per ZIP Code'])

for incident in incidentFile:
    incidentZip = incident['Incident Zip'][:5]
    if incidentZip != '':
        if incidentZip in zipDict:
            zipDict[incidentZip].addIncident()
        else:
            zipDict[incidentZip] = Zip('n')
            zipDict[incidentZip].addIncident()

outputFile = open('output_problem3.txt', 'w')

for key in sorted(zipDict.iterkeys()):
    outputLine = key + " " + str(zipDict[key].incidentProportion()) + "\n"
    outputFile.write(outputLine)

outputFile.close()
zipFileRaw.close()
incidentFileRaw.close()
