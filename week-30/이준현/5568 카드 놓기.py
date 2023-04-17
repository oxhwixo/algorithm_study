import sys

input = sys.stdin.readline
n = int(input())
k = int(input())

arr = list(int(input()) for i in range(n))
all = set()
ans = 0
check = [0] * k
visited = [False] * n


def DFS(depth):
    global ans
    if depth == k:
        temp = ""
        for i in range(k):
            temp += str(check[i])
        temp = int(temp)
        if temp not in all:
            all.add(temp)
            ans += 1
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            check[depth] = arr[i]
            DFS(depth + 1)
            visited[i] = False


DFS(0)
print(ans)
