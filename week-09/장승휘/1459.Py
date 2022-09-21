# 1459 걷기
# 실버 4

import sys

input = sys.stdin.readline
x, y, w, s = map(int, input().split())

dis = 0
if w * 2 > s :
	rest = max(x, y) - min(x, y)
	dis = s * min(x, y) 
	if w < s:
		dis += w * rest
	elif w > s and (rest%2 == 1):
		dis += s * (rest - 1) + w
	elif w > s:
		dis += s * rest


else :
	dis = w * (x + y)

print(dis)