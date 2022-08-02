n = int(input())
array = list(map(int, input().split()))

start = 0
end =  n - 1
res = -1
while (start <= end):
	mid = (start + end) // 2
	if mid == array[mid]:
		res = mid
		break
	elif mid > array[mid]:
		start = mid + 1
	else:
		end = mid - 1

print(res)