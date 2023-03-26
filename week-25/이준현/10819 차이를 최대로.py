from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max_value = 0

for perm in permutations(arr):
    sum_value = 0
    for i in range(2, n + 1):
        sum_value += abs(perm[i - 2] - perm[i-1])
    if sum_value > max_value:
        max_value = sum_value
print(max_value)
