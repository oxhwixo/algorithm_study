# 1564 팩토리얼5
# 실버 2

n = int(input())

ans = 1
for i in range(1, n + 1):
	ans *= i
	while str(ans)[-1] == "0":
		ans //= 10
	ans %= 1000000000000

print(str(ans)[-5:])