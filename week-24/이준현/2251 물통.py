import sys
from collections import deque

input = sys.stdin.readline
A, B, C = map(int, input().split())
q = deque()
ans = []
visited = [[False] * (B + 1) for _ in range(A + 1)]
q.append((0, 0))

while q:
    a, b = q.popleft()

    if visited[a][b]:
        continue
    visited[a][b] = True

    c = C - (a + b)
    if a == 0:
        ans.append(c)

    # C에서 A, B에 물주기
    q.append((a + min(c, A - a), b))
    q.append((a, b + min(c, B - b)))
    # B에서 A, C에 물주기
    q.append((a + min(b, A - a), b - min(b, A - a)))
    q.append((a, b - min(b, C - c)))
    # A에서 B, C에 물주기
    q.append((a - min(a, B - b), b + min(a, B - b)))
    q.append((a - min(a, C - c), b))
ans.sort()
for i in ans:
    print(i, end=' ')
