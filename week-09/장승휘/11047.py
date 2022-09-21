# 11047 동전 0
# 실버 4

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
res = 0

for _ in range(n):
	arr.append(int(input()))

# 뒤에서부터 확인해서 최대한 사용하기 
for i in reversed(arr): # 최대 10번
	if i <= k:
		res += int(k//i)
		k = k % i
	
print(res)



