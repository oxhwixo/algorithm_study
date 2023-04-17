alphabets = list(input())
n = len(alphabets)

result = "z" * n

for i in range(1, n-1):
    for j in range(i + 1, n):
        fir = alphabets[:i]
        sec = alphabets[i:j]
        thi = alphabets[j:]
        
        fir.reverse()
        sec.reverse()
        thi.reverse()
        
        temp = "".join(fir+sec+thi)
        result = min(result, temp)

print(result)