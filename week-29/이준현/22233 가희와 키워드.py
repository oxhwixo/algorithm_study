import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = set()
for _ in range(n):
    arr.add(input().rstrip())

for _ in range(m):
    value = list(input().rstrip().split(','))
    for i in value:
        if i in arr:
            arr.remove(i)
    print(len(arr))

# for _ in range(m):
#     value = list(input().rstrip().split(','))
#     for i in value:
#         arr.discard(i)
#     print(len(arr))
