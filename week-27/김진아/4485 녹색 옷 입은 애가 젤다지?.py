import heapq

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def search(count):
    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    distance[0][0] = arr[0][0]
    
    while q:
        cost, x, y = heapq.heappop(q)
        
        if x == n - 1 and y == n - 1:
            print('Problem ' + str(count) + ': ' + str(distance[x][y]))
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                nc = cost + arr[nx][ny]
                
                if nc < distance[nx][ny]:
                    distance[nx][ny] = nc
                    heapq.heappush(q, (nc, nx, ny))

count = 1

while True:
    n = int(input())
    if n == 0:
        break
    
    arr = [list(map(int, input().split())) for _ in range(n)]
    distance = [[int(1e9)] * n for _ in range(n)]
    
    search(count)
    count += 1