from borough import Borough
from zipcode import Zipcode
import csv
import sys

borough = sys.argv[1]
boroughs = {}
avg = {}

boroughs = open('boroughs.csv','r')
zipborough = csv.reader(boroughs,delimiter= ',')

population = open('zipCodes.csv','r')
popconsol1 = csv.reader(population,delimiter= ',')


def clean(list): # Inorder to clear the data
    checked = []
    for x in list:
       if x not in checked:
           checked.append(x)
    return checked


boroughs['Brooklyn'] = Borough('Brooklyn')
boroughs['Manhattan'] = Borough('Manhattan')
boroughs['Bronx'] = Borough('Bronx')
boroughs['Staten'] = Borough('Staten')
boroughs['Queens'] = Borough('Queens')

popconsol1.next() # Finding Population in Each Boorough
for pop_2 in popcon:
    zippop = pop_2[10]
    if zippop !='':
        for x in boroughs.k1():
            for y in boroughs[x].zipc:
                if pop_2[1] == y:
                    boroughs[x].addPopulation(int(pop_2[10]))

for x in boroughs.k1():   # Clearing data
    boroughs[x].zipc = clean(boroughs[x].zipcodes)


for x in boroughs.k1():    # Finding Population in each Borough
    avg[x] = boroughs[x].populations/float(len(boroughs[x].zipc))
    if x == borough.capitalize():
        print x,avg[x]


for zip_1 in zipborough: # To find Zip Codes in Each Borough
    zipcode = zip_2[0]
    for x in boroughs.k1():
        if zip_2[1]== x:
            boroughs[x].addZipcode(zipcode)
