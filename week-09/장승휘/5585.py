# 5585번 거스름돈
# 브론즈 2

n = 1000 - int(input())
count = 0

while int(n//500) > 0:
	n -= 500
	count += 1

while int(n//100) > 0:
	n -= 100
	count += 1

while int(n//50) > 0:
	n -= 50
	count += 1

while int(n//10) > 0:
	n -= 10
	count += 1

while int(n//5) > 0:
	n -= 5
	count += 1

while int(n//1) > 0:
	n -= 1
	count += 1

print(count)