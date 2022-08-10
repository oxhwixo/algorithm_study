import sys

def dfs(v):
	for i in graph[v]:
		if visited[i] == 0:
			visited[i] = visited[v] + 1
			dfs(i)

n = int(sys.stdin.readline().strip())
s, e = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().strip())
graph = [[] for _ in range (n + 1)]
for i in range(m):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [0] * (n + 1)
dfs(s)
print(visited[e] if visited[e] > 0 else -1)

