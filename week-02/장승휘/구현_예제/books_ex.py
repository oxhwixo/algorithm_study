n = int(input())
user_move = input().split()

x, y = 1, 1
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for move in user_move:
	for i in range (4):
		if move == move_types[i]:
			nx = x + move_x[i]
			ny = y + move_y[i]
	if nx < 1 or nx > n or ny < 1 or ny > n:
		continue
	x = nx
	y = ny

print (x, y)