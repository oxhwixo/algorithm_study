# 13549 숨바꼭질 3
# 골드 5

from collections import deque

n, k = map(int, input().split())
graph = [-1] * 100001
graph[n] = 0
queue = deque([n])

while queue:
	x = queue.popleft()

	for i in [x + 1, x - 1, x * 2]:
		if 0 <= i <= 100000 and graph[i] == -1:
			if i == x * 2:
				graph[i] = graph[x]
				queue.appendleft(i)
			else:
				graph[i] = graph[x] + 1
				queue.append(i)

print(graph[k])



