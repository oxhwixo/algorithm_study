import heapq

def solution(food_times, k):
	if sum(food_times) <= k:
		return -1

	q = []
	for i in range(len(food_times)):
		heapq.heappush(q, (food_times[i], i + 1))
		# 음식 시간, 음식 번호 -> 시간순으로 정렬된 우선순위 큐

	sum_value = 0
	prev = 0
	length = len(food_times)

	while sum_value + ((q[0][0] - prev) * length) <= k:
		# 이미 쓴 시간 + 이제 쓸 시간이 k 보다 작거나 같을 때 반복문
		now = heapq.heappop(q)[0]
		sum_value += (now - prev) * length
		length -= 1
		prev = now

	result = sorted(q, key = lambda x: x[1])
	return result[(k - sum_value) % length][1]