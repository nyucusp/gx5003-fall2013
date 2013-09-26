import sys

class Borough:
	zipcodes = None
	def __init__(self):
		self.zipcodes = {}
	def addZipcode(self,zip,pop):
		self.zipcodes[zip]=pop
	def avPop(self):
		sum = 0
		for k in self.zipcodes.keys():
			sum=sum+self.zipcodes[k]
		return sum/float(len(self.zipcodes.keys()))

zip2bor = {}
fboroughs = open('boroughs.csv')
for line in fboroughs:
	tokens = line.replace('\n','').split(',')
	zip2bor[tokens[0]]=tokens[1]

fzipcodes = open('zipCodes.csv','r')
bor2pop = {'Bronx':Borough(),'Staten':Borough(),'Manhattan':Borough(),'Brooklyn':Borough(),'Queens':Borough()}
for line in fzipcodes:
	tokens = line.replace('\n','').split(',')
	if tokens[10].isdigit() and tokens[0] in zip2bor:
		bor2pop[zip2bor[tokens[0]]].addZipcode(tokens[0],int(tokens[10]))

print str(bor2pop[sys.argv[1]].avPop())

