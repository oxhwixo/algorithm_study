n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

minValue = 1e9
temp = []

def calculate(numbers):
    totalS, totalB = 1, 0
    for n in numbers:
        totalS *= n[0]
        totalB += n[1]

    return abs(totalS - totalB)
    
def dfs(m, start):
    global minValue
    if len(temp) == m:
        minValue = min(calculate(temp), minValue)
        return

    for i in range(start, n):
        if arr[i] not in temp:
            temp.append(arr[i])
            dfs(m, start + 1)
            temp.pop()
    
for i in range(1, n + 1):
    dfs(i, 0)
    
print(minValue)