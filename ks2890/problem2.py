n = input("Enter intergers in brackets '[]' please")


def seq_sub(n):
	while len(n) > 1:
		n = [i - n[0] for i in n]
		yield abs(n[1])
		n = n[1:]

def jolly(n):
		print sorted(seq_sub(n)) == range(1, len(n))


jolly(n)
