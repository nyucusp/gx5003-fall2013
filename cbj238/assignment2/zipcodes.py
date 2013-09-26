incidentFile="Incidents_grouped_by_Address_and_Zip.csv"
boroughsFile="boroughs.csv"
dataFile = "zipCodes.csv"

import re
from parsecsv import ParseCSV

def GetZipData():
    '''
    Reads zipCodes.csv into memory, returns it as a dict.
    '''
    parser = ParseCSV(dataFile)

    return parser.getLabelledData()

def GetZipPopulationDensity():
    '''
    Calculates the population density from zipCodes.csv's area and population fields.
    Returns it as a dict of:
    { ("zip code" : population density )}
    '''
    dataDict = GetZipData()

    # Compute the population density for each zip code.
    # First, grab the (zip code, area, population) from the dict
    data = (dataDict["name"], dataDict["area"], dataDict["Total Population per ZIP Code"])

    # Calculate the population density for each zip, store it in the array
    resultData = []
    for i in xrange(len(data[0])):
        x = (data[0][i], data[1][i], data[2][i])
        if x[1] is not '' and x[2] is not '': # if area of population is empty, exclude it
            resultData.append ( (x[0], float(x[2]) / float(x[1])) )

    # return it as a dict.
    return dict(resultData)

def GetZipPopulation():
    '''
    Same as above but only gets the population.
    '''
    dataDict = GetZipData()

    # Get list of zip code, population
    data = (dataDict["name"], dataDict["Total Population per ZIP Code"])
    resultData = []
    for i in xrange(len(data[0])):
        x = (data[0][i], data[1][i])
        if x[0] is not '' and x[1] is not '':
            resultData.append( (x[0], x[1]) )

    return dict(resultData)

def GetZipIncidentsFromFile():
    '''
    returns a dict of
    { (Zip Code):incidents }
    '''
    parser = ParseCSV(incidentFile, (1, 2))
    (fields, data) = parser.getRawData()

    # Not all of the zip codes and counts are well-formed.
    # Using this regex to try and only find numbers in them.
    numberParser = re.compile(r'[^\d.]+')

    zipsDict = {}
    for i in xrange(len(data[0])):

        zipCode = data[0][i]
        zipCount = numberParser.sub('', data[1][i])   # I'm not actually sure if this is a count. It looks like it might be, but there's no description anywhere.

        # I am likewise going to assume that any entry (aka a blank one) is just "1".
        if zipCount is '':
            zipCount = 1
        if zipCode is '':
            continue
        # It seems like there are a bunch of errors  in the formatting
        # This is attemptin gto deal with that noise
        elif len(zipCode) > 5 and zipCode[0:5].isdigit():
            zipCode = zipCode[0:5]
        elif len(zipCode) > 5 and zipCode.isdigit():
            print zipCode
            continue

        try:
            if zipCode in zipsDict:
                zipsDict[zipCode] += int(zipCount)
            else:
                zipsDict[zipCode] = int(zipCount)
        except ValueError:
            print "Value Error occured for ZipCode", zipCode, " and count", zipCount

    return zipsDict

class Borough:
    name = None
    zipcodes = None

    def __init__(self, name):
        self.name = name
        self.zipcodes = []

    def __eq__(self, other):
        return other.name == self.name

    def addZipcode(self, zip):
        self.zipcodes.append(zip)

    def getTotalPopulation(self):
        pass

    def getAveragePopulation(self):
        pass

def GetZipsBorough():
    '''
    I've decided I like the dictionary mehtod better than the clas methof for thos example.
    '''
    parser = ParseCSV(boroughsFile)
    (fields, data) = parser.getRawData()

    zipBoroughs = {}

    for listItem in data:
        zipCode = listItem[0]
        borough = listItem[1]

        if zipCode not in zipBoroughs:
            zipBoroughs[zipCode] = borough

    return zipBoroughs

