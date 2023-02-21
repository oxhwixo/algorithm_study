# 1021 회전하는 큐
# 실버 3

from collections import deque

n, m = map(int, input().split())
wants = list(map(int, input().split()))

q = deque([i + 1 for i in range(n)])
count = 0

for want in wants:
	while True:
		if q[0] == want:
			q.popleft()
			break
		else:
			# 큐 길이를 반으로 나눈 값 보다
			# 작으면 popleft 크면 pop
			if q.index(want) <= len(q)//2:
				while q[0] != want:
					q.append(q.popleft())
					count += 1
			else:
				while q[0] != want:
					q.appendleft(q.pop())
					count += 1

print(count)
