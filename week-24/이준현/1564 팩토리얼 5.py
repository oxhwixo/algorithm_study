import sys

input = sys.stdin.readline

n = int(input().rstrip())
fac = [0] * (n + 1)
fac[1] = 1
for i in range(2, n + 1):
    # 5자리 수가 되지 않을떄
    fac[i] = fac[i - 1] * i
    while fac[i] % 10 == 0:
        fac[i] = int(fac[i] / 10)
    fac[i] %= 1000000000000
print(str(fac[n])[-5:])
