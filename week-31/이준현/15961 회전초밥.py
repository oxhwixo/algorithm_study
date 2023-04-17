import sys
from collections import defaultdict

input = sys.stdin.readline
n, d, k, c = map(int, input().split())
arr = list(int(input()) for i in range(n))

left, right = 0, k - 1
dict = defaultdict(int)
dict[c] += 1

for i in range(right + 1):
    dict[arr[i]] += 1
result = -int(1e9)
while left < n:
    result = max(len(dict), result)
    dict[arr[left]] -= 1
    if dict[arr[left]] == 0:
        del dict[arr[left]]
    left += 1
    right += 1
    dict[arr[right % n]] += 1

print(result)
# q = deque(arr[0:k])
# cnt = 0
# for i in range(k, n):
#     q.append(arr[i])
#     q.popleft()
# for i in range(0, k):
#     q.append(arr[i])
#     q.popleft()
#
# print(cnt)


# ans = []
# for i in range(n):
#     if i + k < n:
#         s = set(arr[i:i + k])
#         s.add(c)
#         ans.append(len(s))
#     else:
#         index = (i + k) % n
#         if index == 0:
#             index += 1
#         s = set(arr[i:n]) | set(arr[0:index])
#         s.add(c)
#         ans.append(len(s))
# print(max(ans))
