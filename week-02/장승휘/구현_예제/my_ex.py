n = int(input())
move = input().split()

col = 1
row = 1

for i in move:
	if i == 'L':
		if col == 1:
			continue
		col -= 1
	elif i == 'R':
		if col == n:
			continue
		col += 1
	elif i == 'U':
		if row == 1:
			continue
		row -= 1
	elif i == 'D':
		if row == n:
			continue
		row += 1

print (row, col)

# 움직임 배열 크기만큼 반복문 사용해서 움직이기
# 벗어나는 움직임은 continue로 무시