n, start, M = map(int, input().split())

m = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(n + 1)]
dp[0][start] = 1

for i in range(n):
    for j in range(M + 1):
        if dp[i][j] == 1:
            if j + m[i] <= M:
                dp[i + 1][j + m[i]] = 1
            if j - m[i] >= 0:
                dp[i + 1][j - m[i]] = 1

if sum(dp[n]) == 0:
    print(-1)
else:
    for i in range(M, -1, -1):
        if dp[n][i] == 1:
            print(i)
            break
