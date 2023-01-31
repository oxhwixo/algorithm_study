# 17836 공주님을 구해라!
# 골드 5

from collections import deque

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
	queue = deque([(0, 0)])
	sword = 1e9
	
	while queue:
		x, y = queue.popleft()

		if graph[x][y] == 2:
			sword = visit[x][y] + (n - 1 - x) + (m - 1 - y)

		if x == n - 1 and y == m - 1:
			return min(visit[x][y], sword)

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if (0 <= nx < n and 0 <= ny < m) and (graph[nx][ny] != 1):
				if visit[nx][ny] == 0:
					queue.append((nx, ny))
					visit[nx][ny] = visit[x][y] + 1

	return sword

ans = bfs()

if t >= ans:
	print(ans)
else:
	print("Fail")
