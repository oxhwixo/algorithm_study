# 16198 에너지모으기
# 실버 1

import sys
input = sys.stdin.readline

def bt(x):
    global ans

    if len(balls) == 2:
        ans = max(ans, x)
        return 
    
    for i in range(1, len(balls) - 1):
        energy = balls[i - 1] * balls[i + 1]
        temp = balls.pop(i)
        bt(x + energy)
        balls.insert(i, temp)

n = int(input())
balls = list(map(int, input().split()))
ans = 0
bt(0)

print(ans)