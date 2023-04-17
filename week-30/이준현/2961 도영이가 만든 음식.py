import sys

input = sys.stdin.readline

n = int(input())
arr = list((list(map(int, input().split())) for i in range(n)))
INF = 1e9
min_dif = INF
visited = [False] * n
check = [1, 0] * n


def DFS(depth):
    if depth == n:
        return
    global min_dif
    sour = 1
    bitter = 0
    for i in range(n):
        if visited[i]:
            sour *= arr[i][0]
            bitter += arr[i][1]
    dif = abs(sour - bitter)
    if dif < min_dif:
        min_dif = dif
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            DFS(depth + 1)
            visited[i] = False


for i in range(n):
    visited[i] = True
    DFS(0)
    visited[i] = False
print(min_dif)
