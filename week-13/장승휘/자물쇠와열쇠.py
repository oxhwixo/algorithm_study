# key 회전 시키는 함수
def rotate_key(key, N):
	temp = [[0] * N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			temp[j][N - 1 - i] = key[i][j]

	return temp

# 자물쇠 부분 확인하는 함수
def check_lock(new_lock,N, M):
	for i in range(M):
		for j in range(M):
			if new_lock[N - 1 + i][N - 1 + j] != 1:
				return False
	return True

def solution(key, lock):
	N = len(key)
	M = len(lock)

	# 2 * N + M - 2 크기의 보드 생성해서 가운데에 lock 복사하기 (N < M 조건에 의해 M * 3 해도됨)
	new_lock = [[0] * (2 * N + M - 2) for _ in range (2 * N + M - 2)]
	for i in range(0, M):
		for j in range(0, M):
			new_lock[N - 1 + i][N - 1 + j] = lock[i][j]

	for _ in range(4):
		key = rotate_key(key, N)
		for x in range(0, N + M - 1):
			for y in range(0, N + M - 1):
				for i in range(N):
					for j in range(N):
						new_lock[x + i][y + j] += key[i][j]
				if check_lock (new_lock, N, M) == True:
					return True
				for i in range(N):
					for j in range(N):
						new_lock[x + i][y + j]-= key[i][j]

	return False

# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))