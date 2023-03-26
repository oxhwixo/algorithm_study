import math
import sys

input = sys.stdin.readline
test = int(input())
for _ in range(test):
    jo_x, jo_y, jo_r, bak_x, bak_y, bak_r = map(int, input().split())
    distance = math.sqrt((jo_x - bak_x) ** 2 + (jo_y - bak_y) ** 2)
    # 위치, 반지름 모두 동일할떄 => 무한
    if distance == 0 and jo_r == bak_r:
        print(-1)
        # 원이 닥 붙어있을떄
    elif abs(jo_r - bak_r) == distance or abs(jo_r + bak_r) == distance:
        print(1)
    # 반지름의 합이 길이보다 길떄
    elif abs(jo_r - bak_r) < distance < abs(jo_r + bak_r):
        print(2)
    else:
        print(0)
