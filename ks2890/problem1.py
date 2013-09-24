def solve(n):
	if n % 2 == 0:
		return n/2
	else:
		return 3*n + 1

cache = [0,1]

for i in range (2,1000000):
	value = i
	value_num = 0
	end = False

	while value > 1 and not end:
		value = solve(value)
		if value < len(cache):
			value_num += cache[value]
			end = True
		value_num += 1
	cache.append(value_num)

print cache.index(max(cache))