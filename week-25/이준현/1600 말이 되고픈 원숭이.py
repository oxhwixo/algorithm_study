import sys
from collections import deque

input = sys.stdin.readline
MAX = 1e9
horse_step = int(input())
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]
dist = [[[MAX] * (horse_step + 1) for _ in range(n)] for _ in range(m)]
# 왼쪽 위 아래, 왼쪽 위 위, 오른쪽 위위, 오른쪽 위 아래, 왼쪽 아래 위, 왼쪽 아래 아래, 오른쪽 아래 아래, 오른쪽 아래 위
h_dx = [2, 2, 1, 1, -2, -2, -1, -1]
h_dy = [1, -1, 2, -2, 1, -1, 2, -2]
# 상 하 좌 우
m_dx = [-1, 1, 0, 0]
m_dy = [0, 0, -1, 1]


def BFS():
    q = deque()
    if arr[0][0] != 1:
        dist[0][0][0] = 0
        q.append((0, 0, 0))
    while q:
        x, y, cnt = q.popleft()
        if x == m - 1 and y == n - 1:
            print(dist[x][y][cnt])
            exit(0)
        for i in range(4):
            nx = x + m_dx[i]
            ny = y + m_dy[i]
            if nx < 0 or m <= nx or ny < 0 or n <= ny or dist[nx][ny][cnt] != MAX:
                continue
            if arr[nx][ny] == 1:
                continue
            q.append((nx, ny, cnt))
            dist[nx][ny][cnt] = dist[x][y][cnt] + 1

        if cnt < horse_step:
            for i in range(8):
                nx = x + h_dx[i]
                ny = y + h_dy[i]
                if nx < 0 or m <= nx or ny < 0 or n <= ny or dist[nx][ny][cnt + 1] != MAX:
                    continue
                if arr[nx][ny] == 1:
                    continue
                q.append((nx, ny, cnt + 1))
                dist[nx][ny][cnt + 1] = dist[x][y][cnt] + 1


BFS()
print(-1)
