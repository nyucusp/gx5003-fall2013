import csv  #read the csv file
myFileRaw = open('zipCodes.csv','r')
myFile=csv.DictReader(myFileRaw, delimiter=',')
output=[]

for line in myFile:
    zipCode=line['zip code tabulation area']
    if (line['Total Population per ZIP Code']!=''): #ignore the zip code without population
        pop=int(line['Total Population per ZIP Code'])
        area = float(line['area'])
        density=round(pop/area,2)
        output.append([zipCode,density])

output.sort(key=lambda variable:variable[0]) #sorted by the zip code

outputFile = open('output_density_problem2.txt','w')
for line in output:
     lineFormat = str(line[0]) + " " + str(line[1]) + "\n" #convert list to string for output  
     outputFile.write(lineFormat)
outputFile.close()
myFileRaw.close()
