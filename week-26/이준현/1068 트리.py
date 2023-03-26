import sys

input = sys.stdin.readline
n = int(input())


def DFS(v):
    arr[v] = 1e9
    for i in range(n):
        if v == arr[i]:
            DFS(i)


arr = list(map(int, input().split()))
delete = int(input())
ans = 0

DFS(delete)
for i in range(n):
    if arr[i] != 1e9 and i not in arr:
        ans += 1
print(ans)
