dataFile = "zipCodes.csv"

fields = []
dataDict = {}

with open(dataFile, 'r') as f:
    # read the first line for the headers
    firstLine = f.readline()

    # get the fields from the line
    fields = firstLine.split(',')

    # store the fields as the keys in the dict
    for i in xrange(len(fields)):
        fields[i] = fields[i].strip()
        dataDict[fields[i].strip()] = []

    # now read all the lines in, and append the things to their 
    for line in f:
        values = line.split(',')

        for ind in xrange(len(values)):
            dataDict[fields[ind]].append(values[ind].strip())

# Compute the population density for each zip code.
# First, grab the (zip code, area, population)
data = (dataDict["name"], dataDict["area"], dataDict["Total Population per ZIP Code"])
# print data

resultData = []
for i in xrange(len(data[0])):
    x = (data[0][i], data[1][i], data[2][i])
    if x[1] is not '' and x[2] is not '':
        resultData.append ( (x[0], float(x[2]) / float(x[1])) )

outFile = open("output_density_problem2.txt", 'w')
resultDict = dict(resultData)
for k in sorted( resultDict.keys() ):
    outFile.write(k + " " + str(resultDict[k]) + "\n")

outFile.close()