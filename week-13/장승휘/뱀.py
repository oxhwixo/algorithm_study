n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보 

# 맵에 사과 있는곳 1로 표시
for _ in range(k):
	a, b = map(int, input().split())
	data[a][b] = 1

l = int(input())
for _ in range(l):
	x, c = input().split()
	info.append((int(x), c))

# 동 남 서 북 (처음에 오른쪽을 보고있음)
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

def turn(direction, c):
	if c == "L":
		# -1 % 4 = 몫 -1 나머지 3 (-4 + 3 = -1)
		direction = (direction - 1) % 4 
	else:
		direction = (direction + 1) % 4
	return direction 

def simulate():
	x, y  = 1, 1 # 뱀 머리 위치
	data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
	direction = 0 # 처음에는 동쪽 (오른쪽)
	time = 0 # 시작 후 지난 초 정보 저장
	index = 0 # 다음 회전 정보
	q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
	while True:
		nx = x + dx[direction]
		ny = y + dy[direction]
		# 맵 범위 안에 있고 뱀의 몸통이 없는 위치라면
		if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
			# 사과가 없다면 이동 후 꼬리 제거
			if data[nx][ny] == 0:
				data[nx][ny] = 2 # 새로 전진한 칸은 뱀이 위치했다고 표시
				q.append((nx, ny)) # 한 칸 앞으로 가면서
				px, py = q.pop(0)  
				data[px][py] = 0 # 맨 뒤 꼬리를 제거
			# 사과가 있으면 이동 후 꼬리 그대로 두기
			if data[nx][ny] == 1:
				data[nx][ny] = 2
				q.append((nx,ny))
		# 벽이나 뱀의 몸통과 부딪혔다면
		else:
			time += 1
			break
		x, y = nx, ny
		time += 1
		if index < l and time == info[index][0]:
			direction = turn(direction, info[index][1])
			index += 1
	return time

print(simulate)


