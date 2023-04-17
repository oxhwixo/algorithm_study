import sys
from collections import deque

input = sys.stdin.readline
test = int(input())
for _ in range(test):
    cmd = input().rstrip()
    value = int(input())
    q = deque(input().strip()[1:-1].split(","))
    flag = False
    cnt = 0
    for i in range(len(cmd)):
        if cmd[i] == "R":
            cnt += 1
        elif cmd[i] == "D":
            if len(q) == 0 or q[0] == '':
                flag = True
                break
            if cnt % 2 == 0:
                q.popleft()
            else:
                q.pop()
    if flag:
        print("error")
        continue
    if cnt % 2:
        q.reverse()
    print('[' + ','.join(q) + ']')
