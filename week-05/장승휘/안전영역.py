import sys
sys.setrecursionlimit(100000) 
# 무한대의 recursion 으로 인한 overflow가 발생하는 것을 방지하기 위해 stack 최대 깊이 지정

n = int(sys.stdin.readline().strip())
graph = []
for _ in range(n):
	graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, h):
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and graph[nx][ny] > h:
			visited[nx][ny] = True
			dfs(nx, ny, h)

result = 0
for k in range(max(map(max,graph))): # 배열에서 가장 큰 값 찾기
	visited = [[False] * n for _ in range(n)]
	# 한번 돌리는게 아니라 높이별로 여러번 해야해서 원본 자료에 그대로 visit 표시 불가능!!
	count = 0
	for i in range(n):
			for j in range(n):
				if graph[i][j] > k and not visited[i][j]:
					count += 1
					visited[i][j] = True
					dfs(i, j, k)
	result = max(result, count)

print(result)

# bfs

# import sys
# sys.setrecursionlimit(100000) 
# from collections import deque

# n = int(sys.stdin.readline().strip())
# graph = []
# for _ in range(n):
# 	graph.append(list(map(int, sys.stdin.readline().split())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x, y, h):
# 	queue = deque([(x, y)])
# 	while queue:
# 		x, y = queue.popleft()
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]

# 			if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and graph[nx][ny] > h:
# 				visited[nx][ny] = True
# 				queue.append((nx, ny))

# result = 0
# for k in range(max(map(max,graph))):
# 	visited = [[False] * n for _ in range(n)]
# 	count = 0
# 	for i in range(n):
# 			for j in range(n):
# 				if graph[i][j] > k and not visited[i][j]:
# 					count += 1
# 					visited[i][j] = True
# 					bfs(i, j, k)
# 	result = max(result, count)

# print(result)
