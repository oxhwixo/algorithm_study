n, m = map(int,input().split())
data = list(map(int, input().split()))

weight = [0] * 11
for x in data:
	weight[data] += 1

result = 0
for i in range(1,m + 1):
	n -= weight[i]
	result = weight[i] * n

count = 0
