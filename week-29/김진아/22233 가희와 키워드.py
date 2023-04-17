n, m = map(int, input().split())
memo = set([input() for _ in range(n)])
blog = [input().split(',') for _ in range(m)]

for keywords in blog:
    memo -= set(keywords)
    print(len(memo))    