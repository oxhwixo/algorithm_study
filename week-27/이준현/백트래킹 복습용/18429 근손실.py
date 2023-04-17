import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
visited = [False] * len(arr)


def DFS(day, total):
    global ans
    if total < 500:
        return
    if day == n:
        ans += 1
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            DFS(day + 1, total - k + arr[i])
            visited[i] = False

DFS(1, 500)
print(ans)
