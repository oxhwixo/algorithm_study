# 1541 잃어버린 괄호
# 실버 3

divide_minus = input().split('-')
num = []

for i in divide_minus:
	num_temp = 0
	divide_plus = i.split('+')
	for j in divide_plus:
		num_temp += int(j)
	num.append(num_temp)

res = num[0]
for i in num[1:]:
	res -= i

print(res)