# 5568 카드 놓기
# 실버 4 

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]
temp = []
ans = set()

def bt(depth):
    if depth == k:
        new_num = ""
        for i in range(k):
            new_num += str(cards[temp[i]])
        ans.add(int(new_num))
        return
    
    for i in range(n):
        if i not in temp:
          temp.append(i)
          bt(depth + 1)
          temp.remove(i)

bt(0)
print(len(ans))
