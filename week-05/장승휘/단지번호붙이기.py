# dfs, bfs 둘다 다시 풀어볼 것!
import sys

n = int(sys.stdin.readline().strip())
graph = []
for _ in range(n):
	graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = 0
count = 1
count_arr = []

def dfs(x, y):
	global count

	if x < 0 or y < 0 or x > n - 1 or y >  n - 1:
		return False 

	if graph[x][y] != 0:
		graph[x][y] = 0
		for i in range(4):
			if dfs(x + dx[i], y + dy[i]) == True:
				count += 1
		return True

	return False

for i in range(n):
	for j in range(n):
		if dfs(i, j) == True:
			count_arr.append(count)
			count = 1
			total += 1

print(total)
count_arr.sort()
for i in count_arr:
	print(i)

# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(graph, a, b):
#     queue = deque()
#     queue.append((a, b))
#     graph[a][b] = 0
#     count = 1

#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))
#                 count += 1
#     return count


# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# cnt = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             cnt.append(bfs(graph, i, j))

# cnt.sort()
# print(len(cnt))
# for i in range(len(cnt)):
#     print(cnt[i])