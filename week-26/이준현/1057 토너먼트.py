import sys

input = sys.stdin.readline

n, jimin, han = map(int, input().split())
cnt = 1
while True:
    one = int((jimin + 1) / 2)
    two = int((han + 1) / 2)
    if one == two:
        print(cnt)
        exit(0)
    else:
        cnt += 1
    jimin = one
    han = two

