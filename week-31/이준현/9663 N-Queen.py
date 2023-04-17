import sys

input = sys.stdin.readline
from copy import deepcopy

n = int(input())
visited = [[False] * n for i in range(n)]
cnt = 0

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def visit(x, y, direction, b):
    if x < 0 or n <= x or y < 0 or n <= y:
        return
    visited[x][y] = b
    x += dx[direction]
    y += dy[direction]
    visit(x, y, direction, b)


def DFS(depth):
    global cnt
    global visited
    if depth == n:
        cnt += 1
        return
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                temp = deepcopy(visited)
                for k in range(8):
                    visit(i, j, k, True)
                DFS(depth + 1)
                visited = temp


DFS(0)
print(cnt)
