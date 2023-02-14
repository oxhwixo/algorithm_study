# 1010 다리 놓기
# 실버 5

import math

t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	print( math.factorial(m) // (math.factorial(m - n) * math.factorial(n)))
	# math.comb(m, n) 도 가능


# dp로 풀이 - n, m 입력값에 대한 표를 만들어서 규칙 찾으면 됨
# dp = [[1] * 31 for _ in range(31)]
# for i in range(31):
# 	dp[1][i] = i
# for i in range(2, 31):
# 	for j in range(i + 1, 31):
# 		dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

# for _ in range(t):
# 	n, m = map(int, input().split())
# 	print(dp[n][m])