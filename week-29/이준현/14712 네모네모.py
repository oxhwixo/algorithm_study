import sys

sys.setrecursionlimit(30000)
n, m = map(int, input().split())
graph = [[0] * (m + 1) for i in range(n + 1)]
cnt = 0


def DFS(x, y):
    global cnt

