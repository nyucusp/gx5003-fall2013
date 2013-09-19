#Kara Leary
#Assignment 1 - Problem 3
#Urban Informatics

import sys
import numpy
import array

lines=sys.argv[1]
newlines = lines.split('\\n')
fields=0
k=0
last='false'

for lines in newlines:


        fields=fields+1
        nm = newlines[k]
        n = int(nm[0])
        m = int(nm[2])

        array=numpy.zeros((n,m))

        for i in xrange(1+k,n+k+1):
                currentline=newlines[i]
                for j in xrange(0,m):
                        currentspot=currentline[j]
                        if currentspot=='*':
                                if i==1+k:
                                        array[i-k,j]+=1
                                        if j!=0:
                                                array[i-1-k,j-1]+=1
                                                array[i-k,j-1]+=1
                                        if j!=m-1:
                                                array[i-1-k,j+1]+=1
                                                array[i-k,j+1]+=1
                                        elif j==0:
                                                array[i-1-k,j+1]+=1
                                                if i!=1+k:
                                                        array[i-2-k,j+1]+=1
                                                        array[i-2-k,j]+=1
                                                if i!=n+k:
                                                        array[i-k,j]+=1
                                                        array[i-k,j+1]+=1
                                elif i==n+k:
                                        array[i-2-k,j]+=1
                                        if j!=0:
                                                array[i-2-k,j-1]+=1
                                                array[i-1-k,j-1]+=1
                                        if j!=m-1:
                                                array[i-2-k,j+1]+=1
                                                array[i-1-k,j+1]+=1
                                elif j==m-1:
                                        array[i-1-k,j-1]+=1
                                        if i!=k+1:
                                                array[i-2-k,j-1]+=1
                                                array[i-2-k,j]+=1
                                        if i!=n+k:
                                                array[i-k,j-1]+=1
                                                array[i-k,j]+=1	
                                else:
                                        array[i-2-k,j-1]+=1
                                        array[i-2-k,j]+=1
                                        array[i-2-k,j+1]+=1
                                        array[i-1-k,j-1]+=1
                                        array[i-1-k,j+1]+=1
                                        array[i-k,j-1]+=1
                                        array[i-k,j]+=1
                                        array[i-k,j+1]+=1


        count=0
        print 'Field #', fields
        for i in range(0+k,n+k):
                currentline=newlines[i+1]
                count=0
                for j in range(0,m):
                        currentspot=currentline[j]
                        if currentspot=='*': 
                                print "*",
                        else: 
                                print int(array[i-k,j]),
                        count+=1
                        if count==m:
                                print ''

        print ''
        
        if last=='true':
                sys.exit()
        
        k = k+n+1
        if k==len(newlines)-n:
                last='true'


