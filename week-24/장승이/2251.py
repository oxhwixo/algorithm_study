# 2251 물통
# 골드 5

# 모든 경우의 수를 찾는 완전탐색 BFS
# 물이 옮겨지는 모든 경우의 수를 찾고, A 물통이 비어있을 때 정답배열에 추가

from collections import deque

a, b, c = map(int, input().split())

q = deque()
q.append((0, 0))

visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True

ans = []

def visit(x, y):
	if not visited[x][y]:
		visited[x][y] = True
		q.append((x, y))

def bfs():
	while q:
		# x, y, z = a, b, c 각각의 현재 물 상태
		x, y = q.popleft()
		z = c - x - y

		if x == 0:
			ans.append(z)
		
		water = min(x, b - y) # a를 비우거나, b를 꽉 채우거나 [a --> b]
		visit(x - water, y + water)
		water = min(x, c - z) # a를 비우거나, c를 꽉 채우거나 [a --> c]
		visit(x - water, y)
		water = min(y, a - x) # b를 비우거나, a를 꽉 채우거나 [b --> a]
		visit(x + water, y - water)
		water = min(y, c - z) # b를 비우거나, c를 꽉 채우거나 [b --> c]
		visit(x, y - water)
		water = min(z, a - x) # c를 비우거나, a를 꽉 채우거나 [c --> a]
		visit(x + water, y)
		water = min(z, b - y) # c를 비우거나, b를 꽉 채우거나 [c --> b]
		visit(x, y + water)

bfs()

ans.sort()
for i in range(len(ans)):
	if i == len(ans) - 1:
		print(ans[i])
	else:
		print(ans[i], end = " ")
