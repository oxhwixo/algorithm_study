import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
dist = [0] * (100000 + 1)

queue = deque()
queue.append(n)

while queue:
	x = queue.popleft()
	if x == k:
		print(dist[x])
		break

	for j in (x-1, x+1, x*2):
		if 0 <= j <= 100000 and dist[j] == 0:
		# if 0 <= j and dist[j] == 0 로 하면 Out of range
		# 앞에 조건이 이미 False면 뒤에는 확인 하지 않는듯
			dist[j] = dist[x] + 1
			queue.append(j)
