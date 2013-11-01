#Problem 3
#Haozhe Wang

"""General idea
build list of lists
parse the text file;
split the file by colon;
read the author names and keep names from same articles in the same list;
check alllists, if "Erdos" was in the list, grand 1 to the authors in the same list;
store the 1's to a new list;
loop through the large list and match each 1's with the list;
if the author with socre 1 shows up, grand the rest in the list 2;
do the same for the rest until no more matches;
export the author names and numbers assgined to another list, assign "infinity" to no-match;
read the wanted names;
match each wanted names with the exported list;
export the names  in the search list.
"""

lines =  open('input3.txt').readlines()
scenario = lines[0]
linecount = 0
