# 18111 마인크래프트
# 실버 2

# 인벤토리가 비어있으면 채워져야한다.
# 0층부터 256층까지 전부 확인

import sys

input = sys.stdin.readline
n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
last_floor = 0

for floor in range(257):
	use_block, take_block = 0, 0
	
	for i in range(n):
		for j in range(m):

			if graph[i][j] >= floor:
				take_block += graph[i][j] - floor
			else:
				use_block += floor - graph[i][j]
	
	if use_block > take_block + b:
		continue

	count = take_block * 2 + use_block
	
	if count <= ans:
		ans = count
		last_floor = floor

print(ans, last_floor)