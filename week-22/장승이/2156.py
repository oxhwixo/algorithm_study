# 2156 포도주 시식
# 실버 1

n = int(input())

wines = [0]
for _ in range(n):
	wines.append(int(input()))
dp = [0] * 10001
dp[1] = wines[1]

if n > 1:
	dp[2] = wines[1] + wines[2]

for i in range(3, n + 1):
	dp[i] = max(dp[i - 1], dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i])

print(dp[n])