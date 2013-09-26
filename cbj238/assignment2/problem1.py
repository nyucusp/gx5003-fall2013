import sys
import gitlog
from dateutil.parser import parse

dateIn = parse(sys.argv[1])

log = gitlog.GitLog('logsofar.txt')
entryList = log.getEntriesAfterDate(dateIn)

for entry in entryList:
    print entry
print "========================================================="
print "There were", len(entryList), "entries after the date input"

'''authorDict = log.getAuthorEntryCount()
for k in sorted(authorDict.keys()):
    print k, authorDict[k]'''


