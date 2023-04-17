# 15961 회전초밥

import sys
input = sys.stdin.readline

from collections import deque

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

answer = 0

def solution(start):
    global answer
    sushi = set()

    for i in range(k):
        index = (start + i) % n
        sushi.add(arr[index])

    sushi.add(c)
    answer = max(answer, len(sushi))
    
for i in range(n):
    solution(i)
    
print(answer)
