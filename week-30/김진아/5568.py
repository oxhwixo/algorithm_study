# 5568 카드 놓기

n = int(input())
k = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()

temp = []
answer = []

visited = [False] * n

def dfs():
    global answer
    if len(temp) == k:
        answer.append(int("".join(map(str, temp))))
        return
    
    prev = 0
    
    for i in range(n):
        if prev != arr[i] and not visited[i]:
            temp.append(arr[i])
            prev = arr[i]
            visited[i] = True
            dfs()
            temp.pop()
            visited[i] = False

dfs()

print(len(list(set(answer))))