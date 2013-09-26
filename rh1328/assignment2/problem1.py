import sys
from dateutil import parser

def compare(sysDatetime,logFile):
	#input: python problem1.py "09/19/2013 09:12:15"
	#sysDatetime = only in parenths
	#parses input date and time into datetime object
	sysDateTime = parser.parse(sysDatetime)
	print sysDateTime

	for line in logFile:
		#since line goes through the file sequentially, we can 
		# hold onto author and commit names to display the commits
		# as well as looking for the date. Since the look for Author
		#and commit happens before date, it will be the corresponding
		#date to the author and commit (because it's sequential)
		if line.find("commit") != -1:
			commit = line
		if line.find("Author: ") != -1:
			author = line
		dateIndex = line.find("Date: ") 
		if dateIndex != -1:
			fileDateTime = line[12:32]
			convertedFileDt = parser.parse(fileDateTime)
			if convertedFileDt > sysDateTime:
				print author, commit, convertedFileDt
				#print convertedFileDt 	

def main():
	logFile = open('logAfterAssignment1.txt', 'r')
	datetime = sys.argv[1]
	compare(datetime, logFile)

if __name__ == "__main__":
	main()
