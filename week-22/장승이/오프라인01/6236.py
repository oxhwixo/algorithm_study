# 6236 용돈 관리
# 실버 2
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
costs = [int(input()) for _ in range(n)]
start = min(costs)
end = sum(costs)

while start <= end:
	mid = (start + end) // 2
	money = mid
	withdrawal_count = 1

	for i in range(n):
		if money < costs[i]:
			money = mid
			withdrawal_count += 1
		money -= costs[i]

	# m번보다 더 많이 인출 or 인출 금액이 적은 경우
	if withdrawal_count > m or mid < max(costs):
		start = mid + 1

	# 여기서 m번 보다 적게 인출된 경우가 아니라
	# 딱 m번 인출했을 때의 최소값을 구할 수 있는 이유는
	# 최소값이 아닐때는 돈이 남아서! m번 보다 적게 인출 될 수 있지만,
	# 최소값이라는 자체가 m번에 딱 맞춰져 있다는 의미..
	else:
		end = mid - 1
		k = mid 

print(k)
