import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]


res = -1
for i in range(n):  # i: 시작 행 위치
    for j in range(m):  # j: 시작 열 위치
        for a in range(-n, n):  # a: 행 방향 등차
            for b in range(-m, m):  # b: 열 방향 등차
                num = ''
                y, x = i, j
                # 행과 열 시작 위치부터 등차를 더해가며 숫자 생성
                while 0 <= y < n and 0 <= x < m:
                    num += arr[y][x]
                    if a == 0 and b == 0:
                        break
                    if int(math.sqrt(int(num))) ** 2 == int(num):
                        res = max(int(num), res)
                    y += a
                    x += b
print(res)
