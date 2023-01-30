# 7576 토마토
# 골드 5

from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
answer = 0

for i in range(n):
	for j in range(m):
		if graph[i][j] == 1:
			queue.append([i, j])

def bfs():
	while queue:
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and graph[nx][ny] == 0:
				queue.append([nx, ny])
				graph[nx][ny] = graph[x][y] + 1

bfs()

for one_line in graph:
	if 0 in one_line:
		print(-1)
		exit(0)
		
	else:
		answer = max(answer, max(one_line))

print(answer - 1)