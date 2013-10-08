import sys

myFile = open('input2.txt', 'r')
input_lines = []
for line in myFile:
	if line[-1] == '\n':
		input_lines.append(line[:-1])
myFile.close()
#add '/n' after the last string in case it can't be read
input_lines.append('')

def get_winner(can_name,parse_votes):
#get the winner in this function, there are three scenarios: 
#(1)get the winner whose ballots recieved more than 50% of the votes,(2)cadidates are ties,
#(3)no winner in the first round, eliminate the weakest candidate and run the function again
	winner_outcome=False
	#use True and False to see if we have the winner_outcome
	votes_num=len(parse_votes)

	can_number_frequency={}
	for votes in parse_votes:
		first_can_number=int(votes[0])
		if first_can_number not in can_number_frequency:
			can_number_frequency[first_can_number]=0

		can_number_frequency[first_can_number]+=1

#see if there's any candidate recieves more than 50% of votes
	for can_number in can_number_frequency:
		if float(can_number_frequency[can_number])/votes_num > 0.5:
			winner_outcome=True
			print can_name[can_number-1]
			return

#if candidates are tied
	voting_counts=[]
	for i in can_number_frequency:
		voting_counts.append(can_number_frequency[i])


	if max(voting_counts)==min(voting_counts) and len(voting_counts)>1:
		winner_outcome=True
		for canN in can_number_frequency:
			print can_name[canN-1]
			return

#if there's no winner in above cycle, eliminate the weakest candidates, and run again
	if winner_outcome==False:	
		new_votes=[]	
		can_washout = []
		min_can = min(voting_counts)
		for i in can_number_frequency:
			if can_number_frequency[i]==min_can:
				can_washout.append(i)
#add i into new_votes if it dosen't appear in can_wash, so weakest candidates will be eliminated
		for n in range(len(parse_votes)):
			new_votes.append([])
			for i in parse_votes[n]:
				if int(i) not in can_washout:
					new_votes[n].append(i)
		
		get_winner(can_name,new_votes)


def get_candidates_and_votes(input_lines):
#get the information of the name of candicates and the ballots, seperate them with different cases
	case_number=int(input_lines[0])
	blank = []
	case_context = []
	for all_line in range(1,len(input_lines)):
		if input_lines[all_line] == '':
			blank.append(all_line)
			#use blank to identify each case
	for case_line in range(blank[0]):
		case_list=input_lines[blank[case_line]+1:blank[case_line+1]]
		case_context.append(case_list)	
#put the information of candidates number, candidates'name and ballots into case_context
	for i in range(len(case_context)):
		seperate_case = case_context[i]
		#seperate each case in case_context so we can run it seperately
	
		parse_votes = []#get votes in seperate_case
		can_number=int(seperate_case[0])
		ballots = seperate_case[(can_number+1):]#the position where ballots start	
		for b in ballots:
			parse_votes.append(b.split(' '))

	#get the name of candidates
		candidates=seperate_case[1:(can_number)+1]
	
		get_winner(candidates,parse_votes)
			

get_candidates_and_votes(input_lines)

