myFile = open('input3.txt', 'r')
input_lines = []
for line in myFile:
	if line[-1] == '\n':
		input_lines.append(line[:-1])
myFile.close()

def get_scenerio_info(input_lines):
	scenerios_context=[]
	paperlines_parse=[]
	paper_author_context=[]
	scenerio_number=int(input_lines[0])
	for i in range(1,len(input_lines)):
			scenerios_context.append(input_lines[i])
	startline=0
	for s_number in range(scenerio_number):
		paper_number=int(scenerios_context[startline+0].split()[0])
		author_number=int(scenerios_context[startline+0].split()[1])
		paper_lines=scenerios_context[startline+1:startline+paper_number+1]#get paper database 
		author_list=scenerios_context[startline+1+paper_number:startline+paper_number+author_number+1]#get author name
		startline=startline+paper_number+author_number+1
	
		#clean the papper database input by removing ".:" and ".,"
		for papers in paper_lines:
			co_author_name_string=papers.split(":")[0]
			s=co_author_name_string[:-1]
			co_author_list=s.split("., ")
			co_author_list=[author_name+'.' for author_name in co_author_list]#add "." in the end of the last author
			paperlines_parse.append(co_author_list)
		paper_author_context.append((paperlines_parse,author_list))
		return paper_author_context

paper_author_context=get_scenerio_info(input_lines)

def get_Erdos_number(paperlines_parse,author_list):
    co_authors_dict={}
    for co_author_relaitonhsip in paperlines_parse:
        for co_author in co_author_relaitonhsip:
            if co_author not in co_authors_dict:
                co_authors_dict[co_author]=set(co_author_relaitonhsip)
            else:
                co_authors_dict[co_author]=co_authors_dict[co_author].union(set(co_author_relaitonhsip))

    Erdos='Erdos, P.'
    for author in author_list:
        searched=set([])
        distance=1
        searched=searched.union(co_authors_dict[author])
        while Erdos not in searched:        
            distance+=1
            new_searched=set([])
            for au in searched:
                new_searched=new_searched.union(co_authors_dict[au])
            if len(new_searched.difference(searched))==0:
                distance="infinity"
                break
            searched=searched.union(new_searched)
        print author,distance

for i in range(len(paper_author_context)):
    print "Scenario" ,str(i)
    get_Erdos_number(paper_author_context[i][0],paper_author_context[i][1])




