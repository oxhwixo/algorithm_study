# 1699 제곱수의 합
# 실버 2

n = int(input())

d = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j**2 > i:
            break
        d[i] = min(d[i], d[i - j**2] + 1)

print(d[n])