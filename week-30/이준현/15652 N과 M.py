import sys

input = sys.stdin.readline
n, m = map(int, input().split())

li = list(range(1, n + 1))

check = [0] * m
ans = []


def DFS(depth):
    if depth == m:
        ans.append(list(map(int, check)))
        return
    for k in range(n):
        if check[depth - 1] <= li[k]:
            check[depth] = li[k]
            DFS(depth + 1)
for i in range(n):
    check[0] = li[i]
    DFS(1)
    check[0] = 0
for i in ans:
    for j in i:
        print(j, end=' ')
    print()
