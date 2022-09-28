# 1931 회의실 배정
# 실버 1

import sys
input = sys.stdin.readline

n = int(input().strip())
data = []
for _ in range(n):
	first, second = map(int, input().split())
	data.append((first, second))
	
data.sort(key= lambda x: (x[1], x[0]))

last_time = 0
cnt = 0

for start, end in data:
	if start >= last_time:
		cnt += 1
		last_time = end
	
print(cnt)