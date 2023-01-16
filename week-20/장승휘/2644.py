# 2644 촌수계산
# 실버 2

import sys
sys.setrecursionlimit(300000)

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node] + 1
            dfs(n)
            
n = int(input())
s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

check = [0] * (n + 1)

dfs(s)

print(check[e] if check[e] > 0 else -1)