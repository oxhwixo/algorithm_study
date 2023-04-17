# 14712 넴모넴모

n, m = map(int, input().split())
arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

result = 0

def solution(count):
    global result
    
    if count == m * n:
        result += 1
        return
    
    x = count // m + 1
    y = count % m + 1
    
    solution(count + 1)
    
    if arr[x - 1][y] == 0 or arr[x][y - 1] == 0 or arr[x - 1][y - 1] == 0:
        arr[x][y] = 1
        solution(count  + 1)
        arr[x][y] = 0

solution(0)
print(result)