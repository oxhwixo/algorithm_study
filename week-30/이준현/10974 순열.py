import sys

input = sys.stdin.readline

n = int(input())
check = [0] * n
check_list = list(range(1, n + 1))


def DFS(depth):
    if depth == n:
        for i in range(n):
            print(check[i], end=' ')
        print()
    else:
        for i in range(n):
            if check_list[i] in check:
                continue
            check[depth] = check_list[i]
            DFS(depth + 1)
            check[depth] = 0
DFS(0)
