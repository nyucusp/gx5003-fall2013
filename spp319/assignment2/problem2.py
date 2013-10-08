lines =  open('zipCodes.csv').readlines()
header = lines.pop(0).strip().split(',')

density_by_zip = {}
for line in lines:
    columns = line.strip().split(',')

    _zip = columns[1]
    if columns[7] and columns[10]:
        area = float(columns[7])
        pop = int(columns[10])
        density_by_zip[_zip] = pop / area

outFile = open("output_density_problem2.txt", "w")
for z in sorted(density_by_zip.keys()):
    print >> outFile, z, density_by_zip[z]

outFile.close()

"""

with open('zipCodes.csv', 'rb') as f:
    next(f)
    scanner = csv.reader(f)

    for col in scanner:

        numOfRec = len(col)
        #print numOfRec
        #populate lists of areas and pops
        zipInfo = [ col[7], col[10]]
        #print zipInfo
        #populate dictionary with zip as keys to lists of area and pop
        zipDict = { col[0]: zipInfo}
        newZipDict = { col[0]: zipInfo}
        #print newZipDict
        #print zipDict

        def returnZips():
            #clean out empty populations
            for keys in zipDict:
                tempInfo = zipDict[keys]
                if not tempInfo[1]:
                    del newZipDict[keys]

                else:
                    newZipDict.update({keys : zipDict[keys]})
                #return newZipDict
            return newZipDict

        finalDict = finalDict.update(returnZips())
        k=[]
        z=[]
        #k = finalDict.keys()
        i=0

        print len(k)


        outFile = open('output_density_problem2.txt', 'w')
        outFile.write("|  Zip Code  |  Population Density  |\n")
        for keys in sorted(finalDict.iterkeys()):
            outFile.write(str(keys) + "    " + str(finalDict[keys]))











# def round_num(a,b):
#     num = round(a,b)
#     return num

# user_num = float(sys.argv[1])
# to_what = int(sys.argv[2])

# print round_num(user_num, to_what)

# def csvCache(a,b):

"""
