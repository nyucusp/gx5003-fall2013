#compute avg population of the zip areas of a given borough
#output = just number, avg population
import sys

class Borough:
    name = None
    #array of zipcode types
    zipcodes = None
   
    def __init__(self, name):
        self.name = name
        self.zipcodes = []
 
    def addZipcode(self, zipp):
        self.zipcodes.append(zipp)

    def avgPop(self):
       #calculates average population of that borough
        total = 0
        cnt = 0
        for obj in self.zipcodes:
            #there is no population data for some zips, so we must count the number
            #of zips that have population data in osrder to accurate compute total
            if obj.population != None:
                cnt += 1
                total += obj.population
		print total
		print cnt
        average = total/cnt
        return average
        
class Zipcode:
    number = None
    #population per zip
    population = None
    
    def __init__(self, number):
        self.number = number

def main():
    boroughInput = sys.argv[1]
    
    manhattan = Borough('Manhattan')
    bronx = Borough('Bronx')
    brooklyn = Borough('Brooklyn')
    staten = Borough('Staten')
    queens = Borough('Queens')

#populate the zipcodes arrays in each object with zipcode object which has
#attributes number and population
    data = open("boroughs.csv", 'r')
    for line in data:
        line = line.strip()
        arr = line.split(',')
        zipcode = Zipcode(arr[0])
        if arr[1] == 'Brooklyn':
            brooklyn.addZipcode(zipcode)
        elif arr[1] == 'Manhattan':
            manhattan.addZipcode(zipcode)
        elif arr[1] == 'Bronx':
            bronx.addZipcode(zipcode)
        elif arr[1] == 'Staten':
            staten.addZipcode(zipcode)
        elif arr[1] == 'Queens':
            queens.addZipcode(zipcode)


#the following code adds populations to the zipcode (population is  a member of the Zipcode class)
#zip and population are accessed by ---- for i in borough: i.number =, i.population = 
    zipdata = open("zipCodes.csv", "r")
    columnHeader = True
    for lines in zipdata:
        if columnHeader:
            columnHeader = False
            continue
        lines = lines.strip()
        arrs = lines.split(",")
        if (arrs[10]):
            pop = int(arrs[10])
            zipCode = arrs[1]

#add population to Zipcode objects
            for objects in brooklyn.zipcodes:
                if objects.number == zipCode:
                    #print zipCode
                    zipIndex = brooklyn.zipcodes.index(objects)
                    brooklyn.zipcodes[zipIndex].population = pop

            for objects in manhattan.zipcodes:
                if objects.number == zipCode:
                    #print zipCode
                    zipIndex = manhattan.zipcodes.index(objects)
                    manhattan.zipcodes[zipIndex].population = pop

            for objects in staten.zipcodes:
                if objects.number == zipCode:
                    #print zipCode
                    zipIndex = staten.zipcodes.index(objects)
                    staten.zipcodes[zipIndex].population = pop

            for objects in queens.zipcodes:
                if objects.number == zipCode:
                    #print zipCode
                    zipIndex = queens.zipcodes.index(objects)
                    queens.zipcodes[zipIndex].population = pop

            for objects in bronx.zipcodes:
                if objects.number == zipCode:
                    #print zipCode
                    zipIndex = bronx.zipcodes.index(objects)
                    bronx.zipcodes[zipIndex].population = pop

#handle input and output proper avg population
    if boroughInput == 'brooklyn':
        print brooklyn.avgPop()
    elif boroughInput == 'queens':
        print queens.avgPop()
    elif boroughInput == 'bronx':
        print bronx.avgPop()
    elif boroughInput == 'statenisland':
        print staten.avgPop()
    elif boroughInput == 'manhattan':
        print manhattan.avgPop()
    else:
        print "not a valid input."
                    
    
if __name__ == "__main__":
    main()
    

