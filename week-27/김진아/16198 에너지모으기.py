n = int(input())
weights = list(map(int, input().split()))
result = 0

def search(num):
    global result
    if len(weights) == 2:
        result = max(result, num)
    
    for i in range(1, len(weights) - 1):
        target = weights[i - 1] * weights[i + 1]
        v = weights.pop(i)
        search(num + target)
        weights.insert(i, v)

search(0)
print(result)