import sys

input = sys.stdin.readline

test = int(input().strip())
for _ in range(test):
    start_x, start_y, end_x, end_y, = map(int, input().split())
    planet = int(input())
    arr = []
    count = 0
    for _ in range(planet):
        value = list(map(int, input().split()))
        arr.append(value)
    for i in arr:
        x, y, distance = i
        start_flag = pow(start_x - x, 2) + pow(start_y - y, 2) < pow(distance, 2)
        end_flag = pow(end_x - x, 2) + pow(end_y - y, 2) < pow(distance, 2)
        # 출발점은 행성궤도에 있고 도착점은 그렇지 않을때
        if start_flag and not end_flag:
            count += 1
        # 도착점은 행성궤도에 있고 출발점은 그렇지 않을떄
        elif end_flag and not start_flag:
            count += 1
    # 둘다 같은 곳에 있거나 둘다 안속해 있을떄
    print(count)
