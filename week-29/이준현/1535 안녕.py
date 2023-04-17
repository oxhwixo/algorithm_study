import sys

input = sys.stdin.readline

n = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))
dp = [[0] * 100 for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 100):
        if hp[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - hp[i - 1]] + happy[i - 1])

print(dp[n][99])
