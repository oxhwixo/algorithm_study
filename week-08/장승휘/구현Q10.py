# 열쇠 90도 회전
def rotate_90(a):
	n = len(a)
	m = len(a[0])
	result = [[0] * n for _ in range(m)]
	for i in range(n):
		for j in range(m):
			result[j][n - i - 1] = a[i][j]
	return result

# 자물쇠 중간부분이 전부 1인지 체크
def check(new_lock):
	lock_length = len(new_lock)
	for i in range(lock_length, lock_length * 2):
		for j in range(lock_length, lock_length * 2):
			if new_lock[i][j] !=  1:
				return False
	return True

def solution(key, lock):
	n = len(lock)
	m = len(key)

	# 자물쇠 3배 크기
	new_lock = [[0] * (n * 3) for _ in range(n * 3)] 

	for i in range(n):
		for j in range(n):
			# 3배 크기 자물쇠 가운데에 원래 자물쇠 넣기
			new_lock[i + n][j + n] = lock[i][j] 
	
	for rotation in range(4):
		key = rotate_90(key)

		# 원래 자물쇠의 맨 오른쪽 아래 인덱스까지만 확인
		for x in range(n * 2): 
			for y in range(n * 2):

				# 자물쇠에 열쇠 넣기
				for i in range(m):
					for j in range(m):
						new_lock[x + i][y + j] += key[i][j]
					
				if check(new_lock) == True:
					return True
				
				# 자물쇠에서 열쇠 다시 빼기
				for i in range(m):
					for j in range(m):
						new_lock[x + i][y + j] -= key[i][j]
		return False
