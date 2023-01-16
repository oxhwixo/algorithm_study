# 1024 수열의 합 
# 실버 2

N, L = map(int, input().split())

# N = X + (X + 1) + (X + 2) + ... + (X + L - 1)
# N = LX + (1 + 2 + ... + L - 1)
# N = LX + (L - 1)(2 + L - 1 - 1)/2
# N = LX + L(L - 1)/2
# LX = N - L(L - 1)/2
# (N - L(L - 2)/2)가 L로 나누어 떨어지면 X는 정수

check = 0
for i in range(L, 101):
	x = N - (i * (i - 1) / 2)

	if x % i == 0 and x // i >= 0:
		x = int(x / i)
		check = 1

		for j in range(0, i):
			print(x + j, end = ' ')
		break

if check == 0 :
	print(-1)


