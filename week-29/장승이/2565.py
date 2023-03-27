# 2565 전깃줄
# 골드 5

import sys

input = sys.stdin.readline

n = int(input())
data = sorted(list(map(int, input().split())) for _ in range(n))

d = [1] * n
for i in range(n):
    for j in range(i):
        if data[i][1] > data[j][1]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))