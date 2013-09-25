from zipcodes import *

zipDensityDict = GetZipPopulationDensity()

outFile = open("output_density_problem2.txt", 'w')
for k in sorted( resultDict.keys() ):
    outFile.write(k + " " + str(resultDict[k]) + "\n")

outFile.close()