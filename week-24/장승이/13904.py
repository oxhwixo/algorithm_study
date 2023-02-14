# 13904 과제
# 골드 3

import sys
input = sys.stdin.readline

n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]

datas.sort()
temp = []
result = 0

for day in range(n, 0, -1): # 마지막 날 부터 거꾸로 계산
	while datas and datas[-1][0] >= day:
		temp.append(datas.pop()[1])
	if temp:
		temp.sort()
		result += temp.pop()

print(result)