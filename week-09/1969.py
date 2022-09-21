# 1969번 DNA
# 실버 5

n, m = map(int, input().split())
dna = []
res = ""
cnt = 0

for _ in range(n):
	dna.append(input())

for i in range(m):
	check = [0, 0, 0, 0] # A, C, G, T
	for j in range(n):
		if dna[j][i] == 'A':
			check[0] += 1
		elif dna[j][i] == 'C':
			check[1] += 1
		elif dna[j][i] == 'G':
			check[2] += 1
		elif dna[j][i] == 'T':
			check[3] += 1	
	idx = check.index(max(check))
	if idx == 0:
		res += 'A'
	elif idx == 1:
		res += 'C'
	elif idx == 2:
		res += 'G'
	elif idx == 3:
		res += 'T'
	cnt += n - max(check)

print(res)
print(cnt)

# "각 행"의 "같은 열"을 비교하는데서 헤맸음.
# 열 길이만큼 반복문을 만들고 그 안에 행 길이만큼의 이중반복문을 만들어준다!
# 인덱스 구하는 부분도 다시 봐두기


# 딕셔너리로도 풀어보자
# n,m=map(int,input().split())
# dna=[]
# res=""
# cnt=0
 
# for _ in range(n):
#     dna.append(input())

# for i in range(m):
#     check=dict()

#     for j in dna:
#         if(j[i] in check):
#             check[j[i]]+=1
#         else:
#             check[j[i]]=1
		
#     check=sorted(check.items(), key=lambda x: (-x[1],x[0]))

#     res+=check[0][0]
#     cnt+=n-check[0][1]

# print(f"{res}/n{cnt}")