import csv

zipFileRaw = open('zipcodes.csv', 'rU')
zipFile = csv.DictReader(zipFileRaw, delimiter=',')

zipAreas = []
for line in zipFile:
    popl = line['Total Population per ZIP Code']
    if popl != '':
        popl = int(popl)
        area = float(line['area'])
        density = popl/area
    else:
        density = "No population in this zip."
    zipAreas.append([line['name'], density])

zipAreas.sort(key=lambda variable: variable[0])

outputFile = open("output_density_problem2.txt", 'w')
for line in zipAreas:
    lineContent = str(line[0]) + " " + str(line[1]) + "\n"
    outputFile.write(lineContent)

outputFile.close()
zipFileRaw.close()
