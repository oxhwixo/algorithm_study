n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

temp = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 바이러스 퍼뜨리기
def virus(x, y):
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if nx >= 0 and nx < n and ny >= 0 and ny < m:
			if temp[nx][ny] == 0:
				temp[nx][ny] = 2
				virus(nx, ny)

def get_score():
	score = 0
	for i in range(n):
		for j in range(m):
			if temp[i][j] == 0:
				score += 1
	
	return score

def dfs(num_of_wall):
	global result
	if num_of_wall == 3:
		for i in range(n):
			for j in range(m):
				temp[i][j] = graph[i][j]
		for i in range(n):
			for j in range(m):
				if temp[i][j] == 2:
					virus(i, j)
		result = max(result, get_score())
		return
	
	# 벽세우기
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 0:
				graph[i][j] = 1
				num_of_wall += 1
				dfs(num_of_wall)
				graph[i][j] = 0
				num_of_wall -= 1

dfs(0)
print(result)
