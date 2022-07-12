data = list(map(int, input()))
# 와 너무 놀랍다 data = list(map(int, input().split())) 이렇게 하면 스페이스 기준으로 입력을 자르는데
# data = list(map(int, input())) 이렇게 하면 그냥 연속해서 입력한 문자열이 한 글자씩 정수형으로 변환되고 각각 다른 인덱스를 가진 배열이 됨
# 원리는 input으로 입력을 받으면 그게 하나의 문자열 리스트가 되고,
# 문자열 리스트는 순서가 있는 Iterable 이기 때문에 map 에서 차례로 각각 int()가 적용되어 정수로 바뀌어 반환됨.. 

len = len(data)
res = 0

for i in range(len):
	if i == 0:
		res = data[i]
		continue
	if res == 0 or res == 1:
		res += data[i]
	else:
		res *= data[i]

print(res)