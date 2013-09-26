incidentFile="Incidents_grouped_by_Address_and_Zip.csv"
boroughsFile="boroughs.csv"
dataFile = "zipCodes.csv"

import re

def CleanListStrings(strlist):
    for i in xrange(len(strlist)):
        strlist[i] = strlist[i].strip()

def GetZipData():
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

    return (fields, dataDict)

def GetZipPopulationDensity():
    (fields, dataDict) = GetZipData()

    # Compute the population density for each zip code.
    # First, grab the (zip code, area, population)
    data = (dataDict["name"], dataDict["area"], dataDict["Total Population per ZIP Code"])
    # print data

    resultData = []
    for i in xrange(len(data[0])):
        x = (data[0][i], data[1][i], data[2][i])
        if x[1] is not '' and x[2] is not '':
            resultData.append ( (x[0], float(x[2]) / float(x[1])) )

    return dict(resultData)

def GetZipPopulation():
    (fields, dataDict) = GetZipData()

    # Get list of zip code, population
    data = (dataDict["name"], dataDict["Total Population per ZIP Code"])
    resultData = []
    for i in xrange(len(data[0])):
        x = (data[0][i], data[1][i])
        if x[0] is not '' and x[1] is not '':
            resultData.append( (x[0], x[1]) )

    return dict(resultData)

def GetZipIncidentsFromFile():
    numberParser = re.compile(r'[^\d.]+')
    fileHandle = open(incidentFile, 'r')

    headers = fileHandle.readline().split(',')
    
    # Clean them up
    CleanListStrings(headers)

    zipsDict = {}

    for line in fileHandle:
        lineItems = line.split(',')
        CleanListStrings(lineItems)

        zipCode = lineItems[1]
        zipCount = numberParser.sub('', lineItems[2])   # I'm not actually sure if this is a count. It looks like it might be, but there's no description anywhere.

        # I am likewise going to assume that any entry is just "1".
        if zipCount is '':
            zipCount = 1
        if zipCode is '':
            continue

        try:
            if zipCode in zipsDict:
                zipsDict[zipCode] += int(zipCount)
            else:
                zipsDict[zipCode] = int(zipCount)
        except ValueError:
            print "Value Error occured for ZipCode", zipCode, " and count", zipCount

    return zipsDict

def GetZipsBorough():
    fileHandle = open(boroughsFile, 'r')
    headers = fileHandle.readline().split(',')
    # Clean then up...
    CleanListStrings(headers)

    zipsDict = {}

    for line in fileHandle:
        lineItems = line.split(',')
        CleanListStrings(lineItems)

        zipCode = lineItems[0]
        borough = lineItems[1]

        if zipCode not in zipsDict:
            zipsDict[zipCode] = borough

    return zipsDict