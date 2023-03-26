# a, b, c = map(int, input().split())
# result = []
#
# if a <= c:
#     result.append(a)
#     result.append(c - a)
#     if a >= b:
#         result.append(a - b)
# if b <= c:
#     result.append(b)
#     result.append(c - b)
#     if b >= a:
#         result.append(b - a)
#
# result.append(c)
#
# resultArray = []
# for item in result:
#     if item not in resultArray:
#         resultArray.append(item)
# resultArray.sort()
#
# for item in resultArray:
#     print(item, end=" ")
from collections import deque

a, b, c = map(int, input().split())

# q의 쌍은 각각 a, b에 들어가는 물의 양
q = deque([(0, 0)])

visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True

answer = []

def water(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

while q:
    # a, b에 각 들어있는 물의 양 x, y
    x, y = q.popleft()
    z = c - x - y

    if x == 0:
        answer.append(z)

    # A => B
    amount = min(x, b - y) # a에 남아있는 물과 b가 꽉차기 전까지 채울 수 있는 물 중 최소값
    water(x - amount, y + amount)

    # A => C
    amount = min(x, c - z)
    water(x - amount, y)

    # B => A
    amount = min(y, a - x)
    water(x + amount, y - amount)

    # B => C
    amount = min(y, c - z)
    water(x, y - amount)

    # C => A
    amount = min(z, a - x)
    water(x + amount, y)

    # C => B
    amount = min(z, b - y)
    water(x, y + amount)

answer.sort()
for num in answer:
    print(num, end=' ')