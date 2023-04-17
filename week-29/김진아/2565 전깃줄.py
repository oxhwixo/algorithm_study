n = int(input())
arr = []
dp = [0 for i in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x:x[0])

for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# arr.sort()

# m = max(map(max, arr))
# graph2 = [[] for _ in range(m + 1)]

# for i in range(n):
#     for a, b in arr[:i]:
#         if arr[i][1] < b:
#             graph2[arr[i][0]].append(a)
#             graph2[a].append(arr[i][0])

# count = 0
# answer = []

# while True:
#     result = sum(map(sum, graph2))
#     if result == 0:
#         break
    
#     m = max(map(len, graph2))
#     for i in range(len(graph2)):
#         if len(graph2[i]) == m:
#             answer.append(i)
#             for j in graph2[i]:
#                 graph2[j].remove(i)
#                 graph2[i].remove(j)
            
# print(len(list(set(answer))))         
#     #