n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
max = data[n - 1]
next_max = data[n - 2]
# 데이터 정렬해주면 맨 끝이 가장 큰 수, 맨 끝에서 앞에 있는 수가 다음으로 큰 수

result = int(((m // (k + 1)) * k) * max + (m % (k + 1)) * max + (m // (k + 1)) * next_max)
# 반복되는 수열(규칙)을 이용해서 해결
# 가장 큰 수를 연속해서 더한 후에 그 다음으로 큰 수를 더하는 수열
# (m / (k + 1)) 는 수열이 반복되는 횟수이다. 여기에 k 를 곱하면 몇 번 가장 큰 수가 더해지는지 알 수 있다.
# m 이 k + 1 로 딱 떨어지지 않을 때는, 나머지 수 만큼 큰 수가 더해진다.
# 그 다음으로 큰 수가 더해지는 횟수는 수열이 반복되는 횟수와 같다.
print(max, next_max)
print(result)