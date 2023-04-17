# 14719 빗물

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = list(map(int, input().split()))

rain = [[0 for _ in range(w)] for _ in range(h)]

for i in range(w):
    for j in range(h - 1, h - arr[i] - 1, -1):
        rain[j][i] = 1

count = 0

def solution(height):
    global count
    tempCnt = 0
    start = False
    
    for i in range(w):
        if rain[height][i] == 1:
            if start:
                count += tempCnt
                tempCnt = 0
            else:
                start = True
        else:
            if start:
                tempCnt += 1

for i in range(h):
    solution(i)
    
print(count)