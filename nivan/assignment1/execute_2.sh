#Running the code as written yields the following errors:
# execute_2.sh: line 4: .PHONY: command not found
# execute_2.sh: line 5: clean:: command not found
# execute_2.sh: line 6: MY_PROGRAM: command not found
# execute_2.sh: line 6: 4: command not found
# execute_2.sh: line 7: MY_PROGRAM: command not found
# execute_2.sh: line 7: 5: command not found
# execute_2.sh: line 8: MY_PROGRAM: command not found
# execute_2.sh: line 8: 4: command not found
# execute_2.sh: line 9: MY_PROGRAM: command not found
# execute_2.sh: line 9: 4: command not found
# execute_2.sh: line 10: MY_PROGRAM: command not found
# execute_2.sh: line 10: 5: command not found
# execute_2.sh: line 11: MY_PROGRAM: command not found
# execute_2.sh: line 11: 2: command not found
# execute_2.sh: line 12: MY_PROGRAM: command not found
# execute_2.sh: line 12: 11: command not found
# execute_2.sh: line 13: MY_PROGRAM: command not found
# execute_2.sh: line 13: 5: command not found
# execute_2.sh: line 14: MY_PROGRAM: command not found
# execute_2.sh: line 14: 9: command not found
# execute_2.sh: line 15: MY_PROGRAM: command not found
# execute_2.sh: line 15: 10: command not found
# execute_2.sh: line 16: MY_PROGRAM: command not found
# execute_2.sh: line 16: 3: command not found
# execute_2.sh: line 17: MY_PROGRAM: command not found
# execute_2.sh: line 17: 1: command not found

#MY_PROGRAM=python expect_problem2.py
 
#MY_PROGRAM=python ../../rad416/Assignment1/problem2.py 

# passed commandline call as a full string to be executed
MY_PROGRAM="python ../../rad416/Assignment1/problem2.py" 

# I'm assuming this has to do with the make file for testing our code 
# .PHONY : clean
# clean:
       # $(MY_PROGRAM) 4 1 4 2 3
       # $(MY_PROGRAM) 5 1 4 2 -1 6
       # $(MY_PROGRAM) 4 1 4 3 6
       # $(MY_PROGRAM) 4 1 4 2 3
       # $(MY_PROGRAM) 5 7 10 13 12 9
       # $(MY_PROGRAM) 2 0 1
       # $(MY_PROGRAM) 11 10 1 4 1 4 9 4 3 6 15 8
       # $(MY_PROGRAM) 5 2 4 6 7 8
       # $(MY_PROGRAM) 9 1 2 1 4 9 16 7 9 12
       # $(MY_PROGRAM) 10 1 2 11 4 7 14 9 10 5 14
       # $(MY_PROGRAM) 3 4 4 6
       # $(MY_PROGRAM) 1 4


#reference program using the $ reference
$MY_PROGRAM 4 1 4 2 3
$MY_PROGRAM 5 1 4 2 -1 6
$MY_PROGRAM 4 1 4 3 6
$MY_PROGRAM 4 1 4 2 3
$MY_PROGRAM 5 7 10 13 12 9
$MY_PROGRAM 2 0 1
$MY_PROGRAM 11 10 1 4 1 4 9 4 3 6 15 8
$MY_PROGRAM 5 2 4 6 7 8
$MY_PROGRAM 9 1 2 1 4 9 16 7 9 12
$MY_PROGRAM 10 1 2 11 4 7 14 9 10 5 14
$MY_PROGRAM 3 4 4 6 
$MY_PROGRAM 1 4


#Output from code
# Jolly
# Not jolly
# Jolly
# Jolly
# Jolly
# Not jolly
# Jolly
# Jolly
# Jolly
# Jolly
# Jolly
# Jolly