import sys

input = sys.stdin.readline

n, k = map(int, input().split())

start = 0
end = n // 2
while start <= end:
    mid = (start + end) // 2
    column = n - mid
    total = (mid + 1) * (column + 1)
    if total == k:
        print("YES")
        exit(0)
    if total > k:
        end = mid - 1
    else:
        start = mid + 1
print("NO")

