import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
day = 0


def bfs(a, b, graph, visit):
    unit = []  # 연합에 가입한 나라 좌표
    people = 0  # 나라 인구수의 합

    q = deque()
    q.append((a, b))
    unit.append((a, b))
    people += graph[a][b]
    visit[a][b] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    unit.append((nx, ny))
                    people += graph[nx][ny]
                    visit[nx][ny] = True

    newPeople = people // len(unit)

    for a, b in unit:
        graph[a][b] = newPeople

    return True if len(unit) >= 2 else False


while True:
    visit = [[False] * n for _ in range(n)]
    stop = True  # stop이 True면 while문 종료

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                check = bfs(i, j, arr, visit)
                if check:
                    stop = False

    if stop:
        break
    else:
        day += 1

print(day)

# def BFS(x, y, visited):
#     global day
#     q = deque()
#     q.append((x, y))
#     people_sum = 0
#     unit = []
#     while q:
#         a, b = q.popleft()
#         visited[a][b] = True
#         people_sum += arr[a][b]
#         unit.append((a, b))
#         for k in range(4):
#             nx = a + dx[k]
#             ny = b + dy[k]
#             if nx < 0 or n <= nx or ny < 0 or n <= ny:
#                 continue
#             if visited[nx][ny]:
#                 continue
#             if not l <= abs(arr[a][b] - arr[nx][ny]) <= r:
#                 continue
#             q.append((nx, ny))
#     same_people = people_sum // len(unit)
#     for x, y in unit:
#         arr[x][y] = same_people
#     # if len(unit) >= 1:
#     #     return False
#     # else:
#     #     return True
#     return True if len(unit) >= 2 else False
#
#
# while True:
#     visited = [[False] * (n + 1) for _ in range(n)]
#     stop = True
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j]:
#                 flag = BFS(i, j, visited)
#                 if flag:
#                     stop = False
#     if stop:
#         break
#     else:
#         day += 1
#
# print(day)
