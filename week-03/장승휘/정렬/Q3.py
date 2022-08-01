n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
	if a[i] < b[i]:
		a[i], b[i] = b[i], a[i]
	else:
		break

print(sum(a))

# 처음에 생각한 방법.. 최소 최대값 찾는 연산을 k번 하기 때문에 타임아웃 날듯?
# for i in range(k):
# 	min_idx = a.index(min(a))
# 	max_idx = b.index(max(b))
# 	a[min_idx], b[max_idx] = b[max_idx], a[min_idx]