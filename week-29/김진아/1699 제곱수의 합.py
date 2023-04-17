import math
n = int(input())
result = 0
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = i
    for j in range(1, math.floor(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)
        
print(dp[n])