# 10974 모든 순열
# 실버 3

n = int(input())
ans = []
def bt(depth):
    if depth == n:
        for i in range(n):
            print(ans[i], end = ' ')
        print()
        return
    
    for i in range(1, n + 1):
        if i not in ans:
          ans.append(i)
          bt(depth + 1)
          ans.remove(i)

bt(0)