import math

T = int(input())

for _ in range(T):
    start_x, start_y, end_x, end_y = map(int, input().split())
    n = int(input())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))

    result = 0

    for c_x, c_y, r in c:
        # 시작점부터 행성계 중점까지의 거리
        start_distance = math.sqrt(math.pow(abs(start_x - c_x), 2) + math.pow(abs(start_y - c_y), 2))
        # 도착점부터 행성계 중점까지의 거리
        end_distance = math.sqrt(math.pow(abs(end_x - c_x), 2) + math.pow(abs(end_y - c_y), 2))

        # 시작점과 도착점이 모두 행성계 내부에 있음
        if start_distance < r and end_distance < r:
            continue
        elif start_distance > r and end_distance > r:
            continue
        else:
            result += 1
    print(result)