myFile = open('C:/Users/nivan/Desktop/internshipFiles/shuf_Q13.tsv','r')

myClerk = 'Clerk#000000738'

dictcount = {}
dictsum = {}

for line in myFile:
    indexOfClerk = line.find(myClerk)
    if(indexOfClerk != -1):
        tokens = line.split('\t')
        year = tokens[0]
        if(year in dictcount):
            dictcount[year] = dictcount[year]+1
        else:
            dictcount[year] = 1

        if(year in dictsum):
            dictsum[year] = dictsum[year]+ float(tokens[1])
        else:
            dictsum[year] = float(tokens[1])

for key in dictcount.keys():
    print 'the average in ' + key + ' is ' + str(dictsum[key]/dictcount[key])
