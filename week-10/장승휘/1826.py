# 1826 연료채우기
# 골드3
import heapq

n = int(input()) # 주유소 개수
stations = [list(map(int, input().split())) for _ in range(n)] # 주유소 위치, 주유량
dest, current_fuel = map(int, input().split()) # 마을 위치, 남은 연료 양
stations.append([dest, 0])
stations.sort()
heap = []

cnt = 0
for i in range(len(stations)):
	if current_fuel - stations[i][0] < 0 :
		while heap:
			current_fuel += -heapq.heappop(heap)
			cnt += 1
			if current_fuel - stations[i][0] >= 0 :
				break
	if len(heap) == 0 and current_fuel - stations[i][0] < 0:
		cnt = -1
		break
	else: # 바로 위에 있는 조건문이 True가 아니면 실행됨. 맨 처음 If 조건문이랑은 상관 없음
		heapq.heappush(heap, -stations[i][1])

print(cnt)