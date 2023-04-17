n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False] * (n + 1)
result = 0
    
def search(x):
    if not visited[x]:
        visited[x] = True
        for item in arr[x]:
            search(item)
        return True
    
for i in range(1, n + 1):
    if search(i):
        result += 1

print(result)