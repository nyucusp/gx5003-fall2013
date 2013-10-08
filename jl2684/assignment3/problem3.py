
import sys
import numbers 
import os 
import ast 
from operator import itemgetter

inputFile = open('input3.txt','r') 
inputLine = inputFile.readlines()

### Clear the Input ### 

inputClean = []
for x in inputLine:
	x =	x.rstrip(os.linesep)
	inputClean.append(x) 

#print inputClean

casenumbercounter = 1 
for x in inputClean: 
	if x == str(casenumbercounter):
		casenumbercounter = str(casenumbercounter + 1) ## Count the Case ## 
		casenumberindex = inputClean.index(x) 

		### Case Layout ### 
		casenumber = inputClean[casenumberindex]		
		booknumbers = inputClean [casenumberindex + 1][0]
		namenumbers = inputClean [casenumberindex + 1][2]
		print "Scenario " + str(casenumber)

		bookstring = inputClean[(casenumberindex + 2):(casenumberindex + 2 + int(booknumbers))]
		outputnames_list = inputClean[(casenumberindex + 2 + int(booknumbers)):(casenumberindex + 2 + int(booknumbers) + int(namenumbers))]
		
		authors_per_book_list = []
		for x in bookstring:
			authors_per_book_list.append((x[:x.index('.:')]).split('., '))


		all_name_list = [] 
		for x in authors_per_book_list:
			for names in x: 
				all_name_list.append(names)

		## Assign Initially All the values of the Dictionary as "Inifinity" My goal is to change them by the proximity to "Erdos, P" ##
		dic_name_en = dict([names, "infinity"] for names in all_name_list)
		dic_name_en["Erdos, P"] = 0 ## Assign "Erdos, P" Value "0" ## 

		counter = 0 
		while counter <= int(len(all_name_list)):
			for x in authors_per_book_list:
					anchorlist = [] 
					for key, value in dic_name_en.iteritems(): 
						if value == int(counter): ## Each count represents the Proximity to Erdo ## 
							anchorlist.append(key)
							for anchor in anchorlist: 
								if anchor in x: 
									for y in x: 
										if dic_name_en[y] == 'infinity': 
											dic_name_en[y] = (int(counter) + 1) ## If the value hasn't changed, changed to the counter number representing the proximity. ## 
											dic_name_en["Erdos, P"] = 0 ## Keep changing Erdos, P's value to "0" ##
										else: 
											pass ## If the value has already changed in the previous round, skip adding one ##
					else: 
						pass 
			counter += 1 
		### Output ### 
		for x in outputnames_list:
			ym = x[:-1] 
			print str(ym) + '. ' + str(dic_name_en[ym])

inputFile.close