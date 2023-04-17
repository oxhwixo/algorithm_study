# 1535 안녕
# 실버 2

# 냅색 알고리즘

import sys
input = sys.stdin.readline


N = int(input()) 
L = [0] + list(map(int, input().split())) # Lost
P = [0] + list(map(int, input().split())) # Pleasure
dp = [[0] * 101 for _ in range(N + 1)] 

for i in range(1, N+1): 
    for j in range(1, 101): # 체력은 1 ~ 100
        if L[i] <= j: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + P[i]) 
        else: 
            dp[i][j] = dp[i-1][j] 

print(dp[N][99])