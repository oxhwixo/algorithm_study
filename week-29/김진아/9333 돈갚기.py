n = int(input())
arr = [list(map(float, input().split())) for _ in range(n)]

for r, b, m in arr:
    interest = b * r * 0.01
    debt = b + round(b * r * 0.01, 2)
    month = 0
    flag = True
    
    while debt > 0:
        debt -= m
        debt += round(debt * r * 0.01, 2)
        month += 1
        if month > 1200 : 
            print('impossible')
            flag = False
            break
    
    if flag: 
        print(month)