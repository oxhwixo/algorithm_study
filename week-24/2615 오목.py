arr = [list(map(int, input().split())) for _ in range(19)]

dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]

def solution(x, y):
    target = arr[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        cnt = 1

        while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == target:
            cnt += 1

            if cnt == 5:
                if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and arr[x - dx[i]][y - dy[i]] == target:
                    break
                if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and arr[nx + dx[i]][ny + dy[i]] == target:
                    break
                print(target)
                print(x + 1, y + 1)
                exit(0)
            nx += dx[i]
            ny += dy[i]

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            solution(i, j)

print(0)