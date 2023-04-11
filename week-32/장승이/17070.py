# 17070 파이프 옮기기1
# 골드5

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

ans = 0

def dfs(x, y, code): # code = 0:가로 1:세로 2:대각선
    global ans
    if x == n - 1 and y == n - 1:
        ans += 1
        return
    
    if code == 0 or code == 2:
        ny = y + 1
        if ny < n and graph[x][ny] == 0:
            dfs(x, ny, 0)
    if code == 1 or code == 2:
        nx = x + 1
        if nx < n and graph[nx][y] == 0:
            dfs(nx, y, 1)           
    
    nx = x + 1
    ny = y + 1
    if nx < n and ny < n and graph[nx][ny] == 0 and graph[nx - 1][ny] == 0 and graph[nx][ny - 1] == 0:
        dfs(nx, ny, 2)
    
    
if graph[n-1][n-1] == 1:
    print(0)
else:
    dfs(0, 1, 0)
    print(ans)
    
