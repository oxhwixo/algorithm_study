# 1174 줄어드는 수
# 골드 5

n = int(input())

def bt(num):
    ans.append(int(num))
    for j in range(0, int(num[-1])): # 제일 끝 자리 보다 낮은 수 까지
        bt(num + str(j))

if n > 1023: # 987654321의 index가 1023
    print(-1)

else:
    ans = []
    for i in range(10):
        bt(str(i))
    print(sorted(ans)[n - 1])