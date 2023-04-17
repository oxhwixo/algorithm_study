import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def DFS(v):
    if visited[v]:
        return
    visited[v] = True
    for i in range(len(graph[v])):
        DFS(graph[v][i])


for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
        ans += 1

print(ans)
