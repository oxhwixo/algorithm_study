import sys

input = sys.stdin.readline

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
student = [list(map(int, input().split())) for _ in range(m)]
ans = []
for i in range(m):
    cnt = 0
    for j in range(n):
        flag = True
        for course in schedule[j][1:]:
            if course not in student[i][1:]:
                flag = False
                break
        if flag:
            cnt += 1
    ans.append(cnt)
for i in ans:
    print(i)
