#Your task is to perform some computations based on this file. Your
#code should compute the population density(ratio between population and
#area) in each zip code and output it in a file called
#"output_density_problem2.txt". Zip codes with no population
#information should be ignored. The lines should contain the zip code
#and the calculated density (separated by a white space). The lines also
#should be sorted by the zip code in "lexicographical order".

import csv
import sys
from operator import itemgetter


#NOTE: 6390, although being the smallest number, will appear at the end of
#the file because lexicographical order characterizes first by first digit,
#then second if they are they same, etc. Lexicographical does not
#necessarily equal ascending order because it's not comparing whole numbers.
def populationDensity(line):
    #ratio bewteen population and area
    #total population /area = population density
    arr = line.split(",")
    if (arr[10]):
        population = int(arr[10])
        area = float(arr[7])
        zipCode = arr[1]
        outputFile = open('output.txt', 'w')
        density = population/area
        #zipcode density
        textToSave = zipCode + " " + str(density) + "\n"
        #write to a temporary file because we have to sort them later
        with open("output_density_problem2_temp.txt", 'a') as f: 
            f.write(textToSave)

def sortData():
    #read file that contains the zips and density
    with open ("output_density_problem2_temp.txt", 'r') as toSort:
        lines = [line.split() for line in toSort]
    #sort the file
        lines.sort(key=itemgetter(0))
    #write the sorted info to the real file and display
    with open ("output_density_problem2.txt", 'a') as fi:
        for index in lines:
            fi.write(index[0]+" "+index[1]+"\n")
        


def main():
    data = open("zipCodes.csv", "r")
    columnHeader = True
    for line in data:
        if columnHeader:
            columnHeader = False
            continue
        line = line.strip()
        populationDensity(line)
    sortData()


if __name__ == "__main__":
    main()
