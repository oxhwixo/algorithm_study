import sys
from collections import deque


input = sys.stdin.readline


test = int(input())

for _ in range(test):
    stock = int(input())
    q = deque()
    ans = 0
    arr = list(map(int, input().split()))
    arr.reverse()
    max_value = arr[0]
    for i in range(1, stock):
        if arr[i] >= max_value:
            max_value = arr[i]
        else:
            ans += max_value - arr[i]
    print(ans)

    # 이 코드는 87프로에서 시간초과 뜬다.
    # 주식이 다음날 주식이 오르면 사고, 내리면 판다.
    # for i in arr:
    #     q.append(i)
    #     if i >= max_value:
    #         max_value = i
    # while q:
    #     day_stock = q[0]
    #     q.popleft()
    #     if day_stock == max_value:
    #         if q:
    #             max_value = max(q)
    #     else:
    #         ans += max_value - day_stock
    # print(ans)
    #
    #
# 1 2 1 5 2 3