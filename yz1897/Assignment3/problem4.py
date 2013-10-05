# -*- coding: utf-8 -*-
"""
Created on Wed Oct 02 17:04:13 2013
@author: Frank Zha,NetID yz1897
"""
#this global variable holds the relative directory of input file
input_filename="input4.txt"

from problem1 import getlines


def Locate_Char(ch,matrix):
    '''
    find all coordinate of a given charactor
    '''
    y=0;char_pos_list=[]
    for line in matrix:
        for x in range(len(line)):
            if line[x]==ch:
                char_pos_list.append((y,x))
        y+=1
    return char_pos_list

def move(pos,di):#move all coordinate in a frame to a direction
    new_pos=[]
    for i in pos:
        new_pos.append((i[0]+di[0],i[1]+di[1]))
    return new_pos
    
def intersect(a,b):#find overlapping point in a frame
    x=[]
    for i in a:
        if i in b:
            x.append(i)
    return x

def Find_Strings(wdf):
    words=wdf[1]
    matrix=wdf[0]
    
    directs=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(-1,1),(1,-1)]

    for word in words:
        wordlen=len(word)
        '''
        for each charactor in the word, there is
        an array of coordinate where the char
        appears in the matrix, I call it a frame
        The frames are ordered according to 
        the sequence of chars in the word.
        The idea is:
            Move first frames to each direction, on the
            way of movement, find a point in first frame
            that have overlaping points in all rest frames.
        '''
        frame_list=[]
        for i in range(wordlen):
            frame_list.append(Locate_Char(word[i],matrix))                    
        
        possible=[]
        for di in directs:
            head=frame_list[0]
            for i in range(1,wordlen):

                head=move(head,di)#move one step to a direction
                head=intersect(head,frame_list[i])
                if len(head)==0:
                    break
            if len(head)!=0:
                back_direction=(-di[0]*(wordlen-1),-di[1]*(wordlen-1))
                head=move(head,back_direction)
            possible.extend(head)
        print possible[0][0]+1,possible[0][1]+1
            
    
def Parse_data(lines):
    '''
    Make the lines from data structured
    '''
    case_count=int(lines[0])
    lines=[line.lower() for line in lines]
    startline=2
    Waldorfs=[]
    matrix=[]
    while case_count>0:
        case_count-=1
        x,y=lines[startline].split(' ')
        matrix=lines[startline+1:startline+int(x)+1]
        z=int(lines[startline+int(x)+1])
        tests=lines[startline+int(x)+2:startline+int(x)+2+z]
        Waldorfs.append((matrix,tests))
    return Waldorfs
    
        
if __name__=="__main__":    
    lines=getlines(input_filename)
    Waldorfs=Parse_data(lines)
    for wdf in Waldorfs:
        Find_Strings(wdf)
        print ""
    
    
    