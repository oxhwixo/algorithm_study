# 1041 주사위
# 골드 5

import sys

input = sys.stdin.readline

n = int(input().strip())
dice = list(map(int, input().split()))
ans = 0
min_list = []

if n == 1:
	print(sum(dice) - max(dice))

# 완성된 정육면체는 큐브 모양이며 맨 아래면은 보이지 않음
# 큐브를 이루는 블록들의 겉으로 보여지는 면은 1, 2, 3개 중 하나
# 면이 1개 보이는 블록 개수 = 4 * (n - 2)(n - 1) + (n - 2)(n - 2)
# 면이 2개 보이는 블록 개수 = 4 * (n - 2) + 4 * (n - 1)
# 면이 3개 보이는 블록 개수 = 4개 (가장 상단 모서리 4개)
# 주사위는 마주보는 면을 제외하고 모든 면이 인접
# 따라서 마주보는 면 중 최소를 찾아 리스트 저장
# 리스트에 저장된 세 값으로 결과 구하기

else:
	min_list = [min(dice[0], dice[5]),min(dice[1], dice[4]),min(dice[2], dice[3])]
	min_list.sort()
	
	n1 = 4 * (n - 2) * (n - 1) + (n - 2) * (n - 2)
	n2 = 4 * (n - 2) + 4 * (n - 1)
	n3 = 4

	ans = n1 * min_list[0] + n2 * sum(min_list[:2]) + n3 * sum(min_list)
	print(ans)
