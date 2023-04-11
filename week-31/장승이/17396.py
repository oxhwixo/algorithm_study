# 17369 백도어
# 골드 5

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [10000000001] * n
view = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
distance[0] = 0
heapq.heappush(q, (0, 0)) # dist, cost
while q:
    now, dist = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            if view[i[0]] != 1 or (view[i[0]] and i[0] == n - 1):
              heapq.heappush(q, (i[0], cost))

print(distance[n - 1] if distance[n - 1] != 10000000001 else -1)
