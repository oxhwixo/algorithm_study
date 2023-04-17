# 2961 도영이가 만든 맛있는 음식
# 실버 2

import sys
input = sys.stdin.readline

n = int(input())
foods = [list(map(int, input().split(" "))) for _ in range(n)]
ans = []
temp_idx = []

def bt(num, depth):
    if depth == n:
        return
    for i in range(num, n):
        temp_idx.append(i)
        mult = 1
        add = 0
        print(temp_idx)
        for j in temp_idx:
            mult *= foods[j][0]
            add += foods[j][1]
        ans.append(abs(mult-add))
        bt(i + 1, depth + 1)
        temp_idx.remove(i)

bt(0, 0)
print(min(ans))