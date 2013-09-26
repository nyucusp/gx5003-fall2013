import sys
#This program receives a date and time (in 24HR format), identifies all the commits that happened 
#after this date and time, and outputs the commit's Author and Date to indicate delay in submitting files

from datetime import datetime  #importing datetime class from same-name module
# Combination of date & time. 
# Attributes: year, month, day, hour, minute, second, microsecond, & tzinfo

from dateutil.parser import parse #since datetime alone is not enough, because %z doesn't work for datetime.strptime and 

#CutOff = datetime.strptime(sys.argv[1],"%m/%d/%Y %H:%M:%S")

CutOff = parse(sys.argv[1]+' -0400') #I'm assuming the same timezone 

myFile = open('logAfterAssignment1.txt','r')

'''
The format of each commit record is:
	commit f220498760e845be957e21e889f6be512aa60ed6
	Merge: f9f79ee a2fadd7
	Author: Nivan Ferreira <nivan.ferreira@gmail.com>
	Date:   Fri Sep 20 10:27:36 2013 -0400

Or:
	commit a2fadd736d9705d5d86aeb175de1275319da70d9
	Author: ke638 <elliott.katherine.s@gmail.com>
	Date:   Fri Sep 20 10:21:57 2013 -0400

Date line is after Author line, so we must park the Author name while parsing till Date is checked against CutOff
'''

print 'The commits after cutoff date & time of' , CutOff , 'are:'

global AuthorTemp
AuthorTemp = ""

for line in myFile:
	#Line will be commit, merge, Author, or Date. The first two are of no interest at this point
	GetAuthor = line.find("Author:")
	if (GetAuthor != -1): #found an Author line
		AuthorTemp = line [8:] 
		#Park the Author value in a temp slot till Date is checked 
		#location 8 is where the value of the Author starts	in our file	
		#When if exits, the "for" loops to next line (Date:), where the below "if" validates Date vs CutOff
		
	else:
		GetDate = line.find("Date:")
		if (GetDate != -1): #found Date line w/ format "Date:   Fri Sep 20 10:27:36 2013 -0400" in 24HR format
			commitDateStr = line [12:]
			#We take string starting at location 12, since we have a date & can ingore the day of the week 
			'''
			For late investigation:
			The .txt file can have a day of the month which is not zero-padded, so using strptime with %d doesn't work, 
			even with some string manipulation to insert the zero. 
			I was also getting errors when using %z ('z' is a bad directive in format) when using it for timezone.
				
			'''
			DateToValidate = parse(commitDateStr)
			if DateToValidate > CutOff:
				print DateToValidate
				print AuthorTemp
			
	

myFile.close()
