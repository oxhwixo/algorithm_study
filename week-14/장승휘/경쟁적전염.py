from collections import deque

n, k = map(int, input().split())

graph = []
virus_data = []

for i in range(n):
	graph.append(list(map(int, input.split())))
	for j in range(n):
		if graph[i][j] != 0:
			# 바이러스 종류, 초 (해당 초의 상태), X, Y
			virus_data.append((graph[i][j], 0, i, j))

virus_data.sort()
q = deque(virus_data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
	virus, s, x, y = q.popleft()
	# s가 target_s 일 때는 이미 s초의 상태가 저장되어있는 상태
	# 여기서 break하지 않으면 s초를 넘어간 이후의 상태까지 구하는 것
	if s == target_s: 
		break

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if 0 <= nx and nx < n and 0 <= ny and ny < n:
			if graph[nx][ny] == 0:
				graph[nx][ny] = virus
				q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])

