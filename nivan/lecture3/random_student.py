students = []

#
myFile = open('studentslist.txt','r')
fileLines = myFile.readlines()
print fileLines
students = fileLines

#
numberOfStudents = len(students)
print numberOfStudents

#Now I'm going to select a random student
import random 
index = random.randint(0,numberOfStudents-1)
print 'the lucky person is ' + students[index] 
