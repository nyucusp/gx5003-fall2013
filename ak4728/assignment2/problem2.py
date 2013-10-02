import csv, sys
#Read csv file as a list
csvfile = list(csv.reader(open('Zipcodes.csv')))
#Create a new list of dictionaries
csvdics = []
#Converts every row into a dictionary
for row in csvfile:
    row_dict = {}
    for i in (1,7,10): #We only need row 1,7, and 10
        row_dict['column_%s' % i] = row[i] #Gives every column a name such as column_1
    csvdics.append(row_dict)
#Two different lists for Zip Codes and Population Densities
list1 =[]
list2 = []
for i in range(1, 2451): #This can be changed to len(row)
    x = csvdics[i].values() #x is a list which includes the zipcode, population and area
    a = ' '.join(csvdics[i].values()) #joins them together to split them
    b = a.split(' ') 
    area = b.pop(0) 
    pop = b.pop(0)
    id = b.pop(0) #Zip code
    if(x[1]==''): #Zip codes with no population information is ignored, instead of x[1] id can be used here. I am just lazy
        i=i+1
    else:
        list1.append(float(pop)/float(area)) #calculates the population density
        list2.append(id) #Zipcodes 

dict = dict(zip(list2, list1)) #creates a dictionary with values of zipcodes and densities

outputFile = open('output_density_problem2.txt','w')
outputFile.write( "Zip Code\tPopulation Density\n") #header
for key in sorted(dict.iterkeys()): #sorted list
    outputFile.write(str(key) + "\t\t" + str(dict[key])+"\n")

