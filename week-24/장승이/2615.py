# 2615 오목
# 실버 1

graph = [list(map(int, input().split())) for _ in range(19)]

# 우상, 우, 우하, 하
dx = [ -1, 0, 1, 1]
dy = [ 1, 1, 1, 0]

# 좌하, 좌, 좌상, 상 
six_check_x = [1, 0, -1, -1]
six_check_y = [-1, -1, -1, 0]

for x in range(19):
	for y in range(19):
		if graph[x][y] == 1  or graph[x][y] == 2:

			flag = graph[x][y]

			for i in range(4):
				count = 1
				nx, ny = x + dx[i], y + dy[i]

				# 같은 방향에 같은 색의 돌이 있으면 그 방향으로 직진
				while nx >= 0 and nx < 19 and ny >= 0 and ny < 19 and graph[nx][ny] == flag:
					count += 1
					nx, ny = nx + dx[i], ny + dy[i]

				if count == 5:
					check_six = False

					if i == 0: # 우상 - 좌하
						six_x, six_y = x + six_check_x[0], y + six_check_y[0]
					elif i == 1: # 우 - 좌
						six_x, six_y = x + six_check_x[1], y + six_check_y[1]
					elif i == 2: # 우하 - 좌상
						six_x, six_y = x + six_check_x[2], y + six_check_y[2]
					elif i == 3: # 하 - 상
						six_x, six_y = x + six_check_x[3], y + six_check_y[3]
						
					if six_x >= 0 and six_x < 19 and six_y >= 0 and six_y < 19 and graph[six_x][six_y] == flag:
						check_six = True

					if check_six == False:
						print(flag)
						print(x + 1, y + 1)
						exit(0)

print(0)