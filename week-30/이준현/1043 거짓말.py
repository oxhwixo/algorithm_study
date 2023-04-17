import sys

input = sys.stdin.readline

# 진실을 아는 사람이 오면 반드시 진실을 말해야 한다. => 과장을 말한 사람과 진실을 아는 사람이 공존해서는 안된다.

n, m = map(int, input().split())
true_list = set(list(map(int, input().split()))[1:])
graph = [[] for i in range(n + 1)]
ans = 0

if len(true_list) == 0:
    print(m)
    exit(0)
party = []
for i in range(m):
    party.append(set(list(map(int, input().split()))[1:]))
for _ in range(m):
    for i in range(m):
        if party[i] & true_list:
            true_list = true_list.union(party[i])
for i in range(m):
    if party[i] & true_list:
        continue
    ans += 1
print(ans)
