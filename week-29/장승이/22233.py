# 22232 가희와 키워드
# 실버 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = set([input().strip() for _ in range(n)])

for _ in range(m):
    keywords -= set(list(input().strip().split(",")))
    print(len(keywords))