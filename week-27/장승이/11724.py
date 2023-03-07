# 11724 연결 요소의 개수
# 실버 2

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(i):
    visited[i] = True
    for item in graph[i]:
        if visited[item] == False:
          dfs(item)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
  if not visited[i]:
     dfs(i)
     count += 1
 
print(count)