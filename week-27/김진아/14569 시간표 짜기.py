n = int(input())
lessons = []

for _ in range(n):
    temp = list(map(int, input().split()))
    lessons.append(temp[1:])

m = int(input())
students = []

for _ in range(m):
    temp = list(map(int, input().split()))
    students.append(temp[1:])

for student in students:
    result = 0
    for lesson in lessons:
        if len(list(set(lesson) - set(student))) == 0:
            result += 1
    
    print(result)