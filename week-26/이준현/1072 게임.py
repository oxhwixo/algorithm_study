import math
import sys

input = sys.stdin.readline

x, y = map(int, input().split())
z = math.floor(y * 100 / x)

if z >= 99:
    print(-1)
    exit(0)

start = 1
end = x
ans = 0
while start <= end:
    mid = (start + end) // 2
    temp = math.floor((y + mid) * 100 / (x + mid))
    if temp == z:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1
print(ans)
