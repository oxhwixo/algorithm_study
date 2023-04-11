# 21610 마법사 상어와 비바라기
# 골드5

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dir_move = [list(map(int, input().split())) for _ in range(m)]
dx = 0, -1, -1, -1, 0, 1, 1, 1
dy = -1, -1, 0, 1, 1, 1, 0, -1
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
cloud = deque(cloud)


def move_rain(dir, dist):
    global n
    size = len(cloud)
    for _ in range(size):
        x, y = cloud.popleft()
        nx = (x + dx[dir] * dist) % n
        ny = (y + dy[dir] * dist) % n
        if 0 > nx:
            nx += n
        if 0 > ny:
            ny += n
        cloud.append((nx, ny))
        # 구름 사라진 자리
        visited[nx][ny] = True
        graph[nx][ny] += 1


def dup():
    while cloud:
        # 대각선 검사
        x, y = cloud.popleft()
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                graph[x][y] += 1


for dir, dist in dir_move:
    visited = [[False] * n for _ in range(n)]
    # 구름 이동 후 비
    move_rain(dir - 1, dist)
    # 물 복사
    dup()
    # 구름 생성
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and not visited[i][j]:
                cloud.append((i, j))
                graph[i][j] -= 2
answer = 0
for i in range(n):
    for j in range(n):
        answer += graph[i][j]
print(answer)