def turn_left():
	global direction
	direction -= 1
	if direction == -1:
		direction = 3

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

memo = [[0] * m for _ in range (n)]
memo[x][y] = 1

map_array = []
for i in range(n):
	map_array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0

while True:
	turn_left()
	nx = x + dx[direction]
	ny = y + dy[direction]

	if memo[nx][ny] == 0 and map_array[nx][ny] == 0:
		memo[nx][ny] = 1
		x = nx
		y = ny
		count += 1
		turn_time = 0
		continue

	else:
		turn_time += 1

	if turn_time == 4:
		nx = x - dx[direction]
		ny = y - dy[direction]
		
		if map_array[nx][ny] == 0:
			x = nx
			y = ny
		
		else:
			break
		turn_time = 0

print(count)
