import sys

input = sys.stdin.readline

arr = []
for i in range(19):
    arr.append(list(map(int, input().split())))

# 오른쪽, 아래, 왼쪽 아래, 오른쪽 아래
dx = [0, 1, 1, 1]
dy = [1, 0, -1, 1]
black_list = []
white_list = []
black_flag = False
white_flag = False
ans = []
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            black_list.append((i, j))
        if arr[i][j] == 2:
            white_list.append((i, j))

for i, j in black_list:
    for k in range(4):
        if black_flag:
            continue
        nx = i
        ny = j
        ans.append((nx, ny))
        nx += dx[k]
        ny += dy[k]
        count = 1
        while -1 < nx < 19 and -1 < ny < 19 and arr[nx][ny] == 1:
            ans.append((nx, ny))
            nx += dx[k]
            ny += dy[k]
            count += 1
        if count == 5:
            nx -= dx[k] * 6
            ny -= dy[k] * 6
            black_flag = True
            if -1 < nx < 19 and -1 < ny < 19:
                if arr[nx][ny] == 1:
                    ans.clear()
                    black_flag = False
                    continue
        else:
            ans.clear()

if not black_flag:
    for i, j in white_list:
        for k in range(4):
            if white_flag:
                continue
            nx = i
            ny = j
            ans.append((nx, ny))
            nx += dx[k]
            ny += dy[k]
            count = 1
            while -1 < nx < 19 and -1 < ny < 19 and arr[nx][ny] == 2:
                ans.append((nx, ny))
                nx += dx[k]
                ny += dy[k]
                count += 1
            if count == 5:
                nx -= dx[k] * 6
                ny -= dy[k] * 6
                white_flag = True
                if -1 < nx < 19 and -1 < ny < 19:
                    if arr[nx][ny] == 2:
                        ans.clear()
                        white_flag = False
                        continue
            else:
                ans.clear()

ans_x, ans_y = 20, 20

for i, j in ans:
    if j == ans_y:
        if i < ans_x:
            ans_x = i
    elif j < ans_y:
        ans_x = i
        ans_y = j
if black_flag:
    print(1)
    print(ans_x + 1, ans_y + 1)
elif white_flag:
    print(2)
    print(ans_x + 1, ans_y + 1)
else:
    print(0)
