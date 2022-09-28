# 2141 우체국
# 골드 4

import sys
input = sys.stdin.readline 

n = int(input().strip())
village = []
total_people = 0

for _ in range(n):
	x, a = map(int, input().split())
	village.append((x, a))
	total_people += a

village.sort()
check = 0
for i in range(n):
	check += village[i][1]
	if check >= (total_people/2):
		print(village[i][0])
		break

# 총인원/2를 넘는 지점에 설치 