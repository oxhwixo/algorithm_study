import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, a)