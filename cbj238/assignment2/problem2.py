from zipcodes import *

zipDensityDict = GetZipPopulationDensity()

outFile = open("output_density_problem2.txt", 'w')
for k in sorted( zipDensityDict.keys() ):
    outFile.write(k + " " + str(zipDensityDict[k]) + "\n")

outFile.close()