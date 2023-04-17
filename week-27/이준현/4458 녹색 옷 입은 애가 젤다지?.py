import sys
import heapq

input = sys.stdin.readline

# 단순한 다익스트라로 생각하면 될 느낌?
# 루피의 값을 간선의 가중치로 생각하고 0, 0 => n, n까지의 최단거리를 구하면 될꺼같은 느낌
INF = 1e9
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while True:
    n = int(input())
    if n == 0:
        break
    dist = [[INF] * n for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist[0][0] = arr[0][0]
    q = [(arr[0][0], 0, 0)]
    while q:
        distance, x, y = heapq.heappop(q)
        if dist[x][y] < distance:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or n <= ny:
                continue
            cost = distance + arr[nx][ny]
            if dist[nx][ny] > cost:
                dist[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    ans.append(dist[n - 1][n - 1])
for i in range(len(ans)):
    print("Problem " + str(i + 1) + ": " + str(ans[i]))
