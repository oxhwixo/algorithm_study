import sys
from itertools import combinations

input = sys.stdin.readline
ans = []
n = int(input())
for i in range(1, 11):
    for j in combinations(range(0, 10), i):
        j = list(j)
        j.sort(reverse=True)
        value = "".join(map(str, j))
        ans.append(int(value))
ans.sort()
if n - 1 >= len(ans):
    print(-1)
else:
    print(ans[n - 1])
# 0 1 2 3 4 5 6 7 8 9 - 10개
# 10
# 20 21
# 30 31 32
# 40 41 42 43
# .
# .
# .
# 90 91 ... 98 - 9개
# 210
# 320 321
# 430 431 432
# 0~9에서 len 만큼 뽑은 다음 순서에 맞게 배치하면 끝 인느낌
# 가능한 최대값
# 9,876,543,210
