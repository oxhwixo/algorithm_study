# 17086 아기상어2
# 실버 2

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
array = []
sharks = deque()

for i in range(n):
	temp = list(map(int, input().split()))
	for j in range(m):
		if temp[j] == 1:
			sharks.append((i, j))
	array.append(temp)

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def bfs():
	while sharks:
		x, y = sharks.popleft()
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < m:
				if array[nx][ny] == 0:
					sharks.append((nx, ny))
					array[nx][ny] = array[x][y] + 1

bfs()
safe_distance = max(map(max, array))
print(safe_distance)


