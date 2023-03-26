import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(-x[0], -x[1]))

maxDate = arr[0][0]
temp = [[] for _ in range(maxDate)]
result = 0

for i in range(maxDate):
    for d, w in arr:
        if d >= i + 1:
            temp[i].append(w)

for i in range(maxDate - 1, -1, -1):
    if temp[i]:
        m = max(temp[i])
        result += m
        for j in temp:
            if m in j:
                j.remove(m)

print(result)