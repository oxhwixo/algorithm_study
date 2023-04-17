import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
INF = 1e9
for _ in range(m):
    a, b, distance = map(int, input().split())
    graph[a].append((b, distance))
    graph[b].append((a, distance))
v1, v2 = map(int, input().split())


def dickstra(x, y, dist):
    q = [(x, y)]
    while q:
        v, d = heapq.heappop(q)
        if dist[v] < d:
            continue
        for i, j in graph[v]:
            cost = d + j
            if dist[i] > cost:
                dist[i] = cost
                heapq.heappush(q, (i, cost))


dist1 = [INF] * (n + 1)
dist1[1] = 0
dickstra(1, 0, dist1)

distV1 = [INF] * (n + 1)
distV1[v1] = 0
dickstra(v1, 0, distV1)

distV2 = [INF] * (n + 1)
distV2[v2] = 0
dickstra(v2, 0, distV2)

between = distV1[v2]
betweenV1_1 = dist1[v1]
betweenV2_1 = dist1[v2]
ans = min(betweenV1_1 + distV2[n], betweenV2_1 + distV1[n], betweenV1_1 + distV1[n] + between,
          betweenV2_1 + distV2[n] + between) + between
if ans >= INF:
    print("-1")
else:
    print(ans)
