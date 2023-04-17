# 2943 토끼
# 실버 2

import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

k = int(math.sqrt(n))
box = [0] * n
cup = [0] * (n // k + 1)

# 내가 한 타임에 "넣은 성냥 수"만 세는게 아니라 
# "성냥 넣은 곳들의 총 성냥"을 세는것임!!!
# 컵이든 성냥갑이든 성냥은 1개 이상 들어갈 수 있음!!

for _ in range(m):
    berry, start = map(int, input().split())

    # start는 0부터 N-1 순이지만 end는 1부터 N 순임.
    # 인덱싱이랑 컵 시작, 마지막 구간 계산할 때 주의 필요함
    start -= 1
    end = berry + start 
    ans = 0

    # 시작 토끼부터 컵의 시작 구간(index % k == 0) 전 까지 반복
    while (start < end and start % k != 0):
        box[start] += 1
        ans += box[start]
        start += 1

   # end != n 이라면 뒷 순번 토끼부터 확인하며 성냥갑에 성냥 넣어줌 
   # end % k == 0이 되면 컵의 마지막구간임. (start는 0부터 N-1 순이지만 end는 1부터 N 순임에 주의)
   # 컵의 마지막구간 만나기 전 까지 성냥갑에 성냥 넣어줌
    if (end != n):
        while (start < end and end % k != 0):
          end -= 1
          box[end] += 1
          ans += box[end]

  # 이제 start는 컵의 시작구간이고 end는 컵의 마지막구간임
  # 앞으로 넣을 성냥은 전부 컵에 들어감
    while(start < end):
        cup[start // k - 1] += 1
        ans += cup[start // k - 1]
        start += k

    print(ans)
    