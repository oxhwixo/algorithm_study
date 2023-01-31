n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maximum = -1e9
minimum = 1e9

def dfs(i, arr):
	global add, sub, mul, div, maximum, minimum

	if i == n:
		maximum = max(maximum, arr)
		minimum = min(minimum, arr)

	else:
		if add > 0:
			add -= 1
			dfs(i + 1, arr + data[i])
			add += 1
		
		if sub > 0:
			sub -= 1
			dfs(i + 1, arr - data[i])
			sub += 1

		if mul > 0:
			mul -= 1
			dfs(i + 1, arr * data[i])
			mul += 1
		
		if div > 0:
			div -= 1
			dfs(i + 1, int(arr / data[i]))
			div += 1
	
dfs(1, data[0])

print(maximum)
print(minimum)