import sys
from itertools import combinations

input = sys.stdin.readline

number = input().rstrip()
max_value = 0
min_value = 1e9


def DFS(num, count):
    for i in num:
        if int(i) % 2 == 1:
            count += 1
    if len(num) == 1:
        return count
    if len(num) == 2:
        return DFS(str(int(num[0]) + int(num[1])), count)
    else:
        ans_list = []
        for comb in combinations(range(1, len(num)), 2):
            comb = list(comb)
            comb.sort()
            first = int(num[:comb[0]])
            second = int(num[comb[0]:comb[1]])
            third = int(num[comb[1]:])
            ans_list.append(DFS(str(first + second + third), count))
        return min(ans_list)


def MAX(num, count):
    for i in num:
        if int(i) % 2 == 1:
            count += 1
    if len(num) == 1:
        return count
    if len(num) == 2:
        return MAX(str(int(num[0]) + int(num[1])), count)
    else:
        ans_list = []
        for comb in combinations(range(1, len(num)), 2):
            comb = list(comb)
            comb.sort()
            first = int(num[:comb[0]])
            second = int(num[comb[0]:comb[1]])
            third = int(num[comb[1]:])
            ans_list.append(MAX(str(first + second + third), count))
        return max(ans_list)


print(DFS(number, 0), MAX(number, 0))
