# 1912 연속합
# 실버 2

n = int(input())
array = list(map(int, input().split()))

dp = [-1001] * (n + 1)
dp[0] = array[0]

for i in range(1, n):
	dp[i] = max(dp[i - 1] + array[i], array[i])

print(max(dp))