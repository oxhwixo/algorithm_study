import sys
from decimal import Decimal
sys.setrecursionlimit(30000)
input = sys.stdin.readline
cnt = 0


def Recursive(r, amount, m):
    global cnt
    if cnt >= 1200:
        print("impossible")
        return
    amount += (amount * r) / 100
    amount = round(amount, 8)
    if (amount * 1000) % 10 == 5:
        amount += 0.001
    amount = round(amount, 2)
    amount -= m
    cnt += 1
    if amount > 0:
        Recursive(r, amount, m)
    else:
        print(cnt)
        return


n = int(input())
for _ in range(n):
    R, B, M = map(float, input().split())
    Recursive(R, B, M)
    cnt = 0
