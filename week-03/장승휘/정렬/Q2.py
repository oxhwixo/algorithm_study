n = int(input())

array = []

for i in range (n):
	student = input().split()
	array.append((student[0], int(student[1])))

array = sorted(array, key = lambda x: x[1])

for i in range (n):
	print(array[i][0], end=" ")