import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    maxNum = arr[-1]
    for i in range(N - 2, -1, -1):
        if arr[i] > maxNum:
            maxNum = arr[i]
        else:
            result += maxNum - arr[i]
    print(result)