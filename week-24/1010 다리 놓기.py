import math

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    temp = [i for i in range(m)]
    result = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(result)