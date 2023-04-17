import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
ans = 0


def DFS(arr, total):
    global ans
    if len(arr) == 2:
        ans = max(ans, total)
    for i in range(1, len(arr) - 1):
        DFS(arr[:i] + arr[i + 1:], total + arr[i - 1] * arr[i + 1])


DFS(li, 0)
print(ans)
