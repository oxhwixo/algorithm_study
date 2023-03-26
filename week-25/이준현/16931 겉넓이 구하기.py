import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
for i in range(n):
    for j in range(m):
        for k in range(1, arr[i][j] + 1):
            cnt = 6
            # 1층이 아니면 무조건 밑면 하나 빠짐
            if k != 1:
                cnt -= 1
            # 해당 돌 위에 돌이 있어도 하나 빠짐
            if k < arr[i][j]:
                cnt -= 1
            for a in range(4):
                nx = i + dx[a]
                ny = j + dy[a]

                if nx < 0 or n <= nx or ny < 0 or m <= ny:
                    continue
                if arr[nx][ny] >= k:
                    cnt -= 1
            ans += cnt
print(ans)
