import sys
import gitlog

#collabName = sys.argv[1]

log = gitlog.GitLog('logsofar.txt')

authorDict = log.getAuthorEntryCount()
for k in sorted(authorDict.keys()):
    print k, authorDict[k]


