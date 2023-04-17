import sys

input = sys.stdin.readline
h, n = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[0] * h for _ in range(n)]
ans = 0
rain = []
for i in range(n):
    for j in range(arr[i]):
        graph[i][j] = 1


def up_check(x, y):
    while True:
        if x < 0 or x >= n or y < 0 or y >= h:
            return False
        if graph[x][y] == 1:
            return True
        x = x - 1


def down_check(x, y):
    while True:
        if x < 0 or x >= n or y < 0 or y >= h:
            return False
        if graph[x][y] == 1:
            return True
        x = x + 1


def DFS(x, y):
    global ans
    up = up_check(x, y)
    down = down_check(x, y)
    if up and down:
        graph[x][y] = 2
        ans += 1


for i in range(n):
    for j in range(h):
        if graph[i][j] == 0:
            DFS(i, j)
print(ans)
