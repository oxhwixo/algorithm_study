import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
INF = 1e9
arr = [[] * (v + 1) for _ in range(v + 1)]
distance = [INF] * (v + 1)
start = int(input())
for i in range(e):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))
distance[start] = 0
q = [(0, start)]
while q:
    dist, v = heapq.heappop(q)
    if distance[v] < dist:
        continue
    for i in range(len(arr[v])):
        cost = arr[v][i][1] + dist
        if distance[arr[v][i][0]] > cost:
            distance[arr[v][i][0]] = cost
            heapq.heappush(q, (cost, arr[v][i][0]))

for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)


