import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
q = deque()
pq = []
for i in range(1, n + 1):
    q.append(i)
find_value = list(map(int, input().split()))

cnt = 0

for i in range(m):
    rotate_right = 0
    rotate_left = 0
    while q[rotate_right] != find_value[i]:
        rotate_right -= 1
    while q[rotate_left] != find_value[i]:
        rotate_left += 1
    if rotate_left == rotate_right:
        q.popleft()
    else:
        if rotate_left < - rotate_right:
            q.rotate(-rotate_left)
            cnt += rotate_left
        else:
            q.rotate(-rotate_right)
            cnt -= rotate_right
        q.popleft()
print(cnt)

# 1 2 3 4 5 6 7 8 9 10 - 1번연산 사용 // 2번 사용횟수 : 0, 3번 사용횟수 : 0
# 2 3 4 5 6 7 8 9 10  - 1번연산 사용 -> 2번을 찾아냄  // 2번 사용횟수 : 0, 3번 사용횟수 : 0
# 3 4 5 6 7 8 9 10 - 1번연산 사용 // 2번 사용횟수 : 0, 3번 사용횟수 : 0
# 4 5 6 7 8 9 9 10 - 1번연산 사용 // 2번 사용횟수 : 0, 3번 사용횟수 : 0
# 5 6 7 8 9 10 - 3번 연산 사용 // 2번 사용횟수 : 0, 3번 사용횟수 : 1
# 10 5 6 7 8 9 - 1번연산 사용  // 2번 사용횟수 : 0, 3번 사용횟수 : 0
# 5 6 7 8 9 - 3번 연산 사용 // 2번 사용횟수 : 0, 3번 사용횟수 : 2
# 9 5 6 7 8 - 1번연산 사용 - 9 를 찾음 // 2번 사용횟수 : 0, 3번 사용횟수 : 0
# 5 6 7 8 - 1번연산 사용 - 5를 찾음 // 2번 사용횟수 : 0, 3번 사용횟수 : 0
# ---
# 남은 것 6, 7, 8 // 2번 사용횟수 : 0, 3번 사용횟수 : 2
# ans = 2?
# 5 6 7 8 9 10
# 10 5 6 7 8 9
# 5 6 7 8
