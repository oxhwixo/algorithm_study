n = int(input())
data = list(map(int, input().split()))
data.sort()

person = 0
group = 0

for i in data:
	person += 1
	if i == person:
		group += 1
		person = 0

print(group) 