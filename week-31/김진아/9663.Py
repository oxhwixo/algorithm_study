# 9663 N-Queen

n = int(input())
arr= [0] * n
result = 0

def adjacent(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x - i:
            return False
    return True

def solution(x):
    global result
    
    if x == n:
        result += 1
    else:
        for i in range(n):
            arr[x] = i
            if adjacent(x):
                solution(x + 1)

solution(0)
print(result)