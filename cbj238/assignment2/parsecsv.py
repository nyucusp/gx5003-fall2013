
def CleanListStrings(strlist):
	''' This is for handling white space and '\n's that appear '''
	for i in xrange(len(strlist)):
		strlist[i] = strlist[i].strip()

class ParseCSV:
	fieldNames = []
	data = []
	
	def __init__(self, filename):
		with open(filename, 'r') as fileHandle:
			self.readHeader(fileHandle)
			self.readData(fileHandle)

	def readHeader(self, fileHandle):
		# read the first line for the headers
		firstLine = fileHandle.readline()

		# get the fields from the line
		self.fieldNames = firstLine.split(',')

		# store the fields as the keys in the dict
		CleanListStrings(self.fieldNames)

	def readData(self, fileHandle):
		# Initialize data to blank lists of the same length as the data
		self.data = [[] for x in self.fieldNames]

		# now read all the lines in, and append the things to their respective lists
		for line in fileHandle:
		    values = line.split(',')

		    CleanListStrings(values)

		    for ind in xrange(len(values)):
		    	self.data[ind].append(values[ind])

	def getRawData(self):
		return (self.fieldNames, self.data)

	def getDataWithLabels(self):
		dataDict = {}

		for i in xrange(len(self.fieldNames)):
			dataDict[self.fieldNames[i]] = self.data[i]

		return dataDict
