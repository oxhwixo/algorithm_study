import sys


input = sys.stdin.readline
n =  int(input().strip())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for x in coin:
	if target < x:
		break
	target += x

print(target)