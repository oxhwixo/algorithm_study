n, m = map(int, input().split())

res = 0

for i in range (n):
	data = list(map(int, input().split()))
	data_min = min(data)
	if res < data_min:
		res = data_min

print(res)

# 달라진 풀이 : 풀이 중 min() 함수를 사용하는 예시와 같은데
# 나는 조건문으로 res 변수와 입력되는 리스트의 가장 작은 수를 비교 했고, 책은 max 함수로 res 와 min(data) 를 비교함
