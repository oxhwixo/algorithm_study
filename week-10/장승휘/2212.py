# 2212 센서
# 골드 5

# N개의 센서 - K개의 집중국을 세워서 "수신 가능 영역"을 조절
# # 각 영역의 거리 합 최소화

n = int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수
sensors = list(map(int, input().split()))

sensors.sort()
sensors_distance = [sensors[i] - sensors[i-1] for i in range(1, n)]
sensors_distance.sort()

print(sum(sensors_distance[:n - k]))

# 센서 8
# 집중국 3
# (1 3 5 6) / (9 10) / (15 16) 
# 2 - 2 - 1 - <3> - 1 - <5> - 1
