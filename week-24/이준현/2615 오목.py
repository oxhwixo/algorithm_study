import sys

input = sys.stdin.readline
arr = []
visited = [[False] * 18 for i in range(19)]
for _ in range(19):
    arr.append(list(map(int, input().split())))
visited = [[False] * 19 for i in range(19)]
white_flag = False
black_flag = False
white = []
black = []
ans = []
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            black.append((i, j))
        if arr[i][j] == 2:
            white.append((i, j))

# 상, 하, 좌, 우, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

for i, j in black:
    if not black_flag:
        for direct in range(8):
            if not black_flag:
                count = 0
                nx = i
                ny = j
                ans.append((i, j))
                for k in range(5):
                    nx = nx + dx[direct]
                    ny = ny + dy[direct]
                    if (nx < 0 or 18 < nx or ny < 0 or 18 < ny or arr[nx][ny] == 2 or arr[nx][ny] == 0) and count != 4:
                        ans.clear()
                        break
                    elif count == 4 and (
                            nx < 0 or 18 < nx or ny < 0 or 18 < ny or arr[nx][ny] == 2 or arr[nx][ny] == 0):
                        continue
                    if arr[nx][ny] == 1:
                        count += 1
                        ans.append((nx, ny))
                    if count == 4 and arr[nx][ny] != 1:
                        nx = nx - dx[direct]
                        ny = ny - dy[direct]

                if count >= 4:
                    nx = nx - 5 * dx[direct]
                    ny = ny - 5 * dy[direct]
                    black_flag = True
                    if 0 <= nx <= 18 and 0 <= ny <= 18:
                        if arr[nx][ny] == 1:
                            ans.clear()
                            black_flag = False
            else:
                break
    else:
        break

if not black_flag:
    for i, j in white:
        if not white_flag:
            for direct in range(8):
                if not white_flag:
                    count = 0
                    nx = i
                    ny = j
                    ans.append((i, j))
                    for k in range(5):
                        nx = nx + dx[direct]
                        ny = ny + dy[direct]
                        if (nx < 0 or 18 < nx or ny < 0 or 18 < ny or arr[nx][ny] == 2 or arr[nx][
                            ny] == 0) and count != 4:
                            ans.clear()
                            break
                        elif count == 4 and (
                                nx < 0 or 18 < nx or ny < 0 or 18 < ny or arr[nx][ny] == 2 or arr[nx][ny] == 0):
                            continue
                        if arr[nx][ny] == 1:
                            count += 1
                            ans.append((nx, ny))
                        if count == 4 and arr[nx][ny] != 1:
                            nx = nx - dx[direct]
                            ny = ny - dy[direct]

                    if count >= 4:
                        nx = nx - 5 * dx[direct]
                        ny = ny - 5 * dy[direct]
                        white_flag = True
                        if 0 <= nx <= 18 and 0 <= ny <= 18:
                            if arr[nx][ny] == 1:
                                ans.clear()
                                white_flag = False
                else:
                    break
        else:
            break
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
