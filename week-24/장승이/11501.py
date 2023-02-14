# 11501 주식
# 실버 2

import sys

input = sys.stdin.readline

test = int(input())
for _ in range(test):
	n = int(input())
	numbers = list(map(int, input().split()))

	value = 0
	max = 0

	for i in range(n - 1, -1, -1): # n - 1 부터 0까지
		if numbers[i] > max:
			max = numbers[i]
		else:
			value += max - numbers[i]
			
	print(value)
