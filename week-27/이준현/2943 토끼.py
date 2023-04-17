import math
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(M)]
k = int(math.sqrt(N))
cup = [0 for _ in range(N // k + 1)]
stick = [0 for _ in range(N + 1)]
for i in range(M):
    s, a = arr[i]
    ans = 0
    # 컵을 하기 위한 첫번쨰 인자가 되기 전까지 성냥을 더함 + (전체 갯수 - 성냥 개수) // k로 더할만큼의 컵의 index를 구함 ,  이때 필요한 컵의 기초 인덱스가 필요함
    # 기초 컵의 index는 A를 통해 계산할 수 있어야함.
    # 컵을 다 배치하고 난 다음에 놓을 성냥을 배치해야함
    if s >= k:
        stick_idx = a % k
        stick_idx = (k + 1 - stick_idx) % k
    else:
        stick_idx = a % k
    cup_idx = (a - 2 + k) // k
    s -= stick_idx
    cup_cnt = s // k
    for j in range(stick_idx):
        stick[a + j] += 1
        ans += stick[a + j]
    for j in range(cup_cnt):
        cup[cup_idx + j] += 1
        ans += cup[cup_idx + j]
    end_cnt = s - (cup_cnt * k)
    end_idx = a + (cup_cnt * k) + stick_idx
    if end_idx == k * (len(cup) - 1) + 1 and end_cnt == N - ((len(cup) - 1) * k):
        cup[-1] += 1
        ans += cup[-1]
    else:
        for j in range(end_cnt):
            stick[end_idx + j] += 1
            ans += stick[end_idx + j]
    print(ans)
