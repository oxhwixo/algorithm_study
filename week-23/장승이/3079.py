# 3079 입국심사
# 골드 5

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
times = [int(input().strip()) for _ in range(n)]

start = min(times)
end = min(times) * m
ans = 0

while start <= end:
	mid = (start + end) // 2
	people = 0

	# (mid_time // 심사_time) == mid_time 동안 심사 받을 수 있는 인원  
	for time in times:
		people += mid // time
		if people >= m:
			break

	if people >= m:
		ans = mid
		end = mid - 1
	else:
		start = mid + 1

print(ans)
