import sys
import borough as boroughClass
boroughInput =sys.argv[0]
boroughInput =boroughInput.title()
boroughName= open ('boroughs.csv','r')
zippop= open('zipCodes.csv','r')
#setting the input as part of the boroughClass
boroughObj= borough(boroughInput)

#add the list of the zip codes to the boroughClass
boroughDict=csv.DictReader(boroughName,'zipvalues','name')
for row in boroughDict:
	if row['name']==boroughInput:
		boroughObj.addZipcode(row['zippop)'])

		#get the total population
popboInput=csv.DictReader(zippop)
totalpop = 0
count = 0
for row in popboInput:
	if row ['total pop per zip'] != '':
		population = row ['total pop per zip']
		zipCode = row ['name']
		if zipCode in boroughObj.zipCodes:
			count =count +1
			totalpop = totalpop + int(pop)

			#average =
			boroughObj.calcAvgPop(totalpop,count)
			print boroughObj.avg
		main()
