import sys

input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0] * (k + 1) for i in range(n + 1)]
arr_w = [0]
arr_v = [0]
for i in range(n):
    w, v = map(int, input().split())
    arr_w.append(w)
    arr_v.append(v)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = arr_w[i]
        v = arr_v[i]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
