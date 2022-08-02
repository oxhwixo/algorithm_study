from bisect import bisect_left, bisect_right

def counting(array, left, right):
	left_idx = bisect_left(array, left)
	right_idx = bisect_right(array, right)
	return right_idx - left_idx

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = counting(array, x, x)

if count == 0:
	print(-1)
else:
	print(count)