import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[False] * (m + 1) for _ in range(n + 1)]
ans = 0


def DFS(x, y):
    global ans
    if y == 1 and x == n + 1:
        ans += 1
        return
    if y == m:
        nx, ny = x + 1, 1
    else:
        nx, ny = x, y + 1
    DFS(nx, ny)
    if not (graph[x - 1][y] and graph[x][y - 1] and graph[x - 1][y - 1]):
        graph[x][y] = True
        DFS(nx, ny)
        graph[x][y] = False

DFS(1, 1)
print(ans)