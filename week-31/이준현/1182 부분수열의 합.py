import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
check = []
cnt = 0
visited = [False] * n


def DFS(depth, x):
    global cnt
    if depth == n:
        if sum(check) == s:
            cnt += 1
        return
    else:
        sum_value = sum(check)
        if sum_value == s and len(check) != 0:
            cnt += 1
        for i in range(x, n):
            if not visited[i]:
                visited[i] = True
                check.append(arr[i])
                DFS(depth + 1, i)
                check.pop()
                visited[i] = False


DFS(0, 0)
print(cnt)
