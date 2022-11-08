# 문자열 압축

def solution(s):
	answer = len(s)
	i = 1

	while i < len(s)//2 + 1 :  
		split_s = [ s[j: j + i] for j in range(0, len(s), i)]

		temp_answer = ""
		count = 1
		j = 0

		while j < len(split_s): 
			# 파이썬은 and 연산시에 앞의 식이 참이 아니면 뒤의 식이 실행되지 않으므로 out of index 방지 가능
			while j < len(split_s) - 1 and split_s[j] == split_s[j + 1]:
				count += 1
				j += 1
			# count가 1일 때는 temp_str에 문자열만 추가 
			if count == 1:
				temp_answer += split_s[j]
				j += 1
			# count가 1이 아닐 때는 temp_str에 반복된 횟수인 count + 문자열 추가 
			else:
				temp_answer += str(count) + split_s[j]
				count = 1
				j += 1

		answer = min(answer, len(temp_answer))
		i += 1
			
	return answer
