# 13305 주유소
# 실버 3

import sys
input = sys.stdin.readline

n = int(input().strip())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

cost = price[0]
res = 0

for i in range(n - 1):
	cost = min(cost, price[i])
	res += dis[i] * cost

print(res)
		