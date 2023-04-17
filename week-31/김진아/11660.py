# 11660 구간 합 구하기 5

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0 for _ in range(n + 1)]]

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    arr.append([0] + temp)

sumArr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        sumArr[i][j] = arr[i][j] + temp
        temp += arr[i][j]

def solution(x1, y1, x2, y2):
    answer = 0
    
    for i in range(x1, x2 + 1):
        answer += sumArr[i][y2] - sumArr[i][y1 - 1]
    
    print(answer)
    
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    solution(x1, y1, x2, y2)
    