import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = [[] for _ in range (n + 1)]
for i in range(m):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [0] * (n + 1)
global cnt
cnt = 0

def dfs(v):
	for i in graph[v]:
		global cnt
		if visited[i] == 0:
			cnt += 1 
			visited[i] = 1
			dfs(i)

dfs(1)
print(cnt - 1)