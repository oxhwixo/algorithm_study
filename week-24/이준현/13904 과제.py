import sys
from collections import deque
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
task = []
max_day = 0
for i in range(n):
    x, y = map(int, input().split())
    if x > max_day:
        max_day = x
    task.append((x, y))
task.sort(reverse=True)
task = deque(task)
day = min((len(task), max_day))
ans = 0
task_list = PriorityQueue()

while day != 0:
    while task and task[0][0] >= day:
        time, cost = task[0]
        task.popleft()
        if time >= day:
            task_list.put(-cost)
    if not task_list.empty():
        ans -= task_list.get()
    day -= 1
print(ans)
