# 10974 모든 순열
n = int(input())
s = []

visited = [False] * (n + 1)

def dfs():
    if len(s) == n:
        print(*s)
        return
    
    prev = 0
    
    for i in range(1, n + 1):
        if prev != i and visited[i] == False:
            s.append(i)
            prev = i
            visited[i] = True
            dfs()
            s.pop()
            visited[i] = False

dfs()