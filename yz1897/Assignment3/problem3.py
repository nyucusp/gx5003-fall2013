# -*- coding: utf-8 -*-
"""
Created on Fri Oct 04 11:16:11 2013
@author: Frank Zha,NetID yz1897
"""

#this global variable holds the relative directory of input file
input_filename="input3.txt"

def getlines(fname):
    '''
    Get eachlines in a file without return '\n'
    '''
    f=open(fname,"r")
    lines=f.readlines()
    f.close()
    for i in range(len(lines)):
        if lines[i][-1]=='\n':
            lines[i]=lines[i][:-1]
    return lines

def Parse_Input(lines):

    case_number=int(lines[0])
    #read case by case
    currentline=1
    case_container=[]
    while case_number!=0:
        case_number-=1
        case_line_numbers=lines[currentline].split(" ")
        paper_number=int(case_line_numbers[0])
        author_number=int(case_line_numbers[1])
        papers=lines[currentline+1:currentline+1+paper_number]
        authors=lines[currentline+1+paper_number:currentline+1+paper_number+author_number]
        paper_author_container=[]
        for paperline in papers:
            co_author_string=paperline.split(':')[0]#regardless of the ":" in paper name
            co_author_list=co_author_string[:-1].split("., ")
            co_author_list=[author_name+'.' for author_name in co_author_list]
            paper_author_container.append(co_author_list)   
        currentline=currentline+1+paper_number+author_number
        case_container.append((paper_author_container,authors))
    return case_container

def Find_Distance(case):
    paper_author_container=case[0];authors=case[1]
    '''
    build neighbor network
    index of neighb_dic is the name of an author
    value of neighb_dic is the set of this author's coauthors 
    '''
    neighb_dic={}
    for authorlist in paper_author_container:
        for author in authorlist:
            if author not in neighb_dic:
                neighb_dic[author]=set(authorlist)
            else:
                neighb_dic[author]=neighb_dic[author].union(authorlist)
    for author in neighb_dic:
        neighb_dic[author]=neighb_dic[author]-set([author])

    '''
    Dijkstra Algorithm
    The idea is to use a set to hold all the authors that 
    can be reached in the co-authoring network from the
    starting author. 
    1. The first author in the set is starting author. 
    The author in the set are selected authors.
    2. Every step, add all Neighbours of the selected 
    author into the set until none of them left or no new
    neighbours can be add anymore.
    3. The step number the first time "Erdos P." is in the 
    set is the result 
    '''
    Erdos='Erdos, P.'    
    for author in authors:
        count=1
        neb=neighb_dic[author]
        
        while Erdos not in neb:
            count+=1
            new_neb=set([])
            for nb in neb:
                new_neb=new_neb.union(neighb_dic[nb])
            if len(new_neb-neb)!=0:#there is new neighbor
                neb=neb.union(new_neb)
            else:
                count='infinity';break
        print author,count
        
    #compute the distance    
        
if __name__=="__main__":    
    lines=getlines(input_filename)
    Cases=Parse_Input(lines)
    for i in range(len(Cases)):
        print "Scenario",str(i+1)
        Find_Distance(Cases[i])
        
