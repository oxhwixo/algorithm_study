# 1600 말이 되고픈 원숭이
# 골드 3

import sys
from collections import deque

input = sys.stdin.readline
k = int(input())
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

hx = [2, 2, 1, 1, -2, -2, -1, -1]
hy = [1, -1, 2, -2, 1, -1, 2, -2]

# 일반적인 visited 배열에 특수이동 n번에 대한 정보 추가
# 단순히 n, m에 대한 방문 처리가 아닌
# n, m에 특수이동을 0번 해서 왔는지, 1번 해서 왔는지 구분해서 방문 처리 가능
# visited[ n ][ m ][ k ] 
visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

def solution(a, b):
    q = deque()
    q.append(((a, b, 0, 0))) # x, y, 특수이동횟수, 지금까지의 동작횟수
    visited[a][b][0] = True # 가장 첫 칸은 특수이동횟수 0

    while q:
        x, y, special, cnt = q.popleft()

        if x == n - 1 and y == m - 1:
            return cnt
        
        for i in range(4): # 원숭이 무빙
            nx, ny = x + mx[i], y + my[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny][special] == False:
                    if graph[nx][ny] == 0:
                        visited[nx][ny][special] = True
                        q.append((nx, ny, special, cnt + 1))

        if special < k: # 말 무빙
            for i in range(8):
              nx, ny = x + hx[i], y + hy[i]
              if 0 <= nx < n and 0 <= ny < m:
                  if visited[nx][ny][special + 1] == False:
                      if graph[nx][ny] == 0:
                          visited[nx][ny][special + 1] = True
                          q.append((nx, ny, special + 1, cnt + 1))

    return -1

print(solution(0, 0))
