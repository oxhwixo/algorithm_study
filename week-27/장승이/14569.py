# 14569 시간표 짜기
# 실버 2

n = int(input())
courses = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    courses.append(set(tmp[1:]))

m = int(input())
students = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    students.append(set(tmp[1:]))

for student in students:
    cnt = 0
    for course in courses:
        if course.intersection(student) == course:
            cnt += 1
    print(cnt)