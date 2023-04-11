# 5972 택배 배송
# 골드 5

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for  _ in range(n + 1)]
distance = [1e9] * (n + 1)
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))
q = []
heapq.heappush(q, (1, 0)) # (node, cost)
distance[1] = 0
while q:
    now, dist = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for visit_node in graph[now]:
        cost = dist + visit_node[1]
        if distance[visit_node[0]] > cost:
            distance[visit_node[0]] = cost
            heapq.heappush(q, (visit_node[0], distance[visit_node[0]]))

print(distance[n])