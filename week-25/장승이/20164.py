# 20164 홀수 홀릭 호석
# 골드 5

def count_odd(num:int):
    count = 0
    while num:
        if (num % 10) % 2:
            count += 1
        num //= 10
    return count

def solution(n:str, total_count:int):
    if len(n) == 1:
        odd_counts.append(total_count)
        return
    elif len(n) == 2:
        new_num = int(n[0]) + int(n[1])
        solution(str(new_num), total_count + count_odd(new_num))
    else:
        for i in range(1, len(n)):
            for j in range(i + 1, len(n)):
                part1 = n[:i]
                part2 = n[i:j]
                part3 = n[j:]
                new_num = int(part1) + int(part2) + int(part3)
                solution(str(new_num), total_count + count_odd(new_num))

n = input()
odd_counts = []
solution(n, count_odd(int(n)))
print(min(odd_counts), max(odd_counts))