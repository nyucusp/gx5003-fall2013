import sys
import numpy

"""
SECTION 1: INPUT PARSING
"""



"""
First we open the text file and save the lines to the list input_lines.  Please note
this program is NOT robust enough to handle input that differs even slightly from
the format in the problem (e.g. if there are ANY blank lines between cases there will be an error).  
"""
inputfile = open('input3.txt', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()



"""
Now we parse the file and save the scenarios in scenario_list.  A scenario consists
of a line of two integers (number of papers and number of authors to compute), some papers,
and some authors, all in a list.  

Our parsing works by first running through the file, stopping at the lines which have
the two integers, summing them, and recording these numbers (plus the index of the line)
in a list called new_scenario_markers.  

Then we just use the indices in new_scenario_markers to slice input_lines into scenarios,
which we save in scenario_list.
"""
scenario_list = []
new_scenario_markers=[1]
num_cases = int(input_lines[0])
marker = 1

for i in range(1, num_cases):
    marker += int(input_lines[marker].split()[0])+int(input_lines[marker].split()[1])+1
    new_scenario_markers.append(marker)

new_scenario_markers.append(len(input_lines))

for k in range(0,len(new_scenario_markers)-1):
    scenario_list.append(input_lines[new_scenario_markers[k]:new_scenario_markers[k+1]])










"""
SECTION 1: DEFINING FUNCTIONS TO SOLVE THE PROBLEM
"""


"""
Now we define a function, scenario_solver, that takes a scenario as input, and outputs
the names and erdos numbers of all authors specified.  We will (eventually) call this 
function for each scenario in scenario_list.  In this function, we first split the case into 
two structures.  The first is papers_list, a list of all papers with authors.
The second is authors_to_search, a list of all authors specified to have their erdos
numbers computed.

Next, we create authors_dictionary by calling the function find_all_authors with the
input papers_list.  Find_all_authors is explained and defined below, but authors_dictionary
is a dictionary whose keys are the integers 1,...,n, where there are n total distinct
authors, and values are the author names.

Then, we create papers_dictionary by calling the function find_all_papers with the inputs
authors_dictionary and papers_list.  This is a new dict whose keys are the same as 
authors_dictionary, but whose corresponding keys are lists of papers titles that the
corresponding author has co-authored.  Find_all_papers is defined and explained below.

After this, we call the function create_adjacency_matrix, defined and explained below.
We save it as the variable A.

Next, we find the key corresponding to 'Erdos, P.' and save it in erdos_key.

Now comes the crucial step in scenario_solver.  If i is the key of a particular author
in authors_dictionary, then the first k in 1,...,l for which the (i, erdos_key) entry of A^k 
is nonzero will be the erdos number of (author) i, where l = num_papers.  
This is explained further in the definition of create_adjacency_matrix below.  
So we create a dict called authors_erdos_numbers, and take successive powers of A, 
and check (i, erdos_key) entries.  When they become nonzero for the first time, we record 
the author name as key and erdos number as value in authors_erdos_numbers.

We manually set Paul Erdos's number to 0 (as convention).  Finally, for each element in 
authors_to_search (we alter the string slightly), we print out the name and erdos number.
If there are names in authors_to_search that do not appear in authors_erdos_numbers at all,
we manually print "infinity" as their erdos numbers.
"""
def scenario_solver(current_scenario):
    num_papers = int(current_scenario[0].split()[0])
    papers_list = current_scenario[1:num_papers+1]
    
    authors_to_search = current_scenario[num_papers+1:]

    
    authors_dictionary = find_all_authors(papers_list)
    papers_dictionary = find_all_papers(authors_dictionary, papers_list)
    
    A = create_adjacency_matrix(papers_dictionary)
    
    erdos_key = -1
    for key,value in authors_dictionary.items():
        if value == 'Erdos, P.':
            erdos_key = key
    authors_erdos_numbers = {}
    
    for i in range(1, len(authors_dictionary)+1):
        count = 0
        for k in range(1, num_papers + 1):
            if numpy.linalg.matrix_power(A, k)[i-1, erdos_key - 1] != 0 and count == 0 and erdos_key != -1:
                count += 1
                authors_erdos_numbers[authors_dictionary[i]] = k
            elif k == num_papers and count == 0:
                authors_erdos_numbers[authors_dictionary[i]] = "infinity"
    
    authors_erdos_numbers['Erdos, P.'] = 0
    
    for author in authors_to_search:
        mark = 0
        for key in authors_erdos_numbers:
            if author[:-1] == key or author[:-1]+"." == key:
                print key + " " + str(authors_erdos_numbers[key])
                mark += 1
        if mark == 0:
            print author[:-1] + " " + "infinity"
    
    
"""
We now define the function find_all_authors, which takes a list of papers as input
and outputs a dict called all_authors_dict whose keys are the integers 1,...,n, 
where there are n total distinct authors, and values are the author names.  

This function works by iteratively calling the function find_authors_from_paper, 
then iterating over the returned list of names and adding those names to a set, 
distinct_names.  We use a set to eliminate duplicate names.  Then we temporarily save 
the items in the set to a list, then iterate over the list to add keys and values 
(indices in the list) to the output dict all_authors_dict.

The function find_authors_from_paper, defined below find_all_authors, takes a paper, 
parses it by first splitting on the ':', then taking the list of authors and splitting 
on the ',' to separate first and last names, then reassembling them two at a time and 
returning all authors in a list.
"""
def find_all_authors(papers):
    all_authors_dict = {}
    distinct_names = set()
    
    for line in papers:
        authors_list = find_authors_from_paper(line)
        for elt in authors_list:
            distinct_names.add(elt)    
    
    temp_list = []
    for name in distinct_names:
        temp_list.append(name)
    
    for i in range(0, len(temp_list)):
        all_authors_dict[i+1] = temp_list[i]
    
    return all_authors_dict
    

def find_authors_from_paper(paper):
    authors_list_to_parse = paper.split(':')[0]
    comma_split_list = authors_list_to_parse.split(',')
    list_to_return = []
    for i in range(0, len(comma_split_list)/2):
        list_to_return.append((comma_split_list[2*i] + "," + comma_split_list[2*i + 1]).lstrip())
    
    return list_to_return
   
    

"""
Now we define the function find_all_papers, which takes a dictionary of authors
(the key is an integer and the value is the author name), and a list of papers.  It 
returns a new dict with the same keys as the author dictionary, but whose value for a
given key is the list of all paper titles that the author has (co)authored.  This
returned dict is called papers_dict.
"""
def find_all_papers(authdict, papers):
    papers_dict = {}
    
    for key in authdict:
        list_of_papers = []
        for paper in papers:
            if paper.find(authdict[key]) != -1:
                list_of_papers.append(paper.split(':')[1].lstrip())
        papers_dict[key] = list_of_papers
     
    return papers_dict    
        
        
             
"""
We define a function here called create_adjacency_matrix, which takes a dictionary
p_dict as input.  We expect p_dict to have natural numbers as keys (from 1,...,n) and
lists of strings as values.  The output will be a numpy array object (a matrix) which
is nxn.

This matrix, which we denote Adj_matrix is defined as follows.  Let i,j be two numbers 
between 1 and n.  Suppose that p_dict[i] and p_dict[j] have a string in common.  
Then the (i,j)th entry of Adj_matrix is 1.  If p_dict[i] and p_dict[j] have no strings
in common, then the (i,j)th entry of Adj_matrix is 0.  This matrix is obviously symmetric.
By convention, the diagonal is 0.

This matrix has the following well-known property.  If we create a graph with vertices 
1,...n, and a 1 in the (i,j)th position if an edge connects i and j, and a 0 in the
(i,j)th position if no edge connects i and j, then the kth power of the adjacency
matrix represents the number of paths from vertex i to j of length k.

This will be useful to us, as we will take powers of Adj_matrix and check for the first
power at which an entry of the form (i,l), where l is the key for P. Erdos, becomes 
nonzero.  That power will be the Erdos number of the author corresponding to key i.
""" 
def create_adjacency_matrix(p_dict):
 
    n = len(p_dict)
    Adj_matrix = numpy.zeros((n,n))
    for i in p_dict:
        for j in p_dict:
            if len(set(p_dict[i]).intersection(set(p_dict[j]))) != 0 and i != j:
                Adj_matrix[i-1,j-1] = 1
  
    return Adj_matrix










"""
SECTION 3: OUTPUTTING THE RESULTS
"""
"""
Finally, for each scenario in scenario_list, we call scenario_solver.
"""
for i in range(0,len(scenario_list)):
    print "Scenario" + " "+ str(i+1)
    scenario_solver(scenario_list[i])
