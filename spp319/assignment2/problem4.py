import sys

class Boro():
    def __init__(self):
        #self.name = name
        self.zipCodes = []
        self.pop = 0

    def avgPop(self):
        return float(self.pop) / len(self.zipCodes)

boros = {
    "manhattan": Boro(),
    "bronx": Boro(),
    "queens": Boro(),
    "staten": Boro(),
    "brooklyn": Boro(),
}

lines = open('boroughs.csv').readlines()
for line in lines:
    columns = line.split(',')
    boroName = columns[1].strip().lower()
    zipCode = int(columns[0])

    if boroName in boros:
        boros[boroName].zipCodes.append(zipCode)

#print man.zipCodes

i = 0
lines = open('zipCodes.csv').readlines()
lines.pop(0)
for line in lines:
    columns = line.split(',')
    if columns[1].isdigit() and columns[10].strip():
        zipCode = int(columns[1])
        zipPop = int(columns[10])

        for boro in boros.values():
            if zipCode in boro.zipCodes:
                boro.pop += zipPop

boro = sys.argv[1].strip().lower()
print boros[boro].avgPop()
