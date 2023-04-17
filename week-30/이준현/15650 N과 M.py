import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(range(1, n + 1))

for i in combinations(num_list, m):
    for j in i:
        print(j, end=' ')
    print()

