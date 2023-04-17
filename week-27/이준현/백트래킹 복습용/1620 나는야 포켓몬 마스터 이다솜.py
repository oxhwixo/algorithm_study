import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = dict()
arr2 = dict()
for i in range(1, n + 1):
    name = input().rstrip()
    arr[name] = i
    arr2[i] = name
for _ in range(m):
    find = input().rstrip()
    value = arr.get(find)
    if value is None:
        value = arr2[int(find)]
    print(value)

