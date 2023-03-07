# 4485 녹색 옷 입은 애가 젤다지?
# 골드 4

import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 1

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]

                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

while True:
    n = int(input())
    
    if n == 0:
       break
    
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[1e9] * n for _ in range(n)]

    dijkstra()

    count += 1