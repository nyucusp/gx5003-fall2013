
def CleanListStrings(strlist):
	''' This is for handling white space and '\n's that appear '''
	for i in xrange(len(strlist)):
		strlist[i] = strlist[i].strip()

def gettype(s):
    """ Given a parameter as a string, return
    a tuple containing (type, value)

    type is in [int, float, str]
    value is the int, float, or string"""
    try:
        return "INT", int(s)
    except ValueError:
        try:
            return "FLOAT", float(s)
        except ValueError:
            return "STR", s		

class ParseCSV(object):
	'''
	ParseCSV is a class for handling all CSV reading.
	'''
	fieldNames = []
	fieldTypes = []
	data = []
	
	def __init__(self, filename, fieldSelect=None, skipHeader=False):
		''' init takes the csv filename.
		and reads the csv into memory.

		fieldSelect allows you to enter a tuple which extracts only the 
		column indexes entered from the file, thereby saving space as necessary.

		use skipHeader if this file lacks a header, or if you want to enter the headers yourself.
			Note: if you make this true, you *have* to enter the header yourself.
		'''

		with open(filename, 'r') as fileHandle:
			if not skipHeader:
				self.readHeader(fileHandle, fieldSelect)
			self.readData(fileHandle, fieldSelect)

		self.parseFieldTypes()

	def readHeader(self, fileHandle, fieldSelect):
		'''
		reads the first line of the csv file, which is the header specifying the
		labels for each column
		'''
		# read the first line for the headers
		firstLine = fileHandle.readline()

		# get the fields from the line
		self.fieldNames = firstLine.split(',')

		# store the fields as the keys in the dict
		CleanListStrings(self.fieldNames)

		if fieldSelect is not None:
			self.fieldNames = [ self.fieldNames[x] for x in fieldSelect if (x < len(self.fieldNames))]

	def readData(self, fileHandle, fieldSelect):
		'''
		reads the lines of data from the csv, parses, and stores them in memory
		'''
		# Initialize data to blank lists of the same length as the data
		self.data = [[] for x in self.fieldNames]

		# now read all the lines in, and append the things to their respective lists
		for line in fileHandle:
			values = line.split(',')

			CleanListStrings(values)
			# If fieldSelect is none, use all the values
			if fieldSelect is None:
				try:
					for ind in xrange(len(self.fieldNames)):
					    self.data[ind].append(values[ind])
				except IndexError:
					print "IndexError!!! <{0}>,<{1}>,<{2}>".format(len(self.fieldNames), len(values), values)
			else:
				# else, grab only the columns we care about.
				for fieldIndex in xrange(len(fieldSelect)):
					self.data[fieldIndex].append(values[fieldSelect[fieldIndex]])

	def parseFieldTypes(self):
		self.fieldTypes = []
		for column in self.data:
			index = 0

			#This is to skip blank things.
			while index < len(column) and column[index] == "":
				index += 1

			self.fieldTypes.append(gettype(column[index])[0])

	def getRawData(self):
		'''
		returns the data as a tuple of
		(labels, [list of data lists])
		'''
		return (self.fieldNames, self.fieldTypes, self.data)

	def getLabelledData(self):
		'''
		returns the data as a dict of
		{ "label" : [data]}
		'''
		dataDict = {}

		for i in xrange(len(self.fieldNames)):
			dataDict[self.fieldNames[i]] = self.data[i]

		return dataDict

class ParseBoroughsCSV(ParseCSV):
	filename = "boroughs.csv"
	def __init__(self):
		super( ParseBoroughsCSV, self ).__init__(self.filename)

		self.fieldNames = ["zipcode", "borough"]

		# Make sure that we have unique zip codes
		# To do this... make it a dict.
		fieldDict = dict(zip(self.data[0], self.data[1]))

		# Reconstruct the data so I don't have to re-write the rest of my program...
		self.data = [[], []]
		for k in sorted(fieldDict.keys()):
			self.data[0].append(k)
			self.data[1].append(fieldDict[k])


class ParseZipCodesCSV(ParseCSV):
	filename = "zipCodes.csv"
	def __init__(self):	
		# For this we skip the header so we can make a prettier one.
		super( ParseZipCodesCSV, self ).__init__(self.filename)

		# So, I know there are some data that have missing entries. 
		# First, I go through and grab all the good ones, putting the bad ones into a separate dict.
		goodData = {}
		badData = []

		for index in xrange(len(self.data[0])):
			# Just grab name, area, population - all we need for this assignment
			name = self.data[self.fieldNames.index("name")][index]
			area = self.data[self.fieldNames.index("area")][index]
			population = self.data[self.fieldNames.index("Total Population per ZIP Code")][index]
			
			if self.validate_input(name, area, population):
				if name not in goodData:
					goodData[name] = [area, population]
				else:
					# So, if it's in the data already, see if the area or population are higher
					if area > goodData[name][0] or population > goodData[name][1]:
						goodData[name] = [area, population]
						# print "Updated data {0}: {1}, {2}".format(name, area, population)
			else:
				badData.append([name, area, population])

		# print "Starting - Good: {0}, Bad: {1}".format(len(goodData.keys()), len(badData))
		
		# Now, recreate the data with only the data we care about.
		self.data = [[], [], []]
		for k in sorted(goodData.keys()):
			v = goodData[k]
			self.data[0].append(k)
			self.data[1].append(v[0])
			self.data[2].append(v[1])

		self.fieldNames = ["zipcode", "area", "population"]

		self.parseFieldTypes()

	def validate_input(self, name, area, pop):
		return name.isdigit() and len(name) == 5 and len(area) > 0 and len(pop) > 0


class ParseIncidentsCSV(ParseCSV):
	filename = "Incidents_grouped_by_Address_and_Zip.csv"
	def __init__(self):
		super( ParseIncidentsCSV, self ).__init__(self.filename)

		self.fieldNames = ["address","zip","count"]

		newData = [[], [], []]
		badDataCount = 0
		for index in xrange(len(self.data[0])):
			address = self.data[0][index]
			zipcode = self.data[1][index]
			count = self.data[2][index]

			if self.validate_input(address, zipcode, count):
				newData[0].append(address)
				newData[1].append(zipcode)
				newData[2].append(count)
			else:
				badDataCount += 1
		# print "Bad Incidents: ", badDataCount

		self.data = newData

	def validate_input(self, addr, zipcode, count):
		return zipcode.isdigit() and len(zipcode) == 5 and count.isdigit()
