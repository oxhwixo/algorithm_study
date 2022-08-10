# 가게 좌표가 크기 순 대로 들어온다면
# 굳이 bfs 필요 없겠지만 그렇지 않을 수 있기 때문에 탐색이 필요함

from collections import deque
import sys

def distance(x, y, nx, ny):
	return abs(x - nx) + abs(y - ny)

def bfs(x, y):
	global end_x, end_y
	queue = deque([(x, y)])
	visited = set()

	while queue:
		x, y = queue.popleft()
		if distance(x, y, end_x, end_y) <= 1000 :
			return True
			# 목적지까지 한 번에 가지면 바로 True 반환
		for i in range(s):
			# 가게 개수만큼 확인
			store_x, store_y = store[i]
			if (store_x, store_y) not in visited:
				if distance(x, y, store_x, store_y) <= 1000 :
					visited.add((store_x, store_y))
					queue.append((store_x, store_y))
	return False

result = []
for _ in range(int(sys.stdin.readline().strip())):
	# 맨처음에 입력받는 수 만큼 반복
	s = int(input())
	start_x, start_y = map(int, sys.stdin.readline().split())
	store = [tuple(map(int, sys.stdin.readline().split())) for _ in range(s)]
	end_x, end_y = map(int, sys.stdin.readline().split())
	check = bfs(start_x, start_y)
	result.append('happy' if check else 'sad')

for i in result:
	print(i)

# dfs
# def distance(x, y, nx, ny):
# 	return abs(x - nx) + abs(y - ny)

# def dfs(x, y, status):
# 	global end_x, end_y, visited
# 	if distance(x, y, end_x, end_y) <= 1000 :
# 		return True
# 		# 목적지까지 한 번에 가지면 바로 True 반환
# 	for i in range(s):
# 		# 가게 개수만큼 확인
# 		store_x, store_y = store[i]
# 		if distance(x, y, store_x, store_y) <= 1000 :
# 			if not visited[i]:
# 				visited[i] = True
# 				status = dfs(store_x, store_y, status)
# 	return status

# result = []
# for _ in range(int(input())):
# 	# 맨처음에 입력받는 수 만큼 반복
# 	s = int(input())
# 	start_x, start_y = map(int, input().split())
# 	store = [tuple(map(int, input().split())) for _ in range(s)]
# 	end_x, end_y = map(int, input().split())
# 	visited = [False for _ in range(s)]
# 	check = dfs(start_x, start_y, False)
# 	result.append('happy' if check else 'sad')

# for i in result:
# 	print(i)

