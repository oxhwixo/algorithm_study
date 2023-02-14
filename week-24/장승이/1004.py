# 1004 어린왕자
# 실버3

# 행성을 접하는 경우는 출발점이나 도착점이 행성의 내부에 위치한 경우이다.
# 어떤 점이 원 안에 있는지 알기 위해서는
# 원의 중심과 점사이의 거리가 원의 반지름보다 큰지 작은지를 파악해야한다.
# 같은 원에 대하여 출발점과 도착점 모두 반지름보다 작으면 같은 원 안에 있다는 것에 주의.

import sys

input = sys.stdin.readline
number = int(input())
ans = []

for _ in range(number):
	count = 0
	x1, y1, x2, y2 = map(int, input().split())
	number_of_planet = int(input())
	count = 0

	for _ in range(number_of_planet):
		px, py, pr = map(int, input().split())
		# 점과 점 사이의 거리 구하는 공식 이용
		# 원래는 제곱근을 구해야하지만 반지름에 제곱을 해주면
		# 굳이 math.sqrt 해주지 않아도 된다.
		start_to_middle = (x1 - px) ** 2 + (y1 - py) ** 2
		end_to_middle = (x2 - px) ** 2 + (y2 - py) ** 2
		pr = pr ** 2

		if start_to_middle < pr and end_to_middle < pr:
			continue
		elif start_to_middle < pr:
			count += 1
		elif end_to_middle < pr:
			count += 1
		
	print(count)

