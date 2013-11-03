def find_erdos(name, erdos, papers):

	r = 0
	for line in papers:
		splited = line.split('.:')
		authors = splited[0]
		title = splited[1]
		authors = authors.split('., ')
		#print title
		#print authors

		if name in authors:
			#print authors
			for author in authors:
				print author
				if author in erdos:
					erdos[author] = erdos[author] + 1
				else:
					erdos[author] = 1
					
				#print line[r]
		r = r + 1

	return erdos


txtfile =open('input3.txt', 'r')
input = txtfile.readlines()
#print input

input[0] =1
#print input

print "Scenario " + str(input[0])
P = input[1][0]
#print P
for line in input:
	papers = input[2:2+int(P)]
print papers

erdos1 = {}
print find_erdos('Erdos, P', erdos1, papers)



erdos2 = {}
print find_erdos('Smith, M.N', erdos2, papers)

# erdos = erdos1
# for author in erdos:
# 	erdos2 = find_erdos(author, erdos, papers)

# 	for author2 in erdos2:
# 		if author2 in erdos:
# 			#
# 		else:
# 			print 'erdos number is equal to 1+erdos2'

# 	erdos = erdos2


erdosInf = {}
print find_erdos('Hsueh, Z', erdosInf, papers)


#r = 0
#for line in papers:
	#if  in line:
		#print line