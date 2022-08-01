n = int(input())
data = []
for i in range (n):
	data.append(int(input()))

data = sorted(data, reverse = True)

for i in range (n):
	print(data[i], end=' ')