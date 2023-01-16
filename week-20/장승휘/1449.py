# 1449 수리공 항승
# 실버 3

n, l = map(int, input().split())

spots = list(map(int, input().split()))
spots.sort()

start = 0
cnt = 0

for spot in spots:
	if start < spot:
		start = spot + l - 1
		cnt += 1

print(cnt)