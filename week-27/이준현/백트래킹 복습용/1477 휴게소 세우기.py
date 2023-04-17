import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0)
arr.insert(N, L)
arr.sort()
start, end = 1, L - 1
ans = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, len(arr)):
        dist = abs(arr[i - 1] - arr[i])
        if dist > mid:
            count += (dist - 1) // mid
    if count > M:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
print(ans)
