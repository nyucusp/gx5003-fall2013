myFile=open('input3.txt','r')#read the input file and put all data into an array
readdata=[]
for line in myFile:
	readdata.append(line[:-1])
myFile.close



author_database=[]
author=[]
def get_casedata(readdata):
	for i in range(0,int(readdata[0])):
		startline=0
		database_num=int(readdata[startline+1].split()[0])#get the number of lines of database
		name_num=int(readdata[startline+1].split()[1])#get the number of lines of names

		database=readdata[startline+2:startline+2+database_num]#get the data of database
		name=readdata[startline+2+database_num:startline+database_num+name_num+2]#get the data of author names
		startline=startline+database_num+name_num+2#the startline of next case
		
		for j in database:
			allnames=j.split(",")[0]#delete the paper info
			allname=allnames[:-1]#delete the :
			namedata=allname.split(".,")#split the names
			namedata=[everyname+'.' for everyname in namedata]#add "." into the end of each name
			author_database.append(namedata)
		author.append((author_database,name_num))
		print author	
author=get_casedata(readdata)

