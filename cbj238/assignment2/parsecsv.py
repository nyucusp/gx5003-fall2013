
def CleanListStrings(strlist):
	''' This is for handling white space and '\n's that appear '''
	for i in xrange(len(strlist)):
		strlist[i] = strlist[i].strip()

class ParseCSV:
	'''
	ParseCSV is a class for handling all CSV reading.
	'''
	fieldNames = []
	data = []
	
	def __init__(self, filename, fieldSelect=None):
		''' init takes the csv filename.
		and reads the csv into memory.

		fieldSelect allows you to enter a tuple which extracts only the 
		column indexes entered from the file, thereby saving space as necessary.
		'''

		with open(filename, 'r') as fileHandle:
			self.readHeader(fileHandle, fieldSelect)
			self.readData(fileHandle, fieldSelect)

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
				for ind in xrange(len(values)):
					self.data[ind].append(values[ind])
			else:
				# else, grab only the columns we care about.
				for fieldIndex in xrange(len(fieldSelect)):
					self.data[fieldIndex].append(values[fieldSelect[fieldIndex]])

	def getRawData(self):
		'''
		returns the data as a tuple of
		(labels, [list of data lists])
		'''
		return (self.fieldNames, self.data)

	def getLabelledData(self):
		'''
		returns the data as a dict of
		{ "label" : [data]}
		'''
		dataDict = {}

		for i in xrange(len(self.fieldNames)):
			dataDict[self.fieldNames[i]] = self.data[i]

		return dataDict
