import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m_one, zero, one = 0, 0, 0


def DiQ(x, y, size):
    global m_one, zero, one
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != arr[x][y]:
                for a in range(3):
                    for b in range(3):
                        DiQ(x + (a * size // 3), y + (b * size // 3), size // 3)
                return
    if arr[x][y] == -1:
        m_one += 1
    elif arr[x][y] == 0:
        zero += 1
    elif arr[x][y] == 1:
        one += 1


DiQ(0, 0, n)

print(m_one)
print(zero)
print(one)
