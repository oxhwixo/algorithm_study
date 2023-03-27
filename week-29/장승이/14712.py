# 14712 넴모넴모
# 실버 1

# 모든 맵 탐색하면서 넴모가 생기는 경우 빼주기

n, m = map(int, input().split())

graph = [[0] * (m + 1) for _ in range(n + 1)]
ans = 0

def dfs(cnt):
    global ans

    if cnt == n * m:
        ans += 1
        return 
    
    # 행은 몫으로 열은 나머지연산으로 구함
    # (1, 1) ~ (n, m)
    x = cnt // m + 1 # 행
    y = cnt % m + 1  # 열

    dfs(cnt + 1)
    if graph[x - 1][y] == 0 or graph[x][y - 1] == 0 or graph[x - 1][y - 1] == 0:
        graph[x][y] = 1
        dfs(cnt + 1)
        graph[x][y] = 0

dfs(0)
print(ans)