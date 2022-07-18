n = input()

len = int(len(n) / 2)
right_sum = 0
left_sum = 0

for i in range (len):
	left_sum += int(n[i])
	right_sum += int(n[len * 2 - i - 1])

if left_sum == right_sum:
	print("LUCKY")
else :
	print("READY")