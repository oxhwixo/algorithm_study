# 16931 겉넓이 구하기
# 실버 2

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = n * m * 2

for i in range(n):
    prev = 0
    for j in range(m):
        if arr[i][j] > prev:
            ans += (arr[i][j] - prev) * 2
        prev = arr[i][j]
    
for i in range(m):
    prev = 0
    for j in range(n):
        if arr[j][i] > prev:
            ans += (arr[j][i] - prev) * 2
        prev = arr[j][i] 

print(ans)