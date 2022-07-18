data = input()
row = int(data[1])
col = ord(data[0]) - ord('a') + 1

cnt = 0
steps = [[2, -1], [2, 1], [-2, -1], \
 [-2, 1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

for step in steps:
	next_row = row + step[0]
	next_col = col + step[1]
	if next_row >= 1 and next_row <= 8 \
	and next_col >= 1 and next_col <= 8:
			cnt += 1

print(cnt)