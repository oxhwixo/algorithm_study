from turtle import st


array = input()

str_array = []
res = 0

for i in array:
	if ord(i) < 58 and ord(i) > 47 :
		res += int(i)
	elif ord(i) < 91 and ord(i) > 64 :
		str_array.append(i)

str_array.sort()
str_array.append(str(res))
print(''.join(str_array))