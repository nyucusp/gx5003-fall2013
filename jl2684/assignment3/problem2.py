
import sys
import numbers 
import os 
import ast 
from operator import itemgetter

inputFile = open('input2.txt','r') 
inputLine = inputFile.readlines()

### Clearn the Data ### 

inputClean = []
for x in inputLine:
	x =	x.rstrip(os.linesep)
	inputClean.append(x) 

casecounter = 0 
for x in inputClean: 
	if x == str(''):
		if casecounter == 1:
			print '' ## Adding Space in between more than one election result output ## 
		else: 
			casecounter = 1 

		### Identified Input Information ### 
		numberofcase = inputClean[inputClean.index('') - 1] 
		indexofnumberofcase = inputClean.index('') - 1 
		indexofnumberofcandidates = inputClean.index('') + 1 
		numberofcandidates = inputClean[indexofnumberofcandidates] 
		## No need to worry about the number of candidates being double digit (n <= 20), since it's on a seperate line ##

		### List of Candidates ###  
		listofcandidates =[]
		countforcandidates = 1 
		while countforcandidates <= int(numberofcandidates):
			listofcandidates.append(inputClean[indexofnumberofcandidates + countforcandidates])
			countforcandidates += 1

		### List of Voters ###
		listofvotes = []
#		countforvotes = 1 
		listofvotes = inputClean[(int(indexofnumberofcase) + 3 + int(numberofcandidates)):]

		listofvotessplit = []
		for x in listofvotes: 
			listofvotessplit.append(x.split()) 

		### Dictonary of Voters ### 
		dictofvoters = []
		for x in listofvotessplit:
			dictofvoters.append(dict(zip(x, listofcandidates)))

		### Vote Counting ### 		
		roundcounter = 0
		roundwinnerlist = []
		listofminimum = [] 	

		while roundcounter != len(listofcandidates):	
			for x in dictofvoters:
				roundwinnerlist.append(x['1'])

			if roundwinnerlist.count(listofcandidates[roundcounter]) > (len(listofvotes)*.5):
				print max(roundwinnerlist) 
				break
				## Checked if the first round produced the winner over 50% ##  

			else: 
				roundcounter += 1 
				listofminimum.append(map(itemgetter('1'), dictofvoters).index(min(roundwinnerlist)))
				## Identified the voters who voted for the elimiated candidate ## 

				for x in listofminimum:
					n = dictofvoters[x]

					n[str(0)] = n.pop(str(1)) ## Change the Eliminated Choice's Rank to '0' ##
					n[str(1)] = n.pop(str(roundcounter + 1))	## Change their next choices as their first choice ## 

inputFile.close 