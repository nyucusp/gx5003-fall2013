def main():
    f = open('input3.txt', 'r') # get the input file
    search = '\n' # find '\n' in the input file
    replace = '' 
    lst = f.readlines() #read lines in the input file 
    lst2 = [x.replace(search, replace) for x in lst] #replace the \n with blank in the input list
    erdos = {} # this is the erdos number
    authors = []
    output = ['Smith, M.N.','Hsueh, Z.','Chen, X.']
    
    for line in lst2:
        if ':' in line:
            auline,papers = line.split(':') # in order to select the author in each scenario line, divide it into several chunks  
            author = auline.split(', ') # to find the author, seperate it by comma
            author = map(', '.join, zip(author[::2], author[1::2]))
        else:
            break
        authors.append( author ) # add the name of authors
        for au in author:
            erdos[ au ] = None
    erdos['Erdos, P.'] = 0
    
    for i in authors:
        mi = None
        for a in i:
            if erdos[a] != None and ( erdos[a]<mi or mi is None ):
                mi = erdos[a] #get the numbers

        if mi != None:
            for a in i:
                if erdos[a] == None:
                    erdos[a] = mi+1

    for au in output:
        print au, str(erdos[au]).replace("None", "infinity")
    
if __name__ == '__main__':
    main()
