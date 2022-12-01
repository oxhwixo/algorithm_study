from collections import deque

def separate_uv(p):
	open, close = 0, 0

	for i in range(len(p)):
		if p[i] == '(':
			open += 1
		else: 
			close += 1
		if open == close:
			return p[: i + 1], p[i + 1:]

def check_proper(u):
	stack = deque()

	for i in u:
		if i == '(':
			stack.append(i)
		else:
			if not stack:
				return False
			stack.pop()

	return True if not stack else False

def solution(p):
	if not p:
		return p
	
	u, v = separate_uv(p)

	if check_proper(u):
		return u + solution(v)
	else:
		answer = '('
		answer += solution(v)
		answer += ')'

		for uu in u[1:len(u) - 1]:
			if uu == '(':
				answer += ')'
			else:
				answer += '('
				
	return answer