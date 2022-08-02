def bs(target, start, end):
	if start > end:
		return False
	mid = (start + end) // 2
	if store[mid] == target:
		return True
	elif store[mid] > target:
		return bs(target, start, mid - 1)
	elif store[mid] < target:
		return bs(target, mid + 1, end)

n = int(input())
store = list(map(int, input().split()))
m = int(input())
customer = list(map(int, input().split()))

store.sort()

for i in range(m):
	result = bs(customer[i], 0, n - 1)
	if result == True:
		print('yes', end=' ')
	else:
		print('no', end=' ')
