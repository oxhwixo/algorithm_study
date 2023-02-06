# 9465 스티커
# 실버 1

import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
	n = int(input().strip())
	dp = [list(map(int, input().split())) for _ in range(2)]

	if n > 1:
		dp[0][1] += dp[1][0]
		dp[1][1] += dp[0][0]
	# 자기 자신과 다른 행에 있으면서
	# 열이 -1, -2인 것 둘중에 큰 수를 자기 자신과 더함 
	for i in range(2, n):
		dp[0][i] += max(dp[1][i-1], dp[1][i-2])
		dp[1][i] += max(dp[0][i-1], dp[0][i-2])
	
	print(max(dp[0][n - 1], dp[1][n - 1]))