#Your task is to compute the ratio between the number of incidents and
#the population for each borough. Your code should be named "problem3.py".
#It also should output a file called "output_problem3.txt" that contains in
#each line the name of the borough and the calculated ratio (separated by a white space).
#The lines also should be sorted by the borough name in alphabetical order.

#number of incidents per boro
incBo = {'Manhattan':0, 'Staten':0, 'Bronx':0, 'Queens':0, 'Brooklyn':0 }
#dictionary with borough as key, population as value
popBo = {'Manhattan':0, 'Staten':0, 'Bronx':0, 'Queens':0, 'Brooklyn':0 }
#dictionary with zip as key and population as value
zipPop = {}
#dictionary with zip codes as keys, boroughs as values
zipBo = {}
#number of incidents as value, zip as key
numIncDict = {}


def makeNumIncDict():
    #collects the incidents zips as keys and the number of incidents as values
    global numIncDict
    data = open("Incidents_grouped_by_Address_and_Zip.csv", "r")
    columnHeader = True
    for line in data:
        if columnHeader:
            columnHeader = False
            continue
        line = line.strip()
        line = line.split(',')
        dictKey = line[1]
        dictVal = 1
        #figure out number of incidents by counting number of time zipcode repeats.
        if dictKey in numIncDict:
            numIncDict[dictKey] += 1
        else:    
            numIncDict[dictKey]=dictVal
    count = 0
    for key in numIncDict:
        count += numIncDict[key]


def makeZipPopDict():
    #assumes no repeat in zip codes in boroughs and zipcodes files
    global zipPop
    data = open("zipCodes.csv", "r")
    columnHeader = True
    for line in data:
        if columnHeader:
            columnHeader = False
            continue
        line = line.strip()
        arr = line.split(",")
        if (arr[10]):
            population = int(arr[10])
            zipCode = arr[1]
            zipPop[zipCode] = population        
    

def makeZipBoDict():
    #dictionary with zip codes as keys, boroughs as values
    #assumes that there are no repeat zip codes in the boroughs files
    global zipBo
    data = open("boroughs.csv", 'r')
    for line in data:
        line = line.strip()
        arr = line.split(',')
        zipBo[arr[0]]=arr[1]


def makePopBoDict():
    #key is zipcode
    #zipPop[key] = population for that key
    global popBo
    global zipBo
    for key in zipPop:
        zipCode = key
        #zipBo has borough as value, zipcode as key
#not all of the zip codes in zipcodes.csv are present in boroughs.csv (ie, 11542)
        if zipCode in zipBo:
            borough = zipBo[zipCode]
        #find this borough in the popBo dic (boroughs as key, population as value)
            popBo[borough] += zipPop[zipCode]
   # print popBo

def makeIncBo():
    #key is zip, num incidents = value
    global numIncDict
    global incBo
    for key in numIncDict:
        zipCode = key
        if zipCode in zipBo:
            borough = zipBo[zipCode]
            incBo[borough] += numIncDict[zipCode]
    #sprint incBo

def calculateRatio():
    #number of incidents/population
    #num of inc per borough is in incBo
    #population is in popBo, keys both = boroughs
    finalDict = {'Manhattan':0, 'Staten':0, 'Bronx':0, 'Queens':0, 'Brooklyn':0 }
    for key in incBo:
        incidents = incBo[key]
        population = popBo[key]
        ratio  = 1.*incidents/population
        finalDict[key] += ratio
#sort by borough, write to file called ouput_problem3.txt
    outputFile = open('ouput_problem3.txt', 'w')
    for temp in sorted(finalDict.iterkeys()):
        toPrint = str(temp) + ' '+ str(finalDict[temp]) + '\n'
        outputFile.write(toPrint)
        #print temp, finalDict[temp]
        
    
def main():
    makeZipBoDict()
    makeZipPopDict()
    makeNumIncDict()
    #print zipBo
    #print zipPop
    #print numIncDict
    makePopBoDict()
    makeIncBo()
    calculateRatio()
                
if __name__=="__main__":
    main();
