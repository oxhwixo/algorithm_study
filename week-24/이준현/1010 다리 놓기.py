import math
import sys
input = sys.stdin.readline
from itertools import combinations

test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    arr = []
    count = 0
    # for i in range(1, m + 1):
    #     arr.append(i)
    # data = combinations(arr, n)
    # for i in data:
    #     count += 1
    print(math.comb(m, n))
