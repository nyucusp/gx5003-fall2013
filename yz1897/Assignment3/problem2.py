# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 15:37:31 2013
@author: Frank Zha,NetID yz1897
"""

#this global variable holds the relative directory of input file
input_filename="input2.txt"

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

def Parse_Input(lines):#parse the input
    vote_container=[]
    '''
    Contains the structured data of each case
    vote_container=[(candi_list,order_container),...]
    candi_list contains ordered name list of candidates
    order_container=[orderlist,...]
    orderlist=[order,...] like [1,2,4,3]
    '''    
    case_number=int(lines[0])    
    case_container=[]#contains each lines in a case in a list
    #use empty line to seperate the cases
    blankline=[]
    for line_count in range(len(lines)):#find the index of the blank lines
        if lines[line_count]=='':
            blankline.append(line_count)

    for n in range(case_number-1):#seperate lines by cases
        case=lines[blankline[n]+1:blankline[n+1]]
        case_container.append(case)
    case=lines[blankline[case_number-1]+1:]#the last case is different
    case_container.append(case)
    
    #parse each case
    for case in case_container:
        candi_list=[]
        order_container=[]
        candi_number=int(case[0])
        candi_list=case[1:1+candi_number]
        for vote_string in case[1+candi_number:]:
            order_list=[]
            for o in vote_string.split(" "):
                order_list.append(int(o))
            order_container.append(order_list)
        vote_container.append((candi_list,order_container))        
    return vote_container

def frequence_count(vote_list):
    frequence={}
    #caculate voters frequence of being the first choise
    for i in vote_list:
        if i[0] not in frequence:
            frequence[i[0]]=0
        frequence[i[0]]+=1
    return frequence

def order_frequence(frequence):
    #order the voters by frequence of being first choise
    tobeorder=[]
    for voter in frequence:
        tobeorder.append((frequence[voter],voter))
    return sorted(tobeorder)
    
    
def Rank_Result(cases):
    count=0
    for case in cases:
        count+=1
        vote_list=case[1]
        voter_list=case[0]
        #print voter_list #this line is for test
        while len(vote_list)!=0:
            #print vote_list #this line is for test
            frequence=frequence_count(vote_list)
            ordered_voter_list=order_frequence(frequence)
            if ordered_voter_list[-1][0]>0.5*len(vote_list):
                #if one with largest votes larger than 50 percent
                print voter_list[ordered_voter_list[-1][1]-1]
                break
            elif ordered_voter_list[-1][0]==ordered_voter_list[0][0]:
                #if largest and smallest are equal: every one tied tied
                #print ordered_voter_list #this line is for test
                for voters in frequence:
                    #print voter_list[voters-1],frequence[voters] #this line is for test
                    print voter_list[voters-1]
                break
            else:#delete the last one
                lowest=ordered_voter_list[0][0]
                lastones=[]
                for voters in frequence:
                    if frequence[voters]==lowest:
                        lastones.append(voters)
                new_vote_list=[]
                #use a new list to backup all the right-after-deleting voting result
                for individual_orders in vote_list:
                    for lastone in lastones:
                        individual_orders.remove(lastone)
                    if len(individual_orders)!=0:
                        new_vote_list.append(individual_orders)
                vote_list=new_vote_list
        if count<len(cases):#avoid blanking after the last output
            print ''            
            
'''Test the Parse_Input'''
if __name__=="__main__":
    lines=getlines(input_filename)
    
    vote_container=Parse_Input(lines)    
    Rank_Result(vote_container)

