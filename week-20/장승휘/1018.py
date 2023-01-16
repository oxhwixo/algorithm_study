# 1018 체스판 다시 칠하기
# 실버 4

n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]

count = []

for x in range(n - 7):
	for y in range(m - 7):
		start_w = 0
		start_b = 0

		for i in range(x, x + 8):
			for j in range(y, y + 8):
				if (i + j) % 2 == 0:
					if array[i][j] != 'W':
						start_w += 1
					if array[i][j] != 'B':
						start_b += 1
				else:
					if array[i][j] != 'B':
						start_w += 1
					if array[i][j] != 'W':
						start_b += 1
		count.append(min(start_w, start_b))

print(min(count))