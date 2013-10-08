import sys
import math

input3 = open("input3.txt", "r")
num_scope = int(input3.readline())

for num1 in range (0, num_scope):

    Erd_1 = input3.readline().split()
    num2 = int(Erd_1[0])
    num3 = int(Erd_1[1])
    research = [] 

    for k in range (0, num2):
        research.append(input3.readline())
    auth_asso_erd = {}  # Used to contain all the authors associated with the Erdos paper.
    cite_asso_erd = []  # Used to contain all the citations of authors who collaborated on the Erdos paper.

    for data in research:
        data_new = data.split('.:')
        for insert in data_new:
            cite = insert.split('., ')
            if (cite[0][0] != ' '):
                cite_asso_erd.append(cite)
                for k in range(0, len(cite)):
                    add_cite = cite[k]
                    auth_asso_erd[add_cite] = 1000

    new_auth = []
    for k in range (0, num3):
        new_auth_name = input3.readline().strip('.\n')
        new_auth.append(new_auth_name)


    for loop in range (0, num2):  # For loop used to provide the authors with the lowest scores on the Erdos paper.
        for data in cite_asso_erd:
            low_erd_score = auth_asso_erd[data[0]]
            for abc1 in range(0, len(data)):
                if (auth_asso_erd[data[abc1]] < low_erd_score):
                    low_erd_score = auth_asso_erd[data[abc1]]
            for abc1 in range(0, len(data)):
                if (auth_asso_erd[data[abc1]] > low_erd_score):
                    auth_asso_erd[data[abc1]] = low_erd_score + 1


    for data in cite_asso_erd:  # For loop used to assign the value = 1 for those who collaborated directly on the Erdos paper.
        if 'Erdos, P' in data:
            for abc1 in range(0, len(data)):
                auth_name = data[abc1]
                auth_asso_erd[auth_name] = 1


    for insert in auth_asso_erd:
        if (auth_asso_erd[insert] == 1000):
            auth_asso_erd[insert] = 'Infinite'  # Setting to infinite to score of authors who have score 1000.


    print 'Scenario :', num1 + 1
    for name in new_auth:
        for insert in auth_asso_erd:
            if (str(insert) == str(name)):
                print insert, ". ", auth_asso_erd[insert]


input3.close()
