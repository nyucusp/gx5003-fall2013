# Awais Malik
# Assignment 3
# Problem 3

lines =  open('input3.txt','r')
lines = [line.strip() for line in lines]
lines = [line for line in lines if len(line) > 0]

num_scenarios = lines.pop(0).split()
num_scenarios = num_scenarios[0]

# print num_scenarios

info = lines.pop(0).split()
num_papers = int(info[0])
num_authors = int(info[1])

print num_papers
print num_authors

lines = [item.split(":")[0] for item in lines if item]

# print lines

paper_authors = []

paper_authors = [i.split(".,") for i in lines[0:num_papers]]
    
# print paper_authors

check_authors = []

check_authors = lines[num_papers:(num_papers)+(num_authors)]

# print check_authors

Erdos = {}
Erdos_num = 0

for element in check_authors:
    Erdos[element] = [Erdos_num]   

# I need 3 things:
# 1) A function that calculates the Erdos number for each author in paper_authors
# 2) A loop that goes through each element inside paper_authors and:
#       Checks to see if one of the key of the Erdos dict exists
#       Applies the Erdos number function to get the Erdos number
#       Make the Erdos number the value for the key
# 3) Lastly, I need to loop the entire process for the number of scenarios

print "Scenario: " + num_scenarios
print Erdos
print ''