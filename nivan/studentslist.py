#This is a comment from RAD416

students = ['aas731',  
'acw438',
'agb344',
'ajm777',
'ak4706',
'ak4728',
'am5801',
'cbj238',
'cnl272',
'efm279',
'gz475',
'hj745',
'hm1273',
'hw1067',
'jj1006',
'jl2684',
'jwr300',
'ke638',
'kll392',
'ks2890',
'kx273',
'lcv232',
'lz1023',
'mam1220',
'rad416',
'rh1328',
'rs4606',
'seltzn01',
'spp319',
'yz1897']

numberOfStudents = len(students)
print numberOfStudents

#Now I'm going to select a random student
import random 
index = random.randint(0,numberOfStudents-1)
print 'the lucky person is ' + students[index]
