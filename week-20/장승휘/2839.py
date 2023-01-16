# 2839 설탕 배달
# 실버 4

# 3부터 N까지 작은 숫자부터 큰 숫자 순으로 
# 각각 가장 적은 양의 봉지를 저장해두면 
# 각각 값에서 3, 5 큰 위치에서 이전 값을 재활용 가능

N = int(input())

# 최소값을 구할 것이기 때문에 N의 최대값 보다 큰 수로 초기화
array = [5001] * 5001
array[3] = 1
array[5] = 1

for i in range(6, N + 1):
	array[i] = min(array[i - 3], array[i - 5]) + 1

if array[N] >= 5001:
	print(-1)
else:
	print(array[N])
