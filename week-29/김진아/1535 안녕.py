n = int(input())

strength = [0] + list(map(int, input().split()))
happiness = [0] + list(map(int, input().split()))

arr = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if strength[i] <= j:
            arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - strength[i]] + happiness[i])
        else:
            arr[i][j] = arr[i - 1][j]

print(arr[n][99])