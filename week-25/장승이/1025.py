# 1025 제곱수 찾기

import math

n, m  = map(int, input().split())
arr = [list(input()) for _ in range(n)]

ans = -1
for i in range(n):
    for j in range(m):
        for id in range(-n, n):
            for jd in range(-m, m):
                num = ''
                x, y = i, j
                while 0 <= x < n and 0 <= y < m:
                    num += arr[x][y]
                    if id == 0 and jd == 0:
                        break
                    if int(math.sqrt(int(num))) ** 2 == int(num):
                        ans = max(int(num), ans)
                    x += id
                    y += jd
print(ans)