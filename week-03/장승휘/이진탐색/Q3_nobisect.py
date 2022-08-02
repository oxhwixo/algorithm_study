def counting(array, x):
	n = len(array)

	first_idx = first(array, x, 0, n - 1)

	if first_idx == None:
		return 0
	
	last_idx = last(array, x, 0, n - 1, n)
	return last_idx - first_idx + 1

def first(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	if ((mid == 0 or target > array[mid - 1]) and array[mid] == target):
		return mid
	elif array[mid] >= target: # 같거나 작으면 왼쪽 확인해야함
		return first(array, target, start, mid - 1)
	else:
		return first(array, target, mid + 1, end)

def last(array, target, start, end, n):
	if start > end:
		return None
	mid = (start + end) // 2
	if ((mid == n - 1 or target < array[mid + 1]) and array[mid] == target):
		return mid
	elif array[mid] > target:
		return last(array, target, start, mid - 1, n)
	else: #같거나 크면 오른쪽 확인 해야함
		return last(array, target, mid + 1, end, n)

	# 중간값이랑 타겟이 같을 때, 첫번 째 값 찾을 때는 왼쪽 봐야하고 마지막 값 찾을 때는 오른쪽 봐야함

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = counting(array, x)

if count == 0:
	print(-1)
else:
	print(count)

