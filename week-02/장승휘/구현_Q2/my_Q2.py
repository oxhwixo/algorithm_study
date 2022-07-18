n, m = map(int, input().split())
user = list(map(int, input().split()))
game_map = [[0] * m for _ in range (n)]

cnt = 1
last_cnt = 0

for i in range(n):
	game_map[i] = list(map(int, input().split()))
	last_cnt += game_map[i].count(0)

# direction = 북0, 동1, 남2, 서3
steps = [[-1, 0], [0, 1], [1, 0], [0, -1]]
back_steps = [[1, 0], [0, -1], [-1, 0], [0, 1]]
game_map[user[0]][user[1]] = 2

brack_point = True

while brack_point == True:
	back_step = [user[0] + back_steps[user[2]][0], user[1] + back_steps[user[2]][1]]
	temp_dir = user[2]
	# 현재 위치, 현재 방향에서 뒤로 가는 경우.
	# user[3]은 현재 방향.
	# back_steps[현재방향][0 or 1]
	# 0은 열 1은 행
	
	for i in range (4):
		temp_dir = temp_dir - 1 # 다음 회전 방향
		if temp_dir == -1 :
			temp_dir = 3 
		next_step = [user[0] + steps[temp_dir][0], user[1] + steps[temp_dir][1]]
		# 회전한 방향에서 전진한 위치

		if game_map[next_step[0]][next_step[1]] == 0:
			game_map[next_step[0]][next_step[1]] = 2
			# 방문 했음을 나타내기 위해 이동한 위치의 지도값 업데이트
			cnt += 1
			user[0], user[1], user[2] = next_step[0], next_step[1], temp_dir
			# 전진한 위치가 0이면 유저 위치와 방향을 업데이트해준다.

		elif i == 3 and  game_map[back_step[0]][back_step[1]] == 1: 
			brack_point == False
			# 전 방향 탐색 다 했는데 0을 찾지 못했기 때문에 뒤로 한칸 가줘야 하는데, 이동한 곳이 바다라면 멈춤

		elif i == 3:
			user[0], user[1] = back_step[0], back_step[1]

	if cnt == last_cnt:
		break

print(cnt)