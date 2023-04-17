n, m = map(int, input().split()) 

arr = [[0] * (m + 1) for _ in range(n + 1)]
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
        solution(count + 1)
        arr[x][y] = 0
solution(0)    
print(result)


# import math
# n, m = map(int, input().split())

# def solution(n, r):
#     return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# def minus(k, r):
#     return (n - 1) * (m - 1) * solution(k - (r - r % 4), r % 4) * (r // 4)

# result = 0
# for i in range(0, 4):
#     print(str(n * m) + 'C' + str(i))
#     result += solution(n * m, i)

# for i in range(4, n * m):
#     print(str(n * m) + 'C' + str(i) + '-' + str((n - 1) * (m - 1)) + '*' + str(n * m - (i - i % 4)) + 'C' + str(i % 4))
#     result += solution(n * m, i) - minus(n * m, i)

# print(result)