import math
import sys

input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n = int(input())
    a = [True] * (n + 1)
    a[0] = a[1] = False
    m = int(n ** 0.5)
    arr = []
    ans = 0
    for i in range(2, m + 1):
        if a[i]:
            for j in range(i + i, n + 1, i):
                a[j] = False
    for i in range(n + 1):
        if a[i]:
            if a[n - i] and i <= n // 2:
                ans += 1
    print(ans)
