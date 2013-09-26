from sys import stdin

def count_mines(rows, num_rows, num_cols):
	counts = []

	for r in range(num_rows):
		row_counts = ''

		for c in range(num_cols):
			if rows[r][c] == '*':
				row_counts += '*'
			else:
				count = 0

				# look at previous row
				if r > 0 and c > 0 and rows[r-1][c-1] == '*':
					count += 1
				if r > 0 and rows[r-1][c] == '*':
					count += 1
				if r > 0 and c < num_cols - 1 and rows[r-1][c+1] == '*':
					count += 1

				# look at this row
				if c > 0 and rows[r][c-1] == '*':
					count += 1
				if rows[r][c] == '*':
					count += 1
				if c < num_cols - 1 and rows[r][c+1] == '*':
					count += 1

				# look at next row
				if r < num_rows -1 and c > 0 and rows[r+1][c-1] == '*':
					count += 1
				if r < num_rows -1 and rows[r+1][c] == '*':
					count += 1
				if r < num_rows -1 and c < num_cols - 1 and rows[r+1][c+1] == '*':
					count += 1

				row_counts += str(count)
		
		counts.append(row_counts)

	return counts

field_num = 1

line = stdin.readline()
while line:
	dimensions = line.split()
	num_rows = int(dimensions[0])
	num_cols = int(dimensions[1])

	rows = []
	for r in range(num_rows):
		row = stdin.readline()
		row = row.strip()
		rows.append(row)

	if len(rows) > 0:
		row_counts = count_mines(rows, num_rows, num_cols)
		print "Field #", field_num
		for counted_row in row_counts:
			print counted_row
		print

	line = stdin.readline()
	field_num += 1