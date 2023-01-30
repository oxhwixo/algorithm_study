# 21316 스피카
# 실버 3

graph = [[] for _ in range(13)]
three = []

for _ in range(12):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

for i in range(1, 13):
	if len(graph[i]) == 3:
		three.append(i)

for i in three:
	sum = 0
	for j in graph[i]:
		sum += len(graph[j])
	if sum == 6:
		print(i)
		break
