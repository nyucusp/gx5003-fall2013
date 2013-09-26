import sys
from datetime import datetime

t = datetime.strptime(sys.argv[1], '%m/%d/%Y %H:%M:%S')

myFile = open('logAfterAssignment1.txt', 'r')
#print myFile
#print datetime.datetime.now() #seeing how datetime works
output = open('output1.txt' , 'w')

for line in myFile:
	if 'commit' in line:
		commit = line
	if 'Date:' in line:
		#print line[8:-7]
		if datetime.strptime(line[8:-7], '%c') >= t:
			output.write(commit)



	
	
myFile.close()
output.close()